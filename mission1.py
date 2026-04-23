#Input is a list of integers separated by new line character
#First line of input will be N s.t 
#   (1 <= N <= 100) indicating. num of test cases to  follow
#Each of the test cases will consist of a line with an integer X s.t
#   (0<X<= 100) followed by another line consisting f X number of space-sep ints Yn s.t
        #Y.n (-100 <= Yn <= 100)

#For each test case, calculate power of four of Yn (excluding when Yn > 0)
#Print calcualted sum in the output

#Solution 

#1. Read number of test cases first
#2. Store results to print everything at the end

#3. Iterate over each test case 
    #4. Read X, which is the expected number of ints
    #5. Read the next line and split into list of ints
    #6. If count of integers != X, Store -1
    #7. Otherwise, filter out integers > 0
    #8. Raise each remaining number to 4th power and sum them
    #9. Store the result

#10. After all test cases, print each result on individual line
