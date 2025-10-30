from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

from scripts.common import enter_otp, skip_ekyc_prestg

load_dotenv()

os.makedirs("recordings", exist_ok=True)

def test_dealer_link():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="recordings/",
        )
        page = context.new_page()

        # url = "https://nget.digipay.my/esim?DealerCode=INT01-B0062&DealerUserId=MEFFENZA"
        url = "https://dev-get.digipay.my/plans/postpaid/verification/PBH6100253?DealerCode=INT01-B0062&DealerUserId=MEFFENZA"
        #Plan/Product Page
        page.goto(url)

        skip_ekyc_prestg(context,page)

        cookies = context.cookies()
        print("Cookies Before Login:", cookies)

        # heading_name = page.get_by_role("heading", name="Order")
        # heading_name.wait_for(state="visible")
        
        # button = page.get_by_role("button", name="Proceed")
        # button.wait_for(state="visible")
        # button.click()
        print("step")
        page.get_by_text("Convert to eSIM Convert your").click()

        page.wait_for_timeout(1000)

        print("checkbox")
        page.get_by_role("checkbox", name="I confirm that my device is").check()

        print("submit")
        button = page.get_by_role("button", name="Submit")
        button.wait_for(state="visible")
        button.click()

        print("wait for heading visible")
        element = page.get_by_role("heading", name="Choose Identification Type")
        element.wait_for(state="visible")

        print("MyKad")
        page.get_by_text("MyKad").click()

        print("Next")
        button = page.get_by_role("button", name="Next")
        button.wait_for(state="visible")
        button.click()

        print("wait for heading visible")
        element = page.get_by_role("heading", name="Identity Verification")
        element.wait_for(state="visible")
        
        # page.get_by_text("Convert to eSIM Identity").click()

        print("ID")
        page.get_by_role("textbox", name="Account holder ID number").click()
        page.get_by_role("textbox", name="Account holder ID number").fill("930101018071")

        # page.get_by_role("textbox", name="Enter your details below to").click()
        # page.get_by_text("Convert to eSIM Identity").click()

        print("MSISDN")
        page.get_by_role("textbox", name="Enter your details below to").click()
        page.get_by_role("textbox", name="Enter your details below to").fill("60104368280")

        print("60 second - Recaptcha")
        page.wait_for_timeout(60000)
        # Recaptcha
        # page.locator("iframe[name=\"a-utiwwkajc6xs\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
        
        print("Next")
        button = page.locator("section form div").filter(has_text="Next")
        button.wait_for(state="visible")
        button.click()
        
        print("wait for heading visible")
        element = page.get_by_role("heading", name="Identity Verification")
        element.wait_for(state="visible")

        print("otp")
        enter_otp(page,6,5,4,4,5,6)
        # page.locator("input[name=\"otp1\"]").fill("6")
        # page.locator("input[name=\"otp2\"]").fill("5")
        # page.locator("input[name=\"otp3\"]").fill("4")
        # page.locator("input[name=\"otp4\"]").fill("4")
        # page.locator("input[name=\"otp5\"]").fill("5")
        # page.locator("input[name=\"otp6\"]").fill("6")
        # page.get_by_role("button", name="Submit").click()

        cookies = context.cookies()
        print("Cookies After Login:", cookies)

        # choose_your_next_step(page, "npl")

        # choose_sim_type(page, "esim")

        # check_device_compatibility_link(page,False)

        # esim_compatible_checkbox(page)

        # skip_ekyc(context,page)

        # terms_and_conditions_link_and_checkbox(context,page,False)

        # enter_new_nric(context,page)

        cookies = context.cookies()
        print("All Cookies:", cookies)
        
        page.wait_for_timeout(10000)
        context.close()
        browser.close()

if __name__ == "__main__":
    test_dealer_link()