"use client";

import { useState } from "react";

export default function ReviewForm({ onSubmit }) {
  const [link, setLink] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setResult(null);

    try {
      const response = await fetch("https://fakereviewdetector-backend.onrender.com/detect", {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({ link }),
      });

      if (!response.ok) {
        throw new Error(`Server responded with ${response.status}`);
      }

      const data = await response.json();
      setResult(data.result);
      onSubmit(link);
    } catch (err) {
      setError("Error connecting to server. Please try again.");
    }
  };

  return (
    <div className="max-w-md mx-auto bg-white p-6 rounded-lg shadow-md">
      <h2 className="text-xl font-bold mb-4">Fake Review Detector</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={link}
          onChange={(e) => setLink(e.target.value)}
          placeholder="Enter review link"
          className="w-full p-2 border rounded"
          required
        />
        <button type="submit" className="w-full bg-blue-500 text-white p-2 mt-2 rounded">
          Submit
        </button>
      </form>
      {result && <p className="mt-4 font-bold">Result: {result}</p>}
      {error && <p className="mt-4 text-red-500">{error}</p>}
    </div>
  );
}
