from playwright.sync_api import (sync_playwright, Playwright, Page, Locator)
import time
import yaml

ID = None
PASSWORD = None


def run_playwright():
    # Launch the browser (supports 'chromium', 'firefox', 'webkit')
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)

        # Create a new browser context
        # context = browser.new_context()

        # Create a new page within the context
        # page = context.new_page()
        page = browser.new_page()

        # Navigate to a web page
        page.goto('https://www.aladin.co.kr/login/wlogin_popup.aspx')

        # Perform actions on the page
        # page.click('document.querySelector("#Email")')  # Click on a link
        page.fill('input[name="Email"]', ID)
        page.fill('input[name="Password"]', PASSWORD)

        time.sleep(2)
        login_button = page.query_selector('div.button_login1_2016')
        login_button.click()

        page.goto('https://www.aladin.co.kr/events/wevent.aspx?EventId=248788')

        # radio_button = page.query_selector('input[type="radio"][value="2"]')
        # radio_button.click()


        point_button = page.query_selector('img[id=ucContent_wa_savemoney_btn_butDownload]')
        # point_button = page.query_selector('#ucContent_wa_savemoney_btn_butDownload')
        time.sleep(3)
        point_button.click()

        # test_button = page.query_selector('div.event01')
        # time.sleep(3)
        # test_button = page.query_selector('//*[@id="container"]/div[1]/div[5]/div/div/div[2]/a/span')



        time.sleep(5)
        # test_button.click()
        # time.sleep(100)

        # Wait for page navigation
        # page.wait_for_navigation()
        # time.sleep(10)

        # Take a screenshot
        # page.screenshot(path='example.png')

        # Close the browser
        browser.close()

def set_account():
    global ID
    global PASSWORD

    # account = None
    with open("account.yaml", "r") as f:
        account = yaml.safe_load(f)

    ID = account["account"]["id"]
    PASSWORD = account["account"]["password"]

def get_point(page: Page):
    page.goto('https://www.aladin.co.kr/login/wlogin_popup.aspx')

    id_input: Locator = page.locator('input[name=Email]')
    pw_input: Locator = page.locator('input[name=Password]')
    id_input.fill(ID)
    pw_input.fill(PASSWORD)
    time.sleep(2)

    login_button: Locator = page.locator('div.button_login1_2016')
    login_button.click()

    page.goto('https://www.aladin.co.kr/events/wevent.aspx?EventId=248788')

    # point_button: Locator = page.locator('img[id=ucContent_wa_savemoney_btn_butDownload]')
    point_button: Locator = page.locator('#ucContent_wa_savemoney_btn_butDownload')

    time.sleep(3)
    point_button.click()

    time.sleep(5)


def run(playwright: Playwright):
    # Launch the browser (supports 'chromium', 'firefox', 'webkit')

    browser = playwright.firefox.launch(headless=False)
    page = browser.new_page()
    get_point(page)
    browser.close()


def main():
    set_account()
    with sync_playwright() as playwright:
        run(playwright=playwright)


main()
