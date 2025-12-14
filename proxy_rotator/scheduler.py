import time
import threading


class ProxyScheduler:
    def __init__(self, pool, interval_minutes=10, mode="random"):
        self.pool = pool
        self.interval = interval_minutes * 60
        self.mode = mode
        self.current = None
        self._stop = False

    def start(self):
        def loop():
            while not self._stop:
                self.pool.refresh()
                self.current = self.pool.get(self.mode)
                print(f"[proxy_rotator] Switched → {self.current.url}")
                time.sleep(self.interval)

        t = threading.Thread(target=loop, daemon=True)
        t.start()

    def stop(self):
        self._stop = True
