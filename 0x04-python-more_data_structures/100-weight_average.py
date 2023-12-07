#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        total_sum = 0
        weight_sum = 0
        for i in my_list:
            total_sum = total_sum + i[0]*i[1]
            weight_sum = weight_sum + i[1]
        return total_sum/weight_sum
