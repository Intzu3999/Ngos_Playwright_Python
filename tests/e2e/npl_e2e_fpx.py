from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from scripts.common import check_device_compatibility_link, choose_your_next_step, choose_sim_type, esim_compatible_checkbox, complete_payment, skip_ekyc, skip_ekyc_prestg
from scripts.npl import enter_new_nric, npl_select_supplementary_msisdn, terms_and_conditions_link_and_checkbox, click_proceed_button, npl_select_principal_msisdn
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
        page.goto("https://dev-get.digipay.my/plans/postpaid/PBH6100266?DealerCode=INT01-B0062&DealerUserId=MEFFENZA")
        # context.clear_cookies()
        page.wait_for_timeout(3000)

        heading_name = page.get_by_role("heading", name="Order")
        heading_name.wait_for(state="visible")
        
        button = page.get_by_role("button", name="Proceed")
        button.wait_for(state="visible")
        button.click()

        choose_your_next_step(page, "npl")

        choose_sim_type(page, "esim")

        check_device_compatibility_link(page,False)

        esim_compatible_checkbox(page)

        skip_ekyc_prestg(context,page)

        terms_and_conditions_link_and_checkbox(context,page,False)

        enter_new_nric(context,page)

        #skip_recaptcha(page)
        
        # button = page.get_by_role("button", name="Check Eligibility")
        # button.wait_for(state="visible")
        # button.click()

        # cookies = context.cookies()
        # print("Cookies Before Login:", cookies)

        # npl_select_principal_msisdn(page, max_retries=10)        

        # npl_select_supplementary_msisdn(page, max_retries=10)

        # REVIEW YOUR SELECTION PAGE
        # heading_name = page.get_by_role("heading", name="Review Your Selection")
        # heading_name.wait_for(state="visible")
        # pass

        # heading_name = page.get_by_role("heading", name="Your Details")
        # heading_name.wait_for(state="visible")
        # pass

        # button = page.get_by_role("button", name="Proceed")
        # button.wait_for(state="visible")
        # button.click()

        # page.wait_for_timeout(200)
        # page.get_by_role("textbox", name="Full Name").click()
        # page.get_by_role("textbox", name="Full Name").fill("EVELYN NPLSTG")

        # page.wait_for_timeout(200)
        # page.get_by_role("textbox", name="Contact Number").click()
        # page.get_by_role("textbox", name="Contact Number").fill("60172383999")

        # page.wait_for_timeout(200)
        # page.get_by_role("textbox", name="Email Address").click()
        # page.get_by_role("textbox", name="Email Address").fill(os.getenv("GMAIL"))

        # page.wait_for_timeout(200)
        # page.get_by_role("textbox", name="Address Line 1").click()
        # page.get_by_role("textbox", name="Address Line 1").fill("16, Jalan Kerja Air Lama Satu,")

        # page.wait_for_timeout(200)
        # page.get_by_role("textbox", name="Address Line 2").click()
        # page.get_by_role("textbox", name="Address Line 2").fill("Taman Shuet Liang")

        # page.wait_for_timeout(200)
        # page.get_by_role("textbox", name="Address Line 3").click()
        # page.get_by_role("textbox", name="Address Line 3").fill("Topeng Kembar")

        # page.wait_for_timeout(200)
        # page.locator(".col-lg-7").click()
        # page.get_by_role("textbox", name="Postcode").click()
        # page.get_by_role("textbox", name="Postcode").fill("68000")

        # page.wait_for_timeout(200)
        # page.get_by_role("button", name="Next").click()


        # SUMMARY OF TRANSACTION PAGE
        # complete_payment(page, "fpx")

        page.wait_for_timeout(10000)
        context.close()
        browser.close()

if __name__ == "__main__":
    test_e2e_npl()
