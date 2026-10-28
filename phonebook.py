#importing the module
import sys

# this function will be the first to run....
def intial_phonebook():
    rows, cols = int(input("Please enter initial numbers of contacts: ")), 5

    #we are collecting numbers of contacts....
    #phonebook already......
    phone_book = []
    print(phone_book)
    for i in range(rows):
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("NOTE: * indicates mandatory fields")
        print(".....................................................................")
        temp = []
        for j in range(cols):
            # we have taken the conditions...
            # such as....
                if j == 0:
                     temp.append(str(input("Enter name*: ")))
                     # we need to check if the user has left the name empty...
                     #name & number...
                     #So implement a condition
                     if temp[j] == '' or temp[j] == ' ':
                          sys.exit(
                               "Name is a mandatory field. process exiting due to blank field")          
                            # This will exit.......
                if j == 1:
                     temp.append(int(input("Enter number*: ")))
                     # (more comments = ...)
                     #(even more)
                     #to........
                if j == 2:
                     temp.append(str(input("Enter email address: ")))
                     # SOME MORE COMMENTS
                if temp[j] == '' or temp[j] == ' ':
                     temp[j] = None

                     if j == 3:
                          temp.append(str(input("Enter date of birth(dd/mm/yy) :")))
                          #.....
                          #..........
                          #...
                     if temp[j] == '' or temp[j] == ' ':
                          #.....
                          temp[j] = None
                     if j == 4:
                          temp.append(
                               str(input("Enter category(Family/Friends/Work/Others): ")))
                          #blah blah blah
                          