import pytest
from playwright.sync_api import sync_playwright
import os
from datetime import datetime
import random

def complete_payment(page, method: str):
    method = method.lower()
    page.wait_for_timeout(400)

    if method == "fpx":
        page.get_by_text("All of your favourite banks").click()
        page.get_by_role("link", name="Select bank").click()
        page.get_by_role("link", name="Maybank2U").click()
        page.get_by_role("button", name="Next").click()
        page.get_by_role("textbox", name="User Id").fill(os.getenv("M2U_FXP_ID"))
        page.get_by_role("textbox", name="Password").fill(os.getenv("M2U_FXP_PASSWORD"))
        page.get_by_role("button", name="Sign in").click()
        page.get_by_role("button", name="Confirm").click()
        page.get_by_role("button", name="Continue with Transaction").click()

    elif method == "visa":
        # Add Visa card logic here
        pass

    elif method == "mastercard":
        # Add Mastercard logic here
        pass

    elif method == "creditcard":
        # Generic Credit Card flow
        pass

    elif method == "ewallet":
        # Add eWallet logic
        pass

    else:
        raise ValueError(f"Unsupported payment method: {method}")

    page.wait_for_timeout(1000)

def choose_next_step(page, option: str):
    option = option.lower()
    page.wait_for_timeout(2000)
    if option == "npl":
        page.get_by_text("Get New Number").click()
    elif option == "cop":
        page.get_by_text("Change Plans").click()
    elif option == "mnp":
        page.get_by_text("Switch to CelcomDigi Keep").click()
    else:
        raise ValueError(f"Invalid next step option: {option}")

    page.wait_for_timeout(2000)
    page.locator("#serviceModal").get_by_role("button", name="Proceed").click()

def choose_sim_type(page, sim_type: str):
    sim_type = sim_type.lower()
    if sim_type == "esim":
        page.get_by_role("radio").first.check()
    elif sim_type == "psim":
        page.get_by_role("radio").last.check()
    else:
        raise ValueError(f"Unsupported SIM type: {sim_type}")

    page.wait_for_timeout(200)

def skip_ekyc(context, page):
    page1 = context.new_page()
    page1.goto("https://nget.digipay.my/plans/postpaid/skipekyc/update/true")
    page.wait_for_timeout(400)
    page1.close()

def generate_random_nric():
    now = datetime.now()
    
    yy = "88"
    mm = f"{now.month:02d}"
    dd = f"{now.day:02d}" 
    xx = "14"
    last_four_digit = f"{now.strftime('%H%M%S')[-4:]}" 

    return yy + mm + dd + xx + last_four_digit

def enter_new_nric(page):
    new_nric = generate_random_nric()

    page.wait_for_timeout(400)
    page.get_by_role("textbox", name="IC number").click()
    page.get_by_role("textbox", name="IC number").fill(new_nric)
    page.wait_for_timeout(400)
    page.get_by_role("checkbox", name="I agree to the Terms and").check()

def enter_existing_nric(page, existing_nric:str):
    page.wait_for_timeout(400)
    page.get_by_role("textbox", name="IC number").click()
    page.get_by_role("textbox", name="IC number").fill(existing_nric)
    page.wait_for_timeout(400)
    page.get_by_role("checkbox", name="I agree to the Terms and").check()

def generate_random_four_digit():
    return str(random.randint(1000, 9999))

def npl_select_principal_msisdn(page, max_retries: int = 10): 
    for attempt in range(max_retries):
        four_digit = generate_random_four_digit()

        print(f"[Attempt {attempt+1}] Searching: {four_digit}")

        text_field = page.get_by_role("textbox", name="Search a mobile number (Enter")
        text_field.fill(four_digit)
        text_field.press("Enter")

        msisdn_list = page.get_by_role("navigation").locator("div").first

        if msisdn_list.count() > 0:
            msisdn_list.nth(0).click() # i need to improve this.. click the first option
            page.get_by_role("button", name="Proceed").click()
            selected_msisdn = msisdn_list.nth(0).inner_text()
            print(f"✅ Selected MSISDN: {selected_msisdn}")
            page.wait_for_timeout(400)

            if page.locator("h5:has-text('Supplementary Line')").count() > 0:
                print("✅ Successfully Reserved MSISDN")
                return
            else:
                print("⚠️Failed to reserve MSISDN, retrying...")

        else:
            print("No MSISDN found, retrying...")

    raise Exception("❌ Failed too many attempts.")
