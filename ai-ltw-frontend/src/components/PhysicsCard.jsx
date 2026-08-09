import { useEffect, useState } from "react";
import { motion } from "framer-motion";
import { getPhysics } from "../services/api";
import { Atom, Flame, Zap, ArrowRight, BookOpen, AlertCircle, RefreshCw } from "lucide-react";
import "./PhysicsCard.css";

const sanitizeEquation = (eq) => {
  if (!eq) return "";
  return eq
    .replace(/Ã–/g, "×")
    .replace(/Ã—/g, "×")
    .replace(/A\?\?\?/g, "×")
    .replace(/\?/g, "×");
};

export default function PhysicsCard() {
  const [physics, setPhysics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Live test parameters for formula preview
  const [testPower, setTestPower] = useState(120);
  const [testSpeed, setTestSpeed] = useState(400);

  const fetchPhysicsData = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await getPhysics();
      setPhysics(data);
    } catch (err) {
      console.error(err);
      setError("Failed to connect to Physics API endpoint.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchPhysicsData();
  }, []);

  if (loading) {
    return (
      <div className="physics-section">
        <div className="physics-header">
          <span className="section-badge">Physics-Based Modeling</span>
          <h2>Analytical Physics Equations</h2>
        </div>
        <div className="skeleton-container">
          <div className="skeleton-card"></div>
        </div>
      </div>
    );
  }

  if (error || !physics || !physics.absorptivity || !physics.temperature) {
    return (
      <div className="physics-section">
        <div className="error-card">
          <AlertCircle size={32} className="error-icon" />
          <h3>Physics Equations Unavailable</h3>
          <p>{error || "Physics equations metadata could not be fetched."}</p>
          <button onClick={fetchPhysicsData} className="retry-btn">
            <RefreshCw size={16} /> Retry Physics API
          </button>
        </div>
      </div>
    );
  }

  // Calculate live preview metrics
  const lineEnergyCalc = ((testPower / testSpeed) * 60).toFixed(2);
  const tempCalc = (
    (physics.temperature.intercept || 31.6366) +
    (physics.temperature.line_energy_coefficient || 28.1227) * Number(lineEnergyCalc)
  ).toFixed(2);
  const absCalc = (
    (physics.absorptivity.intercept || -7.1616) +
    (physics.absorptivity.power_coefficient || 0.2459) * testPower +
    (physics.absorptivity.speed_coefficient || -0.0090) * testSpeed
  ).toFixed(2);

  return (
    <div className="physics-section">
      <div className="physics-header">
        <div className="header-left">
          <span className="section-badge">First-Principles Modeling</span>
          <h2>Physics-Based Analytical Engine</h2>
          <p>
            Explicit mathematical formulations modeling radiation absorption and heat transfer dynamics in Laser Transmission Welding.
          </p>
        </div>
        <div className="physics-badge">
          <Atom size={18} />
          <span>Physics-Informed ML Hybrid</span>
        </div>
      </div>

      <div className="physics-grid">
        {/* Absorptivity Physics Card */}
        <motion.div
          className="physics-card abs-physics-card"
          whileHover={{ y: -4 }}
          transition={{ duration: 0.25 }}
        >
          <div className="card-header">
            <div className="header-tag abs-tag">
              <Zap size={16} /> Absorptivity Equation
            </div>
            <span className="symbol-label">Variable: A (%)</span>
          </div>

          <div className="equation-box">
            <span className="eq-label">Empirical Analytical Formula</span>
            <div className="formula-display">
              <code>{sanitizeEquation(physics.absorptivity.equation)}</code>
            </div>
          </div>

          <div className="coefficients-title">Parameter Coefficients</div>
          <div className="coefficients-grid">
            <div className="coeff-chip">
              <span className="coeff-name">Intercept</span>
              <span className="coeff-val">{physics.absorptivity.intercept}</span>
            </div>
            <div className="coeff-chip">
              <span className="coeff-name">Power Coeff (β₁)</span>
              <span className="coeff-val">+{physics.absorptivity.power_coefficient}</span>
            </div>
            <div className="coeff-chip">
              <span className="coeff-name">Speed Coeff (β₂)</span>
              <span className="coeff-val">{physics.absorptivity.speed_coefficient}</span>
            </div>
          </div>

          <p className="physics-note">
            <strong>Physics Insight:</strong> Laser Power enhances beam absorption due to local thermal excitation, whereas increased Welding Speed reduces laser interaction time per unit area.
          </p>
        </motion.div>

        {/* Temperature Physics Card */}
        <motion.div
          className="physics-card temp-physics-card"
          whileHover={{ y: -4 }}
          transition={{ duration: 0.25 }}
        >
          <div className="card-header">
            <div className="header-tag temp-tag">
              <Flame size={16} /> Temperature Equation
            </div>
            <span className="symbol-label">Variable: T (°C)</span>
          </div>

          <div className="equation-box">
            <span className="eq-label">Thermal Energy Formula</span>
            <div className="formula-display">
              <code>{sanitizeEquation(physics.temperature.equation)}</code>
            </div>
          </div>

          <div className="coefficients-title">Parameter Coefficients</div>
          <div className="coefficients-grid">
            <div className="coeff-chip">
              <span className="coeff-name">Base Temp Intercept</span>
              <span className="coeff-val">{physics.temperature.intercept} °C</span>
            </div>
            <div className="coeff-chip">
              <span className="coeff-name">Line Energy Coeff (γ₁)</span>
              <span className="coeff-val">+{physics.temperature.line_energy_coefficient}</span>
            </div>
          </div>

          <p className="physics-note">
            <strong>Physics Insight:</strong> Peak interface temperature directly scales with net Line Energy input (E = (Power / Speed) × 60), modeling linear heat accumulation across the polymeric interface.
          </p>
        </motion.div>
      </div>

      {/* Live Physics Calculator Widget */}
      <div className="physics-calculator-widget">
        <div className="widget-header">
          <BookOpen size={18} className="widget-icon" />
          <h4>Interactive Physics Formula Playground</h4>
        </div>
        <div className="widget-controls">
          <div className="widget-input-group">
            <label>Power: <strong>{testPower} W</strong></label>
            <input
              type="range"
              min="80"
              max="150"
              value={testPower}
              onChange={(e) => setTestPower(Number(e.target.value))}
            />
          </div>
          <div className="widget-input-group">
            <label>Speed: <strong>{testSpeed} mm/min</strong></label>
            <input
              type="range"
              min="200"
              max="600"
              value={testSpeed}
              onChange={(e) => setTestSpeed(Number(e.target.value))}
            />
          </div>

          <div className="widget-flow">
            <ArrowRight size={18} className="flow-arrow" />
          </div>

          <div className="widget-results">
            <div className="widget-res-item">
              <span className="w-label">Line Energy</span>
              <span className="w-val">{lineEnergyCalc} J/mm</span>
            </div>
            <div className="widget-res-item">
              <span className="w-label">Physics Absorptivity</span>
              <span className="w-val">{absCalc}%</span>
            </div>
            <div className="widget-res-item">
              <span className="w-label">Physics Interface Temp</span>
              <span className="w-val temp-highlight">{tempCalc} °C</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}