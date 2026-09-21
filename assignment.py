# Exercise 1
def count_characters(text):
    return len(text)
print(count_characters("Hello World"))

# Exercise 2
def remove_spaces(text):
    return text.replace(" ", "")
print(remove_spaces("Python is fun"))

# Exercise 3
def count_vowels(text):
    count = 0
    for i in text:
        if i in "aeiouAEIOU":
            count += 1
    return count
print(count_vowels("Python is amazing"))

# Exercise 4
def replace_vowels(text):
    for vowel in "aeiouAEIOU":
        text = text.replace(vowel, "*")
    return text
print(replace_vowels("Education"))

# Exercise 5
def count_words(text):
    text = text.split()
    return len(text)
print(count_words("Python makes coding fun"))

# Exercise 6
def find_longest_word(text):
    text = text.split()
    longest = text[0]
    for word in text:
        if len(word) > len(longest):
            longest = word
    return longest
print(find_longest_word("Learning Python programming"))
