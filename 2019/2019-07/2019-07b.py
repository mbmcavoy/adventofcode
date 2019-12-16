from enum import Enum

def main():

    # Test getParamMode

    input_file = open("2019/2019-07/input.txt")

    program_string = input_file.readline()
    program = [int(value) for value in program_string.split(",")]

    testResults = []

    combinationCounter = 1
    for place5 in range (5):
        for place6 in range (4):
            for place7 in range (3):
                for place8 in range (2):
                    
                        phaseSettings = [9]
                        phaseSettings.insert(place8, 8)
                        phaseSettings.insert(place7, 7)
                        phaseSettings.insert(place6, 6)
                        phaseSettings.insert(place5, 5)

                        combination = "".join(str(ps) for ps in phaseSettings)

                        amplifiers = []

                        # Instantiate amplifiers
                        for amplifier in range(5):
                            #Initialize Amplifiers
                            amp = intcode(program.copy())
                            amp.inputBuffer.append(phaseSettings[amplifier])
                            amplifiers.append(amp)

                        # Set initial input
                        amplifiers[0].inputBuffer.append(0)

                        cycle = 0
                        while True:

                            amp = amplifiers[cycle % 5]
                            amp.execute()
                            # print(f"Exited program for amplifier {cycle %5} in state {amp.state}")

                            if (cycle % 5 == 4) and amp.state == intcodeState.HALTED:
                                # Last amp has halted, assume all are done?
                                break

                            nextAmp = amplifiers[(cycle + 1) % 5]
                            for i in range(len(amp.outputBuffer)):
                                nextAmp.inputBuffer.append(amp.outputBuffer.pop(0))

                            cycle += 1

                        result = amplifiers[4].outputBuffer.pop(0)
                        print(f"Combination #{combinationCounter}: {combination}, Thruster Command {result}")
                        testResults.append(result)
                        combinationCounter += 1

    print(f"Largest output found: {max(testResults)}")

    #runProgram(program)


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

    def execute(self):
        self.state = intcodeState.ACTIVE

        while True:
            instruction = self.program[self.pc]
            opcode = instruction % 100
            param1Mode = int(instruction / 100) % 10
            param2Mode = int(instruction / 1000) % 10
            param3Mode = int(instruction / 10000) % 10

            #print(f"Instruction {instruction} at PC {self.pc} | {opcode} - {param1Mode} - {param2Mode} - {param3Mode}")

            if (opcode == 1):
                # Addition
                
                input1 = self.program[self.program[self.pc + 1]] if param1Mode == 0 else self.program[self.pc + 1]
                input2 = self.program[self.program[self.pc + 2]] if param2Mode == 0 else self.program[self.pc + 2]

                result = input1 + input2

                resultAddr = self.program[self.pc + 3] if param3Mode == 0 else (self.pc + 3)
                self.program[resultAddr] = result

                # Increment Program Counter
                self.pc += 4
            
            elif (opcode == 2):
                # Multiplication
                
                input1 = self.program[self.program[self.pc + 1]] if param1Mode == 0 else self.program[self.pc + 1]
                input2 = self.program[self.program[self.pc + 2]] if param2Mode == 0 else self.program[self.pc + 2]

                result = input1 * input2

                resultAddr = self.program[self.pc + 3] if param3Mode == 0 else (self.pc + 3)
                self.program[resultAddr] = result

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
                    resultAddr = self.program[self.pc + 1] if param1Mode == 0 else (self.pc + 1)
                    self.program[resultAddr] = result

                    # Increment Program Counter
                    self.pc += 2


            elif (opcode == 4):
                # Output

                output = self.program[self.program[self.pc + 1]] if param1Mode == 0 else self.program[self.pc + 1]
                self.outputBuffer.append(output)

                # Increment Program Counter
                self.pc += 2


            elif (opcode == 5):
                # Jump-if-True

                input1 = self.program[self.program[self.pc + 1]] if param1Mode == 0 else self.program[self.pc + 1]
                
                if (input1 != 0):
                    target = self.program[self.program[self.pc + 2]] if param2Mode == 0 else self.program[self.pc + 2]
                    self.pc = target
                else:
                    self.pc += 3
                

            elif (opcode == 6):
                # Jump-if-False

                input1 = self.program[self.program[self.pc + 1]] if param1Mode == 0 else self.program[self.pc + 1]
                
                if (input1 == 0):
                    target = self.program[self.program[self.pc + 2]] if param2Mode == 0 else self.program[self.pc + 2]
                    self.pc = target
                else:
                    self.pc += 3


            elif (opcode == 7):
                # Less Than
                
                input1 = self.program[self.program[self.pc + 1]] if param1Mode == 0 else self.program[self.pc + 1]
                input2 = self.program[self.program[self.pc + 2]] if param2Mode == 0 else self.program[self.pc + 2]

                result = 1 if (input1 > input2) else 2

                resultAddr = self.program[self.pc + 3] if param3Mode == 0 else (self.pc + 3)
                self.program[resultAddr] = result

                # Increment Program Counter
                self.pc += 4


            elif (opcode == 8):
                # Equals
                
                input1 = self.program[self.program[self.pc + 1]] if param1Mode == 0 else self.program[self.pc + 1]
                input2 = self.program[self.program[self.pc + 2]] if param2Mode == 0 else self.program[self.pc + 2]

                result = 1 if (input1 == input2) else 2

                resultAddr = self.program[self.pc + 3] if param3Mode == 0 else (self.pc + 3)
                self.program[resultAddr] = result

                # Increment Program Counter
                self.pc += 4


            elif (opcode == 99):
                # Halt; program complete
                self.state = intcodeState.HALTED
                return

            else:
                # Error
                print(f"Error encountered! Unknown opcode {opcode} at location {self.pc}")
                self.state = intcodeState.ERROR
                return

    
# Execute the program
if __name__ == "__main__":
    main()
