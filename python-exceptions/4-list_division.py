#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i, newlist = 0, []
    while i < list_length:
        try:
            div = [my_list_1[i] / my_list_2[i]]
            newlist.append(div)
        except ValueError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            i += 1
    return newlist
