throw new Error("Intentional failure to trigger AgenticAI triage")


const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>Agentic AI DevOps Demo</title>
      <style>
        body {
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          background: linear-gradient(to right, #2c3e50, #3498db);
          color: #ecf0f1;
          text-align: center;
          padding: 100px;
        }
        h1 {
          font-size: 3em;
          margin-bottom: 20px;
        }
        p {
          font-size: 1.3em;
          max-width: 700px;
          margin: 0 auto;
        }
        .badge {
          display: inline-block;
          background: #1abc9c;
          color: #fff;
          padding: 10px 20px;
          border-radius: 30px;
          font-weight: bold;
          margin-top: 30px;
        }
      </style>
    </head>
    <body>
      <h1>🚀 Welcome to Agentic AI DevOps</h1>
      <p>This demo showcases a self-healing deployment pipeline with log triage, fix suggestion, and autonomous remediation — powered by lightweight LLMs.</p>
      <div class="badge">🔧 Agentic AI Enabled</div>
    </body>
    </html>
  `);
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`🌐 Server running on port ${PORT}`);
});
