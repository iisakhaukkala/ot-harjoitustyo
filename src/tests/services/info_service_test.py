import unittest
from services.info_service import info_service


class TestService(unittest.TestCase):
    def setUp(self):
        pass

    def test_info(self):
        textlist = ["a","b","c"]
        info_service.edit_info(textlist)
        self.assertEqual(info_service.return_info(),"a\nb\nc\n")