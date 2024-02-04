#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i, newlist = 0, []
    while i < list_length:
        try:
            div = my_list_1[i] / my_list_2[i]
            newlist.append(div)
        except TypeError:
            print("wrong type")
            newlist.append(0)
        except IndexError:
            print("out of range")
            newlist.append(0)
        except ZeroDivisionError:
            print("division by 0")
            newlist.append(0)
        finally:
            i += 1
    return newlist
