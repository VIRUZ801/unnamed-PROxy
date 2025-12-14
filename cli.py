import argparse
from proxy_rotator.config import PROXY_LIST, ROTATION_MINUTES, SELECTION_MODE, HEADLESS
from proxy_rotator.core import ProxyPool
from proxy_rotator.scheduler import ProxyScheduler
from proxy_rotator.daemon.service import ProxyDaemon

def main():
    parser = argparse.ArgumentParser(description="Proxy Rotator CLI")
    parser.add_argument("--daemon", action="store_true", help="Run as background daemon")
    parser.add_argument("--mode", type=str, default=SELECTION_MODE, help="Proxy selection mode")
    parser.add_argument("--interval", type=int, default=ROTATION_MINUTES, help="Rotation interval (minutes)")
    args = parser.parse_args()

    pool = ProxyPool(PROXY_LIST)
    scheduler = ProxyScheduler(pool, interval_minutes=args.interval, mode=args.mode)

    if args.daemon:
        daemon = ProxyDaemon(scheduler)
        from proxy_rotator.daemon.lifecycle import DaemonLifecycle
        lifecycle = DaemonLifecycle(daemon)
        lifecycle.run()
    else:
        scheduler.start()
        print("[CLI] Scheduler started. Press Ctrl+C to exit.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("[CLI] Exiting...")

if __name__ == "__main__":
    main()
