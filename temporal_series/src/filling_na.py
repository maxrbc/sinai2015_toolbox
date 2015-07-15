from pandas import read_table
from numpy.random import randint , random_sample
import numpy as np


def making_random_na_test_column(table):
    result  = map((lambda x,y : np.nan if x == 0 else y) ,
                    randint(2 , size = len(table.values)) ,
                    random_sample(len(table.values)))
    return result

def fill_na_in_table(table ,subjects_id , method = 'ffill'):
    #need to recover later the samples subjectsID
    subjects = table[subjects_id]
    result = table.copy().groupby(subjects_id)

    if method == 'ffill' :
        result = result.ffill()
        result = result.bfill()

    elif method == 'bfill' :
        result  = result.bfill()
        result  = result.ffill()

    elif method == 'interfill':
        result = result.interpolate()
        result = result.ffill()
        result = result.bfill()

    else :
        print "Unknown format ... \n"
        print "Should be on of this : \n"
        print " foward_fill : ffill , \n backward_fill : bfill \n , interpolate : interfill \n"
    
    result[subjects_id] = subjects
    return result

def determine_if_na(table):
    have_na = []
    temp = table.isnull()

    for k,v in temp.iteritems():
        if True in list(v):
            have_na.append(k)

    return have_na
