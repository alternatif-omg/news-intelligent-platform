import { useEffect, useState } from "react";
import { getAnalytics } from "../services/api";

export default function Dashboard() {
  const [stats, setStats] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getAnalytics()
      .then((res) => {
        // aman untuk berbagai bentuk response
        setStats(res.data ?? res);
      })
      .catch((err) => {
        console.error("Failed to load analytics:", err);
        setError("Failed to load dashboard data");
      })
      .finally(() => {
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading dashboard...</p>;
  if (error) return <p>{error}</p>;

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Total News: {stats?.total_news ?? 0}</p>
      <p>Top Category: {stats?.top_category ?? "-"}</p>
    </div>
  );
}
