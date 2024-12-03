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

        #store the transitions 
        for line in lines[10:]:
            state, read_char, next_state, write_char, direction = line
            self.transitions[(state, read_char)] = (next_state, write_char, direction)

    #call this fucntion after having started the ntm class 
    '''input --> input_string and max_depth'''
    def trace(self, input_string, max_depth=50):
        tape = list(input_string)                           #tape becomes the input string 
        configurations = [([], self.start_state, tape[:])]  #add the original input to configs
        visited = set()                                     #to track visited configurations
        all_configurations = []                             #for tracing the path

        depth = 0                                           #to track the depth of the tree 
        while configurations:
            #pop the first configuration
            left_of_head, curr_state, curr_tape = configurations.pop(0)

            #mark the current configuration and mark as visited (check if visited too)
            current_config = (tuple(left_of_head), curr_state, tuple(curr_tape))
            if current_config in visited:
                continue
            visited.add(current_config)

            #save current_config to all_configs for later tracing 
            all_configurations.append((left_of_head[:], curr_state, curr_tape[:]))

            #handle empty tapes 
            if not curr_tape:
                curr_tape = ['_']
            
            #GET THE HEAD CHAR
            head_char = curr_tape[0]

            # Check for accept or reject states
            if curr_state == self.accept_state:
                with open("output_test_cases.txt", "a") as file: 
                    file.write(f'Name of the machine: {self.machine_name[0]}\n')
                    file.write(f'Original input string: {input_string}\n')
                    file.write(f"String accepted in {depth} transitions!\n")
                    self.print_path(all_configurations, file=file)  
            elif curr_state == self.reject_state:
                continue

            #PREPARE FOR NEXT TRANSITIONS 
            if (curr_state, head_char) in self.transitions:
                next_state, write_char, direction = self.transitions[(curr_state, head_char)]
                curr_tape[0] = write_char
                
                #if R --> chnage left_tape and pop from curr_tape
                if direction == "R":
                    left_of_head.append(curr_tape.pop(0))
                    if not curr_tape:
                        curr_tape.append('_')
                #if L --> insert to curr_tape and pop from left_tape 
                elif direction == "L":
                    if left_of_head:
                        curr_tape.insert(0, left_of_head.pop())
                    else:
                        curr_tape.insert(0, '_')

                #add the new configuration to configurations 
                new_config = (left_of_head[:], next_state, curr_tape[:])
                configurations.append(new_config)

            depth += 1  
            if depth > max_depth:
                print(f"Execution stopped after {max_depth} steps.")
                return
        
        #if string gets rejected 
        with open("output_test_cases.txt", "a") as file:
            file.write(f'Name of the machine: {self.machine_name[0]}\n')
            file.write(f'Original input string: {input_string}\n')
            file.write(f'String rejected after {depth} transitions\n')
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
        file.write("\n")

def main():
    n_test_cases = 5
    for i in range(n_test_cases):
        machine_file = f'check_ntm{i+1}.csv'
        ntm = NTM(machine_file)
        input_string = ntm.curr_string[0]
        ntm.trace(input_string)

if __name__ == "__main__":
    main()
