
#This is my first Playwright script file.

from playwright.sync_api import sync_playwright

# Using Playwright in synchronous mode
with sync_playwright() as p:
    # Launch the browser
    browser = p.chromium.launch(headless=False)  # headless=True runs it invisibly
    page = browser.new_page()

    # Open Google
    page.goto("https://www.google.com")

    # Print the page title
    print("Page Title:", page.title())

    # Close the browser
    browser.close()

# This is the trail code for source code commit.
#thanks
