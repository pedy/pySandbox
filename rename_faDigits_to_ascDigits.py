## 20190105
import os
from sys import argv
from unicodedata import digit
from curses import ascii

if len(argv) < 2:
    print('Usage: SCRIPTNAME PATH')
    exit()

target_path = argv[1]
if os.getcwd() != target_path:
    try:
        os.chdir(argv[1])
    except FileNotFoundError:
        print('The directory path is not valid.')
        exit()
    else:
        print('Working directory changed to: ', os.getcwd(), '\n')

dir_contents = os.listdir()

changed_count = 0
unchanged_count = 0
for item in dir_contents:
    new_name = ''
    hasChanged = False
    for letter in item:
        try:
            if not ascii.isascii(letter):
                new_name += str(digit(letter))
                hasChanged = True
            else:
                new_name += letter
        except ValueError:
            new_name += str(letter)


    if hasChanged:
        try:
            os.rename(item, new_name)
        except:
            print('<ERROR> Failed to rename ', item)
            pass
        else:
            print(item + ' --> ' + new_name)
            changed_count += 1
    else:
        unchanged_count += 1

    hasChanged = False

print(20*'-')
print(changed_count + unchanged_count, 'Items checked:')
if changed_count > 0:
    print('\t- ', changed_count, ' items renamed.')
if unchanged_count > 0:
    print('\t- ', unchanged_count, ' items left unchanged.')


exit()
