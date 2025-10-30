from playwright.sync_api import sync_playwright
from scripts.helper import generate_random_nric, generate_random_four_digit

def enter_new_nric(context,page):
    page.set_default_timeout(60000)
    new_nric = generate_random_nric()

    heading_name = page.get_by_role("heading", name="Verify Your Identity")
    heading_name.wait_for(state="visible")

    page.get_by_role("textbox", name="IC number").click()
    page.get_by_role("textbox", name="IC number").fill(new_nric)
    page.wait_for_timeout(1000)

    # button = page.get_by_role("button", name="Proceed")
    # button.wait_for(state="visible")
    # button.click()

def enter_existing_nric(page, existing_nric:str):
    heading_name = page.get_by_role("heading", name="Verify Your Identity")
    heading_name.wait_for(state="visible")

    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="IC number").click()
    page.get_by_role("textbox", name="IC number").fill(existing_nric)
    page.wait_for_timeout(1000)

    # button = page.get_by_role("button", name="Proceed")
    # button.wait_for(state="visible")
    # button.click()

def terms_and_conditions_link_and_checkbox(context, page, check_link: bool = True):
    heading_name = page.get_by_role("heading", name="Verify Your Identity")
    heading_name.wait_for(state="visible")

    if check_link:
        with page.expect_popup() as terms_and_condition_page:
            page.get_by_role("link", name="Terms and Conditions").click()
        page2 = terms_and_condition_page.value
        heading_name = page2.get_by_role("heading", name="Terms & Conditions")
        heading_name.wait_for(state="visible")
        page2.wait_for_timeout(1000)
        page2.close()
    else:
        print("Skipping Terms and Conditions link check.")

    page.wait_for_timeout(500)
    page.locator("#termsCheck").check()
    page.wait_for_timeout(500)
    page.locator("#termsCheck").uncheck()
    page.wait_for_timeout(500)
    page.get_by_role("checkbox", name="I agree to the Terms and").check()


def click_proceed_button(page):
    button = page.get_by_role("button", name="Proceed")
    button.wait_for(state="visible")
    button.click()


def npl_select_principal_msisdn(page, max_retries: int = 10): 
    # https://nget.digipay.my/plans/postpaid/select-number/PBH6100266
    heading_name = page.get_by_role("heading", name="Select new number")
    while heading_name.wait_for(state="visible"):
        button = page.get_by_role("button", name="Proceed")
        button.wait_for(state="visible")
        button.click()


    # for attempt in range(max_retries):
    #     four_digit = generate_random_four_digit()

    #     print(f"[Attempt {attempt+1}] Searching: {four_digit}")

    #     text_field = page.get_by_role("textbox", name="Search a mobile number (Enter")
    #     text_field.fill(four_digit)
    #     text_field.press("Enter")

    #     msisdn_list = page.get_by_role("navigation").locator("div").first

    #     if msisdn_list.count() > 0:
    #         msisdn_list.nth(0).click() # i need to improve this.. click the first option
    #         page.get_by_role("button", name="Proceed").click()
    #         selected_msisdn = msisdn_list.nth(0).inner_text()
    #         print(f"✅ Selected MSISDN: {selected_msisdn}")
    #         page.wait_for_timeout(1000)

    #         if page.locator("h5:has-text('Supplementary Line')").count() > 0:
    #             print("✅ Successfully Reserved MSISDN")
    #             return
    #         else:
    #             print("⚠️Failed to reserve MSISDN, retrying...")

    #     else:
    #         print("No MSISDN found, retrying...")

    # raise Exception("❌ Failed too many attempts.")

def npl_select_supplementary_msisdn(page, max_retries: int = 10):
    heading_name = page.get_by_role("heading", name="Supplementary Line")
    while heading_name.wait_for(state="visible"):
        page.timeout(2000)
        print("Choose your Supplementary plan then click Proceed!")
        button = page.get_by_role("button", name="Proceed")
        button.wait_for(state="visible")
        button.click()
    # pass 
