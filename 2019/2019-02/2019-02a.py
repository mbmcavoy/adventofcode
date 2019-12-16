



def main():
    input_file = open("2019/2019-02/input.txt")

    program_string = input_file.readline()
    program = [int(value) for value in program_string.split(",")]

    #Print the program
#    for value in program:
#        print(value)

    pc = 0

    while True:
        opcode = program[pc]
        
        inputAddr1 = program[pc + 1]
        input1 = program[inputAddr1]

        inputAddr2 = program[pc + 2]
        input2 = program[inputAddr2]

        outputAddr = program[pc + 3]

        if (opcode == 1):
            # Addition
            result = input1 + input2
            program[outputAddr] = result
        
        elif (opcode == 2):
            # Multiply
            result = input1 * input2
            program[outputAddr] = result
        
        elif (opcode == 99):
            # Halt; program complete
            print(f"Halt! Result is {program[0]}")
            break

        else:
            # Error
            print(f"Error encountered! Opcode {opcode} at location {pc}")

        pc += 4


# Execute the program
if __name__ == "__main__":
    main()
