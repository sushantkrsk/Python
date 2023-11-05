#python too support java handling and allow user too handle file ie to read and write file along 
# with many file handling operation to operate file. this concept file handling have stracted over various other language but the implementation is either complicated or lengthy but like other concept of python then file handling 
# concept here is also easy and short. python treat file different as text or binary and this is important. each living code including sequence of character and they have form a text file.
# each line of file is terminated with 
# special character called EDL (end of line). characters like comma , or new line character

#working of open function:
# before operating any operation on a file 
# like reading or writing first we have to open last file.
# # for this we should use python in-built function: open()
# #but at the time of opening we have to specify 
# a mode which represent the function of opening file.
# where the following mode is supported
# r: open and existing file for write operation
# if the file already contains some data thrn it will be overridden
# but if the file is not present then it creates the file as well
# a: open and exiting file for append operation.
# it wont override exiting data
# r+: is used to read and write the previous data in the file will be overidden
# to read and write data it will override existing data
# a+: to append and read data from the file. it wont override existing data

