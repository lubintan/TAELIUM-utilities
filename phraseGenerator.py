from random import randint
import csv

LOWER_ALPHA = ['a','b','d','e','f','g','h','i','j','m','n','p','q','r', 't','u','v','w','x','y','z']
UPPER_ALPHA = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z']
NUM = ['0','1','2','3','4','5','6','7','8','9']
SPECIAL = ['-','_']

LENGTH = 55

def generate():

    phrase = ''

    for i in range(LENGTH):
        whatType = randint(0,3)

        if whatType == 0:
            phrase += LOWER_ALPHA[randint(0,len(LOWER_ALPHA)-1)]
        elif whatType == 1:
            phrase += UPPER_ALPHA[randint(0, len(UPPER_ALPHA)-1)]
        elif whatType == 2:
            phrase += NUM[randint(0, len(NUM)-1)]
        elif whatType == 3:
            phrase += SPECIAL[randint(0, len(SPECIAL)-1)]


    return phrase


def main(num):

    overallString =''


    with open('phrases.txt','w') as f:

        for i in range(num):
            thisPhrase = generate()

            overallString += 'passphraseList.add("'
            overallString += thisPhrase
            overallString +='");'
            overallString +='\n'




        f.write(overallString)
    print overallString

if __name__ == '__main__':

    main(int(raw_input('Please enter number of phrases you wish to generate:')))
