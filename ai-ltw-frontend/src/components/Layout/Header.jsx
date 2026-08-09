import { useEffect, useState } from "react";
import { Cpu, Database, Wifi } from "lucide-react";
import { getPhysics } from "../../services/api";
import "./Header.css";

export default function Header() {
  const [online, setOnline] = useState(true);

  useEffect(() => {
    async function checkHealth() {
      try {
        await getPhysics();
        setOnline(true);
      } catch (err) {
        console.warn("Backend connectivity check failed:", err);
        setOnline(false);
      }
    }
    checkHealth();
  }, []);

  return (
    <header className="header">
      <div className="logoSection">
        <div className="logo">⚡</div>
        <div>
          <h1>AI Laser Transmission Welding</h1>
          <p>Physics-Informed Process Optimization & Machine Learning Platform</p>
        </div>
      </div>

      <div className="status">
        <div className="statusItem">
          <Database size={18} />
          <span>Model v1.0</span>
          <div className={online ? "greenDot" : "redDot"} />
        </div>

        <div className="statusItem">
          <Cpu size={18} />
          <span>FastAPI</span>
          <div className={online ? "greenDot" : "redDot"} />
        </div>

        <div className="statusItem">
          <Wifi size={18} />
          <span>API 8000</span>
          <div className={online ? "greenDot" : "redDot"} />
        </div>
      </div>
    </header>
  );
}