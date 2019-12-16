def main():

    # Test getParamMode

    input_file = open("2019/2019-05/input.txt")

    program_string = input_file.readline()
    program = [int(value) for value in program_string.split(",")]

    runProgram(program)


def getOpcode(instruction):
    return instruction % 100

def getParamMode(instruction, parameter):
    return int(instruction  / (10 ** (parameter + 1))) % 10


# This executes the program
def runProgram(program):
    pc = 0

    while True:
        instruction = program[pc]
        print(f"Address {pc}: Instruction {instruction}")
        opcode = getOpcode(instruction)

        if (opcode == 1):
            # Addition
            
            #Get Input # 1
            paramModeInput1 = getParamMode(instruction, 1)
            if (paramModeInput1 == 0):
                # Position Mode
                position = program[pc + 1]
                input1 = program[position]
            elif (paramModeInput1 == 1):
                # Immedeate Mode
                input1 = program[pc + 1]
            else:
                print(f"Invalid Parameter Mode {paramModeInput1} for Parameter 1; instruction at {pc}")

            # Get Input # 2
            paramModeInput2 = getParamMode(instruction, 2)
            if (paramModeInput2 == 0):
                # Position Mode
                position = program[pc + 2]
                input2 = program[position]
            elif (paramModeInput2 == 1):
                # Immedeate Mode
                input2 = program[pc + 2]
            else:
                print(f"Invalid Parameter Mode {paramModeInput2} for Parameter 1; instruction at {pc}")

            # Calculate Result
            result = input1 + input2

            # What to do with result?
            paramModeOutput = getParamMode(instruction, 3)
            if (paramModeOutput == 0):
                # Position Mode
                position = program[pc + 3]
                program[position] = result
            elif (paramModeOutput == 1):
                # Immedeate Mode
                program[pc + 3] = result
            else:
                print(f"Invalid Parameter Mode {paramModeOutput} for Parameter 1; instruction at {pc}")

            # Increment Program Counter
            pc += 4
        
        elif (opcode == 2):
            # Multiplication
            
            #Get Input # 1
            paramModeInput1 = getParamMode(instruction, 1)
            if (paramModeInput1 == 0):
                # Position Mode
                position = program[pc + 1]
                input1 = program[position]
            elif (paramModeInput1 == 1):
                # Immedeate Mode
                input1 = program[pc + 1]
            else:
                print(f"Invalid Parameter Mode {paramModeInput1} for Parameter 1; instruction at {pc}")

            # Get Input # 2
            paramModeInput2 = getParamMode(instruction, 2)
            if (paramModeInput2 == 0):
                # Position Mode
                position = program[pc + 2]
                input2 = program[position]
            elif (paramModeInput2 == 1):
                # Immedeate Mode
                input2 = program[pc + 2]
            else:
                print(f"Invalid Parameter Mode {paramModeInput2} for Parameter 1; instruction at {pc}")

            # Calculate Result
            result = input1 * input2

            # What to do with result?
            paramModeOutput = getParamMode(instruction, 3)
            if (paramModeOutput == 0):
                # Position Mode
                position = program[pc + 3]
                program[position] = result
            elif (paramModeOutput == 1):
                # Immedeate Mode
                program[pc + 3] = result
            else:
                print(f"Invalid Parameter Mode {paramModeOutput} for Parameter 1; instruction at {pc}")

            # Increment Program Counter
            pc += 4

        elif (opcode == 3):
            # Input
            
            #print("Enter the system ID to diagnose:")           
            result = int(input("Enter the system ID to diagnose: "))
            print(f"You entered: {result}")

            # What to do with result?
            paramModeOutput = getParamMode(instruction, 1)
            if (paramModeOutput == 0):
                # Position Mode
                position = program[pc + 1]
                program[position] = result
            elif (paramModeOutput == 1):
                # Immedeate Mode
                program[pc + 1] = result
            else:
                print(f"Invalid Parameter Mode {paramModeOutput} for Parameter 1; instruction at {pc}")

            # Increment Program Counter
            pc += 2


        elif (opcode == 4):
            # Output

            #Get Output
            paramModeOutput = getParamMode(instruction, 1)
            if (paramModeOutput == 0):
                # Position Mode
                result = program[program[pc + 1]]
            elif (paramModeOutput == 1):
                # Immedeate Mode
                result = program[pc + 1]
            else:
                print(f"Invalid Parameter Mode {paramModeOutput} for Parameter 1; instruction at {pc}")
            
            print(f"Program output: {result}")

            pc += 2

        elif (opcode == 5):
            # Jump-if-True

            #Get Input # 1
            paramModeInput1 = getParamMode(instruction, 1)
            if (paramModeInput1 == 0):
                # Position Mode
                position = program[pc + 1]
                input1 = program[position]
            elif (paramModeInput1 == 1):
                # Immedeate Mode
                input1 = program[pc + 1]
            else:
                print(f"Invalid Parameter Mode {paramModeInput1} for Parameter 1; instruction at {pc}")

            # Get Input # 2
            paramModeInput2 = getParamMode(instruction, 2)
            if (paramModeInput2 == 0):
                # Position Mode
                position = program[pc + 2]
                input2 = program[position]
            elif (paramModeInput2 == 1):
                # Immedeate Mode
                input2 = program[pc + 2]
            else:
                print(f"Invalid Parameter Mode {paramModeInput2} for Parameter 1; instruction at {pc}")

            # Increment Program Counter
            if (input1 != 0):
                pc = input2
            else:
                pc += 3

        elif (opcode == 6):
            # Jump-if-False

            #Get Input # 1
            paramModeInput1 = getParamMode(instruction, 1)
            if (paramModeInput1 == 0):
                # Position Mode
                position = program[pc + 1]
                input1 = program[position]
            elif (paramModeInput1 == 1):
                # Immedeate Mode
                input1 = program[pc + 1]
            else:
                print(f"Invalid Parameter Mode {paramModeInput1} for Parameter 1; instruction at {pc}")

            # Get Input # 2
            paramModeInput2 = getParamMode(instruction, 2)
            if (paramModeInput2 == 0):
                # Position Mode
                position = program[pc + 2]
                input2 = program[position]
            elif (paramModeInput2 == 1):
                # Immedeate Mode
                input2 = program[pc + 2]
            else:
                print(f"Invalid Parameter Mode {paramModeInput2} for Parameter 1; instruction at {pc}")

            # Increment Program Counter
            if (input1 == 0):
                pc = input2
            else:
                pc += 3

        elif (opcode == 7):
            # Less Than
            
            #Get Input # 1
            paramModeInput1 = getParamMode(instruction, 1)
            if (paramModeInput1 == 0):
                # Position Mode
                position = program[pc + 1]
                input1 = program[position]
            elif (paramModeInput1 == 1):
                # Immedeate Mode
                input1 = program[pc + 1]
            else:
                print(f"Invalid Parameter Mode {paramModeInput1} for Parameter 1; instruction at {pc}")

            # Get Input # 2
            paramModeInput2 = getParamMode(instruction, 2)
            if (paramModeInput2 == 0):
                # Position Mode
                position = program[pc + 2]
                input2 = program[position]
            elif (paramModeInput2 == 1):
                # Immedeate Mode
                input2 = program[pc + 2]
            else:
                print(f"Invalid Parameter Mode {paramModeInput2} for Parameter 1; instruction at {pc}")

            # Calculate Result
            if (input1 < input2):
                result = 1
            else:
                result = 0
            
            # What to do with result?
            paramModeOutput = getParamMode(instruction, 3)
            if (paramModeOutput == 0):
                # Position Mode
                position = program[pc + 3]
                program[position] = result
            elif (paramModeOutput == 1):
                # Immedeate Mode
                program[pc + 3] = result
            else:
                print(f"Invalid Parameter Mode {paramModeOutput} for Parameter 1; instruction at {pc}")

            # Increment Program Counter
            pc += 4

        elif (opcode == 8):
            # Equals
            
            #Get Input # 1
            paramModeInput1 = getParamMode(instruction, 1)
            if (paramModeInput1 == 0):
                # Position Mode
                position = program[pc + 1]
                input1 = program[position]
            elif (paramModeInput1 == 1):
                # Immedeate Mode
                input1 = program[pc + 1]
            else:
                print(f"Invalid Parameter Mode {paramModeInput1} for Parameter 1; instruction at {pc}")

            # Get Input # 2
            paramModeInput2 = getParamMode(instruction, 2)
            if (paramModeInput2 == 0):
                # Position Mode
                position = program[pc + 2]
                input2 = program[position]
            elif (paramModeInput2 == 1):
                # Immedeate Mode
                input2 = program[pc + 2]
            else:
                print(f"Invalid Parameter Mode {paramModeInput2} for Parameter 1; instruction at {pc}")

            # Calculate Result
            if (input1 == input2):
                result = 1
            else:
                result = 0
            
            # What to do with result?
            paramModeOutput = getParamMode(instruction, 3)
            if (paramModeOutput == 0):
                # Position Mode
                position = program[pc + 3]
                program[position] = result
            elif (paramModeOutput == 1):
                # Immedeate Mode
                program[pc + 3] = result
            else:
                print(f"Invalid Parameter Mode {paramModeOutput} for Parameter 1; instruction at {pc}")

            # Increment Program Counter
            pc += 4


        elif (opcode == 99):
            # Halt; program complete
            print("Program Halted")
            return

        else:
            # Error
            print(f"Error encountered! Unknown opcode {opcode} at location {pc}")
            return "error"

# Execute the program
if __name__ == "__main__":
    main()
