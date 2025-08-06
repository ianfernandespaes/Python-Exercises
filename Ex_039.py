phrase = str(input("Enter a sentence: ")).strip().upper()
print('The letter A appears {} times in the sentence'.format(phrase.count('A')))
print('The first letter A appears at position {}'.format(phrase.find('A') + 1))
print('The last letter A appears at position {}'.format(phrase.rfind('A') + 1))
