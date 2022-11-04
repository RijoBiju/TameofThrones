import unittest
from source.messageVerify import VerifyMessage
from source.messageDecrypter import Decrypter
import geektrust

class TestCases(unittest.TestCase):

    def test_matchKingdoms(self):
        verified_kingdom = VerifyMessage.matchKingdoms('FIRE', 'XLUAIHDRAGON')
        self.assertEqual(verified_kingdom, 'FIRE')

    def test_decryptMessage(self):
        deciphered_message = Decrypter.decryptMessage('FIRE', 'DRAGONJXGMUT')
        self.assertEqual(deciphered_message, 'XLUAIHDRAGON')

    def test_check_for_duplicates(self):
        ally = [None, None, 'FIRE', 'AIR', 'WATER']
        self.assertEqual(geektrust.check_for_duplicates(ally), True)

    def test_result(self):
        ally = [None, None, 'FIRE', 'AIR', 'WATER']
        self.assertEqual(geektrust.result(ally), 'SPACE FIRE AIR WATER')

    def test_get_kingdom_and_message(self):
        self.assertEqual(geektrust.get_kingdom_and_message('FIRE DRAGON JXGMUT'), ('FIRE', 'DRAGONJXGMUT'))

if __name__=='__main__':
    unittest.main()