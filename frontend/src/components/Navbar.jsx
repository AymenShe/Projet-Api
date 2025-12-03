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
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M12 4C7.58 4 4 7.58 4 12V16C4 17.1 4.9 18 6 18H9V14H15V12H9V10H15C16.66 10 18 11.34 18 13V18H19C20.1 18 21 17.1 21 16V12C21 7.58 17.42 4 12 4ZM11 14H15V18H11V14Z"
            fill="#FF0000" />
        </svg>
        <strong>Motommerce</strong>
      </Link>
      <nav style={{ display: "flex", gap: 16, alignItems: "center" }}>
        <Link to="/">Home</Link>
        <Link to="/shop">Shop</Link>
        <Link to="/stores">Magasins</Link>
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
