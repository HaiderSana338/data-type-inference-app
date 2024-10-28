// src/App.js
import React from 'react';
import FileUpload from './components/FileUpload';
import 'bootstrap/dist/css/bootstrap.min.css';  // Bootstrap styles
import './App.css';  // Custom app-wide styles

function App() {
  return (
    <div className="App">
      <FileUpload />
    </div>
  );
}

export default App;
