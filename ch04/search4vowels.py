def search4vowels(word):
    """Return a boolean based on any vowels found."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    # 如果(交集)不包含元音，则found为空集
    return bool(found)
