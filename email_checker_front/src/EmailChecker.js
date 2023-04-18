import React, { useState } from 'react';
import axios from 'axios';
import './EmailChecker.css';

function EmailChecker() {
  const [email, setEmail] = useState('');
  const [result, setResult] = useState({});
  const [isValid, setIsValid] = useState(null);

  const handleChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:8000/api/linked/', { email })
      .then((response) => {
        setResult(response.data);
        setIsValid(response.status === 200);
      })
      .catch((error) => {
        console.log(error);
      });

    axios.post('http://localhost:8000/api/validate/', { email })
      .then((response) => {
        setIsValid(response.status === 200);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  return (
    <div className="email-checker-container">
      <h2>Email Checker</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Email:
          <input type="email" value={email} onChange={handleChange} />
        </label>
        <button type="submit">Check</button>
      </form>
      {isValid !== null && (
        <div className="validation-container">
          <h3>Validation:</h3>
          <span className={`validation-status ${isValid ? 'valid' : 'invalid'}`}>
            {isValid ? 'Valid email address' : 'Invalid email address'}
          </span>
        </div>
      )}
      {Object.keys(result).length !== 0 && (
        <div className="result-container">
          <h3>Result:</h3>
          <ul>
            {Object.keys(result).map((key) => (
              <li key={key}>
                <span className="service-name">{key}:</span>
                <span className={`status ${result[key].status.toLowerCase()}`}>
                  {result[key].status}
                </span>
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default EmailChecker;
