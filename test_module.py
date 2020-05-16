#! /usr/bin/python3

import sys
print("SYS MODULES BEFORE MODIFICATION")
print(sys.path)

sys.path = sys.path[::-1]
print("SYS MODULES AFTER MODIFICATION")
print(sys.path)

# print(sys.modules)