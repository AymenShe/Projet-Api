import Hero from "../components/Hero.jsx";
import ProductGrid from "../components/ProductGrid.jsx";
import { useFetch } from "../hooks/useFetch.js";

export default function Home() {
  const { data: products } = useFetch("/products?limit=4");
  return (
    <div className="grid" style={{ gap: 18 }}>
      <Hero />
      <section>
        <h2>Meilleures ventes</h2>
        <ProductGrid products={products || []} />
      </section>
    </div>
  );
}