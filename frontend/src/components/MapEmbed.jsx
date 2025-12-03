export default function MapEmbed({ lat, lng }) {
  if (!lat || !lng) return null;
  const src = `https://www.openstreetmap.org/export/embed.html?bbox=${lng - 0.02}%2C${lat - 0.02}%2C${lng + 0.02}%2C${lat + 0.02}&layer=mapnik&marker=${lat}%2C${lng}`;
  return (
    <iframe
      title="map"
      style={{ width: "100%", height: 260, border: "1px solid var(--border)", borderRadius: 12 }}
      src={src}
    />
  );
}