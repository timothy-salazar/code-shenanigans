



def check_frequency_count(text):
    """ Input: 
            text: string - a string of characters. A guess at 
                a translation
        Output: 
            score: float - some sort of score that represents how
                well the frequency count matches what we'd expect to see.
    """ 

    freq_count = get_frequency_count(text)
    # something
    

def get_frequency_count(text):
    """ Input:
            text: string - a string of characters. A guess at
                a translation
        Output:
            freq_count: list of floats 26 long? Maybe a python dictionary
                with letter as key and frequency as value? idk

    """
    pass

def get_word_score(text):
    """ Input:
            text: string - a string of characters. A guess at
                a translation.
        Output:
            score: some sort of score that represents how much of the
                text is "real words". Maybe just a percentage or something.
    """
    words = get_words(text)
    pass

def get_words(text):
    """ Input:
            text: string - a string of characters. A guess at
                a translation.
        Output:
            words: list of words contained in text that are present
                in some sort of dictionary (not a python dictionary, a 
                for-realzies dictionary)

    Question: Do we assume that the spaces in the text represent spaces between
    words? If not, we'd have multiple possible interpretations - that is to 
    say, if the first part of the text is "catamaran" we would need to choose 
    between "catamaran" as a word, or "cat", "a", "ran", etc. 

    """
    pass

