import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassassa_oikea_maara_rahaa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_oikea_maara_edullisia(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_oikea_maara_maukkaita(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_jos_maksu_riittava_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 60)

    def test_kateistosto_lisaa_lounaita_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kateisosto_toimii_jos_maksu_ei_riittävä_edullinen(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 200)

    def test_kateisosto_ei_lisaa_lounaita_jos_maksu_ei_riittava_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        
        self.assertEqual(self.kassapaate.edulliset, 0)        

    def test_kateisosto_toimii_jos_maksu_riittava_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 100)

    def test_kateistosto_lisaa_lounaita_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kateisosto_toimii_jos_maksu_ei_riittävä_maukas(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 300)

    def test_kateisosto_ei_lisaa_lounaita_jos_maksu_ei_riittava_maukas(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        
        self.assertEqual(self.kassapaate.maukkaat, 0)        

    def test_korttiosto_toimii_jos_maksu_riittava_edullinen(self):
        onnistui = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(onnistui, True)

    def test_korttiosto_lisaa_lounaita_edullinen(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_korttiosto_toimii_jos_maksu_ei_riittävä_edullinen(self):
        kortti = Maksukortti(100)
        onnistui = self.kassapaate.syo_edullisesti_kortilla(kortti)

        self.assertEqual(onnistui, False)

    def test_korttiosto_ei_lisaa_lounaita_jos_maksu_ei_riittava_edullinen(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        
        self.assertEqual(self.kassapaate.edulliset, 0)     

    def test_korttiosto_toimii_jos_maksu_riittava_maukas(self):
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(onnistui, True)

    def test_korttiosto_lisaa_lounaita_maukas(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_korttiosto_toimii_jos_maksu_ei_riittävä_maukas(self):
        kortti = Maksukortti(100)
        onnistui = self.kassapaate.syo_maukkaasti_kortilla(kortti)

        self.assertEqual(onnistui, False)

    def test_korttiosto_ei_lisaa_lounaita_jos_maksu_ei_riittava_maukas(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        
        self.assertEqual(self.kassapaate.maukkaat, 0)    

    def test_kortin_lataus_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)
        self.assertEqual(self.maksukortti.saldo, 1100)

    def test_kortin_lataus_ei_tee_vaaraa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.saldo, 1000)




    