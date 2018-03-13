def search4vowels(word):
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    # found = vowels.intersection(set(word))
    # return found
    return vowels.intersection(set(word))
