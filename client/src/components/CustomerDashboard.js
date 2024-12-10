import React, { useState, useEffect } from "react";

const CustomerDashboard = () => {
    const [orders, setOrders] = useState([]);

    useEffect(() => {
        fetch("/api/orders/my-orders")
            .then((res) => res.json())
            .then((data) => setOrders(data));
    }, []);

    return (
        <div>
            <h2>Your Orders</h2>
            <ul>
                {orders.map((order) => (
                    <li key={order.id}>
                        {order.menuSelection} - {order.status}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default CustomerDashboard;
