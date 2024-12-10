import React, { useState, useEffect } from "react";

const ChefDashboard = () => {
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        fetch("/api/orders")
            .then((res) => res.json())
            .then((data) => setOrders(data));
    }, []);

    const markAsReady = (orderId) => {
        fetch(`/api/orders/${orderId}`, {
            method: "PATCH",
        }).then(() => {
            setOrders(orders.map((order) =>
                order.id === orderId ? { ...order, status: "Ready" } : order
            ));
        });
    };

    return (
        <div>
            <h2>Chef Dashboard</h2>
            <ul>
                {orders.map((order) => (
                    <li key={order.id}>
                        {order.name} - {order.menuSelection} - {order.status}
                        <button onClick={() => markAsReady(order.id)}>Mark as Ready</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default ChefDashboard;
