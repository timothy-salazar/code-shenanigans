from randomGuess import initialize_secrets
from randomGuess import initialize_key
from randomGuess import swap_characters
from randomGuess import pretty_print

print("Reading current secrets in the secrets folder...")
secrets = initialize_secrets()
print("Generating initial key...")
key = initialize_key(False)

while True:
    oldLetter = input("Enter a letter you would like to change: ")
    newLetter = input("What would you like to change it to? ")
    for leftLetter, rightLetter in key.items():
        if rightLetter == oldLetter:
            key[leftLetter] = newLetter
            print("Swapped ({}=>{}) to ({}=>{})".format(leftLetter, oldLetter, leftLetter, newLetter))
        elif rightLetter == newLetter:
            key[leftLetter] = oldLetter
            print("Swapped ({}=>{}) to ({}=>{})".format(leftLetter, newLetter, leftLetter, oldLetter))
    key[oldLetter] = newLetter
    key[newLetter] = oldLetter
    text = swap_characters(secrets, key)
    pretty_print(text, key)