str=input("Enter a sentence:").lower()
word=input("Enter a word to search:")

if word in str:
    print(f"{word} word is present in sentence...")
else:
    print(f"The word {word} doesn't exist in the sentence...")