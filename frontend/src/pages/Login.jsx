import { useState } from "react";
import { useAuth } from "../hooks/useAuth.js";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const { login } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const submit = async () => {
    setError("");
    try {
      await login(email, password);
      navigate("/");
    } catch (e) {
      setError("Email ou mot de passe incorrect");
    }
  };

  return (
    <div className="card" style={{ padding: 16, maxWidth: 420, margin: "0 auto" }}>
      <h2>Connexion</h2>
      {error && (
        <div style={{
          backgroundColor: "rgba(255, 100, 100, 0.1)",
          color: "var(--error, #ef4444)",
          padding: "8px 12px",
          borderRadius: "6px",
          marginBottom: "12px",
          fontSize: "0.9rem",
          textAlign: "center"
        }}>
          {error}
        </div>
      )}
      <input placeholder="Email" value={email} onChange={(e) => setEmail(e.target.value)} />
      <input placeholder="Mot de passe" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      <button className="button" style={{ marginTop: 10, width: "100%" }} onClick={submit}>Se connecter</button>
      <p style={{ marginTop: 12, textAlign: "center" }}>
        Pas de compte ?{" "}
        <a href="/register" style={{ color: "var(--accent)" }}>
          S'inscrire
        </a>
      </p>
    </div>
  );
}
