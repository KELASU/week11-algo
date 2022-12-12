import re
# this variable defines the txt file name
txtname = "hapax.txt"
# the function called hapax_function is used to check or find the hapax words
def hapax_function(txtname):
    lister =[]
    # this opens the txt file which has been defined as a variable
    file = open(txtname,encoding="utf8")
    # it reads the file and split word per word by the space in between each word and it will put it into a list
    listword = file.read().split()
    # Is a new list
    listwords = []

    #loops the list of word in the list called listword
    for word in listword :
        # the variable resword is a way for us to remove the punctuation for the word in list word
        # and the removed punctuatuion is than replace with empty space or none
        # \w is word
        # \s is white space
        # ^ makes it starts from the beginning of the line/word/string
        # and r represents raw string
        # re.sub is a way to replace the contents of the string with a new string
        resword = re.sub(r'[^\w\s]', '', word)
        # .lower() will make sure that capitalization will be ignored because it will turn the whole word lower case
        # the one below will append the word into a list
        listwords.append(resword.lower())
    #frequency represents a dictionary that contains 2 things
    # the key which is the word
    # and the number of the word appearing in the list as the value
    frequency = {key: 0 for key in listwords}
    # the for loop bellow will loop through the words in listwords
    for word in listwords:
        # and than it adds 1 to the value in each key that's defined by the word
        # so everytime a word appear the value of the word +1
        # for example the word is " a dog meets a dog with a collar"
        # in the dictionary it will appear as {"a":3, "dog":2, "meets":1, "with":1, "collar":1}
        frequency[word] += 1
    # and then we have another for loop bellow which loops trhought the word(keys) in the dictionary called frequency
    for word in frequency:
        #and than it will check if the key in the dictionary have the value 1
        if frequency[word] == 1:
            # if the value of the key is 1 than it will append the word or key into the list called lister 
            # and the word that is appended to the list called lister are all hapax
            lister.append(word)
    # and than it will return the list called lister after it finish all processes
    # the list contains all the hapax words
    return lister
# variable a is just to define the function
# and hapax_function(txtname) is to run the function
a = hapax_function(txtname)
# and finally print(a) prints the returned list called lister that contains all the hapax words
print(a)