import React, { useState, useEffect } from 'react';
import './Profile.css';

const Profile = () => {
  const [user, setUser] = useState(null);

  useEffect(() => {
    fetch('/api/profile')
      .then(response => response.json())
      .then(data => setUser(data))
      .catch(error => console.error('There was an error fetching the user profile!', error));
  }, []);

  return (
    <div className="profile">
      {user ? (
        <div>
          <h1>{user.username}</h1>
          <p>Email: {user.email}</p>
          <h2>Order History</h2>
          <ul>
            {user.orders.map(order => (
              <li key={order.id}>
                Order #{order.id} - {order.total_price} on {order.order_date}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default Profile;