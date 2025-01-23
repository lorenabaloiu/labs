import string
def word_frequency(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

text = input("Enter a sentence: p")
print(word_frequency(text))