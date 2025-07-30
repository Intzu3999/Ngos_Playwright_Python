from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from helper.initiation_pages import check_device_compatibility_link, choose_your_next_step, choose_sim_type, esim_compatible_checkbox
from helper.identity_verification import enter_new_nric, terms_and_conditions_link_and_checkbox
from helper.ekyc import skip_ekyc
from helper.npl_add_principal_number import npl_select_principal_msisdn
from helper.npl_add_supplementary_number import npl_select_supplementary_msisdn
from helper.transaction_summary import complete_payment 

import os

load_dotenv()

os.makedirs("recordings", exist_ok=True)

def test_e2e_npl():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="recordings/",
        )
        page = context.new_page()
       
        #Plan/Product Page
        page.goto("https://nget.digipay.my/plans/postpaid/PBH6100266")
        heading_name = page.get_by_role("heading", name="Order")
        heading_name.wait_for(state="visible")

        button = page.get_by_role("button", name="Proceed")
        button.wait_for(state="visible")
        button.click()

        choose_your_next_step(page, "npl")

        choose_sim_type(page, "esim")

        check_device_compatibility_link(page)

        esim_compatible_checkbox(page)

        skip_ekyc(context, page)

        enter_new_nric(context,page)

        terms_and_conditions_link_and_checkbox(page)

        #skip_recaptcha(page)
        page.wait_for_timeout(29000)
        page.get_by_role("button", name="Check Eligibility").click()
        
        npl_select_principal_msisdn(page, max_retries=10)

        # Select new Supplementary number page
        # expect(page.locator("h5")).to_match_aria_snapshot("- heading \"Supplementary Line\" [level=5]")
        # expect(page.locator("body")).to_match_aria_snapshot("- heading \"Add Supplementary Line(s)\" [level=3]")
        page.wait_for_timeout(1000)
        page.get_by_role("navigation").locator("div").first.click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Proceed").click()




        # YOUR SELECTION PAGE        
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Proceed").click()
        
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
        page.get_by_role("textbox", name="Email Address").fill(os.getenv("GMAIL"))

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

        page.wait_for_timeout(1000)
        page.get_by_role("button", name="Next").click()



        # SUMMARY OF TRANSACTION PAGE
        complete_payment(page, "mastercard")

        # 

        page.wait_for_timeout(10000)
        context.close()
        browser.close()

if __name__ == "__main__":
    test_e2e_npl()
