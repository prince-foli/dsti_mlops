# Always run from unit_testing_best_practice/test

import sys
sys.path += ['../src'] 
from sample import *

def test_add_one():
    assert add_one(3) == 4, " Adding 1 to 3 must always give 4 !!! "
