# CSCI 1550, hw13pr2
# Filename: hw13pr2.py
# Name: Peter Morales
# Problem description: Making your own testing suite!!
#

import math
import random

def mag(vec):
    magVal = 0
    for x in vec:
        magVal = magVal + x**2
    magVal = math.sqrt(magVal)
    return magVal

def divByMag(vec):
    magVal = mag(vec)
    N = len(vec)
    vecOut = [0]*N
    for k in range(N):
        vecOut[k] = vec[k]/magVal
    return vecOut

# Helpful fuctions from the notes
def close_to(x1, x2, precision):
    return abs(x1-x2) < precision

def vec_close_to(v1, v2, precision):
    bool_out = True
    for k in len(v1):
        bool_out = bool_out and close_to(v1[k],v2[k],precision)
    return bool_out

def test_divByMag_errors():
    test_result = True
    try:
        mag()
        test_result = False
        #print(test_result)
    except TypeError:
        test_result = test_result and True
        #print(test_result)

    try:
        mag(5)
        test_result = False
        #print(test_result)
    except TypeError:
        test_result = test_result and True
        #print(test_result)

    try:
        mag(5.1)
        test_result = False
        #print(test_result)
    except TypeError:
        test_result = test_result and True
        #print(test_result)

    try:
        mag('w')
        test_result = False
        #print(test_result)
    except TypeError:
        test_result = test_result and True
        #print(test_result)

    try:
        mag(1,2)
        test_result = False
        #print(test_result)
    except TypeError:
        test_result = test_result and True
        #print(test_result)

    try:
        mag(1 +'x')
        test_result = False
        #print(test_result)
    except TypeError:
        test_result = test_result and True
        #print(test_result)
    
    return test_result


def test_divByMag():
    try:
        assert close_to(mag([5,5,0]),math.sqrt(50),10**(-6))
        assert close_to(mag([2,1]),math.sqrt(5),10**(-6))
        assert close_to(mag([2,2,2,2]),4,10**(-6))
        assert mag([0,0,0,0]) == 0
        assert mag([]) == 0
        x = random.choice(range(1,99))
        assert mag([-x]) == x

        test_result = True
    except AssertionError:
        test_result = False
    except:
        test_result = False

    return test_result

# Driver code
def perform_tests():
    print("test_mag() ... ", end=' ')
    if test_divByMag():
        print("OK")
    else:
        print("FAILED")
    print("\n")
    print("test_mag_errors() ... ", end=' ')
    if test_divByMag_errors():
        print("OK")
    else:
        print("FAILED")

