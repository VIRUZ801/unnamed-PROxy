import requests


class ProxyClient:
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def get(self, url, **kwargs):
        proxy = self.scheduler.current
        if not proxy:
            raise RuntimeError("ProxyScheduler not started")

        return requests.get(
            url,
            proxies=proxy.as_requests(),
            **kwargs,
        )

    def post(self, url, **kwargs):
        proxy = self.scheduler.current
        if not proxy:
            raise RuntimeError("ProxyScheduler not started")

        return requests.post(
            url,
            proxies=proxy.as_requests(),
            **kwargs,
        )
