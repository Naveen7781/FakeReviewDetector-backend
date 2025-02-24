"use client";  // Required for using useState

import { useState } from "react";
import ReviewForm from "@/components/ReviewForm";

export default function Home() {
  const handleReviewSubmit = async (link) => {
    try {
      const response = await fetch("/api/detect", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ link }),
      });

      const data = await response.json();

      if (response.ok) {
        alert(`This review is ${data.fake ? "FAKE" : "REAL"}`);
      } else {
        alert(`Error: ${data.error}`);
      }
    } catch (error) {
      console.error("Error submitting review:", error);
      alert("Server error. Try again.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <ReviewForm onSubmit={handleReviewSubmit} />
    </div>
  );
}
