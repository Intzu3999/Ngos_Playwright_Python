from playwright.sync_api import sync_playwright
from helper.helper import generate_random_four_digit

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
            page.wait_for_timeout(1000)

            if page.locator("h5:has-text('Supplementary Line')").count() > 0:
                print("✅ Successfully Reserved MSISDN")
                return
            else:
                print("⚠️Failed to reserve MSISDN, retrying...")

        else:
            print("No MSISDN found, retrying...")

    raise Exception("❌ Failed too many attempts.")
