
vowels = ['a', 'e', 'i', 'o', 'u']
word = input("Provide a word to search for vowels: ")
found = []

for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
# 再迭代不重复输出word中的元音字 
for vowel in found:
    print(vowel)
