from unittest import TestCase, main
from unittest.mock import patch
from page import PagesRequester


class TestPagesRequester(TestCase):
    def setUp(self):
        self.page = PagesRequester('https://google.com')

    def test_mage_request(self):
        with patch('requests.get') as mocked_get:
            response = self.page.get()
            print(response)
            mocked_get.assert_called()

    def test_content_returned(self):
        fake_content = 'Hello'

        class FakeResponse:
            def __init__(self):
                self.content = fake_content

                with patch('requests.get', return_value=FakeResponse) as mocked_get:
                    result = self.page.get
                    self.assertEqual(result, fake_content)


if __name__ == "__main__":
    main()
