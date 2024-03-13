'''
    Basic assembler implementation

    Assumptions: The input file is valid

    Limitation: only works with Add.asm file as this file contains no symbolic references

    Solution: see complete assembler code that works for all files

'''
# to read arguments passed in CLI
import sys

dest_dict = {"M" : "001", "D" : "010", "DM" : "011", "A" : "100", "AM" : "101", "AD" : "110", "ADM" : "111" }

# where x represents A or M
comp_dict = {
                "0" : "101010",
                "1" : "111111" ,
                "-1": "111010",
                "D" : "001100",
                "x" : "110000",
                "!D" : "001101" ,
                "!x" :"110001",
                "-D" : "001111",
                "-x" : "110011",
                "D+1" : "011111",    
                "x+1" : "110111",
                "D-1" : "001110",
                "x-1" : "110010",
                "D+x" : "000010",
                "D-x" : "010011",
                "x-D" : "000111",
                "D&x" : "000000",
                "D|x" : "010101"
             }

# function that returns a fully formed 16-bit C-instruction
def AssembleCInstruction(dest, comp):
    
    # default most significant bits for C-instructions
    MSB = "111"

    # for basic assembler no jumps therefore null
    jjj="000"

    # specifies if comp includes A, -1, 0 or 1 or if comp uses M
    a = ""
    
    # check if computation uses A register or M register
    if "M" in comp:
        a = "1"
    else:
        a = "0"

    # destination bits
    ddd = dest_dict[dest]

    # computation bits
    cccccc = ""

    if "A" in comp:
        comp = comp.replace("A", "x")
        cccccc = comp_dict[comp]

    elif "M" in comp:
        comp = comp.replace("M", "x")
        cccccc = comp_dict[comp]
    else:
        cccccc = comp_dict[comp]

    # return complete C-instruction
    C_instruction = MSB + a + cccccc + ddd + jjj + "\n"
    return C_instruction

def main():
    # opens file passed as argument
    with open(sys.argv[1], 'r') as assembly_file:

        # create/overwrite binary output file (.hack)
        output_filename = sys.argv[1].split(".")[0] + "_test.hack"
        binary_file = open(output_filename, "w")

        # iterate over all lines of file
        for instruction in assembly_file.readlines():

            # ignore lines with comments
            if "//" in instruction:
                continue
            # ignore emppty line whitespace (check for newline or carriage return)
            elif instruction in ['\n', '\r\n']:
                continue
            else:
                # remove trailing whitespace 
                instruction = instruction.strip()

                # check for A-instruction
                if instruction.startswith("@"):
                    # convert string number into decimal number
                    A_instruction = int(instruction.strip("@"))

                    # convert decimal number into 16-bit binary number
                    A_instruction = str(format(A_instruction, '016b')) + "\n"
                    
                    # write A-instruction to binary file
                    binary_file.write(A_instruction)

                # other instruction must be C-instruction
                else:
                    # isolate destination (dest) and computation (comp)
                    C_instruction = instruction.split("=")
                    dest = C_instruction[0]
                    comp = C_instruction[1]

                    # get compete C-instruction
                    C_instruction = AssembleCInstruction(dest, comp)

                    # write C-instruction to binary file
                    binary_file.write(C_instruction)

if __name__ == "__main__":
    main()





    
    


            



