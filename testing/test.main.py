import unittest

from init import test, magic

# ===== Nun gehts aber los ===== #

test_match = {
    "game": "fooooosball",
    "teams": [
        {
            "created": "yesterday",
            "members": [
                {
                    "id": "linus.bolls@code.berlin",
                    "elo": 500,
                    "result": -100
                }
            ],
        },
        {
            "created": "yesterday",
            "members": [
                {
                    "id": "tom.lustig@code.berlin",
                    "elo": 750,
                    "result": 100
                }
            ]
        }
    ]
}
class TestSomeStuff(unittest.TestCase):

    def insert_users(self):
        data0, err0 = test.insertUser({ "email": "linus.bolls@code.berlin", "name": "linus" })  
        data1, err1 = test.insertUser({ "email": "linus.bolls@code.berlin", "name": "linus" })
        data2, err2 = test.insertUser({ "email": "tom.lustig@code.berlin", "name": "tom" })

        self.assertIsNone(err0)
        self.assertIsNone(data1)
        self.assertIsNone(err2)

    def insert_match(self):
        data0, err0 = test.insertMatch(test_match)
        self.assertIsNone(err0)

    def test_magic(self):

        data0, err0 = test.insertUser({ "email": "linus.bolls@code.berlin", "name": "linus" })  
        data1, err1 = test.insertUser({ "email": "linus.bolls@code.berlin", "name": "linus" })
        data2, err2 = test.insertUser({ "email": "tom.lustig@code.berlin", "name": "tom" })

        # ===== When user requests link ===== #
        code, err0 = magic.makeMagicLink("linus.bolls@code.berlin", True)

        # ===== Give user jwt when clicks link to authorize subsequent requests ===== #
        encryptedToken, err1 = magic.tokenIfMagic("linus.bolls@code.berlin", code)

        # ===== Validate token on subsequent requests ===== #
        decryptedToken, err2 = magic.validateToken(encryptedToken)

        self.assertIsNone(err0)
        self.assertIsNone(err1)
        self.assertIsNone(err2)

if __name__ == "__main__":
    unittest.main()