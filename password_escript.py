from random import*
import sys
def menu():
    input1=int(input(""" please select what you want to do: 
1.Encrypt              
2.creat_password
3.exit
"""))
    if input1==1:
        encrypt_decrypt()
    elif input1==2:
        creat_password()
    elif input1==3:
        sys.exit
    else:
        print("invalid entry try again")
        menu()
def encrypt_decrypt():
    text=input("what password you want to encrypt?")
    text4=text.encode("utf_16")
    text3=[text,text4]
    print (text4)
    input2=int(input("You want to decrypt your password?:1.Yes/2.No"))
    if input2==1:
        text2=text4.decode("utf_16")
        print(text2)
        f=open("password.txt", "a")
        f.write(str(text3))
        f.close()
    elif input2==2:
        f=open("password.txt", "a")
        f.write(str(text3))
        f.close()
        menu()
    else:
        sys.exit
def creat_password():
    numbers=[0,1,2,3,4,5,6,7,8,9]
    symbols=["!","@","$","%","^","&"]
    lower=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    upper=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    mikoskwdikou=int(input("How many items do you want the code to be?;(4,8,12)"))
    password=[]
    for i in range(int(mikoskwdikou/4)):
        password.append(choice(numbers))
        password.append(choice(symbols))
        password.append(choice(lower))
        password.append(choice(upper))
    shuffle(password)
    print(''.join(str(i) for i in password))
    encrypt_decrypt()
menu()
