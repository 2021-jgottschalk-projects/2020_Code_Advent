import re


def run_instructions(instruction_list):
    # put accumulator as string so we can use eval...
    accumulator = "0"

    step = 0
    keep_going = ""

    already_run = []

    while keep_going != "no":

        try:

            if all_instructions[step][0] == "nop":
                # print("{} {}".format(all_instructions[step][0], all_instructions[step][1]))
                step = eval("{} + 1".format(str(step)))
                already_run.append(step)
            elif all_instructions[step][0] == "acc":
                # print("{} {}".format(all_instructions[step][0], all_instructions[step][1]))
                accumulator = eval("{} {}".format(accumulator, all_instructions[step][1]))
                # print(accumulator)
                # input("Continue?")
                step = eval("{} + 1".format(str(step)))
                already_run.append(step)

            elif all_instructions[step][0] == "jmp":
                # print("{} {}".format(all_instructions[step][0], all_instructions[step][1]))
                move = all_instructions[step][1]
                step = eval("{} + {}".format(str(step), move))
                already_run.append(step)
                # input("continue? ")

            # print("Steps...", already_run)
            if already_run.count(step) > 1:
                print("Accelerator", accumulator)
                print("broken")
                return "broken"

        except IndexError:
            return accumulator

# Main routine goes here


# write data from file
f = open("2020_advent_08_data.txt", "r")

content = f.read()
instructions = content.splitlines()
f.close()

# create list where each instruction is list
# inside it in the form 'command', 'amount'
all_instructions = []
for item in instructions:
    single = item.split(" ")
    all_instructions.append(single)

# print(all_instructions)

instruction_check = 0
for item in all_instructions:
    # print("Instruction to switch", all_instructions[instruction_check][0])
    if all_instructions[instruction_check][0] == "jmp":
        all_instructions[instruction_check][0] = "nop"

        run_it = run_instructions(all_instructions)
        if run_it == "broken":
            all_instructions[instruction_check][0] = "jmp"
        else:
            print("Accumulator", run_it)

    instruction_check += 1

# switch instruction and test it...
# jpm to nop, 826 too high


