#  write your code here 
import argparse

parser = argparse.ArgumentParser(description='This will decode your encoded txt file')
parser.add_argument('file', help="Enter encoded text file")
args = parser.parse_args()

filename = args.file
opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string


def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)


decode_caesar_cipher(encoded_text, -13)
opened_file.close()  # always close the files you've opened



