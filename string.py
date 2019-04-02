import string,random

vowels='aeiou'
consonants='bcdfghjklmnpqrstvwxyz'
letters=string.ascii_lowercase

letter_input_1=input("What Letter Do You want? Enter 'v' For Vowels, 'c' For Consonants,'a' For Any Letter: ")
letter_input_2=input("What Letter Do You want? Enter 'v' For Vowels, 'c' For Consonants,'a' For Any Letter: ")
letter_input_3=input("What Letter Do You want? Enter 'v' For Vowels, 'c' For Consonants,'a' For Any Letter: ")
letter_input_4=input("What Letter Do You want? Enter 'v' For Vowels, 'c' For Consonants,'a' For Any Letter: ")
print(type(letter_input_1))

def generator():
    if letter_input_1=='v':
        letter1=random.choice(vowels)
    elif letter_input_1=='c':
        letter1=random.choice(consonants)
    elif letter_input_1=='a':
        letter1=random.choice(letters)
    else:
        letter1=letter_input_1

    if letter_input_2=='v':
        letter2=random.choice(vowels)
    elif letter_input_2=='c':
        letter2=random.choice(consonants)
    elif letter_input_2=='a':
        letter2=random.choice(letters)
    else:
        letter2=letter_input_2

    if letter_input_3=='v':
        letter3=random.choice(vowels)
    elif letter_input_3=='c':
        letter3=random.choice(consonants)
    elif letter_input_3=='a':
        letter3=random.choice(letters)
    else:
        letter3=letter_input_3

    if letter_input_4=='v':
        letter4=random.choice(vowels)
    elif letter_input_4=='c':
        letter4=random.choice(consonants)
    elif letter_input_4=='a':
        letter4=random.choice(letters)
    else:
        letter4=letter_input_4


    name=letter1+letter2+letter3+letter4
    return(name)
    print(generator())     