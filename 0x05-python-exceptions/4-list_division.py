#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_1[i])
        except ValueError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(None)
        except IndexError:
            print("out of range")
            new_list.append(None)
        finally:
            return new_list
