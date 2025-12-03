import { useState } from "react";
import { useFetch } from "../hooks/useFetch.js";
import ProductGrid from "../components/ProductGrid.jsx";

export default function Shop() {
  const [query, setQuery] = useState("");
  const [category, setCategory] = useState("");
  const { data: products } = useFetch(`/products?search=${query}&category=${category}`);

  return (
    <div className="grid" style={{ gap: 12 }}>
      <header style={{ textAlign: "center" }}>
        <h1>Catalogue</h1>
        <p style={{ color: "var(--muted)" }}>Trouvez votre équipement ultime.</p>
      </header>
      <div className="card" style={{ padding: 14, display: "flex", gap: 10, flexWrap: "wrap" }}>
        <input placeholder="Rechercher..." value={query} onChange={(e) => setQuery(e.target.value)} />
        <select value={category} onChange={(e) => setCategory(e.target.value)}>
          <option value="">Toutes catégories</option>
          <option value="Casque">Casque</option>
          <option value="Veste">Veste</option>
          <option value="Protection">Protection</option>
        </select>
      </div>
      <ProductGrid products={products || []} />
    </div>
  );
}