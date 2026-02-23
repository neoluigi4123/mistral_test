from ddgs import DDGS
import requests
import trafilatura

def web(query: str, num_results: int = 5) -> str:
    """
    Browse the web or search using DuckDuckGo.
    """
    query = query.strip()

    if query.lower().startswith(("http://", "https://")):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            response = requests.get(query, headers=headers, timeout=10)
            response.raise_for_status()

            # Use trafilatura - much better extraction
            text = trafilatura.extract(
                response.text,
                include_comments=False,
                include_tables=False,
                no_fallback=False
            )

            if text:
                # Clean up and limit
                text = ' '.join(text.split())  # Normalize whitespace
                return text[:2000]  # More reasonable limit
            
            return "Could not extract content from page."

        except Exception as e:
            return f"Error: {e}"

    else:
        results = DDGS().text(query, max_results=num_results)
        return results
    
if __name__ == "__main__":
    response = web("What is the capital of france ?")
    print(response)
