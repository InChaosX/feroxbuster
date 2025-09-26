# dirhuntr


Web Security Academy > Information disclosure > Exploiting > Lab





`dirhuntr` is a lightweight and customizable **Python tool** for directory and file enumeration.  
It uses asynchronous requests (`aiohttp` + `asyncio`) for fast and efficient discovery of hidden or unlinked web resources.  
The goal is to provide a simple starting point similar to tools like `feroxbuster` or `gobuster`, tailored for testing your own environments.  

> ⚠️ **Legal Disclaimer**  
> Do **not** use this tool on systems you do not own or do not have explicit permission to test. Unauthorized scanning may be illegal and could lead to serious consequences.  
> Use responsibly in staging, testing, or lab environments only.  

---

## Features
- Asynchronous HTTP requests (high speed).
- Custom wordlist support.
- Detects common HTTP status codes:
  - `200` → Resource exists and accessible.
  - `301/302` → Redirects.
  - `401` → Resource exists but requires authentication.
  - `403` → Resource exists but access is forbidden.
- Results saved to `results.txt`.
- Simple to extend with file extensions, JSON output, or rate limiting.

---

## Requirements
- Python **3.9+**
- Install dependencies:
  ```bash
  pip install -r requirements.txt
