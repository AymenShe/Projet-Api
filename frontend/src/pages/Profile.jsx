import { useAuth } from "../hooks/useAuth.js";
import { useEffect, useState } from "react";
import api from "../services/api.js";

export default function Profile() {
  const { user } = useAuth();
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    if (user) {
      api.get("/users/me/orders").then((res) => setOrders(res.data));
    }
  }, [user]);

  if (!user) return <p>Connectez-vous.</p>;

  return (
    <div className="grid" style={{ gap: 10 }}>
      <div className="card" style={{ padding: 14 }}>
        <h2>Profil</h2>
        <p>{user.name}</p>
        <p>{user.email}</p>
      </div>
      <div className="card" style={{ padding: 14 }}>
        <h3>Historique commandes</h3>
        {orders.map((o) => (
          <div key={o.id} style={{ borderBottom: "1px solid var(--border)", paddingBottom: 8, marginBottom: 8 }}>
            <strong>#{o.id}</strong> — {o.status} — € {Number(o.total).toFixed(2)}
          </div>
        ))}
      </div>
    </div>
  );
}