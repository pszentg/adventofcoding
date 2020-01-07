def run_instructions(inputs):
    # needs pairs of 4
    index = 0
    while index < len(inputs):
        # all opcodes operates on the numbers found at the index stored in
        # i + 1, i + 2 and i + 3
        # eg. i+1 is 0, i+2 is 1, i+3 is 2, that means the operation should be
        # made on inputs[0], inputs[1] and the results should be stored in
        # inputs[2]

        # print(f'set to operate on: {inputs[index:index+4]}')
        target_index = int(inputs[index + 3])
        source_index_1 = int(inputs[index + 1])
        source_index_2 = int(inputs[index + 2])
        try:
            # print(f'actual values to operate on: '
            #       f'{inputs[source_index_1]} and '
            #       f'{inputs[source_index_2]}')
            if int(inputs[index]) == 1:
                # Opcode 1 adds together numbers
                inputs[target_index] = \
                    int(inputs[source_index_1]) + \
                    int(inputs[source_index_2])
                # print(f'result of adding is {inputs[target_index]}')

            elif int(inputs[index]) == 2:
                # Opcode 2 multiplies
                inputs[target_index] = \
                    int(inputs[source_index_1]) * \
                    int(inputs[source_index_2])
                # print(f'result of multiplying is {inputs[target_index]}')

            elif int(inputs[index]) == 99:
                # opcode 99 finishes
                print('halting')
                print(f'first number: {inputs[0]}')
                return

            elif index == len(inputs) - 4:
                # opcodes needs a bundle of 4 to operate
                pass

            index = index + 4
        except IndexError:
            print("instruction set wasn't long enough")
            return


with open("input.txt") as f:
    input_set = f.read().split(",")

    input_set[1] = 12
    input_set[2] = 2

    run_instructions(input_set)

# part #2: determine what instruction set can produce 19690720 in inputs[0] by
# manipulating inputs[1] and inputs[2]

a = 0
b = 0
while True:
    with open("input.txt") as f:
        original_input_set = f.read().split(",")
    while int(input_set[0]) < 19690720:
        input_set = original_input_set
        input_set[1] = a
        input_set[2] = b
        print(f'running with a: {a} and b: {b}')
        run_instructions(input_set)
        if int(input_set[0]) == 19690720:
            print(f'\n\n\n found the solution: a is {a}, b is {b}\n\n\n')
            break
        else:
            a += 1

    if int(input_set[0]) == 19690720:
        print(f'\n\n\n found the solution: a is {a}, b is {b}\n\n\n')
        break

    a = 0
    b += 1
