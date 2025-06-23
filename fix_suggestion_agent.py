import requests
import json

def suggest_fix(error_summary: str) -> str:
    payload = {
        "model": "tinyllama",
        "messages": [
            {
                "role": "user",
                "content": f"Given the error below from a Node.js app, suggest a fix in one line:\n\n{error_summary}"
            }
        ]
    }

    try:
        response = requests.post("http://localhost:11434/api/chat", json=payload, stream=True)
        response.raise_for_status()
        full_response = ""
        for line in response.iter_lines():
            if line:
                try:
                    message = line.decode('utf-8').strip()
                    json_part = message.split("data:")[-1].strip()
                    parsed = json.loads(json_part)
                    full_response += parsed.get("message", {}).get("content", "")
                except Exception:
                    continue
        return full_response.strip()

    except Exception as e:
        return f"Error contacting model: {str(e)}"
