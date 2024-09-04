// src/App.js
import React from 'react';
import { BrowserRouter as Route, Routes } from 'react-router-dom';
import Register from './components/Register';

function App() {
  return (
      <Routes>
        <Route path="/register" component={Register} />
        {/* other routes */}
      </Routes>
  );
}

export default App;


