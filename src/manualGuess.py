from randomGuess import initialize_secrets
from randomGuess import initialize_key
from randomGuess import translate
from randomGuess import pretty_print

def swap_characters(oldLetter, newLetter):
    for leftLetter, rightLetter in key.items():
        if rightLetter == oldLetter:
            key[leftLetter] = newLetter
            print("Swapped ({}=>{}) to ({}=>{})".format(leftLetter, oldLetter, leftLetter, newLetter))
        elif rightLetter == newLetter:
            key[leftLetter] = oldLetter
            print("Swapped ({}=>{}) to ({}=>{})".format(leftLetter, newLetter, leftLetter, oldLetter))
    key[oldLetter] = newLetter
    key[newLetter] = oldLetter

if __name__ == "__main__":
    print("Reading current secrets in the secrets folder...")
    secrets = initialize_secrets()
    print("Generating initial key...")
    key = initialize_key(False)

    while True:
        oldLetter = input("Enter a letter you would like to change: ")
        newLetter = input("What would you like to change it to? ")
        swap_characters(oldLetter, newLetter)
        text = translate(secrets, key)
        pretty_print(text, key)