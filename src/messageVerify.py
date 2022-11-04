animal_letter_count = {
    'LAND':{'P':1, 'A':2, 'N':1, 'D':1},
    'WATER':{'O':2, 'C':1, 'T':1, 'P':1, 'U':1, 'S':1},
    'ICE':{'M':3, 'A':1, 'O':1, 'T':1, 'H':1},
    'AIR':{'O':1, 'W':1, 'L':1},
    'FIRE':{'D':1, 'R':1, 'A':1, 'G':1, 'O':1, 'N':1}
}

class VerifyMessage:

    def matchKingdoms(kingdom, message):
        frequency_of_letters = animal_letter_count.get(kingdom)
        count = 0
        for key in frequency_of_letters.keys():
            letter_frequncy_count = message.count(key)
            if letter_frequncy_count >= int(frequency_of_letters.get(key)):
                count += int(frequency_of_letters.get(key))
        if count == sum(frequency_of_letters.values()):
            return kingdom