// Program: Multiply numbers such that R2 = R0 * R2

// Pseudocode

// i = 1 
// sum = 0
//
// if (i == R0) goto END
// else sum = sum + R1
//
// i = i = 1 goto LOOP


// Implementation

// define variable i as a counter
@i
M = 0	 // initialise i to 0

// R2  to hold cumulative sum
@R2
M = 0	// initialise sum to 0

// loop iterating R0 times and each time adding R1 to sum variable
(LOOP)
    // if i == R0 (terminate loop if i == R1)
    @i
    D = M
    @R0
    D = D - M
    @END	// goto address of END if condition satisfied
    D;JEQ

    // R2  = R2 + R1 (add to cumulative sum)
    @R1
    D = M
    @R2
    M = M + D

    // i = i + 1 (increment counter)
    @i
    M = M + 1

    // go back to start of loop
    @LOOP
    0;JMP

// end of program (infinite loop)
(END)
    @END
    0;JMP 
