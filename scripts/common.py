import os

def choose_your_next_step(page, option: str):
    option = option.lower()
    heading_name = page.get_by_text("Choose your next step")
    heading_name.wait_for(state="visible")

    page.screenshot(path='choose_your_next_step.png')

    if option == "npl":
        page.get_by_text("Get New Number").click()
        page.screenshot(path='choose_your_next_step_npl.png')
    elif option == "cop":
        page.get_by_text("Change Plans").click()
        page.screenshot(path='choose_your_next_step_npl.png')
    elif option == "mnp":
        page.get_by_text("Switch to CelcomDigi Keep").click()
        page.screenshot(path='choose_your_next_step_npl.png')
    else:
        raise ValueError(f"Invalid next step option: {option}")
    
    page.wait_for_timeout(500)

    button = page.locator("#serviceModal").get_by_role("button", name="Proceed")
    button.wait_for(state="visible")
    button.click()

def choose_sim_type(page, sim_type: str):
    sim_type = sim_type.lower()
    page.screenshot(path='choose_sim_type_1.png')
    heading_name = page.get_by_role("heading", name="Choose your SIM type")
    heading_name.wait_for(state="visible")
    page.wait_for_timeout(500)
    
    if sim_type == "esim":
        page.get_by_role("radio").first.check()
        page.screenshot(path='choose_sim_type_2.png')
    elif sim_type == "psim":
        page.get_by_role("radio").last.check()
        page.screenshot(path='results/screenshots/choose_sim_type_2.png')
    else:
        raise ValueError(f"Unsupported SIM type: {sim_type}")
    
    page.wait_for_timeout(500)

def check_device_compatibility_link(page,check_link: bool = True):
    heading_name = page.get_by_role("heading", name="Is your phone eSIM compatible?")
    heading_name.wait_for(state="visible")

    if check_link:
        with page.expect_popup() as device_compatibility_page:
            page.get_by_role("link", name="Check Device Compatibility").click()
        page2 = device_compatibility_page.value
        heading_name = page2.get_by_role("heading", name="CelcomDigi eSIM - Compatible")
        heading_name.wait_for(state="visible")
        page2.wait_for_timeout(1000)
        page2.close()
    elif not check_link:
        print("Skipping Device Compatibility link check.")

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

def skip_ekyc_prestg(context, page):
    page1 = context.new_page()
    page1.goto("https://dev-get.digipay.my/plans/postpaid/skipekyc/update/true")
    page.wait_for_timeout(1000)
    page1.reload()
    page.wait_for_timeout(1000)
    page1.close()

def skip_ekyc(context, page):
    page1 = context.new_page()
    page1.goto("https://nget.digipay.my/plans/postpaid/skipekyc/update/true")
    page.wait_for_timeout(1000)
    page1.reload()
    page.wait_for_timeout(1000)
    page1.close()

def enter_otp(page, otp1: int, otp2: int, otp3: int, otp4: int, otp5: int, otp6: int):
    page.locator("input[name=\"otp1\"]").click()
    page.locator("input[name=\"otp1\"]").fill("6")
    page.locator("input[name=\"otp2\"]").fill("5")
    page.locator("input[name=\"otp3\"]").fill("4")
    page.locator("input[name=\"otp4\"]").fill("4")
    page.locator("input[name=\"otp5\"]").fill("5")
    page.locator("input[name=\"otp6\"]").fill("6")

    button = page.get_by_role("button", name="Submit")
    button.wait_for(state="visible")
    button.click()

    # if len(otp_code) != 6 or not otp_code.isdigit():
    #     raise ValueError("OTP code must be a 6-digit string.")

    # heading_name = page.get_by_role("heading", name="Identity Verification")
    # heading_name.wait_for(state="visible")

    # for i, digit in enumerate(otp_code):
    #     input_field = page.locator(f"input[name='otp{i+1}']")
    #     input_field.click()
    #     input_field.fill(digit)
    #     page.wait_for_timeout(300)

    # page.wait_for_timeout(500)

    # button = page.get_by_role("button", name="Submit")
    # button.wait_for(state="visible")
    # button.click()

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