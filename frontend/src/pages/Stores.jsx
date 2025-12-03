import { useEffect, useState } from "react";
import api from "../services/api.js";
import StoreMap from "../components/StoreMap.jsx";

export default function Stores() {
    const [stores, setStores] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        api.get("/stores/")
            .then((res) => setStores(res.data))
            .catch((err) => console.error("Error fetching stores:", err))
            .finally(() => setLoading(false));
    }, []);

    return (
        <div className="grid" style={{ gap: 18 }}>
            <div className="card" style={{ padding: 14 }}>
                <h2>Nos Magasins</h2>
                <p style={{ marginBottom: 14, color: "var(--muted)" }}>
                    Retrouvez tous nos points de vente sur la carte ci-dessous.
                </p>
                {loading ? (
                    <p>Chargement de la carte...</p>
                ) : (
                    <StoreMap stores={stores} />
                )}
            </div>

            <div className="grid" style={{ gridTemplateColumns: "repeat(auto-fill, minmax(300px, 1fr))", gap: 14 }}>
                {stores.map((store) => (
                    <div key={store.id} className="card" style={{ padding: 14 }}>
                        <h3>{store.name}</h3>
                        <p style={{ color: "var(--muted)" }}>{store.address}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}
