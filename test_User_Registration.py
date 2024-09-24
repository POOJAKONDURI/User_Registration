'''

@Author: Pooja
@Date: 24-09-2024
@Last Modified by: Pooja 
@Last Modified: 24-09-2024
@Title : pytest on user registartion.

'''

import pytest
from User_Registration import chck_name,chck_mail,chck_mobilenum,chck_paswdrule1,chck_passwdrule2,chck_passwdrule3,chck_passwdrule4

def test_chck_name():
    assert chck_name("John") == 1  # Valid name
    assert chck_name("jo") == 0     # invalid(<3))
    assert chck_name("john") == 0   # Invalid (does not start with uppercase)
    assert chck_name("J") == 0       # Invalid (<3)

def test_chck_mail():
    assert chck_mail("test@example.com") == True  # Valid
    assert chck_mail("test.example@example.com") == True  # Valid 
    assert chck_mail("invalid-email") == False    # Invalid email bcox no m
    assert chck_mail("test@.com") == False         # Invalid email

def test_chck_mobilenum():
    assert chck_mobilenum("91 1234567890") == 1  # Valid mobile number
    assert chck_mobilenum("1234567890") == 0     # Invalid (format)
    assert chck_mobilenum("91 12345") == 0        # Invalid (too short)

def test_chck_paswdrule1():
    assert chck_paswdrule1("Password1") == True  # Valid password(>8 charecter)
    assert chck_paswdrule1("Short") == False      # Invalid (<8)

def test_chck_passwdrule2():
    assert chck_passwdrule2("Password1") == True  # Contains uppercase
    assert chck_passwdrule2("password1") == False  # No uppercase

def test_chck_passwdrule3():
    assert chck_passwdrule3("Password1") == True  # Contains number
    assert chck_passwdrule3("Password") == False   # No number

def test_chck_passwdrule4():
    assert chck_passwdrule4("Password!") == True   # Exactly one special character
    assert chck_passwdrule4("Password!!") == False  # More than one special character
    assert chck_passwdrule4("Password") == False    # No special character
    assert chck_passwdrule4("Password!@") == False   # More than one special character
