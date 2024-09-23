'''

@Author: Pooja
@Date: 23-09-2024
@Last Modified by: Pooja 
@Last Modified: 23-09-2024
@Title :User registration problems UC8-password with only one special cnaracter.

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
        passwd (str): The password to set.

    Returns:
        True : True if passwd is greater or equall to eight characters, False otherwise.
        """
      if len(passwd1) >= 8 :
        return True
      else :
        return False

def chck_passwdrule2(passwd1):
    """
    Validates password with atleast one upeercase.

    Parameters:
        passwd1 (str): password.

    Returns:
        True : True if passwd has uppercase False otherwise.
        """
    if re.search(r'[A-Z]',passwd1):
        return True
    else :
        return False

def chck_passwdrule3(passwd1):
    """
    Validates password with atleast one numeric value.

    Parameters:
        passwd1 (str): password.

    Returns:
        True : True if passwd has atleast one numeric value False otherwise.
        """
    if re.search(r'[0-9]',passwd1):
        return True
    else:
        return False

def chck_passwdrule4(passwd1):
    """
    Validates password with one specisl charecter.

    Parameters:
        passwd1 (str): password.

    Returns:
        True : True if passwd have one special charecter False otherwise.
        """
    special_characters = re.findall(r'[!@#$%^&*(),.?":{}|<>]', passwd1)
    if len(special_characters) != 1:
        return False

    # If all rules are passed, return True
    return True




     
      
      
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

      passwd1 = input("enter password : ")
      # Rule 1: Minimum 8 characters
      if not chck_paswdrule1(passwd1):
        print("Password must be at least 8 characters long.")
        return

    # Rule 2: At least one uppercase letter
      if not chck_passwdrule2(passwd1):
        print("Password must contain at least one uppercase letter.")
        return

    # Rule 3: At least one numeric digit
      if not chck_passwdrule3(passwd1):
        print("Password must contain at least one numeric digit.")
        return

    # Rule 4: Exactly one special character
      if not chck_passwdrule4(passwd1):
        print("Password must contain exactly one special character.")
        return

      print("Password successfully set!")

        
if __name__ == "__main__":
      main()