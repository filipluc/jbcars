'''
Created on Dec 16, 2016

@author: Filip

GUM login  - Chrome
'''

import unittest
from xmlrunner import *
import os
import sys


rootDir = "d:\Github\jbcars"
# add all paths inside rootDir in sys.path, in order for the import to find all tests
for root, dirs, files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    sys.path.append(root)


#from AddCars import addcarall
from AddCars import addcar_single
from AddCars import addcarTOATE

#suite1 = addcarall.suite()
suite2 = addcar_single.suite()
suite3 = addcarTOATE.suite()


def suite():
    suite = unittest.TestSuite()
    tests = [suite2]
    #tests = [suite1, suite2]
    for test in tests:
        suite.addTest(test)
    #close the application at the end of all tests
    #suite.addTest(suite0)    
    return suite
    

###   - pentru xmlrunner 1.7.7, insa trateaza assertul ca eroare:
#result = XMLTestRunner(output='unittest').run(suite())

####  - pentru xmlrunner 0.1, folosit la Sikuli - se foloseste open in loc de file, care nu mai exista in python3
result = XMLTestRunner(open("unittest.xml", "w")).run(suite())

#write multiple suites in one file  -- nu merge in jenkins, nu recunoaste xml-ul, pentru ca sunt mai multe suite  -- pentru xmlrunner 1.7.7
# with open('unittest.xml', 'w') as output:
#     #unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output))
#     result = XMLTestRunner(output=output).run(suite())

