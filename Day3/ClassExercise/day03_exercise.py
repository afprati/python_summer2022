## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test in your script and see your results.
def count_vowels(word):
    count = 0
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    
    if type(word) in [int]:
        raise TypeError("This is an integer, not a string")
    
    for alphabet in word: 
        if alphabet in vowels:
            count = count + 1
    print(count)

word= 1
count_vowels(word)

import unittest

class Test_count_vowels(unittest.TestCase):
	
	def test_not_string(self):
		with self.assertRaises(TypeError): 
			count_vowels(5)
		

if __name__ == '__main__': 
	unittest.main()