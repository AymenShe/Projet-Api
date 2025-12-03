import { useContext, useState } from "react";
import { CartContext } from "../context/CartContext.jsx";
import { useNavigate } from "react-router-dom";
import api from "../services/api.js";
import MapEmbed from "../components/MapEmbed.jsx";
import { useAuth } from "../hooks/useAuth.js";

export default function Checkout() {
  const { items, total } = useContext(CartContext);
  const [deliveryType, setDeliveryType] = useState("shipping");
  const [pickupList, setPickupList] = useState([]);
  const [selectedPoint, setSelectedPoint] = useState(null);
  const [address, setAddress] = useState({ name: "", street: "", city: "", zip: "", country: "" });
  const [payment, setPayment] = useState({ cardNumber: "", name: "", exp: "", cvc: "" });
  const [paying, setPaying] = useState(false);
  const [payError, setPayError] = useState("");
  const navigate = useNavigate();
  const { user } = useAuth();

  const findPickup = async () => {
    const { data } = await api.get(`/stores/nearby?q=${address.city || "Paris"}`);
    setPickupList(data);
  };

  const pay = async () => {
    setPayError("");
    if (!user) {
      setPayError("Veuillez vous connecter pour payer.");
      return;
    }
    if (!payment.cardNumber || !payment.name || !payment.exp || !payment.cvc) {
      setPayError("Renseignez les informations de paiement.");
      return;
    }
    if (items.length === 0) {
      setPayError("Votre panier est vide.");
      return;
    }
    setPaying(true);
    const payload = {
      items: items.map((i) => ({ product_id: i.id, quantity: i.qty, price: i.price })),
      delivery_type: deliveryType === "pickup" ? "pickup" : "shipping",
      pickup_point: selectedPoint,
      payment: { cardNumber: payment.cardNumber, name: payment.name, exp: payment.exp, cvc: payment.cvc }
    };
    try {
      const { data } = await api.post(`/orders/?user_id=${user.id}`, payload);
      navigate(`/confirmation/${data.id}`);
    } catch (e) {
      setPayError("Paiement refusé ou connexion perdue.");
    } finally {
      setPaying(false);
    }
  };

  return (
    <div className="grid" style={{ gap: 12 }}>
      <div className="card" style={{ padding: 14 }}>
        <h2>Livraison</h2>
        <div className="grid" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 10 }}>
          {["shipping", "pickup"].map((mode) => (
            <label key={mode} className="card" style={{ padding: 10, border: deliveryType === mode ? "1px solid var(--accent)" : "1px solid var(--border)" }}>
              <input type="radio" name="delivery" value={mode} checked={deliveryType === mode} onChange={() => setDeliveryType(mode)} />
              {mode === "shipping" ? "Livraison a domicile" : "Point de retrait"}
            </label>
          ))}
        </div>
        <div className="grid" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 10, marginTop: 10 }}>
          {["name", "street", "city", "zip", "country"].map((field) => (
            <input key={field} placeholder={field} value={address[field]} onChange={(e) => setAddress({ ...address, [field]: e.target.value })} />
          ))}
        </div>
        {deliveryType === "pickup" && (
          <>
            <button className="button" style={{ marginTop: 10 }} onClick={findPickup}>Trouver un point</button>
            <div className="grid" style={{ gridTemplateColumns: "1fr 1fr", gap: 10, marginTop: 10 }}>
              <div>
                {pickupList.map((p) => (
                  <div key={p.id} className="card" style={{ padding: 10, border: selectedPoint?.id === p.id ? "1px solid var(--accent)" : "1px solid var(--border)" }} onClick={() => setSelectedPoint(p)}>
                    <strong>{p.name}</strong>
                    <p style={{ color: "var(--muted)" }}>{p.address}</p>
                  </div>
                ))}
              </div>
              <MapEmbed lat={selectedPoint?.lat} lng={selectedPoint?.lng} />
            </div>
          </>
        )}
        <div className="card" style={{ marginTop: 12, padding: 10 }}>
          <h3>Paiement sécurisé (simulé)</h3>
          <div className="grid" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))", gap: 10 }}>
            <input placeholder="Nom sur la carte" value={payment.name} onChange={(e) => setPayment({ ...payment, name: e.target.value })} />
            <input placeholder="Numéro de carte" value={payment.cardNumber} onChange={(e) => setPayment({ ...payment, cardNumber: e.target.value })} />
            <input placeholder="Expiration (MM/AA)" value={payment.exp} onChange={(e) => setPayment({ ...payment, exp: e.target.value })} />
            <input placeholder="CVC" value={payment.cvc} onChange={(e) => setPayment({ ...payment, cvc: e.target.value })} />
          </div>
          {payError && <p style={{ color: "salmon", marginTop: 8 }}>{payError}</p>}
        </div>
      </div>
      <div className="card" style={{ padding: 14 }}>
        <h2>Recapitulatif</h2>
        {items.map((i) => (
          <div key={i.id} style={{ display: "flex", justifyContent: "space-between" }}>
            <span>{i.name} x {i.qty}</span>
            <span>{"\u20ac " + (i.price * i.qty).toFixed(2)}</span>
          </div>
        ))}
        <div style={{ display: "flex", justifyContent: "space-between", marginTop: 12 }}>
          <strong>Total</strong><strong>{"\u20ac " + total.toFixed(2)}</strong>
        </div>
        <button className="button" style={{ marginTop: 12, width: "100%" }} disabled={paying} onClick={pay}>
          {paying ? "Paiement en cours..." : "Payer maintenant"}
        </button>
      </div>
    </div>
  );
}
