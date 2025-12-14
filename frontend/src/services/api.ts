export const API_BASE_URL = import.meta.env.VITE_API_URL;

export async function getHealth() {
  const res = await fetch(`${API_BASE_URL}/health`);
  return res.json();
}
