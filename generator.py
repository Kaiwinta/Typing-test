from random import randint


def generate_text(list_letter : str , maxlength : int, maxword : int):
    """
        Variable:
            list_letter : a str of all the letter that the user want to practice 
            maxlength  : the maximum length of a word muss be superior as 3
            maxwords : the maximum amout of word in a try muss be superior as 10
    
    """
    #To only have unique letter and avoid easy typing 
    list_unique_letter = []
    print(list_letter)

    if list_letter.lower() == 'all':
        list_unique_letter = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z" ]
    
    
    for i in list_letter.lower():
        if i not in list_unique_letter:
            list_unique_letter.append(i)

    #Generation of the random things to type
    text = ''
    nbmot =0
    while nbmot < maxword:
        word = ''
        #We want at least word with 3 charaters
        for i in range (randint(3,maxlength)):
            word+= list_unique_letter[randint(0,len(list_unique_letter)-1)]
        #Adding the word to the text with a space
        text += word +" "
        nbmot+=1
    return text[:-1]
