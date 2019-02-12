# Pandas Python Challenge


This is an example of a Pipe Delimited data file that we receive from one of our courthouses in Texas. Since the data comes in various different formats across courthouses, it is often necessary to transform this data and standardize it for our website.

In this challenge, we want to extract lists of full_names (Grantors and Grantees) for each of the documents in the data file.
  

Given the file **Index_133634.csv**. Complete the python code to do the following:

1) Read this delimited file **Index_133634.txt** into a Pandas data frame using the provided headers.

2) Now that you have the data in a dataframe, extract lists of GRANTOR and GRANTEES (which are persons names) for each document. Each document is identified by a unique number labeled INST.NUM. 

3) Recombine the names into this format LNAME, FNAME MNAME TITLE.


Example output is provided in the file **expected_output.json**. This file will be used to check your output.

