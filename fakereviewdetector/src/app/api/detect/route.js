export async function POST(req) {
    try {
      const { link } = await req.json();
  
      if (!link) {
        return new Response(JSON.stringify({ error: "No link provided" }), {
          status: 400,
        });
      }
  
      // Simulating backend processing for now
      const fakeReviewProbability = Math.random(); // Replace with actual model call
  
      return new Response(JSON.stringify({ 
        message: "Review analyzed successfully", 
        fakeProbability: fakeReviewProbability 
      }), {
        status: 200,
        headers: { "Content-Type": "application/json" },
      });
  
    } catch (error) {
      return new Response(JSON.stringify({ error: "Server error" }), {
        status: 500,
      });
    }
  }
  