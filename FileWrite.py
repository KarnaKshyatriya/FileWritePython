import os


while True:
    choice=input("Please enter your choice \n 1> Write \n 2> Read \n 3> Close")
    if choice=="1":
        lines=input("Please enter your lines of Text")
        mode = "a" if  os.path.exists("myFileWrite.txt") else "x"
        with open("myFileWrite.txt",mode) as f:
            f.write(lines+"\n")
    elif choice=="2":
        if os.path.exists("myFileWrite.txt"):
            with open("myFileWrite.txt","r") as f:
                print(f.read())
        else:
            print("The file doesnt exist")
    elif choice=="3":
        break
    else:
        print("Enter aid Choice")
    