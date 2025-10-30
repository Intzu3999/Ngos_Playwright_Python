from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import time
import os

load_dotenv()

os.makedirs("recordings", exist_ok=True)

def test_esim_ekyc_cookie():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="recordings/",
        )
        page = context.new_page()
       
        #Plan/Product Page
        page.goto("https://dev-get.digipay.my/esim/esim-switch")
        # page.goto("https://dev-get.digipay.my/esim/replacement")
        # page.goto("https://dev-get.digipay.my/esim/new")
        # page.goto("https://dev-get.digipay.my/esim/activation")
        # context.clear_cookies()

        page.wait_for_timeout(2000)
        page.get_by_label("I confirm that my device is").check()
        page.wait_for_timeout(2000)
        button = page.get_by_role("button", name="Next").or_(page.get_by_role("button", name="Submit"))
        button.click()

        page.wait_for_timeout(2000)
        page.get_by_text("MyKad").click()
        page.wait_for_timeout(2000)
        button = page.get_by_role("button", name="Next").or_(page.get_by_role("button", name="Submit"))
        button.click()

        page.wait_for_timeout(2000)
        page.get_by_placeholder("Account holder ID number").click()
        page.get_by_placeholder("Account holder ID number").fill("880910020002")
        # page.get_by_placeholder("Account holder ID number").click(modifiers=["ControlOrMeta"])
        page.wait_for_timeout(2000)
        page.get_by_placeholder("Mobile number").click()
        page.get_by_placeholder("Mobile number").fill("601140106416")

        page.wait_for_timeout(60000)
        countdown(60)
        
        page.get_by_role("button", name="Next").click()

        page.wait_for_timeout(1000)
        page.locator("input[name=\"otp1\"]").click()

        page.wait_for_timeout(200)
        page.locator("input[name=\"otp1\"]").fill("6")

        page.wait_for_timeout(200)        
        page.locator("input[name=\"otp2\"]").fill("5")

        page.wait_for_timeout(200)
        page.locator("input[name=\"otp3\"]").fill("4")

        page.wait_for_timeout(200)
        page.locator("input[name=\"otp4\"]").fill("4")

        page.wait_for_timeout(200)
        page.locator("input[name=\"otp5\"]").fill("5")

        page.wait_for_timeout(200)
        page.locator("input[name=\"otp6\"]").fill("6")

        page.wait_for_timeout(200)        
        page.get_by_role("button", name="Submit").click()

        cookies = context.cookies()
        print("Cookies:", cookies)

        page.wait_for_timeout(5000)
        context.close()
        browser.close()


def countdown(seconds):
    for i in range(seconds, 0, -1):
        print(f"countdown... {i}", end="\r")
        time.sleep(1)
    print(" " * 50, end="\r")  # Clear the line after countdown is done