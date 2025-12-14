import aiohttp
import time
import random


class AsyncProxy:
    def __init__(self, url: str):
        self.url = url
        self.alive = True
        self.latency = None


class AsyncProxyPool:
    def __init__(self, proxies: list[str], timeout: int = 10):
        self.timeout = timeout
        self.proxies = [AsyncProxy(p) for p in proxies]

    async def _check(self, session, proxy):
        start = time.time()
        try:
            async with session.get(
                "https://httpbin.org/ip",
                proxy=proxy.url,
                timeout=self.timeout,
            ):
                proxy.latency = time.time() - start
                proxy.alive = True
        except Exception:
            proxy.alive = False

    async def refresh(self):
        async with aiohttp.ClientSession() as session:
            await asyncio.gather(
                *[self._check(session, p) for p in self.proxies]
            )

    async def get(self, mode="random"):
        alive = [p for p in self.proxies if p.alive]
        if not alive:
            raise RuntimeError("No alive proxies")

        if mode == "fastest":
            return min(alive, key=lambda p: p.latency or float("inf"))

        return random.choice(alive)
