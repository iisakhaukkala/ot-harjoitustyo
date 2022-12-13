import unittest
from repositories.info_repository import info_repository


class TestService(unittest.TestCase):
    def setUp(self):
        pass

    def test_info(self):
        textlist = ["a","b","c"]
        info_repository.edit_info(textlist)
        self.assertEqual(info_repository.return_info(),"a\nb\nc\n")