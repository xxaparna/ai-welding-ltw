import { useState } from "react";
import { motion } from "framer-motion";
import { predictWelding } from "../services/api";
import { Zap, Gauge, Play, RotateCcw, Sliders, AlertCircle } from "lucide-react";
import "./PredictionForm.css";

export default function PredictionForm({ setResult }) {
  const [power, setPower] = useState(120);
  const [speed, setSpeed] = useState(400);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handlePredict = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await predictWelding(power, speed);
      setResult(data);
    } catch (err) {
      console.error(err);
      setError("Failed to execute prediction. Please ensure FastAPI backend is running.");
    } finally {
      setLoading(false);
    }
  };

  const applyPreset = (p, s) => {
    setPower(p);
    setSpeed(s);
  };

  return (
    <div className="prediction-form-card">
      <div className="form-header">
        <div className="header-icon-box">
          <Sliders size={22} />
        </div>
        <div>
          <h3>Process Input Controls</h3>
          <p>Set primary manufacturing parameters for prediction</p>
        </div>
      </div>

      {error && (
        <div className="form-error-alert">
          <AlertCircle size={16} />
          <span>{error}</span>
        </div>
      )}

      {/* Laser Power Input */}
      <div className="control-group">
        <div className="control-label-row">
          <span className="control-title">
            <Zap size={18} className="icon-power" /> Laser Power
          </span>
          <span className="control-val-badge power-badge">{power} W</span>
        </div>

        <div className="slider-wrapper">
          <input
            type="range"
            min="80"
            max="150"
            value={power}
            onChange={(e) => setPower(Number(e.target.value))}
            className="custom-range power-range"
          />
        </div>

        <div className="slider-limits">
          <span>Min: 80 W</span>
          <span>Nominal: 115 W</span>
          <span>Max: 150 W</span>
        </div>
      </div>

      {/* Welding Speed Input */}
      <div className="control-group">
        <div className="control-label-row">
          <span className="control-title">
            <Gauge size={18} className="icon-speed" /> Welding Speed
          </span>
          <span className="control-val-badge speed-badge">{speed} mm/min</span>
        </div>

        <div className="slider-wrapper">
          <input
            type="range"
            min="200"
            max="600"
            value={speed}
            onChange={(e) => setSpeed(Number(e.target.value))}
            className="custom-range speed-range"
          />
        </div>

        <div className="slider-limits">
          <span>Min: 200 mm/min</span>
          <span>Nominal: 400 mm/min</span>
          <span>Max: 600 mm/min</span>
        </div>
      </div>

      {/* Parameter Presets */}
      <div className="preset-container">
        <span className="preset-label">Quick Presets:</span>
        <div className="preset-buttons">
          <button type="button" onClick={() => applyPreset(90, 500)} className="preset-btn">
            Low Heat (90W, 500mm/m)
          </button>
          <button type="button" onClick={() => applyPreset(120, 400)} className="preset-btn active-preset">
            Nominal (120W, 400mm/m)
          </button>
          <button type="button" onClick={() => applyPreset(140, 250)} className="preset-btn">
            High Penetration (140W, 250mm/m)
          </button>
        </div>
      </div>

      {/* Action Button */}
      <motion.button
        className="predict-submit-btn"
        onClick={handlePredict}
        disabled={loading}
        whileHover={{ scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
      >
        {loading ? (
          <span className="btn-loading-state">
            <RotateCcw className="spinner-icon" size={18} /> Executing ML Inference...
          </span>
        ) : (
          <span className="btn-ready-state">
            <Play size={18} /> Run AI Process Prediction
          </span>
        )}
      </motion.button>
    </div>
  );
}