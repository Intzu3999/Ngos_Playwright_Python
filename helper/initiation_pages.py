from playwright.sync_api import sync_playwright

def choose_your_next_step(page, option: str):
    option = option.lower()
    heading_name = page.get_by_text("Choose your next step")
    heading_name.wait_for(state="visible")

    if option == "npl":
        page.get_by_text("Get New Number").click()
    elif option == "cop":
        page.get_by_text("Change Plans").click()
    elif option == "mnp":
        page.get_by_text("Switch to CelcomDigi Keep").click()
    else:
        raise ValueError(f"Invalid next step option: {option}")
    
    page.wait_for_timeout(500)

    button = page.locator("#serviceModal").get_by_role("button", name="Proceed")
    button.wait_for(state="visible")
    button.click()

def choose_sim_type(page, sim_type: str):
    sim_type = sim_type.lower()
    heading_name = page.get_by_role("heading", name="Choose your SIM type")
    heading_name.wait_for(state="visible")
    page.wait_for_timeout(500)
    
    if sim_type == "esim":
        page.get_by_role("radio").first.check()
    elif sim_type == "psim":
        page.get_by_role("radio").last.check()
    else:
        raise ValueError(f"Unsupported SIM type: {sim_type}")
    
    page.wait_for_timeout(500)

def check_device_compatibility_link(page):
    heading_name = page.get_by_role("heading", name="Is your phone eSIM compatible?")
    heading_name.wait_for(state="visible")

    with page.expect_popup() as device_compatibility_page:
        page.get_by_role("link", name="Check Device Compatibility").click()
    page2 = device_compatibility_page.value
    heading_name = page2.get_by_role("heading", name="CelcomDigi eSIM - Compatible")
    heading_name.wait_for(state="visible")
    page2.wait_for_timeout(1000)
    page2.close()

def esim_compatible_checkbox(page):
    heading_name = page.get_by_role("heading", name="Is your phone eSIM compatible?")
    heading_name.wait_for(state="visible")

    page.get_by_role("checkbox", name="I confirm that my device is").check()
    page.wait_for_timeout(500)
    page.get_by_role("checkbox", name="I confirm that my device is").uncheck()
    page.wait_for_timeout(500)
    page.get_by_role("checkbox", name="I confirm that my device is").check()
    page.wait_for_timeout(500)

    button = page.get_by_role("button", name="Proceed")
    button.click()
