str=input("Enter a sentence:").lower()
word=input("Enter a word to be replaced:").lower()
rword=input("Enter a word will be replace:")

if str=="" and word=="" and rword=="":
    print("Above fields are required please fill them")
else:
    print(str.replace(word,rword))