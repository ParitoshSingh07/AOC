# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 18:34:21 2019

@author: Pari
"""

inp = '''
3,8,1001,8,10,8,105,1,0,0,21,34,51,76,101,114,195,276,357,438,99999,3,9,1001,9,3,9,1002,9,3,9,4,9,99,3,9,101,4,9,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,1002,9,4,9,101,3,9,9,102,5,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1001,9,3,9,102,2,9,9,101,4,9,9,102,3,9,9,101,2,9,9,4,9,99,3,9,102,2,9,9,101,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99
'''

lst = inp.strip().split(',')

input_arr = [int(i) for i in lst]
#input_arr[1] = 12
#input_arr[2] = 2

def process_array(input_arr, inp_iter):
    arr = input_arr[:]
    index = 0
    echo_out = None
    while True:
        op_code = arr[index]
#        n_values = len(str(op_code))
        temp = str(op_code).zfill(5)
        mode, operator = temp[:3], int(temp[3:])
        if operator == 99:
            print(arr[0])
#            return arr[0]
            break
        if operator == 3:
#            user_inp = int(input("enter the input val:"))
            print("ask")
            user_inp = next(inp_iter)
            arr[arr[index + 1]] = user_inp
            index += 2
            continue
        elif operator == 4:
            print(arr[arr[index + 1]])
            echo_out = arr[arr[index + 1]]
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
#            return arr[0]
        if operator == 1:
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

    return echo_out


#process_array(input_arr)
#print(process_array(input_arr))

inp = '''
3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5
'''
from itertools import permutations
all_phases = (4, 3, 2, 1, 0)
#permutations(all_phases, len(all_phases))
result_dict = {}
for phase_seq in permutations(all_phases, len(all_phases)):
#phase_seq = (4, 3, 2, 1, 0)
phase_seq = 9,8,7,6,5
    echo_in = [0]
    for phase in phase_seq:
        input_iter = iter((phase, echo_in[-1]))
        result = process_array(input_arr, input_iter)
        echo_in.append(result)
    result_dict[phase_seq] = echo_in[-1]

print(max(result_dict.values()))