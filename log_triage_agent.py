import requests
import json

def triage(log: str) -> dict:
    payload = {
        "model": "tinyllama",
        "messages": [
            {
                "role": "user",
                "content": f"Given the following application logs, summarize the error and suggest a possible root cause.\n\n{log}"
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
        return {"summary": full_response.strip()}

    except Exception as e:
        return {"summary": f"Error contacting model: {str(e)}"}
