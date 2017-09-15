### This script is for passing variable with script run i.e " python script.py name age(digits)
#!/usr/bin/env python
# Years till 100
import sys

name = sys.argv[1]
age = int(sys.argv[2])

print 'Hello', name  ,  'your age is' , age  , 'years'
