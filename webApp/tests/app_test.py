class WebTestSuite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.example.com")

    def test_title(self):
        self.assertEqual(self.driver.title, "Example Domain")

    def test_search(self):
        search_box = self.driver.find_element_by_name("q")
        search_box.send_keys("test")
        search_box.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()