# SequenceAlignment
### Run python code to generate output.txt
Basic : python3 basic.py input.txt
Efficient : python3 efficient.py input.txt

#####
Input String Generator
The input to the program would be a text file, input.txt containing the following
information:
1. First base string
2. Next j lines would consist of indices corresponding the after which the
previous string to be added to the cumulative string
3. Second base string
4. Next k lines would consist of where the base string to be added to the
cumulative string
This information would help generate 2 strings from the original 2 base strings.
This file could be used as an input to your program and your program could use
the base strings and the rules to generate the actual strings. Also note that the
numbers j and k corresponds to the first and the second string respectively. Make
sure you validate the length of the first and the second string to be
2j*str1.length and 2k*str2.length.
#####

Values for Delta and Alphas
Values for α’s are as follows. δe is equal to 30.
A C G T
A 0 110 48 94
C 110 0 118 48
G 48 118 0 110
T 94 48 110 0

####
GOALS:
A. Your program should take input:
1. 2 strings that need to be aligned, should be generated from the string
generator mentioned above.
2. Gap penalty (δe).
3. Mismatch penalty (αpq).

B. Your solution should output output.txt file containing the following information at
the respective lines:
1. The first 50 elements and the last 50 elements of the actual alignment.
2. The time it took to complete the entire solution.
3. Memory required.

C. Implement the memory efficient version of this solution and repeat the tests in
Part B.

D. Plot the results of Part A and Part B:
1. Single plot of CPU time vs problem size for the two solutions.
2. Single plot of Memory usage vs problem size for the two solutions.
