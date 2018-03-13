def search4vowels(word):
    """Display any vowels found in a supplied word."""
    vowels = set('aeiou')
    # word = input("Provide a word to search for vowels: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)
