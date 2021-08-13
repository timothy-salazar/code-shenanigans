import string
import sys
from itertools import cycle

def inv_dict(t):
    return {v: k for k, v in t.items()}

def alpha_dict():
    d = dict()
    for i,j in zip(string.ascii_lowercase, range(1,27)):
        d[i] = j
    return d

def decode_message(s,k):
    d = alpha_dict()
    r = inv_dict(d)
    r[0] = 'z'
    print(''.join([r[(d[i]-d[j])%26] if i != ' ' else i for i,j in zip(s,cycle(k))]))

def encode_message(s,k):
    d = alpha_dict()
    r = inv_dict(d)
    r[0] = 'z'
    print(''.join([r[(d[i]+d[j])%26] if i != ' ' else i for i,j in zip(s,cycle(k))]))

if __name__ == "__main__":
    if sys.argv[1] == 'encode':
        s = sys.argv[2]
        k = sys.argv[3]
        encode_message(s,k)
    else:
        s = sys.argv[1]
        k = sys.argv[2]
        decode_message(s,k)
