import pytest
from playwright.sync_api import sync_playwright
import os

os.makedirs("recordings", exist_ok=True)

def test_e2e_npl():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="recordings/",
        )
        page = context.new_page()
        page.goto("https://nget.digipay.my/plans/postpaid/PBH6100266")
        page.wait_for_timeout(2000)

        #Plan/Product Page
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Proceed").click()

        # Choose Your Next Step page
        page.get_by_text("Get New Number").click()
        page.wait_for_timeout(2000)
        page.locator("#serviceModal").get_by_role("button", name="Proceed").click()

        # select-sim page
        page.wait_for_timeout(2000)
        page.get_by_role("radio").first.check()

        # device-compatible page
        page.wait_for_timeout(2000)
        page.get_by_role("checkbox", name="I confirm that my device is").check()
        page.wait_for_timeout(2000)
        page.locator("form").click()
        page.get_by_role("button", name="Proceed").click()

        # ID verification page
        page.wait_for_timeout(2000)

        # Skip eKYC
        page1 = context.new_page()
        page1.goto("https://nget.digipay.my/plans/postpaid/skipekyc/update/true")
        page.wait_for_timeout(2000)
        page1.close()

        # ID verification page
        page.wait_for_timeout(2000)
        page.get_by_role("textbox", name="IC number").click()
        page.get_by_role("textbox", name="IC number").fill("880725010002")
        page.wait_for_timeout(2000)
        page.get_by_role("checkbox", name="I agree to the  Terms and").check()

        # Quickly perform recaptcha! 20seconds!
        page.wait_for_timeout(20000)

        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Check Eligibility").click()

        page.wait_for_timeout(2000)
        
        # Select new number page
        page.wait_for_timeout(2000)
        page.get_by_role("textbox", name="Search a mobile number (Enter").click()
        page.wait_for_timeout(2000)

        # Do a loop here to keep retry with random four number
        page.get_by_role("textbox", name="Search a mobile number (Enter").fill("6754")
        page.get_by_role("textbox", name="Search a mobile number (Enter").press("Enter")
        page.wait_for_timeout(10000)
        page.get_by_role("button", name="Proceed").click()

        # Select new Supplementary number page
        # expect(page.locator("h5")).to_match_aria_snapshot("- heading \"Supplementary Line\" [level=5]")
        # expect(page.locator("body")).to_match_aria_snapshot("- heading \"Add Supplementary Line(s)\" [level=3]")
        page.wait_for_timeout(1000)
        page.get_by_role("navigation").locator("div").first.click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Proceed").click()

        # Your Selection page        
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Proceed").click()
        
        # expect(page.locator("body")).to_match_aria_snapshot("- heading \"Check Out Details\" [level=5]")        
        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Full Name").click()
        
        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Full Name").fill("EVELYN NPLSTG")

        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Contact Number").click()
        
        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Contact Number").fill("601139221663")

        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Email Address").click()

        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Email Address").fill("eve.keoy@infrontconsulting.com.my")

        # expect(page.locator("body")).to_match_aria_snapshot("- heading \"Address Details\" [level=5]")
        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Address Line 1").click()
        page.get_by_role("textbox", name="Address Line 1").fill("16, Jalan Kerja Air Lama Satu,")

        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Address Line 2").click()
        page.get_by_role("textbox", name="Address Line 2").fill("Taman Shuet Liang")

        page.wait_for_timeout(1000)
        page.get_by_role("textbox", name="Address Line 3").click()
        page.get_by_role("textbox", name="Address Line 3").fill("Topeng Kembar")

        page.wait_for_timeout(1000)
        page.locator(".col-lg-7").click()
        page.get_by_role("textbox", name="Postcode").click()
        page.get_by_role("textbox", name="Postcode").fill("68000")

        page.wait_for_timeout(2000)
        # expect(page.get_by_label("State")).to_match_aria_snapshot("- combobox \"State\":\n  - option \"Select\" [disabled]\n  - option \"Johor\"\n  - option \"Kedah\"\n  - option \"Kelantan\"\n  - option \"Melaka\"\n  - option \"Negeri Sembilan\"\n  - option \"Pahang\"\n  - option \"Perak\"\n  - option \"Perlis\"\n  - option \"Penang\"\n  - option \"Sabah\"\n  - option \"Sarawak\"\n  - option \"Selangor\" [selected]\n  - option \"Terengganu\"\n  - option \"Kuala Lumpur\"\n  - option \"Labuan\"\n  - option \"Putrajaya\"")
        page.get_by_role("button", name="Next").click()

        page.wait_for_timeout(2000)
        # expect(page.locator("body")).to_match_aria_snapshot("- heading \"Summary of transaction\" [level=2]")
        page.get_by_text("All of your favourite banks").click()

        page.wait_for_timeout(2000)
        page.get_by_role("link", name="Select bank").click()

        page.wait_for_timeout(2000)
        page.get_by_role("link", name="Maybank2U").click()

        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Next").click()

        page.wait_for_timeout(2000)
        page.get_by_role("textbox", name="User Id").click()

        page.wait_for_timeout(2000)
        # expect(page.get_by_role("form")).to_match_aria_snapshot("- text: Sign in to continue")
        
        page.wait_for_timeout(2000)
        page.get_by_text("User Id Password Sign in").click()
        
        page.wait_for_timeout(2000)
        page.get_by_role("textbox", name="User Id").click()
        
        page.wait_for_timeout(2000)
        page.get_by_role("textbox", name="User Id").fill("1111")
        
        page.wait_for_timeout(2000)
        page.get_by_role("textbox", name="Password").click()
        
        page.wait_for_timeout(2000) 
        page.get_by_role("textbox", name="Password").fill("1111")
        
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Sign in").click()
        
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Confirm").click()
        
        # expect(page.locator("body")).to_match_aria_snapshot("- text: Your account has been deducted")
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Continue with Transaction").click()

        # ---------------------
        page.wait_for_timeout(10000)
        context.close()
        browser.close()

if __name__ == "__main__":
    test_e2e_npl()
