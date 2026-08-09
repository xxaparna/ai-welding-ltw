import { useState } from "react";
import { motion } from "framer-motion";

import Header from "../components/layout/Header";
import PredictionForm from "../components/PredictionForm";
import PredictionCard from "../components/PredictionCard";
import PerformanceSection from "../components/PerformanceSection";
import PhysicsCard from "../components/PhysicsCard";
import GraphGallery from "../components/GraphGallery";

import "./Dashboard.css";

function Dashboard() {
  const [result, setResult] = useState(null);

  return (
    <div className="page">
      <Header />

      <div className="content">
        {/* Prediction Input & Result Telemetry Section */}
        <motion.div
          className="dashboard"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <PredictionForm setResult={setResult} />
          <PredictionCard result={result} />
        </motion.div>

        {/* Model Performance Telemetry */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <PerformanceSection />
        </motion.div>

        {/* Physics-Based Model Section */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <PhysicsCard />
        </motion.div>

        {/* EDA Graph Gallery */}
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
        >
          <GraphGallery />
        </motion.div>
      </div>
    </div>
  );
}

export default Dashboard;