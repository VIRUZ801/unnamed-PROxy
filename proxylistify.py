import sys
from pathlib import Path

ENV_TEMPLATE = """# Proxy rotation
PROXY_LIST={proxies}
ROTATION_MINUTES=5
SELECTION_MODE=random
TIMEOUT=10

# CLI / headless browser
HEADLESS=true
ASYNC=false
"""

def main():
    if len(sys.argv) != 2:
        print("Usage: python proxylistify.py proxies.txt")
        print("always use dir or ls to double check files ok?")
        sys.exit(1)

    proxies = [
        line.strip()
        for line in Path(sys.argv[1]).read_text().splitlines()
        if line.strip()
    ]

    env_content = ENV_TEMPLATE.format(proxies=",".join(proxies))
    Path(".env").write_text(env_content, encoding="utf-8")

    print(f" .env created with {len(proxies)} proxies")

if __name__ == "__main__":
    main()
