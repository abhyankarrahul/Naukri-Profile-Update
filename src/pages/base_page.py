class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, selector):
        self.page.click(selector)

    def fill(self, selector, value):
        self.page.fill(selector, value)

    def get_text(self, selector):
        return self.page.text_content(selector)

    def wait_for_selector(self, selector):
        self.page.wait_for_selector(selector)

    def is_visible(self, selector):
        return self.page.is_visible(selector)