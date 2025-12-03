import { Link, useNavigate } from "react-router-dom";
import { useContext } from "react";
import { CartContext } from "../context/CartContext.jsx";
import { useAuth } from "../hooks/useAuth.js";

export default function Navbar() {
  const { items } = useContext(CartContext);
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const count = items.reduce((s, p) => s + p.qty, 0);

  return (
    <header className="card" style={{ margin: "12px", padding: "14px 18px", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
      <Link to="/" style={{ display: "flex", gap: 10, alignItems: "center" }}>
        <div style={{ width: 34, height: 34, borderRadius: "50%", background: "var(--accent)" }} />
        <strong>Motommerce</strong>
      </Link>
      <nav style={{ display: "flex", gap: 16, alignItems: "center" }}>
        <Link to="/">Home</Link>
        <Link to="/shop">Shop</Link>
        <Link to="/contact">Contact</Link>
        <Link to="/cart" style={{ position: "relative", padding: "6px 10px", borderRadius: 10, background: "#0f0f18", border: "1px solid var(--border)" }}>
          Panier
          <span style={{ position: "absolute", top: -8, right: -10, background: "var(--accent)", borderRadius: "999px", padding: "2px 6px", fontSize: 12 }}>{count}</span>
        </Link>
        {user ? (
          <>
            <Link to="/profile">Profil</Link>
            <button className="button" style={{ padding: "8px 12px" }} onClick={() => { logout(); navigate("/"); }}>Logout</button>
          </>
        ) : (
          <Link to="/login" className="button" style={{ padding: "8px 12px" }}>Login</Link>
        )}
      </nav>
    </header>
  );
}
