#!/usr/bin/env python3
'''Lab 3 Inv 4 function free_space '''
# Seneca ID: ivassiljenko

import subprocess

def free_space():
   command = "df -h | grep '/$' | awk '{print $4}'"
   result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
   output = result.stdout.decode('utf-8').strip()
   return output

if __name__ == '__main__':
   print(free_space())

