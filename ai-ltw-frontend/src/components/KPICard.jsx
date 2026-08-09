import CountUpModule from "react-countup";
import "./KPICard.css";

const CountUpComponent =
  typeof CountUpModule === "function"
    ? CountUpModule
    : typeof CountUpModule.default === "function"
    ? CountUpModule.default
    : typeof CountUpModule.default?.default === "function"
    ? CountUpModule.default.default
    : CountUpModule;

function KPICard({ title, value, unit, color, icon }) {
  const numericValue = typeof value === "number" ? value : parseFloat(value) || 0;

  return (
    <div className="kpi-card">
      <div className="kpi-icon" style={{ background: color }}>
        {icon}
      </div>

      <div className="kpi-content">
        <h4>{title}</h4>

        <h2>
          {typeof CountUpComponent === "function" ? (
            <CountUpComponent end={numericValue} duration={1.5} decimals={2} />
          ) : (
            <span>{numericValue.toFixed(2)}</span>
          )}
          {" "}
          <span>{unit}</span>
        </h2>
      </div>
    </div>
  );
}

export default KPICard;