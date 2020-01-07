import sys

with open('input') as file:
    program = list(map(int, file.readline().split(',')))

# print(program)



def intcode(proglist, val1 = None, val2 = None):
    if val1:
        proglist[1] = val1
    if val2:
        proglist[2] = val2
        
    count = 0
    temp_list = []
    for stuff in proglist:
        count += 1
        temp_list.append(stuff)
        if count == 4:
#            print(temp_list)
            opcode = temp_list[0]
            value1 = proglist[temp_list[1]]
            value2 = proglist[temp_list[2]]
            result_target = temp_list[3]

            if opcode == 1:
                proglist[result_target] = value1 + value2
            elif opcode == 2:
                try:
                    proglist[result_target] = value1 * value2
                except IndexError:
                    print('error: {}'.format(result_target))
                    
            elif opcode == 99:
                print('Halting Execution, opcode 99')
                break

            temp_list = []
            count = 0

    return proglist


#print(intcode(program, 12, 2))

for param1 in range(100):
    for param2 in range(100):
        checklist = intcode(program.copy(), param1, param2)
        if checklist[0] == 19690720:
            print('noun {} verb {}'.format(param1, param2))
            sys.exit()
