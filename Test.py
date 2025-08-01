from playwright.sync_api import sync_playwright, TimeoutError

Login = "https://ua.segwise.ai/qa_assignment"
Dashboard = "https://ua.segwise.ai/qa_assignment/home?report_date=2024-10-15&preset=last_7_days"

Email= 'input[autocomplete="email"]'
Password = 'input[autocomplete="current-password"]'
submit = 'text=Log in with email'
Chart = 'svg.recharts-surface'

Username = "qa@segwise.ai"
password = "segwise_test"

def test_login_and_assert_chart_present():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        print("Opening login page")
        page.goto(Login)

        print("Filling in email and password")
        page.fill(Email, Username)
        page.fill(Password, password)

        print("Clicking login button")
        page.click(submit)

        print("Waiting for dashboard to load")
        page.wait_for_url(Dashboard, timeout=10000)

        print("Verifying chart visibility")
        try:
            chart = page.wait_for_selector(Chart, timeout=5000)
            assert chart.is_visible(), " Chart is not visible"
            print("Chart is present and visible.")
        except TimeoutError:
            raise AssertionError(" Chart not found on the dashboard.")

        browser.close()

if __name__ == "__main__":
    test_login_and_assert_chart_present()
