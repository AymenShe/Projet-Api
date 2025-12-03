import { createContext, useEffect, useState } from "react";
import api, { setToken } from "../services/api.js";

export const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);

  useEffect(() => {
    const stored = localStorage.getItem("motommerce_auth");
    if (stored) {
      const { token, user } = JSON.parse(stored);
      setToken(token);
      setUser(user);
    }
  }, []);

  const login = async (email, password) => {
    const { data } = await api.post("/users/login", { email, password });
    setToken(data.token);
    setUser(data.user);
    localStorage.setItem("motommerce_auth", JSON.stringify({ token: data.token, user: data.user }));
  };

  const logout = () => {
    setToken(null);
    setUser(null);
    localStorage.removeItem("motommerce_auth");
  };

  return <AuthContext.Provider value={{ user, login, logout }}>{children}</AuthContext.Provider>;
}