from playwright.sync_api import sync_playwright

def scrape_dynamic_data(url):
    """
    Scrape dynamic data from a webpage using Playwright.
    :param url: URL of the webpage to scrape.
    :return: Extracted data as a dictionary or list.
    """
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=False)  # Use headless=False for debugging
        page = browser.new_page()
        
        # Navigate to the target URL
        page.goto(url)
        
        # Wait for the dynamic content to load (adjust selector as needed)
        page.wait_for_selector("#komoditi_id")
        
        # Extract data
        data = page.locator("komoditi_id").all_inner_texts()
        
        # Optionally, extract multiple elements
        # data_list = page.locator("selector_for_dynamic_list").all_inner_texts()
        
        browser.close()
        return {"data": data}  # Return data as a dictionary or any desired format