'''

@Author: Pooja
@Date: 23-09-2024
@Last Modified by: Pooja 
@Last Modified: 23-09-2024
@Title :User registration problems UC4- to enter valid mobile number according to criteria.

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
def chck_mail(mail):
      """
    Validates the format of an email address according to specified rules.

    Parameters:
        email (str): The email address to validate.

    Returns:
        bool: True if the email address is valid, False otherwise.
        """
      
      pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$'
      return bool(re.match(pattern,mail))

def chck_mobilenum(mobile_number):
       """
    Validates the format of mobile num according to specified rules.

    Parameters:
        mobile_number (int): The phone num to validate.

    Returns:
        1: if neter number is true.
        0:otherwise
        """
       #r'^\+?[0-9]{2}\s[0-9]{10}$' 
       if re.search(r'^\d{2}\s\d{10}$',mobile_number):
        #d is decimal num
        return 1
       else:
        return 0
       
def chck_paswdrule1(passwd1):
      """
    Validates password with minimum 8 Character.

    Parameters:
        passwd (str): The email address to validate.

    Returns:
        True : True if passwd is greater or equall to eight characters, False otherwise.
        """
      if len(passwd1) >= 8:
        return True
      else :
        return False

     
      
      
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

      email = input("enter email id: ")
      if chck_mail(email):
        print(f"entered email id {email} is valid")
      else:
        print("invalid emial ID")

      mobile_number = input("enter mobile number : ")
      if chck_mobilenum(mobile_number):
        print(f"given number {mobile_number} is valid")
      else:
         print("invalid mobile number")

      #rule 1
      passwd1 = input("entr password : ")
      if chck_paswdrule1(passwd1):
           print(f"pasword entered {passwd1} is valid")
      else:
           print("entered password is invalid,it must have 8 charcters")

if __name__ == "__main__":
      main()