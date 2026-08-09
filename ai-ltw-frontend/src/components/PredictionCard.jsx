import { motion } from "framer-motion";
import KPICard from "./KPICard";
import { Cpu, ArrowRight, CheckCircle2, AlertTriangle, ShieldAlert } from "lucide-react";
import "./PredictionCard.css";

export default function PredictionCard({ result }) {
  if (!result) {
    return (
      <div className="prediction-results-card empty-results-state">
        <div className="empty-icon-wrapper">
          <Cpu size={36} />
        </div>
        <h3>Prediction Telemetry Standby</h3>
        <p>
          Configure the process parameters on the control panel and click <strong>Run AI Process Prediction</strong> to calculate Line Energy, Absorptivity, and Interface Temperature.
        </p>
      </div>
    );
  }

  // Determine Thermal Weld Quality Window
  const temp = result.interface_temperature;
  let statusBadge = {
    text: "Optimal Welding Window (400 - 650 °C)",
    className: "status-optimal",
    icon: <CheckCircle2 size={16} />
  };

  if (temp < 400) {
    statusBadge = {
      text: "Sub-Optimal / Incomplete Dwell (< 400 °C)",
      className: "status-cold",
      icon: <AlertTriangle size={16} />
    };
  } else if (temp > 650) {
    statusBadge = {
      text: "High Thermal Degradation Risk (> 650 °C)",
      className: "status-hot",
      icon: <ShieldAlert size={16} />
    };
  }

  return (
    <motion.div
      className="prediction-results-card"
      initial={{ opacity: 0, scale: 0.98 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.4 }}
    >
      <div className="results-header">
        <div>
          <h3>Prediction Results Telemetry</h3>
          <p>Real-time ML Model Predictions & Process Engineering Pipeline</p>
        </div>
        <div className={`status-badge ${statusBadge.className}`}>
          {statusBadge.icon}
          <span>{statusBadge.text}</span>
        </div>
      </div>

      {/* Process Flow Diagram */}
      <div className="process-flow-diagram">
        <div className="flow-step">
          <span className="step-tag">Inputs</span>
          <span className="step-val">{result.power}W / {result.speed}mm</span>
        </div>
        <ArrowRight size={14} className="flow-connector" />
        <div className="flow-step">
          <span className="step-tag">Physics</span>
          <span className="step-val">{result.line_energy} J/mm</span>
        </div>
        <ArrowRight size={14} className="flow-connector" />
        <div className="flow-step">
          <span className="step-tag">ML Ensembles</span>
          <span className="step-val">RF / SVR / XGB</span>
        </div>
        <ArrowRight size={14} className="flow-connector" />
        <div className="flow-step highlight-step">
          <span className="step-tag">Outputs</span>
          <span className="step-val">{result.absorptivity}% / {result.interface_temperature}°C</span>
        </div>
      </div>

      {/* KPI Cards Grid */}
      <div className="kpi-grid">
        <KPICard
          title="Laser Power"
          value={result.power}
          unit="W"
          color="#2563eb"
          icon="⚡"
        />

        <KPICard
          title="Line Energy"
          value={result.line_energy}
          unit="J/mm"
          color="#f59e0b"
          icon="📈"
        />

        <KPICard
          title="Absorptivity"
          value={result.absorptivity}
          unit="%"
          color="#10b981"
          icon="🧪"
        />

        <KPICard
          title="Interface Temperature"
          value={result.interface_temperature}
          unit="°C"
          color="#ef4444"
          icon="🔥"
        />
      </div>
    </motion.div>
  );
}