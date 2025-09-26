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
  pip install aiohttp aiofiles

  save code in file name :  dir_enum_async.py

  run script : python dir_enum_async.py 

  


## Usage

Prepare a wordlist.txt file (each line = one path).
Edit the script and set your target URL:

TARGET = "https://example.com"   # Change this to your test environment
WORDLIST_FILE = "wordlist.txt"


## Example Output

Example lines from results.txt:

200 https://test.local/admin
401 https://test.local/secret-panel
403 https://test.local/config.php


200 → File/page exists and is accessible.

401 → File/page exists but requires authentication.

403 → File/page exists but is forbidden.

404 or no entry → File/page does not exist.


## Results
Results will be saved in:

results.txt

