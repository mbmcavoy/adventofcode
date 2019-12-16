



def main():
    input_file = open("2019/2019-02/input.txt")

    program_string = input_file.readline()
    program = [int(value) for value in program_string.split(",")]

    #try out different values
    for verb in range(0, 99):
        for noun in range(0, 99):
            testProgram = program.copy()

            testProgram[1] = noun
            testProgram[2] = verb

            result = runProgram(testProgram)

            if (result == 19690720):
                print(f"Noun: {noun} Verb: {verb} ===> Result {result}")
                print(f"Answer: {100 * noun + verb}")

            


# This executes the program
def runProgram(program):
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
            #print(f"Halt! Result is {program[0]}")
            return program[0]

        else:
            # Error
            #print(f"Error encountered! Opcode {opcode} at location {pc}")
            return "error"

        pc += 4


# Execute the program
if __name__ == "__main__":
    main()
