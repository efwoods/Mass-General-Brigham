import math
import argparse

def convertInputListToInt(val_list):
    converted_val_list = []
    for val in val_list:
        result = int(val)
        converted_val_list.append(result)
    return converted_val_list

# input: 3 numbers
# output: list of absolute values of input 3 numbers
def convertThreeToAbsoluteVal(val1, val2, val3):
    val_list =[]
    val_absolute_list = []
    val_list = [val1, val2, val3]
#    val_list = convertInputListToInt(val_list) #type checking
    for val in val_list:
        val_absolute_list.append(math.fabs(val))
    return val_absolute_list

def maximumAbsoluteOfThree(val1, val2, val3):
    val_absolute_list = []
    val_absolute_list = convertThreeToAbsoluteVal(val1,val2,val3)
    return max(val_absolute_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Return the maximum of the absolute value of three numbers')
    parser.add_argument('first_number', type=float)
    parser.add_argument('second_number', type=float)
    parser.add_argument('third_number', type=float)
    args = parser.parse_args()
    result = maximumAbsoluteOfThree(args.first_number, args.second_number, args.third_number)
    print(result)

    ''' 
    Errors:

    https://www.geeksforgeeks.org/how-to-handle-invalid-arguments-with-argparse-in-python/

    too many arguments
    wrong type of input
    too few args

    '''