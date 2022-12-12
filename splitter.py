import re

def s_splitter(filename):
    with open(filename,'r') as f:
        fileContent = f.read()

    #remove \n(newlines)
    sentences = re.sub(r'\n','',fileContent)
    #add new line after each period
    #preceded by 'Mr', 'Mrs' or 'Dr' and is followed by a space and an uppercase letter
    sentences = re.sub(r'(?<!Mr)(?<!Mrs)(?<!Dr)\.\s([A-Z])', r'.\n\1', sentences)
    #adds new line after !
    sentences = re.sub(r'!\s', '!\n', sentences)
    #adds new line after ?
    sentences = re.sub(r'\?\s', '?\n', sentences)
    
    print (sentences)

s_splitter(filename='splitme.txt')