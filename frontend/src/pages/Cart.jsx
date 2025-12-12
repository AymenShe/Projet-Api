import { useContext } from "react";
import { CartContext } from "../context/CartContext.jsx";
import { Link } from "react-router-dom";
import { useAuth } from "../hooks/useAuth.js";

export default function Cart() {
  const { items, remove, updateQty, total } = useContext(CartContext);
  const { user } = useAuth();
  return (
    <div className="card" style={{ padding: 16 }}>
      <h2>Panier</h2>
      {items.length === 0 && <p>Votre panier est vide.</p>}
      {items.map((item) => (
        <div key={item.id} style={{ display: "flex", gap: 10, alignItems: "center", marginBottom: 10 }}>
          <div style={{ flex: 1 }}>
            <strong>{item.name}</strong>
            <p style={{ color: "var(--muted)" }}>{"\u20ac " + Number(item.price).toFixed(2)}</p>
          </div>
          <input type="number" min="1" value={item.qty} onChange={(e) => updateQty(item.id, Number(e.target.value))} style={{ width: 70 }} />
          <button className="button" onClick={() => remove(item.id)}>Supprimer</button>
        </div>
      ))}
      <div style={{ display: "flex", justifyContent: "space-between", marginTop: 12 }}>
        <strong>Total</strong>
        <strong>{"\u20ac " + total.toFixed(2)}</strong>
      </div>

      {user ? (
        <Link to="/checkout" className="button" style={{ marginTop: 12, display: "inline-block", textAlign: "center" }}>Passer au paiement</Link>
      ) : (
        <div style={{ marginTop: 20, padding: 16, background: "rgba(255, 100, 100, 0.1)", borderRadius: 8, textAlign: "center" }}>
          <p style={{ marginBottom: 10, color: "var(--text)" }}>Vous devez vous connecter avant de passer au paiement</p>
          <Link to="/login" className="button" style={{ display: "inline-block" }}>Se connecter</Link>
        </div>
      )}
    </div>
  );
}
