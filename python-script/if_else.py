#!/usr/bin/env python
# This is some secure program that uses security.
import sys

validPassword = 'secret' #this is our password.

inputPassword = raw_input('Please Enter Password: ')

if inputPassword == validPassword:
    print 'You have access!'
else:
    print 'Access denied!'
    sys.exit(0)

print 'Welcome!'
b = 10
a = raw_input('Please enter a valid value----')
b = raw_input('Please a value for b-----')
b = a
if a == b:
   print 'you have value'
else: 
    print 'no value' 
    sys.exit(0)
print 'Welcome!'

