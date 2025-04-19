const API_BASE = 'https://your-backend-url.com/api';

async function fetchTours() {
  const res = await fetch(`${API_BASE}/tours/`);
  return await res.json();
}