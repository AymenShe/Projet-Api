import { useContext } from "react";
import { CartContext } from "../context/CartContext.jsx";

export default function CartIcon() {
  const { items } = useContext(CartContext);
  const count = items.reduce((s, p) => s + p.qty, 0);
  return <span>?? {count}</span>;
}