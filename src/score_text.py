import nltk

def score_text(text):
    """ Input:
            text: string - a string of characters. A guess at
                a translation
        Output:
            scores: tuple - the frequency count score and word score
    """
    freq_score = get_frequency_count_score(text)
    word_score = get_word_score(text)
    return (freq_score, word_score)

def get_frequency_count_score(text):
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

def get_words(wordList):
    """ Input:
            wordList: list of strings - a list of strings of characters. A guess at
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
    english_words = set(nltk.corpus.words.words())
    # d = enchant.Dict("en_US")
    actualWords = list()
    for word in wordList:
        word = word.lower()
        # isWord = d.check(word)
        if word in english_words:
            actualWords.append(word)
    print(actualWords)
    return actualWords

if __name__ == "__main__":
    print(get_words(["helLO", "cat", "doggo", "HuMaN", "oinoinoin", "belch", "human", "hellO"]))
