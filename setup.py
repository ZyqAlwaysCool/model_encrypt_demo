from distutils.core import setup
from Cython.Build import cythonize
from config import *

def py2so(setup_list):
    setup(ext_modules=cythonize(setup_list))

if __name__ == '__main__':
    py2so(PY2SO_LIST)