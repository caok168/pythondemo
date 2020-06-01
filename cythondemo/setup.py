from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize(["mytest.py"]))

# setup(
#     ext_modules=cythonize("mytest.py"),
# )