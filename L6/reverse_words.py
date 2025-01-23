def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

sentence = input("Enter a sentence: ")
result = reverse_words(sentence)
print("Original Sentence:", sentence)
print("Reversed Words:", result)
