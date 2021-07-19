vowels = ["a","e","i","o","u"]
userInput = input('enter sentence')
def getVowels(userInput):
    for letter in userInput:
        if letter in vowels:
            print(letter)
getVowels(userInput) 