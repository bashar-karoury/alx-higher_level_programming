#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(max(len(my_list_1), len(my_list_2))):
        temp = 0
        try:
            temp = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            temp = 0
        except ZeroDivisionError:
            print("division by 0")
            temp = 0
        except TypeError:
            print("wrong type")
            temp = 0
        finally:
            new_list.append(temp)
    return new_list
