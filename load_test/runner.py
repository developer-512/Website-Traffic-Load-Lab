import asyncio, json, time
from .worker import worker
from .sampler import system_sampler
from .charts import generate_latency_chart
from .reporter import generate_report
from screenshots.capture import capture
from datetime import datetime, timezone

results = []
cpu = []
mem = []

def run_load_test(clients, duration, timeout):
    start = datetime.now(timezone.utc)

    capture("before_test.png")

    async def run():
        end = time.time() + duration
        await asyncio.gather(
            system_sampler(end, cpu, mem),
            *[worker(end, timeout, results) for _ in range(clients)]
        )

    asyncio.run(run())

    generate_latency_chart(results)
    generate_report(results, cpu, mem, start)

    capture("after_test.png")
