#Implementation: A class Username was created. This class takes on an attribute 'Userid'. The class have an init function that initializes the User1 attributes. The class have a method gen_username. This method does the work of extracting the first 2 and 3 letters of each name respectively and adding two random numbers generated with randrange from the random package. An object User1 was created and assigned a Userid of one. The gen_username method was then called on the object to give the username of User1.

#Input: Enter your full name, both should be entered separately. The case of the letters depends on the User. If you want your Username to be uppercase, enter your full name accordingly.
#Example input: Sonia Anthony

#Output: The program will output first 2 strings and first 3 strings of each name, plus two random numbers
#Example output: SoAnt73


#Please take your time to go through this project.
#Your feedbacks are welcomed!




#import the required packages
import random
#define the Username class
class Username:

  # write an __init__ function to initialize the attribute
  def __init__(self, UserId):
    self.UserId = UserId
    print(f'Welcome to the Username Generator Program User {UserId}: ')

  #define the gen_username method 
  def gen_username(self):

    #take full name from users
    full_name = input("Please enter your full name: ")

    #assign the full_names to the Userid attribute
    self.UserId=full_name

    #Split the full_name
    names = full_name.split(" ")

    #Slice the first name to get the first two string in the name
    two_letters_names = names[0][0:2]

    #Slice the second name to get the first 3 string in the name
    three_letters_surname = names[1][0:3]

    #Generate random whole numbers between 10 and 99 using randrange.
    number = '{0:2d}'.format(random.randrange (10,99))
    
    #Use the string join method to join the 2 and 3 letters derived to the 
    #2 numbers
    username = "".join([two_letters_names, three_letters_surname, str(number)])
    print(f'Dear {self.UserId}, your username is : {username} ')
  
User1 = Username('1')
User1.gen_username()
