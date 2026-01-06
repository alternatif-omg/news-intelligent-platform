import { useEffect, useState } from "react";
import api from "../services/api";

export default function useNews() {
  const [news, setNews] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/news")
      .then(res => setNews(res.data))
      .finally(() => setLoading(false));
  }, []);

  return { news, loading };
}
