from playwright.sync_api import sync_playwright
from datetime import datetime

def skip_ekyc(context, page):
    page1 = context.new_page()
    page1.goto("https://nget.digipay.my/plans/postpaid/skipekyc/update/true")
    page.wait_for_timeout(1000)
    page1.close()