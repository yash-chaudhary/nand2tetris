'''
    Complete assembler implementation

    Assumptions: Input file is valid

    Limitation: Avoided using classes 

    Solution: Using a two-pass assembler (first pass adds all labels to symbol table, 
                second pass adds all other variables and converts instructions to binary)
'''

# imports
import sys

# predefined ymbol table
sym_table_dict = {
    'R0' : '0',
    'R1' : '1',
    'R2' : '2',
    'R3' : '3',
    'R4' : '4',
    'R5' : '5',
    'R6' : '6',
    'R7' : '7',
    'R8' : '8',
    'R9' : '9',
    'R1O' : '10',
    'R11' : '11',
    'R12' : '12',
    'R13' : '13',
    'R14' : '14',
    'R15' : '15',
    'SP' : '0',
    'LCL' : '1',
    'ARG' : '2',
    'THIS' : '3',
    'THAT' : '4',
    'SCREEN' : '16384',
    'KGB' : '24576'
}

# computation bits
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

# destination bits (janky solutions to ensure all instructions sets are valid)
dest_dict = {
    "M" : "001", 
    "D" : "010", 
    "DM" : "011",
    "MD" : "011",
    "A" : "100", 
    "AM" : "101", 
    "MA" : "101",
    "AD" : "110",
    "DA" : "110",
    "ADM" : "111",
    "AMD" : "111",
    "DAM" : "111",
    "DMA" : "111",
    "MAD" : "111",
    "MDA" : "111"
}

# jump bits
jmp_dict = {
    'JGT' : '001',
    'JEQ' : '010',
    'JGE' : '011',
    'JLT' : '100',
    'JNE' : '101',
    'JLE' : '110',
    'JMP' : '111'
}

# function that removes whitespace and comments from input assembly file
def process_input(file):
    instructions = []                       # stores list of all instructions
    with open(file, 'r') as assembly_file:
        for line in assembly_file.readlines():
            if "//" in line:                # ignore lines with comments
                continue
            elif line in ['\n', '\r\n']:    # ignore emppty line whitespace (check for newline or carriage return)
                continue
            else:
                line = line.strip()         # remove trailing whitespace 
                instructions.append(line)
    return instructions                     # returns list of instructions


# function that find all label declarations 
def find_labels(instructions):
    '''
        input: list of instructions
        task: find all label declarations in the form: (LABEL) and add index position + 1
        purpose: the position of the label is the address where the program counter will jump to in ROM
        return: none
    '''
    num_declarations = 0
    for i in range(len(instructions)):
        if "(" and ")" in instructions[i]:
            if num_declarations == 0:
                label = instructions[i].strip("()")
                sym_table_dict[label] = i
                num_declarations += 1
            elif num_declarations != 0:
                label = instructions[i].strip("()")
                sym_table_dict[label] = i - num_declarations
                num_declarations += 1
            
# function that handles creating binary code from assembly instructions
def convert_instructions(lines, file):
    
    var_idx = 16
    
    for i in range(len(lines)):

        if "(" and ")" in lines[i]:
            continue

        # check if A-instruction (@xxx)
        elif "@" in lines[i]:
            line = lines[i].strip("@")
            bin_val = ''

            # check if instruction in predefined symbol table
            if (line in sym_table_dict.keys()):
                bin_val = str(format(int(sym_table_dict[line]), '016b')) + "\n"
                
            # check if instruction is just a number 
            elif line.isnumeric():
                 bin_val = str(format(int(line), '016b')) + "\n"
      
            # checks if instruction is all characters in alphabet and store in symbol table at index 16 onwards
            elif "_" in line or "$" in line or "." in line and line.islower(): 
                sym_table_dict[line] = var_idx
                bin_val = str(format(var_idx, '016b')) + "\n"
                var_idx += 1
            
            # write to output file
            file.write(bin_val)

        # check if C-instruction (dest=comp;jump) or (dest=comp where jmp is null)
        elif "=" in lines[i] or ";" in lines[i]:
            bin_val = ''
            
            # default most significant bits for C-instructions
            MSB = "111"

            # set a-bit
            #a = '1' if 'M' in lines[1] else '0'
            
            # dest=comp;jump C-instruction
            if "=" in lines[i] and ";" in lines[i]:
                pass
            
            # comp;jump C-instruction
            elif ";" in lines[i]:
                line = lines[i].split(";")
                dest='000'
                a = '1' if 'M' in line[0] else '0'
                comp = comp_dict[line[0]]
                jmp = jmp_dict[line[1]]
                bin_val = MSB+a+comp+dest+jmp+'\n'

            # dest=comp C-instruction
            else: 
                jmp='000'   # jump set to null for this kind of instruction
                line = lines[i].split("=")
                dest = dest_dict[line[0]]
                a = '1' if 'M' in line[1] else '0'
                comp = comp_dict[line[1].replace('A', 'x').replace('M', 'x')]
                bin_val = MSB+a+comp+dest+jmp+'\n'

            # write to output file
            file.write(bin_val)
                
# driver
def main():
    instructions = process_input(sys.argv[1])   # process input file

    # create output file handle
    output_fn = sys.argv[1].split(".")[0] + "_test.hack"
    binary_file = open(output_fn, "w")
    
    # first pass (add labels to symbol table)
    find_labels(instructions)

    # second pass (adds variables and completes translation)
    convert_instructions(instructions, binary_file)
    
if __name__ == '__main__':
    main()

