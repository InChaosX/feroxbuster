# dir_enum_async.py
import asyncio
import aiohttp
import aiofiles
import sys

TARGET = "https://0a880075030280d0adabd1c0009800d0.web-security-academy.net/"   # غيّر إلى موقعك (بيئة اختبارية)
WORDLIST_FILE = "wordlist.txt"   # ملف يحتوي كل سطر مسار محتمل (مث: admin, backup.zip)
CONCURRENCY = 20                 # عدد الطلبات المتوازية
TIMEOUT = 10

sem = asyncio.Semaphore(CONCURRENCY)

async def check_path(session, path, out_f):
    url = TARGET.rstrip("/") + "/" + path.lstrip("/")
    async with sem:
        try:
            async with session.get(url, timeout=TIMEOUT, allow_redirects=False) as resp:
                status = resp.status
                # اعتبر 200 و 301 و 302 و 401 و 403 مهماً
                if status in (200, 301, 302, 401, 403):
                    line = f"{status} {url}\n"
                    print(line.strip())
                    await out_f.write(line)
        except Exception as e:
            # تعامُل بسيط مع الأخطاء
            print(f"ERR {url} -> {e}")

async def main():
    async with aiofiles.open(WORDLIST_FILE, "r") as f:
        paths = [line.strip() for line in await f.readlines() if line.strip()]

    async with aiofiles.open("results.txt", "w") as out_f:
        timeout = aiohttp.ClientTimeout(total=None)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            tasks = [asyncio.create_task(check_path(session, p, out_f)) for p in paths]
            # تنفيذ ومراقبة التقدم
            for i in range(0, len(tasks), 1000):
                batch = tasks[i:i+1000]
                await asyncio.gather(*batch)

if __name__ == "__main__":
    asyncio.run(main())
