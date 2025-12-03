export default function Contact() {
  return (
    <div className="card" style={{ padding: 18, maxWidth: 720, margin: "0 auto" }}>
      <h2>Contact</h2>
      <p style={{ color: "var(--muted)" }}>Besoin d'aide ? écrivez-nous.</p>
      <div className="grid" style={{ gridTemplateColumns: "repeat(auto-fit, minmax(240px, 1fr))", gap: 12 }}>
        <input placeholder="Nom" />
        <input placeholder="Email" />
      </div>
      <textarea rows="5" placeholder="Votre message" style={{ marginTop: 10 }} />
      <button className="button" style={{ marginTop: 10 }}>Envoyer</button>
    </div>
  );
}