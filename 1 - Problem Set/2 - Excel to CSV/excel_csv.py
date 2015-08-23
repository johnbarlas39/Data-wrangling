# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.
import xlrd
import os
import csv
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = []
    # YOUR CODE HERE
    # Remember that you can use xlrd.xldate_as_tuple(sometime, 0) to convert
    # Excel date to Python tuple of (year, month, day, hour, minute, second)
    
    for i in range(1,9):
        station = sheet.cell_value(0,i)
        values = sheet.col_values(i, start_rowx=1, end_rowx=None)
        max_value = max(values)
        max_pos = values.index(max_value) + 1
        time = xlrd.xldate_as_tuple(sheet.cell_value(max_pos, 0), 0)
        row = [station]
        for t in range(4) : row.append(time[t])
        row.append(max_value)
        data.append(row)
        
    
    return data

def save_file(data, filename):
    # YOUR CODE HERE
    with open(filename, 'w') as f:
        writer = csv.writer(f, delimiter='|')
        writer.writerow(['Station','Year','Month','Day','Hour','Max Load'])
        for item in data:
            writer.writerow(item)
    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    ans = {'FAR_WEST': {'Max Load': "2281.2722140000024", 'Year': "2013", "Month": "6", "Day": "26", "Hour": "17"}}
    
    fields = ["Year", "Month", "Day", "Hour", "Max Load"]
    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            s = line["Station"]
            if s == 'FAR_WEST':
                for field in fields:
                    assert ans[s][field] == line[field]

        
test()