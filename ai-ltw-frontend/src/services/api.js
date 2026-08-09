export const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

export async function predictWelding(power, speed) {
  const response = await fetch(`${API_URL}/predict`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      power,
      speed
    })
  });

  if (!response.ok) {
    throw new Error("Prediction failed");
  }

  return await response.json();
}

export async function getMetrics() {
  const response = await fetch(`${API_URL}/metrics`);
  if (!response.ok) {
    throw new Error("Failed to fetch metrics");
  }
  return await response.json();
}

export async function getPhysics() {
  const response = await fetch(`${API_URL}/physics`);
  if (!response.ok) {
    throw new Error("Failed to fetch physics equations");
  }
  return await response.json();
}