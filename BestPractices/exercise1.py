import unittest

def is_palindrome(word: str):
    reverseWord = ''.join(reversed(word))
    return reverseWord == word


class TestPalindrome(unittest.TestCase):

    def test_isPalindrome(self):
        self.assertEqual(is_palindrome('word'), False)
        self.assertEqual(is_palindrome('oaiao'), True)
        self.assertEqual(is_palindrome('anitalavalatina'), True)

unittest.main()

