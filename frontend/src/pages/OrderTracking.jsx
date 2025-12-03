import { useState } from "react";
import api from "../services/api.js";

export default function OrderTracking() {
  const [orderId, setOrderId] = useState("");
  const [delivery, setDelivery] = useState(null);

  const search = async () => {
    const { data } = await api.get(`/deliveries/${orderId}`);
    setDelivery(data);
  };

  return (
    <div className="card" style={{ padding: 14 }}>
      <h2>Suivi de commande</h2>
      <input placeholder="ID commande" value={orderId} onChange={(e) => setOrderId(e.target.value)} />
      <button className="button" style={{ marginTop: 10 }} onClick={search}>Rechercher</button>
      {delivery && (
        <div style={{ marginTop: 12 }}>
          <p>Status: {delivery.status}</p>
          <ul>
            {JSON.parse(delivery.history || "[]").map((h, idx) => <li key={idx}>{h.status} - {h.at}</li>)}
          </ul>
        </div>
      )}
    </div>
  );
}