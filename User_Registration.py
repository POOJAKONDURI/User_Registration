'''

@Author: Pooja
@Date: 23-09-2024
@Last Modified by: Pooja 
@Last Modified: 23-09-2024
@Title :User registration problems UC1-User need to enter a valid First Name

'''
import re
def chck_firstname(first_name):
      '''
       Definition:
       The check_firstname function is designed to validate a given first name based on specific criteria.
       Parameters:
       first_name (str): A string representing the first name to be checked.
       Return:
       1 if the first_name is at least 3 characters long and starts with an uppercase letter.
       0 otherwise.
    
    '''
      
      x = re.search(r'\b[A-Z]',first_name)
      if len(first_name)>3 and x:
            return 1
      else :
            return 0
      
def main():
      first_name = input("entr your first name: ")
      if chck_firstname(first_name):
            print(f"entered first name {first_name} is valid")
      else:
            print(f"entrd name is not valid")

if __name__ == "__main__":
      main()