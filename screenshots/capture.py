from playwright.sync_api import sync_playwright
import os

def capture(name):
    os.makedirs("artifacts/screenshots", exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("about:blank")
        page.screenshot(path=f"artifacts/screenshots/{name}")
        browser.close()
