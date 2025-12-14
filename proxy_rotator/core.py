import random
import requests
import time


class Proxy:
    def __init__(self, url: str):
        self.url = url
        self.alive = True
        self.latency = None

    def as_requests(self):
        return {"http": self.url, "https": self.url}


class ProxyPool:
    def __init__(self, proxies: list[str], timeout: int = 10):
        self.timeout = timeout
        self.proxies = [Proxy(p) for p in proxies]

    def _check(self, proxy: Proxy):
        start = time.time()
        try:
            requests.get(
                "https://httpbin.org/ip",
                proxies=proxy.as_requests(),
                timeout=self.timeout,
            )
            proxy.latency = time.time() - start
            proxy.alive = True
        except Exception:
            proxy.alive = False

    def refresh(self):
        for proxy in self.proxies:
            self._check(proxy)

    def get(self, mode: str = "random") -> Proxy:
        alive = [p for p in self.proxies if p.alive]
        if not alive:
            raise RuntimeError("No alive proxies")

        if mode == "fastest":
            return min(alive, key=lambda p: p.latency or float("inf"))

        return random.choice(alive)
