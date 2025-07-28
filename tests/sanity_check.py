print("Running test sanity check...")

from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://nget.digipay.my/plans/postpaid/PBH6100266")
        page.wait_for_timeout(2000)
        browser.close()

if __name__ == "__main__":
    run()
