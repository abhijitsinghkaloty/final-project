import re

def badWordChecker(message):
    """
    Takes message as input and checks for words of profanity 
    :PARAMS: STR
    :RETURN: FALSE / :LIST: str
    """
    
    # Lowercase the whole message
    message = message.lower()
    # separate all words into a list
    message = message.split(" ")

    profaneWords = []
    with open("./static/bad-words.txt") as data:
        badWords = data.read()

        badWords = badWords.split("\n")

        for word in message:
            if word in badWords:
                profaneWords.append(word)

    if not profaneWords:
        return False
    else:
        return profaneWords

