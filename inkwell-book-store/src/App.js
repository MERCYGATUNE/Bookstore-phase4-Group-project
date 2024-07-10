
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Navbar from './Components/Navbar';
import Booklist from './Components/Booklist';
import BookDetail from './Components/BookDetail';
import Cart from './Components/Cart';
import Profile from './Components/Profile';
import SignupForm from './Components/SignupForm';
import LoginForm from './Components/LoginForm';
import './App.css';

const App = () => {
  return (
    <Router>
      <Navbar />
      <div className="container">
        <Switch>
          <Route path="/" exact component={Booklist} />
          <Route path="/books/:id" component={BookDetail} />
          <Route path="/cart" component={Cart} />
          <Route path="/profile" component={Profile} />
          <Route path="/signup" component={SignupForm} />
          <Route path="/login" component={LoginForm} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;