import unittest
from country_codes import get_country_code

class CodesTestCase(unittest.TestCase):
    """Testes para 'country_codes.py'."""

    def test_country_codes(self):
        """Nomes como 'Andorra' funcionam?"""
        code = get_country_code('andorra')
        self.assertEqual(code, 'ad')

unittest.main()