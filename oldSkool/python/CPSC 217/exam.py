sentence = "Enter a sentence, words are separated by one space and the sentence ends in a period."
curWord = ""

for i in range(0, len(sentence)):
    if sentence[i] == " ":
        if len(curWord)>=5:
            print(curWord)
        curWord = ""
        continue
    curWord += sentence[i]
    