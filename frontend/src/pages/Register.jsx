import { useState } from "react";
import api from "../services/api.js";
import { useNavigate } from "react-router-dom";

export default function Register() {
  const [form, setForm] = useState({ email: "", full_name: "", password: "", address: "" });
  const navigate = useNavigate();

  const submit = async () => {
    await api.post("/users/", form);
    navigate("/login");
  };

  return (
    <div className="card" style={{ padding: 16, maxWidth: 420, margin: "0 auto" }}>
      <h2>Inscription</h2>
      {["email", "full_name", "password", "address"].map((f) => (
        <input key={f} placeholder={f} type={f === "password" ? "password" : "text"} value={form[f]} onChange={(e) => setForm({ ...form, [f]: e.target.value })} />
      ))}
      <button className="button" style={{ marginTop: 10, width: "100%" }} onClick={submit}>Créer un compte</button>
    </div>
  );
}