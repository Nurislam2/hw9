symbols=["!","\"","#","$","%","&","'","(",")","*","+",",","-",
         ".","/","0","1","2","3","4","5","6","7","8","9",":",";","<","=",">","?","@","A","B","C","D","E","F","G","H","I","J",
         "K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","[",
         "\\","j","^","'","a","b","c","d","e","f","g","h","i","j",
         "k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","{","|","}","~"]
import random
def password():
    pasword=""
    for i in range(0,11):
        pasword+=symbols[random.randint(0,92)]
    return pasword
print(password())