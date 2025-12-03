import { Link } from "react-router-dom";
import RatingStars from "./RatingStars.jsx";
import { useContext, useState } from "react";
import { CartContext } from "../context/CartContext.jsx";

export default function ProductCard({ product }) {
  const { add } = useContext(CartContext);
  const fallback = "/images/pas_image.png"; // Generic fallback
  const [imgSrc, setImgSrc] = useState(product.image_url || fallback);

  return (
    <article className="card" style={{ padding: 14, display: "flex", flexDirection: "column", gap: 10 }}>
      <img
        src={imgSrc}
        alt={product.name}
        onError={() => setImgSrc(fallback)}
        style={{ width: "100%", height: 180, objectFit: "cover", borderRadius: 12, background: "#0f0f18" }}
      />
      <h3>{product.name}</h3>
      <p style={{ color: "var(--muted)", minHeight: 48 }}>{product.description}</p>
      <RatingStars rating={product.rating} />
      <strong>{"\u20ac " + Number(product.price).toFixed(2)}</strong>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <Link to={`/product/${product.id}`} style={{ color: "var(--accent)" }}>Voir</Link>
        <button className="button" onClick={() => add(product, 1)}>Ajouter au panier</button>
      </div>
    </article>
  );
}
