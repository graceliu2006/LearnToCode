text = input("Please Enter Your Text: ").lower()
vowels = set(["a","e","i","o","u"])

consonants = set([])
for letter in text:
    if letter not in vowels:
        if letter not in consonants:
            consonants.add(letter)

print(sorted(consonants))


consonants = set([])
for letter in text:
    consonants.add(letter)
consonants.difference_update(vowels)

print(sorted(consonants))