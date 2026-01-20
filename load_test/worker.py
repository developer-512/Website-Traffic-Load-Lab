import aiohttp, time, random, json
from datetime import datetime, timezone

with open("config/endpoints.json") as f:
    ENDPOINTS = json.load(f)

def pick_url():
    pool = []
    for e in ENDPOINTS:
        pool.extend([e["url"]] * e["weight"])
    return random.choice(pool)

async def worker(end_time, timeout, results):
    async with aiohttp.ClientSession() as session:
        while time.time() < end_time:
            url = pick_url()
            start = time.time()
            error = None
            status = None

            try:
                async with session.get(url, timeout=timeout) as r:
                    await r.text()
                    status = r.status
            except Exception as e:
                error = str(e)

            results.append({
                "ts": datetime.now(timezone.utc).isoformat(),
                "url": url,
                "time": time.time() - start,
                "status": status,
                "error": error
            })
