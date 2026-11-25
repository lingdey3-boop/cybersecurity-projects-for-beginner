import os
def ehco(k):
    print(k)
def cat():
    with open(RE,"r") as gt:
       h=gt.read()
       print(h)
def mkdir():
    os.makedirs(mk)
print("==============LINUX COMMANDS===============")
print("1.echo")
print("2.cd")
print("3.man")
print("4.cat")
print("5.mkdir")
print("6.pwd")
print("7.ls")
print("8.touch")
print("9.cp")
print("10.mv")
print("11.rm")
print("12.grep")
print("13.head")
print("14.tail")
print("15.wc")
i=input("choose the number of the command you want to learn about: ").strip()
if i=="1":
    print("ehco is function in linux which prints the words or sentance in the terminal")
    print('It works extly like pythons print function') 
    print ("for E.g")
    print(""" you type 
              print("hello world")
              it's prints
              hellow world
              in linux you just use ehco ensted of print""")
    print("now try it your self ")
    h=input("echo: ")
    ehco(h)
elif i=="2":
    print("""cd stands for change directory and is the standard Linux command 
             used to navigate between folders in the terminal""")
    print("it works similar like python os.chdir:")
    print("for example")
elif i=="3":
    print("""man is defination function in linux its 
            tell you the defination of the functions inn linux""")
    print("its works like pydoc function in your terminal")
    print("for e.g")
    print("""when you type ( py - m pydoc) in your vs code terminal 
             and then type [help (name of the function)] you get defination""")
    print("now try it yourself")
    print(""" type this in your terminal
               py - m pydoc(enter then type)
               help(name of the function you want the difination)""")
    print(""" Note; in linux you just need to type
              man(name of the function you want the difination of)
              this py -m pydoc will only work for python this 
              was for your understanding only""")
elif i=="4":
    print("""cat is read ing function in linux which help us
             to rea what is written inside a file""")      
    print("it work exgtly like python [with open(gt,r) as t] function")
    print("for e.g")
    print("""when you type this [with open(gt,"r") as t] 
             then type [h=t.read()] and then type
             [print(h)] its prints whst written in the gt file""")
    print("now try it yourself")
    print("write the name of the file you want to read below")
    RE=input("cat: ")
    cat()
elif i=="5":  
    print("mkdir is a short for make directory is a standrad linux command")
    print("line utillty used to created new folders in filesystem")
    print("its work exgesty like python os.mkdir function")
    print("for e.g")
    print("""when you type os.mkdir("a/b/c") in your code its createds a 
             file c inside b and when you type os.makedirs("a/b/c", exist_ok=True)
             its created all the foulders a,b and c """)
    print("now try it yourself")
    print("write the file name you want to created below")
    mk=input("mkdir: ")
    mkdir()
    
elif i == "6":
    print("pwd means print working directory.")
    print("It shows the full path of the folder where you are working.")
    print("In Python, os.getcwd() gives the current working directory.")
    print("Let's try it:")
    print(os.getcwd())

elif i == "7":
    print("ls lists the files and folders in the current directory.")
    print("In Python, os.listdir() gives us a list of those names.")
    print("Let's try it:")
    for name in os.listdir():
        print(name)

elif i == "8":
    print("touch creates a new empty file, or updates a file's time if it exists.")
    print('In Python, open(filename, "a").close() can create a file.')
    print("Try creating a practice file.")
    filename = input("File name, for example notes.txt: ")
    if filename and os.path.basename(filename) == filename:
        with open(filename, "a"):
            pass
        print(f"{filename} is ready.")
    else:
        print("Please enter a simple file name, not a folder path.")

elif i == "9":
    print("cp copies a file from one name to another.")
    print("Python's shutil.copy2(source, destination) does something similar.")
    print("Try copying a file you made for practice.")
    source = input("File to copy: ")
    destination = input("Name for the copy: ")

    if (source and destination
            and os.path.basename(source) == source
            and os.path.basename(destination) == destination):
        if not os.path.isfile(source):
            print("That source file does not exist in this folder.")
        elif os.path.exists(destination):
            print("A file with that destination name already exists; choose another name.")
        else:
            shutil.copy2(source, destination)
            print(f"Copied {source} to {destination}.")
    else:
        print("Please enter simple file names, not folder paths.")

elif i == "10":
    print("mv moves a file or changes its name.")
    print("Python's shutil.move(source, destination) is a similar tool.")
    print("Try it only with a practice file.")
    source = input("File to move or rename: ")
    destination = input("New name: ")

    if (source and destination
            and os.path.basename(source) == source
            and os.path.basename(destination) == destination):
        if not os.path.isfile(source):
            print("That source file does not exist in this folder.")
        elif os.path.exists(destination):
            print("A file with that destination name already exists; choose another name.")
        else:
            shutil.move(source, destination)
            print(f"Moved or renamed {source} to {destination}.")
    else:
        print("Please enter simple file names, not folder paths.")

elif i == "11":
    print("rm removes a file. Be careful: deleting a file may be hard to undo.")
    print("For practice, first create a test file with lesson 8.")
    filename = input("Name of the practice file to remove: ")

    if filename and os.path.basename(filename) == filename:
        if not os.path.isfile(filename):
            print("That file does not exist in this folder.")
        else:
            confirm = input(f"Type yes to permanently remove {filename}: ")
            if confirm == "yes":
                os.remove(filename)
                print(f"{filename} was removed.")
            else:
                print("Nothing was removed.")
    else:
        print("Please enter a simple file name, not a folder path.")

elif i == "12":
    print("grep searches a file for lines containing some text.")
    print("This example checks each line in a file for your search words.")
    filename = input("File to search: ")
    word = input("Text to find: ")

    try:
        with open(filename, "r") as file:
            found = False
            for line_number, line in enumerate(file, start=1):
                if word in line:
                    print(f"Line {line_number}: {line}", end="")
                    found = True
            if not found:
                print("No matching lines were found.")
    except FileNotFoundError:
        print("That file was not found. Check its name and try again.")

elif i == "13":
    print("head displays the first lines of a file.")
    print("This example prints the first five lines.")
    filename = input("File to read: ")

    try:
        with open(filename, "r") as file:
            for line in file.readlines()[:5]:
                print(line, end="")
    except FileNotFoundError:
        print("That file was not found. Check its name and try again.")

elif i == "14":
    print("tail displays the last lines of a file.")
    print("This example prints the last five lines.")
    filename = input("File to read: ")

    try:
        with open(filename, "r") as file:
            for line in file.readlines()[-5:]:
                print(line, end="")
    except FileNotFoundError:
        print("That file was not found. Check its name and try again.")

elif i == "15":
    print("wc counts information in a file. It commonly reports lines, words, and characters.")
    filename = input("File to count: ")

    try:
        with open(filename, "r") as file:
            text = file.read()
            print(f"Lines: {len(text.splitlines())}")
            print(f"Words: {len(text.split())}")
            print(f"Characters: {len(text)}")
    except FileNotFoundError:
        print("That file was not found. Check its name and try again.")

else:
    print("Please choose a number from 1 to 15.")