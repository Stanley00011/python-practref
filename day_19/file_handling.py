"""
File Handling
So far we have seen different Python data types. We usually store our data in different file formats. In addition to handling files, we will also see different file formats(.txt, .json, .xml, .csv, .tsv, .excel) in this section. First, let us get familiar with handling files with common file format(.txt).

File handling is an import part of programming which allows us to create, read, update and delete files. In Python to handle data we use open() built-in function.

# Syntax
open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update
"r" - Read - Default value. Opens a file for reading, it returns an error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""

# Opening Files for Reading
# The default mode of open is reading, so we do not have to specify 'r' or 'rt'. I have created and saved a file named reading_file_example.txt in the files directory. Let us see how it is done:

f = open('./day_19/reading_file_example.txt') 
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# As you can see in the example above, I printed the opened file and it gave some information about it. Opened file has different 
# reading methods: read(), readline, readlines. An opened file has to be closed with close() method.

# read(): read the whole text as string. If we want to limit the number of characters we want to read, we can limit it by passing int value to the read(number) method.

f = open('./day_19/reading_file_example.txt') 
txt = f.read()
print(type(txt))
print(txt)
f.close()

# Instead of printing all the text, let us print the first 10 characters of the text file.
f = open('./day_19/reading_file_example.txt') 
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

# readline(): read only the first line
f = open('./day_19/reading_file_example.txt') 
line = f.readline()
print(type(line))
print(line)
f.close()

# readlines(): read all the text line by line and returns a list of lines
f = open('./day_19/reading_file_example.txt') 
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# Another way to get all the lines as a list is using splitlines():
f = open('./day_19/reading_file_example.txt') 
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()


# After we open a file, we should close it. There is a high tendency of forgetting to close them. There is a new way of opening files using 
# with - closes the files by itself. Let us rewrite the the previous example with the with method:\
with open('./day_19/reading_file_example.txt')  as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

"""
Opening Files for Writing and Updating
To write to an existing file, we must add a mode as parameter to the open() function:

"a" - append - will append to the end of the file, if the file does not exist it creates a new file.
"w" - write - will overwrite any existing content, if the file does not exist it creates.
Let us append some text to the file we have been reading:

"""

with open('./day_19/reading_file_example.txt', 'a')  as f:
    f.write('This text has to be appended at the end')

with open('./day_19/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')

#     Deleting Files
# We have seen in previous section, how to make and remove a directory using os module. 
# Again now, if we want to remove a file we use os module.

# import os
# os.remove('./day_19/example.txt')

# If the file does not exist, the remove method will raise an error, so it is good to use a condition like this:

import os
if os.path.exists('./day_19//example.txt'):
    os.remove('./day_19//example.txt')
else:
    print('The file does not exist')


"""
File Types
File with txt Extension
File with txt extension is a very common form of data and we have covered it in the previous section. Let us move to the JSON file

File with json Extension
JSON stands for JavaScript Object Notation. Actually, it is a stringified JavaScript object or Python dictionary.

Example:
"""

# dictionary
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: A string form a dictionary
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''

# Changing JSON to Dictionary
# To change a JSON to a dictionary, first we import the json module and then we use loads method.

import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# Changing Dictionary to JSON
# To change a dictionary to a JSON we use dumps method from the json module.

import json
# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4) # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)

# when you print it, it does not have the quote, but actually it is a string
# JSON does not have type, it is a string type.

# Saving as JSON File
# We can also save our data as a json file. Let us save it as a json file using the following steps. For writing a json file, we use the json.dump() method,
# it can take dictionary, output file, ensure_ascii and indent.
# In the code above, we use encoding and indentation. Indentation makes the json file easy to read.

""" File with csv Extension
CSV stands for comma separated values. CSV is a simple file format used to store tabular data, such as a spreadsheet or database. CSV is a very common data format in data science.

Example:

"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
"""

import csv
with open('./day_19/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # we use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
"""
File with xlsx Extension
To read excel files we need to install xlrd package. We will cover this after we cover package installing using pip.

import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
"""

""" File with xml Extension
XML is another structured data format which looks like HTML. In XML the tags are not predefined. 
The first line is an XML declaration. The person tag is the root of the XML.
The person has a gender attribute. Example:XML 


<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
"""

import xml.etree.ElementTree as ET
tree = ET.parse('./day_19/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)