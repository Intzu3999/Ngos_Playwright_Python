from playwright.sync_api import sync_playwright
import os

def complete_payment(page, method: str):
    method = method.lower()
    page.wait_for_timeout(1000)

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