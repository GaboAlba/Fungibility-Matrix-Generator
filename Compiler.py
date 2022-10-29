import py_compile
import os 
import sys

os.chdir(sys.path[0])
filename1 = "RunApp.py"
py_compile.compile(filename1)
filename2 = "FungibilityMatrixGen_STL.py"
py_compile.compile(filename2)