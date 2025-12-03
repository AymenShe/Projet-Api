import { useParams, Link } from "react-router-dom";

export default function OrderConfirmation() {
  const { id } = useParams();
  return (
    <div className="card" style={{ padding: 18, textAlign: "center" }}>
      <h2>Merci !</h2>
      <p>Commande #{id} enregistrée.</p>
      <Link to="/track" className="button">Suivre ma commande</Link>
    </div>
  );
}