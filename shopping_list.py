initial_list = input().split("!")


def urgent_item(item):
    if item not in initial_list:
        initial_list.insert(0, item)


def unnecessary(item):
    if item in initial_list:
        initial_list.remove(item)


def correct(old_item,new_item):
    if old_item in initial_list:
        initial_list[initial_list.index(old_item)] = new_item


def rearange(item):
    if item in initial_list:
        initial_list.remove(item)
        initial_list.append(item)


command = input()
while command != "Go Shopping!":
    command=command.split()
    first_index_command = command[0]
    other_inexes = command[1]
    if first_index_command == "Urgent":
        urgent_item(other_inexes)
    elif first_index_command == "Unnecessary":
        unnecessary(other_inexes)
    elif first_index_command == "Correct":
        correct(other_inexes,command[-1])
    elif first_index_command == "Rearrange":
        rearange(other_inexes)
    command = input()
print(", ".join(initial_list))
