#Input is a list of integers separated by new line character
#First line of input will be N s.t
#   (1 <= N <= 100) indicating. num of test cases to  follow
#Each of the test cases will consist of a line with an integer X s.t
#   (0<X<= 100) followed by another line consisting f X number of space-sep ints Yn s.t
        #Y.n (-100 <= Yn <= 100)

#For each test case, calculate power of four of Yn (excluding when Yn > 0)
#Print calcualted sum in the output

#Constraints:
    #No output until all input received and no EOF
    #No blank lines between test case solutions
    #Take input/output from Standard I/O 
    #Final output guaranteed to be within INT32 Range
    # 

#NO FOR LOOPS => USE RECURSION  

#Solution

#1. Define a function to process a single test case
    #1a. Read X, which is the expected number of ints
    #1b. Read next line and parse into a list of ints using .map()
    #1c. If count of ints != X, return -1
    #1d. Use .filter() to keep only non-positive numbers
    #1e. Use .map() to raise each to the 4th power
    #1f. Return the sum

#2. Recursively collect all results
    #2a. Base case: 
        # No test cases left => return accumulated results
    #2b. Recursion
        # Process One Case
        # Add to running sum
        # Make recursive Call


#3. Main function 
#       Read N
#       Collect results
#       Print each on its own line