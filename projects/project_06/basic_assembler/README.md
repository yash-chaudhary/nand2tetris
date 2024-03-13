The basic Hack Assembler is used to translate symbolic Hack mnemonics to their binary codes.

The scope of thos assember includes the following:
* Translate A-instructions into binary code (all instructions of type @xxx where xxx constants are decimals and not symbols)
* Translate C-instructions into binary code (all compute instructions using the Hack instruction set)

The input for the program should be an assembly file *.asm and the output will be a binary file *.hack.

This implementation will not use a symbol table to track symbolic references like (LOOP) or (END). This will be reserved for the complete assembler implementation.
