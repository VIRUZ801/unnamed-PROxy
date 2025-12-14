from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def create_browser(proxy_url: str | None, profile_id: str, headless=True):
    opts = Options()

    opts.add_argument(f"--user-data-dir=/tmp/profile_{profile_id}")

    if proxy_url:
        opts.add_argument(f"--proxy-server={proxy_url}")

    opts.add_argument("--disable-webrtc")
    opts.add_argument("--disable-features=WebRtcHideLocalIpsWithMdns")

    if headless:
        opts.add_argument("--headless=new")

    return Chrome(options=opts)
