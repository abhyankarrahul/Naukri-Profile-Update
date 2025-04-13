def wait_for_element(page, selector, timeout=30):
    """Wait for an element to be visible on the page."""
    page.wait_for_selector(selector, timeout=timeout)

def click_element(page, selector):
    """Click on an element specified by the selector."""
    page.locator(selector).click()

def fill_input(page, selector, value):
    """Fill an input field with the specified value."""
    page.locator(selector).fill(value)

def get_element_text(page, selector):
    """Get the text content of an element."""
    return page.locator(selector).inner_text()