#!/bin/python3
import os
print('Show user with bach')
with open('/etc/passwd') as users:
    for user in users:
        if 'bash' in user:
            print(user, end='')
print('')
