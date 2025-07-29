from playwright.sync_api import sync_playwright
from helper.helper import generate_random_nric

def enter_new_nric(context,page):
    new_nric = generate_random_nric()

    heading_name = page.get_by_role("heading", name="Verify Your Identity")
    heading_name.wait_for(state="visible")

    page.get_by_role("textbox", name="IC number").click()
    page.get_by_role("textbox", name="IC number").fill(new_nric)
    page.wait_for_timeout(1000)

    button = page.get_by_role("button", name="Proceed")
    button.wait_for(state="visible")
    button.click()

def enter_existing_nric(page, existing_nric:str):
    heading_name = page.get_by_role("heading", name="Verify Your Identity")
    heading_name.wait_for(state="visible")

    page.wait_for_timeout(1000)
    page.get_by_role("textbox", name="IC number").click()
    page.get_by_role("textbox", name="IC number").fill(existing_nric)
    page.wait_for_timeout(1000)

    button = page.get_by_role("button", name="Proceed")
    button.wait_for(state="visible")
    button.click()


def terms_and_conditions_link_and_checkbox(page):
    heading_name = page.get_by_role("heading", name="Verify Your Identity")
    heading_name.wait_for(state="visible")

    with page.expect_popup() as terms_and_condition_page:
        page.get_by_role("link", name="Terms and Conditions").click()
    page2 = terms_and_condition_page.value
    heading_name = page2.get_by_role("heading", name="Terms & Conditions")
    heading_name.wait_for(state="visible")
    page2.wait_for_timeout(1000)
    page2.close()

    page.get_by_role("checkbox", name="I agree to the Terms and").check()
    page.wait_for_timeout(500)
    page.get_by_role("checkbox", name="I agree to the Terms and").uncheck()
    page.wait_for_timeout(500)
    page.get_by_role("checkbox", name="I agree to the Terms and").check()
