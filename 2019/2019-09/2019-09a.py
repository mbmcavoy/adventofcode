from enum import Enum

def main():

    # Test getParamMode

    input_file = open("2019/2019-09/input.txt")
    
    program_string = input_file.readline()
    program = [int(value) for value in program_string.split(",")]

    computer = intcode(program)
    # computer.inputBuffer = [1]  # Use for Part 1
    computer.inputBuffer = [2]  # Use for Part 2
    computer.execute()

    print(f"Computer is in state {computer.state}.")

    for output in computer.outputBuffer:
        print(output)


class intcodeState(Enum):
    IDLE = 0
    ACTIVE = 1
    AWAITING_INPUT = 2
    HALTED = 3
    ERROR = -1

class intcode:
    def __init__(self, program):
        self.program = program
        
        self.pc = 0
        self.state = intcodeState.IDLE
        self.inputBuffer = []
        self.outputBuffer = []
        self.relativeBase = 0

    def execute(self):
        self.state = intcodeState.ACTIVE

        while True:
            instruction = self.program[self.pc]
            opcode = instruction % 100
            param1Mode = int(instruction / 100) % 10
            param2Mode = int(instruction / 1000) % 10
            param3Mode = int(instruction / 10000) % 10

            if (opcode == 1):
                # Addition
                
                input1 = self.readValue(self.pc + 1, param1Mode)
                input2 = self.readValue(self.pc + 2, param2Mode)
                result = input1 + input2
                self.writeValue(self.pc + 3, param3Mode, result)

                # Increment Program Counter
                self.pc += 4
            
            elif (opcode == 2):
                # Multiplication
                
                input1 = self.readValue(self.pc + 1, param1Mode)
                input2 = self.readValue(self.pc + 2, param2Mode)
                result = input1 * input2
                self.writeValue(self.pc + 3, param3Mode, result)

                # Increment Program Counter
                self.pc += 4

            elif (opcode == 3):
                # Input
                
                if len(self.inputBuffer) == 0:
                    # No input data available - pause execution
                    self.state = intcodeState.AWAITING_INPUT
                    return

                else:
                    result = self.inputBuffer.pop(0)
                    self.writeValue(self.pc + 1, param1Mode, result)

                    # Increment Program Counter
                    self.pc += 2


            elif (opcode == 4):
                # Output

                output = self.readValue(self.pc + 1, param1Mode)
                self.outputBuffer.append(output)

                # Increment Program Counter
                self.pc += 2


            elif (opcode == 5):
                # Jump-if-True

                input1 = self.readValue(self.pc + 1, param1Mode)
                
                if (input1 != 0):
                    target = self.readValue(self.pc + 2, param2Mode)
                    self.pc = target
                else:
                    self.pc += 3
                

            elif (opcode == 6):
                # Jump-if-False

                input1 = self.readValue(self.pc + 1, param1Mode)
                
                if (input1 == 0):
                    target = self.readValue(self.pc + 2, param2Mode)
                    self.pc = target
                else:
                    self.pc += 3


            elif (opcode == 7):
                # Less Than
                
                input1 = self.readValue(self.pc + 1, param1Mode)
                input2 = self.readValue(self.pc + 2, param2Mode)
                result = 1 if (input1 < input2) else 0
                self.writeValue(self.pc + 3, param3Mode, result)

                # Increment Program Counter
                self.pc += 4


            elif (opcode == 8):
                # Equals
                
                input1 = self.readValue(self.pc + 1, param1Mode)
                input2 = self.readValue(self.pc + 2, param2Mode)
                result = 1 if (input1 == input2) else 0
                self.writeValue(self.pc + 3, param3Mode, result)

                # Increment Program Counter
                self.pc += 4

            elif (opcode == 9):
                # Relative Base Offset
                input1 = self.readValue(self.pc + 1, param1Mode)
                self.relativeBase += input1

                self.pc += 2

            elif (opcode == 99):
                # Halt; program complete
                self.state = intcodeState.HALTED
                return

            else:
                # Error
                print(f"Error encountered! Unknown opcode {opcode} at location {self.pc}")
                self.state = intcodeState.ERROR
                return


    def readValue(self, paramAddress, paramMode):
        maxAddress = len(self.program) - 1
        paramValue = self.program[paramAddress]

        if paramMode == 0:
            # Position Mode
            if paramValue > maxAddress:
                value = 0
            else:
                value = self.program[paramValue]
                
        elif paramMode == 1:
            # Immedeate Mode
            value = paramValue
            
        elif paramMode == 2:
            # Relative Mode
            offsetAddress = self.relativeBase + paramValue
            
            if offsetAddress > maxAddress:
                value = 0
            else:
                value = self.program[offsetAddress]

        else:
            # Unkown Mode -- ERROR
            print(f"Undefined parameter mode {paramMode} at address {self.pc}")
            value = 0

        return value


    def writeValue(self, paramAddress, paramMode, value):
        maxAddress = len(self.program) - 1
        paramValue = self.program[paramAddress]

        if paramMode == 0:
            # Position Mode
            writeAddress = paramValue
                
        # (paramMode == 1): No Immedeate Mode for writes

        elif paramMode == 2:
            # Relative Mode
            writeAddress = self.relativeBase + paramValue
                        
        else:
            # Unkown Mode -- ERROR
            print(f"Undefined parameter mode {paramMode} at address {self.pc}")
            return     

        if writeAddress > maxAddress:
            # Extend memory to reach
            extensionLength = writeAddress - maxAddress
            self.program.extend([0] * extensionLength)

        self.program[writeAddress] = value
       
        return

    
    
# Execute the program
if __name__ == "__main__":
    main()
