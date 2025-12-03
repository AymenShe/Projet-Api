import { useAuth } from "../hooks/useAuth.js";
import { useEffect, useState } from "react";
import api from "../services/api.js";

function OrderItem({ item }) {
  const [product, setProduct] = useState(null);

  useEffect(() => {
    api.get(`/products/${item.product_id}`).then((res) => setProduct(res.data));
  }, [item.product_id]);

  if (!product) return <div>Chargement...</div>;

  return (
    <div style={{ marginLeft: 10, fontSize: "0.9em", color: "var(--muted)" }}>
      {product.name} x {item.quantity} - {(item.price * item.quantity).toFixed(2)} €
    </div>
  );
}

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
            <strong>#{o.id}</strong> - {o.status} - Total: {Number(o.items.reduce((a, i) => a + i.price * i.quantity, 0)).toFixed(2)} €
            {o.items.map((i) => (
              <OrderItem key={i.id} item={i} />
            ))}
          </div>
        ))}
      </div>
    </div>
  );
}