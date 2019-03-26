#Project Euler #1
#!/bin/python3

import sys


n = int(input().strip())
counter = 0
while counter < n:
    inc_num = int(input().strip())
    if inc_num % 3 == 0 or inc_num % 5 == 0:
        
    counter = counter + 1
