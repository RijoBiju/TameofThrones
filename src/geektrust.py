from source.messageDecrypter import Decrypter
from source.messageVerify import VerifyMessage
import sys

def check_for_duplicates(allies):
    repetitive = 0
    for word in allies:
        if word is None:
            pass
        elif allies.count(word) > 1:
            repetitive += 1
    if repetitive > 0:
        return False
    else:
        return True

def result(allies):
    final_string = 'SPACE'
    for kingdom in allies:
        if kingdom is None:
            pass
        else:
            final_string += ' ' + kingdom
    return final_string

def get_kingdom_and_message(text):
    split_text = text.split()
    kingdom = split_text[0]
    cipher_message = ""
    for word in split_text[1:]:
        cipher_message += word
    return kingdom, cipher_message

def main():
    allies = []
    input_file = sys.argv[1]
    with open(input_file, 'r') as f:
        for line in f.readlines():
            kingdom, cipher_message = get_kingdom_and_message(line)
            deciphered_message = Decrypter.decryptMessage(kingdom, cipher_message)
            verified_kingdom = VerifyMessage.matchKingdoms(kingdom, deciphered_message)
            allies.append(verified_kingdom)
    if check_for_duplicates(allies):
        print(result(allies))
    else:
        print('NONE')

if __name__=='__main__':
    main()