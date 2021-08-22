import os
import string
import random

def initialize_secrets():
    secrets = list()
    characterSet = set()
    characterFrequency = {}
    otherSet = set()
    # Get all secret files into list.
    for file in os.listdir('src/secrets'):
        with open('src/secrets/'+file) as secretFile:
            for line in secretFile:
                secrets.append(line.strip())
                for character in line.strip():
                    if character.isalpha():
                        characterSet.add(character)
                        if character not in characterFrequency:
                            characterFrequency[character] = 1
                        else:
                            characterFrequency[character] +=1
                    else:
                        otherSet.add(character)
        #         print("{}: {}".format(file, line.strip()))
        # print('\n')
    # print("Secrets: ")
    # print(secrets)
    print("Character set: {}".format(characterSet))
    print("Total number of alphabetic characters: {}".format(len(characterSet)))
    # print("Frequency of each character: {}".format(characterFrequency))
    print("Other characters set: {}".format(otherSet))
    print("Total number of other characters: {}".format(len(otherSet)))
    return secrets

def initialize_key(randomize):
    key = {}

    alphabet = list(string.ascii_lowercase + string.ascii_uppercase)
    shuffledAlphabet = list(string.ascii_lowercase + string.ascii_uppercase)
    if randomize == True:
        random.shuffle(shuffledAlphabet)
    pairs = zip(alphabet, shuffledAlphabet)

    # print("Key: ")
    for pair in pairs:
        # print(pair)
        key[pair[0]] = pair[1]

    return key

def swap_characters(secrets, key):
    translatedSecrets = list()
    for secret in secrets:
        translatedSecret = ""
        for index in range(0, len(secret)):
            
            character = secret[index]
            if character.isalpha():
                # print(secret[index] + ' => ' + key[character])
                translatedSecret += key[character]
            else:
                translatedSecret += character #Numbers don't need to be converted.
        # print(translatedSecret)
        translatedSecrets.append(translatedSecret)
    # print(translatedSecrets)
    return translatedSecrets

def pretty_print(text, key):
    print('\nKey: ')
    for letter in key:
        print('({}=>{}) '.format(letter, key[letter]), end='')
    print('\nText: ')
    for word in text:
        print(word, end=' ')
    print('\n')
    return True

if __name__ == "__main__":
    secrets = initialize_secrets()
    key = initialize_key(True)
    text = swap_characters(secrets, key)
    pretty_print(text, key)