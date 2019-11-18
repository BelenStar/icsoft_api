import sys, os

sys.path.append('../..auth/')
import unittest
import auth


class TestAuthEncodeToken(unittest.TestCase):

    def test_id_not_empty(self):
        self.assertNotEqual("",auth.encode_auth_token(1))

if __name__ == '__main__':
    unittest.main()
