# Author-Connor Dedic
# Date- 12/9/2023
# Summary-Library of functions for detecting typos

# import libraries

from pandas import read_csv
import pytest

# ---------------------------------------------------------------------------
# General notes
# ALL indexed functions are assumed to be zero indexed
        
# This function will locate serial numbers from correct csv 
# also known as correct list
def readLst(ind, file):
    with open(file) as file_to_read:
        values = []
        for i in file_to_read:
            values.append(i)
    located_value = values[ind]
    return(located_value)
# Uncheck line below to test function

# ---------------------------------------------------------------------------

# This function finds the length of a dataframe
# Input correctlist = True for 'CorrectCSV' and correctlist = False for
# 'IncorrectCSV
def lenOfList(correctlist = True):
    
    if correctlist == True:
        df = read_csv('Correct.csv')
        
    elif correctlist == False:
        df = read_csv('Incorrect.csv')
        
    return(df.shape[0])
    
# Uncheck row below to test function
# print('false list: ' + lenOfList(correctlist = False))
# print('true list: ' + lenOfList(correctlist = True))


# ---------------------------------------------------------------------------

# Scoring- using the Levenshtien Distance algorithm

def scoreCalc(val1, val2):
    val1 = str(val1)
    val2 = str(val2)
    # The cache is a 2-d matrix that will store the data
    cache = [[0 for i in range(len(val2) + 1)] for j in range(len(val1) + 1)]
    
    # base cases
    for j in range(len(val2)+1):
        cache[len(val1)][j] = len(val2)-j
        
    for i in range(len(val1)+1):
        cache[i][len(val2)] = len(val1)-i
        
    # Dynamic Programming
    for i in range(len(val1) -1, -1, -1):
        for j in range(len(val2)-1 ,-1, -1):
            if val1[i] == val2[j]:
                cache[i][j] = cache[i+1][j+1]
            else:
                cache[i][j] = 1 + min(cache[i+1][j],
                                      cache[i][j+1], cache[i+1][j+1])
                
    return(cache[0][0])

# Uncheck to test function below 
# print(scoreCalc('J29054527071', 'J2907545207B1'))
# inputs = 'J2905452707B1', 'J2907545207B1', (expected value = 2)

def testscoreCalc():
    assert scoreCalc('clock', 'clock') == 0
    assert scoreCalc('clock', 'Clock') == 1
    assert scoreCalc('clock', 'Clack') == 2
    assert scoreCalc('clock', 'CloACk') == 3

    
pytest.main(["-v", "--tb=line", "-rN", __file__])

