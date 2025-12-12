import { createContext, useState, useEffect } from "react";

export const CartContext = createContext(null);

export function CartProvider({ children }) {
  const [items, setItems] = useState(() => {
    const stored = localStorage.getItem("motommerce_cart");
    return stored ? JSON.parse(stored) : [];
  });

  useEffect(() => {
    localStorage.setItem("motommerce_cart", JSON.stringify(items));
  }, [items]);

  const add = (product, qty = 1) => {
    setItems((prev) => {
      const existing = prev.find((p) => p.id === product.id);
      if (existing) {
        return prev.map((p) => (p.id === product.id ? { ...p, qty: p.qty + qty } : p));
      }
      return [...prev, { ...product, qty }];
    });
  };

  const remove = (id) => setItems((prev) => prev.filter((p) => p.id !== id));
  const updateQty = (id, qty) => setItems((prev) => prev.map((p) => (p.id === id ? { ...p, qty } : p)));
  const total = items.reduce((sum, p) => sum + p.price * p.qty, 0);

  return <CartContext.Provider value={{ items, add, remove, updateQty, total }}>{children}</CartContext.Provider>;
}