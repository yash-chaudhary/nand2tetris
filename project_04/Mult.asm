// Program: Multiplies R0 and R1 and stores the result in R2

// Implementation

// Multiplication is the same as adding the same number together x number of times

// use variable i to track number of times we have looped 
@i
M = 0	// set i=0

// initialise R0 to 0
@R2
M = 0	// set R2=0

// start a loop that will add R1 to R2 for the amount of R0
(LOOP)

@i
D=M	// set D = i

@R0     // retrieve the number of times we will add R1 to R2 cumulative sum (AKA multiplication)
D=D-M	// check if D=M at which point D=0 and multiplication complete
@END
D;JEQ   // when D=0 jump to end of program

// the following runs if D not equal to M

@R1	// retrieve value of R1
D = M

@R2
M=M+D	// cumulative sum of previous R2 value and new R1 value

// increment variable i
@i
M=M+1

@LOOP
0;JMP	// go to start of loop again

// handle termination
(END)
@END
0;JMP
