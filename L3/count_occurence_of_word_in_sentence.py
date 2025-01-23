from collections import Counter
def count_word_occurrences(sentence):
    words = sentence.lower().split()
    return dict(Counter(words))

sentence = input("Enter a sentence: ")
word_count = count_word_occurrences(sentence)

print(word_count)