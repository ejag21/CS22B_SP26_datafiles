### CS 22B Module 01 - Homework 1
### Name: Esha Jagatia

### This template is for Homework #01 reviewing the material we covered in Module 01 Essentials for CS 22B.

### root folder if applicable
# root='/path/to/folder/'

##### Problem 1: Trim adapter reads and validate bases
## 1. Write a script that reads in adapter_reads.txt line by line and remove the first 14 base pair (characters) that are the adapters. 
## 2. Validate if the read is valid by ensuring that all the characters are in {A,T,C,G}. ie., Not another character eg N.
## 3. Write the valid trimmed reads to a new file, clean_reads.txt, and the invalid reads in another new file,  bad_reads.txt. 
## 4. Print as output, the number of valid and invalid reads. 

valid_reads []
invalid_reads = 0
valid_count = 0

with open("adapter_reads.txt", "r") as infile, \
open("clean_reads.text", "w") as clean_out, \
open("bad_reads.txt", "w") as bad_out:
    
    for line in infile:
        read = line.strip()

        trimmed = read[14:]

        if all(base in "ATCG" for base in trimmed):
            clean_out.write(trimmed + "\n")
            valid_reads.append(trimmed)
            valid_count += 1
        else:
            bad_out.write(trimmed + "\n")
            invalid_reads += 1

print("Valid reads:", valid_count)
print("Invalid reads:", invalid_reads)

##### Problem 2: List comprehension statistic
## 1. Using the valid trimmed reads from problem 1, create a list comprehension command that returns the length of each valid read. 
## 2. Create a second list comprehension command that returns the GC% of each valid read (ie., GC.count/length). 
## 3. Print as output, the minimum length, max length, and average length of your valid trimmed reads. Additionally, print the average GC% rounded to 3 decimals.

lengths = [len(read) for read in valid_reads]

gc_percent = [(read.count("G") + read.count("C")) / len(read) for read in valid_reads]

if lengths:
    print("Min length:", min(lengths))
    print("Max length:", max(lengths))
    print("Average length:", sum(lengths)/len(lengths))
    print("Average GC%:", round(sum(gc_percentages)/len(gc_percentages), 3))

##### Problem 3: Dictionary
## 1. Using the valid trimmed reads from problem 1, build a dictionary called 'base_counts' that has the total counts of A, T, C, G across all valid reads. 
## 2. Use a loop that iterates over the dictionary and compute and print the product of the four counts (A*C*T*G).

base_counts = {"A":0, "T":0, "C":0, "G":0}

for read in valid_reads:
    for base in read:
        base_counts[base] += 1

product =1 
for base in base_counts:
    product *= base_counts[base]


print("Base counts:", base_counts)
print("Product A*C*T*G", product)


#### Problem 4: Function and asserts
## 1. Write a function that returns the percentage of any nt (A,T,C,G) in a sequence, rounded to 2 significant figure. 
## 2. Include 3 asserts to test your code including a known case (eg "AATT" with "A" returning 50.00) and a case with 0%.

## Use this sequence as your test sequence
sequence = TTATAAGCCGATTATAAGCCCGTAACCGGTTAG

def nt_percentage(sequence, nt):
    percent = (sequence.count(nt) / len(sequence)) * 100
    return round(percent, 2)

assert nt_percentage("AATT", "A") == 50.00
assert nt_percentage("AATT", "G") == 0.00
assert nt_percentage("GGGG", "G") == 100.00

print("A%:", nt_percentage(sequence, "A"))
print("T%:", nt_percentage(sequence, "T"))
print("C%:", nt_percentage(sequence, "C"))
print("G%:", nt_percentage(sequence, "G"))