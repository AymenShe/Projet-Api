import Hero from "../components/Hero.jsx";
import ProductGrid from "../components/ProductGrid.jsx";
import { useFetch } from "../hooks/useFetch.js";
import { useAuth } from "../hooks/useAuth.js";
import { useEffect, useState } from "react";
import api from "../services/api.js";

export default function Home() {
  const { data: products } = useFetch("/products?limit=4");
  const { user } = useAuth();
  const [recommendations, setRecommendations] = useState([]);

  useEffect(() => {
    if (user) {
      api.get("/recommendations/")
        .then((res) => setRecommendations(res.data))
        .catch((err) => console.error("Error fetching recommendations:", err));
    }
  }, [user]);

  return (
    <div className="grid" style={{ gap: 18 }}>
      <Hero />

      {user && recommendations.length > 0 && (
        <section>
          <h2>Recommandé pour vous</h2>
          <p style={{ color: "var(--muted)", marginBottom: 10 }}>Basé sur vos achats récents</p>
          <ProductGrid products={recommendations} />
        </section>
      )}

      <section>
        <h2>Meilleures ventes</h2>
        <ProductGrid products={products || []} />
      </section>
    </div>
  );
}