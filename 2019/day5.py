# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 10:32:37 2019

@author: Pari
"""

inp = '''
3,225,1,225,6,6,1100,1,238,225,104,0,1101,65,39,225,2,14,169,224,101,-2340,224,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1001,144,70,224,101,-96,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,92,65,225,1102,42,8,225,1002,61,84,224,101,-7728,224,224,4,224,102,8,223,223,1001,224,5,224,1,223,224,223,1102,67,73,224,1001,224,-4891,224,4,224,102,8,223,223,101,4,224,224,1,224,223,223,1102,54,12,225,102,67,114,224,101,-804,224,224,4,224,102,8,223,223,1001,224,3,224,1,224,223,223,1101,19,79,225,1101,62,26,225,101,57,139,224,1001,224,-76,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1102,60,47,225,1101,20,62,225,1101,47,44,224,1001,224,-91,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1,66,174,224,101,-70,224,224,4,224,102,8,223,223,1001,224,6,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,226,224,102,2,223,223,1005,224,329,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,344,101,1,223,223,8,226,677,224,102,2,223,223,1006,224,359,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,374,1001,223,1,223,1108,226,677,224,1002,223,2,223,1005,224,389,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,404,1001,223,1,223,1108,677,677,224,102,2,223,223,1006,224,419,1001,223,1,223,1008,226,677,224,102,2,223,223,1005,224,434,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,7,677,677,224,102,2,223,223,1006,224,509,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,524,1001,223,1,223,108,226,677,224,1002,223,2,223,1006,224,539,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,569,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,584,101,1,223,223,1107,677,226,224,1002,223,2,223,1005,224,599,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,629,1001,223,1,223,107,677,226,224,1002,223,2,223,1005,224,644,1001,223,1,223,1107,677,677,224,102,2,223,223,1006,224,659,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226
'''

lst = inp.strip().split(',')

input_arr = [int(i) for i in lst]
#input_arr[1] = 12
#input_arr[2] = 2

def process_array(input_arr):
    arr = input_arr[:]
    index = 0
    while True:
        op_code = arr[index]
#        n_values = len(str(op_code))
        temp = str(op_code).zfill(5)
        mode, operator = temp[:3], int(temp[3:])
        if operator == 3:
            user_inp = int(input("enter the input val:"))
            arr[arr[index + 1]] = user_inp
            index += 2
            continue
        elif operator == 4:
            print(arr[arr[index + 1]])
            index += 2
            continue

        if mode[2] == '0':
            numberA = arr[arr[index + 1]]
        else:
            numberA = arr[index + 1]
        if mode[1] == '0':
            numberB = arr[arr[index + 2]]
        else:
            numberB = arr[index + 2]
        if operator == 99:
            print(arr[0])
            break
#            return arr[0]
        elif operator == 1:
            res = numberA + numberB
        elif operator == 2:
            res = numberA * numberB
        elif operator == 5:
            if numberA != 0:
                index = numberB
            else:
                index += 3
            continue
        elif operator == 6:
            if numberA == 0:
                index = numberB
            else:
                index += 3
            continue
        elif operator == 7:
            res = int(numberA < numberB)
        elif operator == 8:
            res = int(numberA == numberB)
#        elif operator == 3:
#            user_inp = int(input("enter the input val:"))
#            arr[arr[index + 1]] = user_inp
#            index += 2
#            continue
#        elif operator == 4:
#            print(arr[arr[index + 1]])
#            index += 2
#            continue
        if mode[0] == '0':
            arr[arr[index + 3]] = res
        else:
            arr[index + 3] = res

        index += 4

    return arr[0]

print(process_array(input_arr))

inp = '''
3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9
'''