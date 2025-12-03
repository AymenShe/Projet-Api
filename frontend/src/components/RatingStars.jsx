export default function RatingStars({ rating = 0 }) {
  const stars = Array.from({ length: 5 }, (_, i) => i < Math.round(rating));
  return (
    <div style={{ display: "flex", gap: 4 }}>
      {stars.map((filled, idx) => <span key={idx}>{filled ? "\u2605" : "\u2606"}</span>)}
    </div>
  );
}
