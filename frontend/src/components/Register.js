// src/components/Register.js
import React from 'react';
import '../styles/register.scss'; 
import logo from '../assets/logo.jpg'; 
import backgroundImg from '../assets/food.jpeg';
function Register() {
    return (
        <div
            className="register-container"
            style={{
                backgroundImage: `url(${backgroundImg})`,
                backgroundSize: 'cover',
                backgroundPosition: 'center',
            }}
        >
            <div className="overlay"></div> {/* Dark overlay for better text readability */}
            <div className="register-box">
                <img src={logo} alt="CookMate Logo" className="logo" />

                <h2>Welcome to CookMate</h2>
                <p className="intro-text">
                    Join the CookMate community and explore a world of culinary delights!
                    Discover new recipes, connect with fellow food enthusiasts, and take your
                    cooking skills to the next level.
                </p>

                <form className="register-form" method="POST">
                    <input
                        type="text"
                        name="username"
                        placeholder="Username"
                        required
                    />
                    <input
                        type="password"
                        name="password"
                        placeholder="Password"
                        required
                    />
                    <input
                        type="password"
                        name="password_confirm"
                        placeholder="Confirm Password"
                        required
                    />
                    <button type="submit">Create Your Account</button>
                </form>

                <p className="sign-in-link">
                    Already have an account? <a href="/login">Sign In</a>
                </p>
            </div>
        </div>
    );
}

export default Register;
