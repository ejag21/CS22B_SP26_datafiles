### This template is for the class exercises covered in M01_L02_review-files for CS 22B.

## root folder if applicable
# root='/path/to/folder/'

##### CL1.1: Count the number of T in the sequence. 
sequence = "ATTGGCTATACCGG"
# ** your code **


##### CL1.2: For the sequence above, convert the sequence from the 4th character to the 9 character to lower case
# ** your code **


##### CL1.3: Find the noncoding(4th to 9th character) and coding regions(all other characters)
## step 1: open the seq.txt file
# ** your code **

## step 2: create 2 new files for coding and noncoding
# ** your code **

## write to new files sequence 4-9 as lowercase to noncode file and all other sequence as uppercase to code file. Don't forget to close() to save the files.
# ** your code **


##### CL1.4: Trim the adapter sequence (14 bp seq at front of each line “ATTCGATTATAAGC”)
## step 1: open the adapter_input.txt file
# ** your code **

## step 2: create an output file
# ** your code **

## step 3: read in each line in the adapter_input file and trim the first 14 characters. Write the remaining sequence to the output file. Do this for each line. Don't forget to close() to save the file. 
