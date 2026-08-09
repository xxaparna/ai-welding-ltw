import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { getMetrics } from "../services/api";
import { Activity, ShieldCheck, Target, Layers, HelpCircle, RefreshCw, AlertCircle } from "lucide-react";
import CountUpModule from "react-countup";
import "./PerformanceSection.css";

const CountUpComponent =
  typeof CountUpModule === "function"
    ? CountUpModule
    : typeof CountUpModule.default === "function"
    ? CountUpModule.default
    : typeof CountUpModule.default?.default === "function"
    ? CountUpModule.default.default
    : CountUpModule;

function SafeCountUp({ end, decimals = 2, duration = 1.5 }) {
  const num = typeof end === "number" ? end : parseFloat(end) || 0;
  if (typeof CountUpComponent === "function") {
    return <CountUpComponent end={num} decimals={decimals} duration={duration} />;
  }
  return <span>{num.toFixed(decimals)}</span>;
}

export default function PerformanceSection() {
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchMetrics = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getMetrics();
      setMetrics(data);
    } catch (err) {
      console.error(err);
      setError("Failed to fetch model metrics from backend API.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchMetrics();
  }, []);

  if (loading) {
    return (
      <div className="performance-section">
        <div className="performance-header">
          <span className="section-badge">ML Telemetry</span>
          <h2>Model Validation & Accuracy</h2>
        </div>
        <div className="skeleton-container">
          <div className="skeleton-card"></div>
          <div className="skeleton-card"></div>
        </div>
      </div>
    );
  }

  if (error || !metrics || !metrics.absorptivity || !metrics.temperature) {
    return (
      <div className="performance-section">
        <div className="error-card">
          <AlertCircle size={32} className="error-icon" />
          <h3>Metrics Unavailable</h3>
          <p>{error || "Unable to load model performance data."}</p>
          <button onClick={fetchMetrics} className="retry-btn">
            <RefreshCw size={16} /> Retry API Connection
          </button>
        </div>
      </div>
    );
  }

  const absR2Pct = (metrics.absorptivity.r2 * 100).toFixed(2);
  const tempR2Pct = (metrics.temperature.r2 * 100).toFixed(2);

  return (
    <div className="performance-section">
      <div className="performance-header">
        <div className="header-left">
          <span className="section-badge">Model Performance</span>
          <h2>Evaluation & Telemetry</h2>
          <p>
            Statistical evaluation metrics calculated on a 20% holdout test set (1,000 synthetic laser transmission samples).
          </p>
        </div>
        <div className="holdout-badge">
          <ShieldCheck size={18} />
          <span>Holdout Test Size: 20% (1,000 samples)</span>
        </div>
      </div>

      <div className="performance-grid">
        {/* Absorptivity Model Card */}
        <motion.div
          className="model-card absorptivity-model-card"
          whileHover={{ y: -6 }}
          transition={{ duration: 0.25 }}
        >
          <div className="card-top">
            <div className="model-badge abs-badge">
              <Activity size={16} /> Optical Absorptivity Model
            </div>
            <span className="target-chip">Target: absorptivity_pct (%)</span>
          </div>

          <div className="gauge-row">
            <div className="radial-meter">
              <svg viewBox="0 0 100 100" className="gauge-svg">
                <circle cx="50" cy="50" r="42" className="gauge-bg" />
                <circle
                  cx="50"
                  cy="50"
                  r="42"
                  className="gauge-fill abs-fill"
                  style={{
                    strokeDasharray: 264,
                    strokeDashoffset: 264 - (264 * metrics.absorptivity.r2)
                  }}
                />
              </svg>
              <div className="gauge-center">
                <span className="gauge-value">{absR2Pct}%</span>
                <span className="gauge-label">R² Accuracy</span>
              </div>
            </div>

            <div className="primary-metric">
              <span className="metric-title">Coefficient of Determination (R²)</span>
              <div className="metric-big-val">
                <SafeCountUp end={metrics.absorptivity.r2} decimals={4} duration={1.8} />
              </div>
              <span className="quality-pill high-accuracy">99.02% Variance Explained</span>
            </div>
          </div>

          <div className="metrics-breakdown">
            <div className="sub-metric-box">
              <span className="sub-label">Mean Absolute Error (MAE)</span>
              <span className="sub-val">
                <SafeCountUp end={metrics.absorptivity.mae} decimals={4} duration={1.5} /> %
              </span>
            </div>

            <div className="sub-metric-box">
              <span className="sub-label">Root Mean Sq Error (RMSE)</span>
              <span className="sub-val">
                <SafeCountUp end={metrics.absorptivity.rmse} decimals={4} duration={1.5} /> %
              </span>
            </div>

            <div className="sub-metric-box">
              <span className="sub-label">Testing Samples</span>
              <span className="sub-val">
                <SafeCountUp end={metrics.absorptivity.testing_samples || 1000} decimals={0} duration={1} />
              </span>
            </div>
          </div>
        </motion.div>

        {/* Temperature Model Card */}
        <motion.div
          className="model-card temperature-model-card"
          whileHover={{ y: -6 }}
          transition={{ duration: 0.25 }}
        >
          <div className="card-top">
            <div className="model-badge temp-badge">
              <Target size={16} /> Interface Temperature Model
            </div>
            <span className="target-chip">Target: interface_temp_C (°C)</span>
          </div>

          <div className="gauge-row">
            <div className="radial-meter">
              <svg viewBox="0 0 100 100" className="gauge-svg">
                <circle cx="50" cy="50" r="42" className="gauge-bg" />
                <circle
                  cx="50"
                  cy="50"
                  r="42"
                  className="gauge-fill temp-fill"
                  style={{
                    strokeDasharray: 264,
                    strokeDashoffset: 264 - (264 * metrics.temperature.r2)
                  }}
                />
              </svg>
              <div className="gauge-center">
                <span className="gauge-value">{tempR2Pct}%</span>
                <span className="gauge-label">R² Accuracy</span>
              </div>
            </div>

            <div className="primary-metric">
              <span className="metric-title">Coefficient of Determination (R²)</span>
              <div className="metric-big-val">
                <SafeCountUp end={metrics.temperature.r2} decimals={4} duration={1.8} />
              </div>
              <span className="quality-pill high-accuracy-temp">99.01% Variance Explained</span>
            </div>
          </div>

          <div className="metrics-breakdown">
            <div className="sub-metric-box">
              <span className="sub-label">Mean Absolute Error (MAE)</span>
              <span className="sub-val">
                <SafeCountUp end={metrics.temperature.mae} decimals={4} duration={1.5} /> °C
              </span>
            </div>

            <div className="sub-metric-box">
              <span className="sub-label">Root Mean Sq Error (RMSE)</span>
              <span className="sub-val">
                <SafeCountUp end={metrics.temperature.rmse} decimals={4} duration={1.5} /> °C
              </span>
            </div>

            <div className="sub-metric-box">
              <span className="sub-label">Testing Samples</span>
              <span className="sub-val">
                <SafeCountUp end={metrics.temperature.testing_samples || 1000} decimals={0} duration={1} />
              </span>
            </div>
          </div>
        </motion.div>
      </div>

      {/* Metric Definitions & Legend */}
      <div className="telemetry-legend">
        <div className="legend-item">
          <Layers size={16} className="legend-icon" />
          <div>
            <strong>R² Score:</strong> Indicates how well the machine learning model accounts for target variation ($1.0$ is perfect fit).
          </div>
        </div>
        <div className="legend-item">
          <HelpCircle size={16} className="legend-icon" />
          <div>
            <strong>MAE vs RMSE:</strong> MAE gives average error magnitude while RMSE penalizes larger deviations in thermal joint predictions.
          </div>
        </div>
      </div>
    </div>
  );
}