import { Cpu, Wifi } from "lucide-react";
import "./Footer.css";

export default function Footer() {
  return (
    <footer className="minimal-footer">
      <div className="footer-container">
        <div className="footer-left">
          <span className="footer-icon">⚡</span>
          <span>AI Laser Transmission Welding Platform</span>
          <span className="divider">•</span>
          <span className="version-chip">v1.0.0 Physics-ML</span>
        </div>

        <div className="footer-right">
          <div className="status-indicator">
            <Wifi size={14} className="status-wifi-icon" />
            <span>FastAPI Server Live (127.0.0.1:8000)</span>
          </div>
        </div>
      </div>
    </footer>
  );
}
