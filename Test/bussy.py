"""

LUCAS' BAD ATTEMPT

initialise variables

loop 69420 times
    open file, read to variable
    for line in file
        append line to list
    for character in list
        variable += character
    list[0] = new variable
    newer variable = list[0][0:length of list - (length of list - 5)]
    print newer variable
    count += 1
    close file

"""


bussy_list = []
count = 0
new_bussy = ""
newer_bussy = ""
while count < 10:
    in_file = open("/workspaces/codespaces-blank/Test/bussy.txt", "r")
    for line in in_file:
        bussy_list.append(line.strip())
    for character in bussy_list:
        new_bussy += character
    bussy_list[0] = new_bussy
    newer_bussy = bussy_list[0][0: len(bussy_list[0]) - (len(bussy_list[0]) - 5)]
    print(newer_bussy)
    count += 1
    in_file.close()
