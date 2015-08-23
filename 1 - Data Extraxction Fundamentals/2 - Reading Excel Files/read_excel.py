#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    #print "\nROWS, COLUMNS, and CELLS:"
    #print "Number of rows in the sheet:", 
    #print sheet.nrows
    #print "Type of data in cell (row 3, col 2):", 
    #print sheet.cell_type(3, 2)
    #print "Value in cell (row 3, col 2):", 
    #print sheet.cell_value(3, 2)
    #print "Get a slice of values in column 3, from rows 1-3:"
    #print sheet.col_values(3, start_rowx=1, end_rowx=4)

    #print "\nDATES:"
    #print "Type of data in cell (row 1, col 0):", 
    #print sheet.cell_type(1, 0)
    #exceltime = sheet.cell_value(1, 0)
    #print "Time in Excel format:",
    #print exceltime
    #print "Convert time to a Python datetime tuple, from the Excel float:",
    #print xlrd.xldate_as_tuple(exceltime, 0)
    
    data = {
            'maxtime': (0, 0, 0, 0, 0, 0),
            'maxvalue': 0,
            'mintime': (0, 0, 0, 0, 0, 0),
            'minvalue': 0,
            'avgcoast': 0
    }
    
    #print "\nMINE:"
    #print "Column name : " + sheet.cell_value(0,1)
    
    maximum = 0
    minimum = 20000
    summation = 0
    average = 0
    
    #rows = sheet.nrows
    #print rows
    
    #print sheet_data[0]
    #print len(sheet_data)
    for row in range(1, len(sheet_data)) :
        cell = sheet.cell_value(row,1)
        if cell > maximum : 
            maximum = cell
            max_row = row
        if cell < minimum : 
            minimum = cell
            min_row = row
        summation += cell
    average = summation / (sheet.nrows - 1)
    max_time = sheet.cell_value(max_row,0)
    min_time = sheet.cell_value(min_row,0)
    
    #print max_time
    #print min_time
    
    #print "Maximum : ",
    #print maximum
    #print "Minimum : ",
    #print minimum
    #print "Average : ",
    #print average
    
    data['maxvalue'] = maximum
    data['minvalue'] = minimum
    data['avgcoast'] = average
        
    data['maxtime'] = xlrd.xldate_as_tuple(max_time,0)
    data['mintime'] = xlrd.xldate_as_tuple(min_time,0)
    
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()