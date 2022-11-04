land_animal = {'SPACE': 'GORILLA', 'LAND': 'PANDA', 'WATER': 'OCTOPUS', 'ICE': 'MAMMOTH', 'AIR': 'OWL', 'FIRE':'DRAGON'}
unicode_of_letter_a = ord('A')
unicode_of_letter_z = ord('Z')

class Decrypter:

    def decryptMessage(kingdom, cipher_message):
        message = ''
        for letter in cipher_message:
            encrypted_message = (ord(letter) - unicode_of_letter_a) + 1
            decrypted_message = (encrypted_message - len(land_animal.get(kingdom))) + unicode_of_letter_a - 1
            if decrypted_message < unicode_of_letter_a:
                decrypted_message = (unicode_of_letter_z - (unicode_of_letter_a - decrypted_message)) + 1
            message += chr(decrypted_message)
        return message