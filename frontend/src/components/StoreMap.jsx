import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "leaflet/dist/leaflet.css";
import L from "leaflet";

import icon from "leaflet/dist/images/marker-icon.png";
import iconShadow from "leaflet/dist/images/marker-shadow.png";

let DefaultIcon = L.icon({
    iconUrl: icon,
    shadowUrl: iconShadow,
    iconSize: [25, 41],
    iconAnchor: [12, 41],
});

L.Marker.prototype.options.icon = DefaultIcon;

export default function StoreMap({ stores }) {
    const defaultCenter = [48.8566, 2.3522]; // Paris
    const center = stores.length > 0 ? [stores[0].latitude, stores[0].longitude] : defaultCenter;

    return (
        <MapContainer center={center} zoom={12} style={{ height: "500px", width: "100%", borderRadius: "12px", zIndex: 0 }}>
            <TileLayer
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {stores.map((store) => (
                <Marker key={store.id} position={[store.latitude, store.longitude]}>
                    <Popup>
                        <strong>{store.name}</strong>
                        <br />
                        {store.address}
                    </Popup>
                </Marker>
            ))}
        </MapContainer>
    );
}
