'''

@Author: Pooja
@Date: 23-09-2024
@Last Modified by: Pooja 
@Last Modified: 23-09-2024
@Title :User registration problems UC2-User need to enter a valid First Name and second name

'''
import re
def chck_name(name):
      '''
       Definition:
       The check_name function is designed to validate a given second name based on specific criteria.
       Parameters:
       first_name (str): A string representing the first name to be checked.
       second_name : string representing sedcond name to be checked
       Return:
       1 if the name is at least 3 characters long and starts with an uppercase letter.
       0 otherwise.
    
    '''
      
      x = re.search(r'\b[A-Z]',name)
      if len(name)>3 and x:
            return 1
      else :
            return 0
      
def main():
      first_name = input("entr your first name: ")
      if chck_name(first_name):
            print(f"entered first name {first_name} is valid")
      else:
            print(f"entrd first name is not valid,It must start with a capital letter and have at least 3 characters.")
            
      second_name = input("enter your second name: ")
      if chck_name(second_name):
            print(f"entered second name {second_name} is valid") 
      else:
            print("enterd second name is invalid,It must start with a capital letter and have at least 3 characters.")

if __name__ == "__main__":
      main()