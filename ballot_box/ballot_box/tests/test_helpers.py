import unittest

from ballot_box.modules import helpers
from werkzeug.contrib.cache import SimpleCache


class TestHelpers(unittest.TestCase):
    def test_get_first(self):
        self.assertEqual(helpers.get_first([1, 2]), 1)
        self.assertEqual(helpers.get_first([], 1), 1)
        self.assertEqual(helpers.get_first(None, 1), 1)

    def test_helpers_date_str_to_iso(self):
        self.assertEqual(helpers.date_str_to_iso('12/1/2014'),
                         '2014-12-01T00:00:00')
        self.assertEqual(helpers.date_str_to_iso('1/28/2014'),
                         '2014-01-28T00:00:00')

    def test_helpers_iif(self):
        self.assertEqual(helpers.iif(True, 'true', 'false'), 'true')
        self.assertEqual(helpers.iif(False, 'true', 'false'), 'false')
        self.assertEqual(helpers.iif(None, 'true', 'false'), 'false')

    def test_helpers_get_cache(self):
        cache = SimpleCache()
        key = 'test'
        original_value = "Item Value"
        value = "Item Value"

        def get_item():
            return value

        self.assertEqual(helpers.get_cache(cache, key, get_item), value)

        value = "Item Value Changed"

        # item should still be in cache so the item value is not changed
        self.assertNotEqual(get_item(), original_value)

        self.assertEqual(helpers.get_cache(cache, key, get_item), original_value)

    def test_helpers_to_css_class(self):
        self.assertEqual(helpers.to_css_class("test Class"), 'test-class')
        self.assertEqual(helpers.to_css_class("test@#$Class"), 'test-class')
        self.assertEqual(helpers.to_css_class("test  Class"), 'test-class')


if __name__ == "__main__":
    unittest.main()