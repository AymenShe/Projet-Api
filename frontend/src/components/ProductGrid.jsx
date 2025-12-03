import ProductCard from "./ProductCard.jsx";

export default function ProductGrid({ products }) {
  const list = Array.isArray(products) ? products : [];
  return (
    <div className="grid" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))" }}>
      {list.map((p) => (
        <ProductCard key={p.id} product={p} />
      ))}
    </div>
  );
}
