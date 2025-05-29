from pprint import pprint


class Database:
    def Openfile(self):
        my_file = input("what file would you like to open? ")
        while my_file != 'nw_data1.txt':
            my_file = input('Sorry this file does not exist please try again or type "n" to quit: ')
            if my_file == 'n':
                return
        print('this file will now be opened')
        f = open(my_file, "r")
        social_NW = f.read()
        f.close()
        display = input("Do you want to display the social network read from the file? (y/n) ")
        if display == 'y':
            pprint(social_NW)
        elif display =='n' :
         print("this file will not be read")
         exit()

DB = Database()
DB.Openfile()

