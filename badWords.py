from better_profanity import profanity as pft


def badWordChecker(message):
    """
    Takes message as input and checks for words of profanity 
    :PARAMS: STR
    :RETURN: BOOL
    """
    
    # separate all words into a list
    message = message.split(" ")

    for word in range(len(message)):

        if message[word - 1] == "not" and word != 0:
            print("here")
            continue
    
        if pft.contains_profanity(message[word]):

            return True

    return False


