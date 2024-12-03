import csv
#start a class to create the NTM before tracing 

class NTM:
    def __init__(self, machine_file):
        self.machine_name = []
        self.curr_string = []
        self.states = []
        self.input_alphabet = []
        self.tape_alphabet = []
        self.start_state = None
        self.accept_state = None
        self.reject_state = None
        self.transitions = {}
        self.read_machine(machine_file)

    #function to read in csv when the class is begun 
    def read_machine(self, machine_file):
        with open(machine_file, 'r') as file:
            reader = csv.reader(file)
            lines = list(reader)

        self.machine_name = lines[0]
        self.curr_string = lines[1]
        self.states = lines[2]
        self.input_alphabet = lines[3]
        self.tape_alphabet = lines[4]
        self.start_state = lines[5][0]
        self.accept_state = lines[6][0]
        self.reject_state = lines[7][0]

        #store transitions, allowing multiple transitions per state and input
        for line in lines[10:]:
            state, read_char, next_state, write_char, direction = line
            key = (state, read_char)
            if key not in self.transitions:
                self.transitions[key] = []
            self.transitions[key].append((next_state, write_char, direction))

    #function to trace input_string through the NTM
    def trace(self, input_string, max_depth=50):
        tape = list(input_string)                           # Tape becomes the input string 
        configurations = [([], self.start_state, tape[:])]  # Add the original input to configs
        visited = set()                                     # To track visited configurations
        all_configurations = []                             # For tracing the path

        max_nondeterminism = 0                              # Track the degree of nondeterminism
        depth = 0                                           # To track the depth of the tree 
        while configurations:
            # Pop the first configuration
            left_of_head, curr_state, curr_tape = configurations.pop(0)

            # Mark the current configuration and mark as visited (check if visited too)
            current_config = (tuple(left_of_head), curr_state, tuple(curr_tape))
            if current_config in visited:
                continue
            visited.add(current_config)

            # Save current_config to all_configs for later tracing 
            all_configurations.append((left_of_head[:], curr_state, curr_tape[:]))

            # Handle empty tapes 
            if not curr_tape:
                curr_tape = ['_']
            
            # GET THE HEAD CHAR
            head_char = curr_tape[0]

            # Check for accept or reject states
            if curr_state == self.accept_state:
                with open("output_test_cases.txt", "a") as file: 
                    file.write(f'Name of the machine: {self.machine_name[0]}\n')
                    file.write(f'Original input string: {input_string}\n')
                    file.write(f"String accepted in {depth} transitions!\n")
                    file.write(f"Degree of nondeterminism: {max_nondeterminism}\n")
                    self.print_path(all_configurations, file=file)
                return
            elif curr_state == self.reject_state:
                continue

            # PREPARE FOR NEXT TRANSITIONS 
            if (curr_state, head_char) in self.transitions:
                transitions = self.transitions[(curr_state, head_char)]
                max_nondeterminism = max(max_nondeterminism, len(transitions))  # Update max

                for next_state, write_char, direction in transitions:
                    new_tape = curr_tape[:]
                    new_tape[0] = write_char
                    
                    # Handle R direction: move head right
                    if direction == "R":
                        new_left = left_of_head[:]
                        new_left.append(new_tape.pop(0))
                        if not new_tape:
                            new_tape.append('_')
                    
                    # Handle L direction: move head left
                    elif direction == "L":
                        new_left = left_of_head[:]
                        if new_left:
                            new_tape.insert(0, new_left.pop())
                        else:
                            new_tape.insert(0, '_')
                    
                    # Add the new configuration to the queue
                    configurations.append((new_left, next_state, new_tape))

            depth += 1  
            if depth > max_depth:
                print(f"Execution stopped after {max_depth} steps.")
                print(f"Degree of nondeterminism during execution: {max_nondeterminism}")
                return

        # If string gets rejected 
        with open("output_test_cases.txt", "a") as file:
            file.write(f'Name of the machine: {self.machine_name[0]}\n')
            file.write(f'Original input string: {input_string}\n')
            file.write(f'String rejected after {depth} transitions\n')
            file.write(f"Degree of nondeterminism: {max_nondeterminism}\n")
            self.print_path(all_configurations, file=file)

    def print_path(self, all_configurations, file=None):
        if file:
            file.write("Tracing path to accepting state:\n")
            for left, state, tape in all_configurations:
                file.write(f"{left} | {state} | {tape}\n")
        else:
            print("Tracing path to accepting state:")
            for left, state, tape in all_configurations:
                print(f"{left} | {state} | {tape}")
        if file:
            file.write("\n")

# Main function
def main():
    n_test_cases = 5
    for i in range(n_test_cases):
        machine_file = f'check_ntm{i+1}.csv'
        ntm = NTM(machine_file)
        input_string = ntm.curr_string[0]
        ntm.trace(input_string)

if __name__ == "__main__":
    main()

