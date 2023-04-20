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


import time

bad_list = []
time_list = []
count = 0
new_bad = ""
newer_bad = ""

while count < 69420:
    # start_time = time.time()
    # if count > 0:
    #   print(time_list[-1])

    in_file = open("bad.txt", "r")

    for line in in_file:
        bad_list.append(line.strip())
        
    for character in bad_list:
        new_bad += character

    bad_list[0] = new_bad
    newer_bad = bad_list[0][0: len(bad_list[0]) - (len(bad_list[0]) - 5)]
    print(newer_bad)
    count += 1
    print(count)
    in_file.close()
    # time_list.append((time.time() - start_time))
