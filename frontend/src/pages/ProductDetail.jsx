import { useParams, Link } from "react-router-dom";
import { useFetch } from "../hooks/useFetch.js";
import { useContext, useState } from "react";
import { CartContext } from "../context/CartContext.jsx";
import RatingStars from "../components/RatingStars.jsx";


export default function ProductDetail() {
  const { id } = useParams();
  const { data: product, loading } = useFetch(`/products/${id}`);
  const { add } = useContext(CartContext);
  const fallback = "/images/pas_image.png";
  const imgSrc = product?.image_url;
  if (loading) return <p>Chargement...</p>;
  if (!product) {
    return (
      <div style={{ textAlign: "center", padding: "60px 20px" }}>
        <div className="card" style={{ maxWidth: 480, margin: "0 auto", padding: 40 }}>
          <h2 style={{ marginBottom: 16 }}>Produit introuvable</h2>
          <p style={{ color: "var(--muted)", marginBottom: 24, fontSize: "1.1rem" }}>
            Le produit que vous essayez de consulter a été supprimé ou n'existe plus.
          </p>
          <Link to="/shop" className="button">
            Retour au catalogue
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="grid" style={{ gap: 14 }}>
      <div className="card" style={{ padding: 16, display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
        <img
          src={imgSrc}
          alt={product.name}
          onError={() => fallback}
          style={{
            width: "100%",      // s'adapte au conteneur
            maxWidth: 300,      // limite pour ne pas être trop grande
            height: "auto",     // garde les proportions
            borderRadius: 12,
            objectFit: "cover",
            background: "#0f0f18"
          }}
        />
        <div>
          <h2>{product.name}</h2>
          <p style={{ color: "var(--muted)" }}>{product.description}</p>
          <RatingStars rating={product.rating} />
          <p>Stock: {product.stock}</p>
          <h3>{"\u20ac " + Number(product.price).toFixed(2)}</h3>
          <button className="button" onClick={() => add(product, 1)}>Ajouter au panier</button>
        </div>
      </div>
      <section className="card" style={{ padding: 14 }}>
        <h3>Avis</h3>
        {(product.reviews || []).map((r) => (
          <div key={r.id} style={{ marginBottom: 10 }}>
            <strong>{r.user_name}</strong> — <RatingStars rating={r.rating} />
            <p>{r.comment}</p>
          </div>
        ))}
      </section>
    </div>
  );
}
