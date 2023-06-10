from random import randint


def generate_text(list_letter : list , maxlength : int, maxword : int):
    """
        Variable:
            list_letter : a list of all the letter that the user want to practice 
            maxlength  : the maximum length of a word muss be superior as 3
            maxwords : the maximum amout of word in a try muss be superior as 10
    
    """
    
    text = ''
    while len(text)< maxword*maxlength/2:
        word = ''
        for i in range (randint(3,maxlength)):
            word+= list_letter[randint(0,len(list_letter)-1)]
        #Adding the word to the text with a space
        text += word +"_"
    return text

liste1 = ["a","b","t","j","e","i","w","p"]
liste2 = ["a","b"]
liste3 = ["a","b","t","j","e"]


print(generate_text(liste1,7 , 15))
print(generate_text(liste2,12,8))
print(generate_text(liste3,6,13))

