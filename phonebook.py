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
                          # 67676767
                          #ggg
                          #ddd
                          #wewer
                          #bla bla
                          # I love milk

                          print(phone_book)
                          return phone_book

                     def menu():
                              #...
                              #....
                              ####
                              print("********************************************************************")
                              print("\t\t\tSMARTPHONE DIRECTORY", flush=False)
                              print("********************************************************************")
                              print("\tYou can now perform the following operations on this phonebook\n")
                              print("1. Add a new contact")
                              print("2. Remove an existing contact")
                              print("3. Delete all contact")
                              print("4. Search for a contact")
                              print("5. Display all contact")
                              print("6. Exit phonebook")

                              #aa
                              #bb
                              choice = int(input("Please enter your name"))

                              return choice

                     def add_contact(pb):
                          #cc
                          #dd
                          dip = []
                          for i in range(len(pb[0])):
                               if i == 0:
                                    dip.append(str(input("Enter name: ")))
                               if i == 1:
                                    dip.append(str(input("Enter number: ")))
                               if i == 2:
                                    dip.append(str(input("Enter e-mail address: ")))
                               if i == 3:
                                    dip.append(str(input("Enter date of birth(dd/mm/yy): ")))
                               if i == 4:
                                    dip.append(
                                         str(input("Enter category(Family/Friends/Work/Others): ")))
                          pb.append(dip)
                         #SWWQD
                          return pb
                def remove_existing(pb):
                     #
                     query = str(
                          input("please enter the name you'd like to remove"))
                     #ee
                     temp = 0
                     #ff

                     for i in range(len(pb)):
                          if query == pb [i][0]:
                               temp += 1
                               #gg
                               print(pb.pop(i))