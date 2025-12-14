import sys

def main():
    proxies = [line.strip() for line in sys.stdin if line.strip()]
    if not proxies:
        print("No proxies provided.", file=sys.stderr)
        sys.exit(1)

    print("PROXY_LIST=" + ",".join(proxies))

if __name__ == "__main__":
    main()
