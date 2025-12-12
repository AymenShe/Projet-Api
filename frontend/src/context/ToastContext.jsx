import { createContext, useContext, useState, useCallback } from "react";

const ToastContext = createContext(null);

export const ToastProvider = ({ children }) => {
    const [toast, setToast] = useState(null);

    const showToast = useCallback((message, type = "info") => {
        setToast({ message, type });
        setTimeout(() => setToast(null), 3000);
    }, []);

    return (
        <ToastContext.Provider value={{ showToast }}>
            {children}
            {toast && (
                <div style={{
                    position: "fixed",
                    bottom: 20,
                    right: 20,
                    background: "var(--card-bg, #1a1a1a)",
                    color: "white",
                    padding: "12px 24px",
                    borderRadius: "8px",
                    border: "1px solid var(--accent, #646cff)",
                    boxShadow: "0 4px 6px rgba(0,0,0,0.3)",
                    zIndex: 1000,
                    animation: "slideIn 0.3s ease-out"
                }}>
                    {toast.message}
                </div>
            )}
        </ToastContext.Provider>
    );
};

export const useToast = () => {
    const context = useContext(ToastContext);
    if (!context) {
        throw new Error("useToast must be used within a ToastProvider");
    }
    return context;
};
