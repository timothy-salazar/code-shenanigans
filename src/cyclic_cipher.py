import string
from itertools import cycle
import argparse

def inv_dict(d):
    """ Input:
            d: dict - a python dictionary that maps each of the letters of 
                the alphabet to a number.
        Output:
            a python dictionary that maps the numbers in d back into letters
    """
    return {v: k for k, v in d.items()}

def alpha_dict():
    """ Input:
            None
        Output:
            d: dict - a python dictionary that maps each of the letters of 
                the alphabet to a number (a=1, b=2, etc.)
    """
    d = dict()
    for i,j in zip(string.ascii_lowercase, range(1,27)):
        d[i] = j
    return d

def reverse_key(k):
    """ Input: 
            k: str - the key to the cesarian cipher
        Output:
            k: str - the reverse of the key, so we can use the same
                function for encoding and decoding.
    """
    d = alpha_dict()
    r = inv_dict(d)
    return ''.join([r[26 - d[i]] for i in k])

def transform_message(s,k):
    """ Input:
            s: string - the text we want to transform
            k: string - the key to the cesarian cipher
        Output:
            adds the value of the first letter of k to the first letter of s, then
            the second letter and so on until the end of k is reached, at which point
            the first letter of k is added to the len(k)+1 letter of s.
            """
    d = alpha_dict()
    r = inv_dict(d)
    r[0] = 'z'
    return ''.join([r[(d[i]+d[j])%26] if i != ' ' else i for i,j in zip(s,cycle(k))])

def get_file(file_path):
    """ Input: 
            file_path: str - the path to the file we want to 
                read in and encode/decode
        Output:
            returns the contents of the file
    """
    try:
        with open(file_path, 'r') as f:
            text = f.read()
        return text.lower()
    except FileNotFoundError:
        print('Invalid file path')

def main(args):
    # Get the message text
    if args.text:
        text = args.text.lower()
    else:
        text = get_file(args.file)
    # Get the key
    key = args.key
    # If we're decoding the message we just need to reverse the key (i.e.,
    # for each letter, convert to a number and substract it from 26) and then
    # we can use the same function for both encoding and decoding 
    if args.decode:
        key = reverse_key(key)
    new_text = transform_message(text, key)
    print(new_text)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='''
        This takes a key and some text provided by the user and either encodes or
        decodes it using a Cesarian cipher.'''
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        '-e', 
        '--encode', 
        action='store_true',
        help='use this option to encode a message')
    mode.add_argument(
        '-d', 
        '--decode', 
        action='store_true',
        help='use this option to decode a message')
    
    message_input = parser.add_mutually_exclusive_group(required=True)
    message_input.add_argument(
        '-t',
        '--text',
        action='store',
        help='raw text to either be encoded or decoded'
    )
    message_input.add_argument(
        '-f',
        '--file',
        action='store',
        help='file path of message to be encoded or decoded'
    )
    parser.add_argument(
        '-k',
        '--key',
        action='store',
        required=True,
        help='the key to the Cesarian cipher. Will be used to encode or decode the message'
    )
    args = parser.parse_args()
    main(args)
    
    # if sys.argv[1] == 'encode':
    #     s = sys.argv[2]
    #     k = sys.argv[3]
    #     encode_message(s,k)
    # else:
    #     s = sys.argv[1]
    #     k = sys.argv[2]
    #     decode_message(s,k)
