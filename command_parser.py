# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Jiayi Zhu
# jzhu42@uci.edu
# 94623196

import shlex

def user_input():
    command_line = input()
    if not command_line:
        return []
    command_lst = shlex.split(command_line)
    return command_lst
