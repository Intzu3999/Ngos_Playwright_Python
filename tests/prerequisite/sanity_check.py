print("Running test sanity check...")

from playwright.sync_api import sync_playwright

def test_launch():
    launch_successful = True
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=False)
            page = browser.new_page()
            page.goto("https://nget.digipay.my/plans/postpaid/PBH6100266")
            page.wait_for_timeout(1000)
            browser.close()
    except Exception as e:
        print(f"❌ Browser launch failed: {e}")
        launch_successful = False
    assert launch_successful, "Browser launch test failed!"
