#!/usr/bin/python3
"""
Script reads stdin line by line and computes metrics
"""

i = 0
status_dict = {}
total_file_size = 0
while(True):
    try:
        line = input()
        tokens = line.split()
        # extract status code and file size
        status_code = tokens[-2]
        file_size = tokens[-1]
        total_file_size += int(file_size)
        if str(status_code) not in status_dict:
            status_dict[str(status_code)] = 1
        else:
            status_dict[str(status_code)] += 1
    except KeyboardInterrupt:
        print("File size:{}".format(total_file_size))
        for key, value in status_dict.items():
            print("{}: {}".format(key, value))

    if i % 10 == 0 and i != 0:
        print("File size:{}".format(total_file_size))
        for key, value in status_dict.items():
            print("{}: {}".format(key, value))
        i = 0
    i += 1
