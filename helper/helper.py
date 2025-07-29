import pytest
from playwright.sync_api import sync_playwright
import os

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

def skip_ekyc(page):
    page1 = context.new_page()
    page1.goto("https://nget.digipay.my/plans/postpaid/skipekyc/update/true")
    page.wait_for_timeout(400)
    page1.close()