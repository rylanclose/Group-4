"""
Irene Corrin 
15310-002
11/05/19
"""
print (__doc__)
import pandas 

data = pandas.read_csv('C:/Users/13302/Downloads/.csv')
def main(): 
    """ This function opens a menu which allows an imput to be entered. There is no argument though will accept a selection until option 8 is selected """
    endProgram = 'no'
    while endProgram == 'no':
            print ('0 for About:')
            print ('1 for Appetizers: ')
            print ('2 for Sandwiches: ')
            print ('3 for Soups: ')
            print ('4 for Meatless: ')
            print ('5 for Chicken: ')
            print ('6 for Beef: ')
            print ('7 for Pork: ')
            print ('8 for Fish: ')
            print ('9 for Shellfish: ')
            print ('10 for Desserts: ')
            print ('11 for FastFood & Others:' )
            print ('12 for Exit:')
            choice = int(input('enter your selection: '))
            if choice == 0:
                print('')
            elif choice == 1:
                
                print 
            elif choice == 2:
                
                print 
            elif choice == 3:
                 
                print 
            elif choice == 4:
                
                print 
            elif choice == 4:
                
                print 
            elif choice == 5:
                
                print 
            elif choice == 7:
                
                print
            elif choice == 8:
                
                print
            elif choice == 9:
                
                print
            elif choice == 10:
                
                print
            elif choice == 11:
                
                print
            elif choice == 12:
                endProgram == 'yes'

