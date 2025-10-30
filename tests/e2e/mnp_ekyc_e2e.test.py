import pytest
from playwright.sync_api import Page, expect
import re


def test_example(page: Page) -> None:
    page.goto("https://nget.digipay.my/plans/postpaid/PBH6100266")
    page.locator(".price-box > div > .d-flex > span").first.click()
    # expect(page.locator("body")).to_match_aria_snapshot("- button \"Proceed\"")
    # page.get_by_role("button", name="Proceed").click()
    # expect(page.locator("#serviceModal")).to_match_aria_snapshot("- text: Switch to CelcomDigi")
    # page.get_by_text("Switch to CelcomDigi Keep").click()
    # expect(page.locator("#serviceModal")).to_match_aria_snapshot("- button \"Proceed\"")
    # page.locator("#serviceModal").get_by_role("button", name="Proceed").click()
    # page.get_by_role("radio").first.check()
    # page.goto("https://nget.digipay.my/plans/postpaid/device-compatible/PBH6100266")
    # page.get_by_role("checkbox", name="I confirm that my device is").check()
    # page.get_by_role("button", name="Proceed").click()
    # page.locator("body").click()
    # page.get_by_role("textbox", name="IC number").click()
    # page.get_by_role("textbox", name="IC number").fill("881006000001")
    # page.get_by_role("textbox", name="IC number").click()
    # page.locator("iframe[name=\"a-t4ykqjduo20m\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    # page.locator("iframe[name=\"c-t4ykqjduo20m\"]").click()
    # page.get_by_role("button", name="Check Eligibility").click()
    # page.get_by_role("heading", name="Scan QR to Verify Your").click()
    # expect(page.get_by_role("heading")).to_contain_text("Scan QR to Verify Your Identity")
    # page.locator(".col-12 > div:nth-child(2)").click()
    # page.goto("https://nget.digipay.my/plans/postpaid/ekyc/non-mobile-ekyc/PBH6100266")
