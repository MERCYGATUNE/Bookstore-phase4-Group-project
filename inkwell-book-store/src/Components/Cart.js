import React, { useState, useEffect } from 'react';
import './Cart.css';

const Cart = () => {
  const [cart, setCart] = useState([]);

  useEffect(() => {
    fetch('/api/cart')
      .then(response => response.json())
      .then(data => setCart(data))
      .catch(error => console.error('There was an error fetching the cart!', error));
  }, []);

  const checkout = () => {
    // Logic to handle checkout
    fetch('/api/checkout', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(cart),
    }).then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('There was an error processing the checkout!', error));
  };

  return (
    <div className="cart">
      <h1>Cart</h1>
      <ul>
        {cart.map(item => (
          <li key={item.id}>
            {item.book.title} - ${item.book.price} x {item.quantity}
          </li>
        ))}
      </ul>
      <button onClick={checkout}>Checkout</button>
    </div>
  );
};

export default Cart;