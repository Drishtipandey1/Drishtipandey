
"""
Topic 11: Working with APIs
-----------------------------------------
Theory:
- API = Application Programming Interface. Web APIs usually use HTTP + JSON.
- RESTful concepts: endpoints (URL), methods (GET/POST/PUT/DELETE), status codes.
- In Python, 'requests' is common, but built-in 'urllib' or 'http.client' also exist.
- Since internet may be unavailable during testing, we mock sample data.
- Always handle errors and timeouts.
"""

import json
from urllib import request, error

def fetch_json(url, timeout=10):
    """Fetch JSON from an API URL (demo)."""
    try:
        with request.urlopen(url, timeout=timeout) as resp:
            if resp.status != 200:
                raise RuntimeError(f"HTTP {resp.status}")
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except error.URLError as e:
        # Offline demo: return mocked data
        print("Network error, using mock:", e)
        return {"id": 1, "title": "mocked todo", "completed": False}

# Example: JSONPlaceholder (public fake API)
todo = fetch_json("https://jsonplaceholder.typicode.com/todos/1")
print("API result:", todo)

# Parsing JSON
title = todo.get("title")
completed = todo.get("completed", False)
print(f"Todo: {title} | Done? {completed}")
