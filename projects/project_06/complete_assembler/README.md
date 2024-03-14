The complete Hack assembler extends the functionality of the basic Hack assembler to convert assembly language into machine language (binary)

The complete Hack assembler functionality is as follows:
* Translate A-instruction into binary code (all instructions of type @xxx where xxx constants are decimals as well as all symbols)
* Translate C-instruction into binary code (all compute instructions using the Hack instruction set)

A Hack assembly program is sequence of text lines being one of the following:
* Assembly instruction: a symbolic A-instruction (@xxx) or  a symbolic C-instruction (dest=comp)
* Label declaration: line in the form of (xxx) where xxx is a symbol
* Comment: lines beginning with double forward slashes (//)

To be more specific there are a few different purposes of symbols:
* Labels: declare and use symbols that mark locations in code e.g LOOP or END directives
    * These pseudo-instructions (xxx) define symbol xxx to refer to the location in Hack ROM holding the next instruction in the program
    * In a Hack assembly program you might see a (LOOP) directive then at the end of the loop @LOOP with a jump instruction 0;JMP
        * The @LOOP instruction will tell ROM where the next instruction is - in this case it will be the start of the loop. 
* Variables: declare and use symbolic variables that store values e.g i or sum
    * mapped to RAM locations starting at RAM[16] 
* Predefined symbols: declare and use special addresses in computer memory using agreed upon symbols
    * R0 ... R15 maps to 0 to 15 in RAM respectively
    * SP, LCL, ARG, THIS, THAT maps to 0, 1, 2, 3, 4 in RAM respectively
    * SCREEN is mapped to 16384
    * KBD is mapped to 24576

Symbol convention: It is important to note that symbols can be any sequence of letters, digits, underscores, dots, dollar sign and colon as long as it does not begin with a digit.
