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

    # List of profane words in the message
    profaneWords = []
    
    # Open data file of bad-words
    with open("./database/bad-words.txt") as data:
        # read in the data
        badWords = data.read()
        # split the words by '\n' and store them as a list
        badWords = badWords.split("\n")

        # Use regex on badWords
        for word in range(len(badWords)):
            badWords[word] = "^." + re.escape(badWords[word]) + ".$"


        # for every word in message
        for word in message:
            
            for badWord in badWords:
                # Check if the word is in badWord 
                # Or if it is like the badWord
                match = re.findall(badWord, word)
                # if match then append word to profaneWords
                if match:
                    profaneWords.append(word)
                    break


    # if the profaneWords is empty return false
    if not profaneWords:
        return False
    # else return the list of profane words present in the message
    else:
        return profaneWords

