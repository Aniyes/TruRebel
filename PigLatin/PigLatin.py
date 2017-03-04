Vowels = 'a', 'i', 'e', 'o', 'u'

def convert_word(word):
    first_letter = word[0]
    if first_letter in Vowels:
        return word[1:] + "yay"
    else:
        return word[1:] + first_letter + "ay"

def convert_sentence(sentence):
    user_sentence = sentence.split(' ')
    latin_Pig = ""

    for word in user_sentence:
        latin_Pig = convert_word(word)
        latin_Pig = latin_Pig + " "
        print(latin_Pig)