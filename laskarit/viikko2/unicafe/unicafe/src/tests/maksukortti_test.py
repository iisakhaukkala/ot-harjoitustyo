import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 1000)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)

        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(self.maksukortti.saldo, 900)

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        kortti = Maksukortti(50)
        kortti.ota_rahaa(200)

        self.assertEqual(kortti.saldo, 50)

    def test_metodi_palauttaa_true_oikein(self):
        self.assertEqual(self.maksukortti.ota_rahaa(100), True)

    def test_metodi_palauttaa_false_oikein(self):
        kortti = Maksukortti(100)
        
        self.assertEqual(kortti.ota_rahaa(200), False)
