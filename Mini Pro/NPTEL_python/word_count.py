sentence = input("Enter a sentence: ")

words = sentence.split()
word_count = len(words)
char_count = len(sentence.replace(" ", ""))

print("Words:", word_count)
print("Characters:", char_count)
