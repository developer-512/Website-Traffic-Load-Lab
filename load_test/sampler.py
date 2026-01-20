import psutil, asyncio, time

async def system_sampler(end_time, cpu, mem):
    while time.time() < end_time:
        cpu.append(psutil.cpu_percent())
        mem.append(psutil.virtual_memory().percent)
        await asyncio.sleep(1)
