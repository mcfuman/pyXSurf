"""  This module contains functions able to read raw data from different formats.
     Returns data and reader with minimal data processing, functions are about formats, 
     not the specific instrument or specific header, that are handled in calling functions
     (e.g. from instrument_reader) 

2018/09/26 New refactoring of data reader. Vincenzo Cotroneo vcotroneo@cfa.harvard.edu"""

from read_sur_files import readsur

def read_sur(file):
    res = readsur(file,raw = False)
    data,x,y = res.points,res.xAxis,res.yAxis
    del res.points
    del res.xAxis
    del res.yAxis
    return (data,x,y),header
    
    