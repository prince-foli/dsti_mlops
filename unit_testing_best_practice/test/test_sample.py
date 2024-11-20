import sys
import os

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

# Now you can import from sample
from sample import *

def test_answer():
    assert func(3) == 4

def test_add_one():
    assert add_one(3) == 4, " Adding 1 to 3 must always give 4 !!! "
