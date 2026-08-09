import React, { useState } from "react";
import Dashboard from "./pages/Dashboard";
import "./App.css";

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error("Dashboard Runtime Error:", error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div style={{
          padding: "40px",
          textAlign: "center",
          fontFamily: "sans-serif",
          maxWidth: "600px",
          margin: "80px auto",
          background: "#ffffff",
          borderRadius: "20px",
          boxShadow: "0 20px 50px rgba(0,0,0,0.1)",
          border: "1px solid #fee2e2"
        }}>
          <h2 style={{ color: "#ef4444", marginTop: 0 }}>Dashboard Encountered an Error</h2>
          <p style={{ color: "#64748b" }}>{this.state.error?.toString()}</p>
          <button
            onClick={() => window.location.reload()}
            style={{
              background: "#2563eb",
              color: "white",
              border: "none",
              padding: "12px 24px",
              borderRadius: "12px",
              fontWeight: "bold",
              cursor: "pointer"
            }}
          >
            Reload Dashboard
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

function App() {
  return (
    <ErrorBoundary>
      <Dashboard />
    </ErrorBoundary>
  );
}

export default App;