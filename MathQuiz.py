Correct = 0
Wrong = 0
#mapping of question number to modulus equations
Questions = {
    '1': '5%2 = ?',
    '2': '6%3 = ?',
    '3': '15%3 = ?',
    '4': '21%5 = ?',
    '5': '35%8 = ?'
}

Answers = {
    '1': '1',
    '2': '0',
    '3': '0',
    '4': '1',
    '5': '3'
}

for i in Answers:
    print (Questions[i])
    response = input("What's the answer?")
    if Answers[i] == response:
        Correct += 1
    else:
        Wrong += 1

print("You got " + str(Correct) + " problems correct!")
print("You got " + str(Wrong) + " problems wrong!")