import { Link } from "react-router-dom";

export default function Hero() {
  return (
    <section className="card" style={{ padding: "36px", textAlign: "center", background: "linear-gradient(135deg, #151520, #1c1c2a)" }}>
      <h1 style={{ fontSize: 44, marginBottom: 10 }}>Accelerez votre style.</h1>
      <p style={{ color: "var(--muted)", marginBottom: 18 }}>Equipez votre prochaine viree avec notre selection premium.</p>
      <Link to="/shop" className="button">Shop now</Link>
    </section>
  );
}
