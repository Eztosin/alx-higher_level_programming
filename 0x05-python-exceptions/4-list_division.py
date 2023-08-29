#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            numerator = my_list_1[i]
            denominator = my_list_2[i]
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            if not (isinstance(numerator, (int, float)) and
                    isinstance(denominator, (int, float))):
                print("wrong type")
                result.append(0)
            elif denominator == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(numerator / denominator)
    return result
