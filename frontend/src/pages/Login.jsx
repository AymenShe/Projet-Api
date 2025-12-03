import { useState } from "react";
import { useAuth } from "../hooks/useAuth.js";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const { login } = useAuth();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const submit = async () => {
    await login(email, password);
    navigate("/");
  };

  return (
    <div className="card" style={{ padding: 16, maxWidth: 420, margin: "0 auto" }}>
      <h2>Connexion</h2>
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
