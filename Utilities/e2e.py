# test_scores_service - it’s purpose is to test our web service. It will get the application
# URL as an input, open a browser to that URL, select the score element in our web page,
# check that it is a number between 1 to 1000 and return a boolean value if it’s true or not.
# 2. main_function to call our tests function. The main function will return -1 as an OS exit
# code if the tests failed and 0 if they passed.

from playwright.sync_api import Playwright, sync_playwright, expect


def test_scores_service(application_url="http://127.0.0.1:5000"):
    # playwright codegen demo.playwright.dev/todomvc
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://demo.playwright.dev/todomvc/")
        page.goto("https://demo.playwright.dev/todomvc/#/")
        page.goto(application_url)

        the_score = page.locator('id=score').text_content()
        the_score = the_score.strip("[]'")
        the_score_as_dig = int(the_score)
        # print(f"This is the text: {the_score}")
        # ---------------------
        context.close()
        browser.close()
        if 0 < the_score_as_dig < 1000:
            print("True")
            return True
        else:
            print("False")
            return False


