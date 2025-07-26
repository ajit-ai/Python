# Find the vowel and consonant in a given string 

def find_vowels(input_string):
    vowels = set('aeiouAEIOU')
    found_vowels = [char for char in input_string if char in vowels]
    return found_vowels

def find_consonants(input_string):
    vowels = set('aeiouAEIOU')
    found_consonants = [char for char in input_string if char.isalpha() and char not in vowels]
    return found_consonants

# Example usage
if __name__ == '__main__':
    test_string = "Hello World!"
    print("Vowels:", find_vowels(test_string))
    print("Consonants:", find_consonants(test_string))