#!/usr/bin/python

import csv
import sys

def usage():
    print sys.argv[0], '<input.csv> <output.csv>'

def main():
    header = 'Name,E-mail 1 - Value,E-mail 2 - Value,Phone 1 - Value,Phone 1 - detail,Phone 2 - Value,Phone 2 - detail,,FacebookID,Facebook Status,Facebook-link,Favorite,poBox,extended address,street address,locality,region,postal code,country name\n'
    exclude = set('+ ()-')
    output = [header]
    with open(sys.argv[1], 'r') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            if row['Name'] and row['Phone 1 - Value']:
                if row['Phone 1 - Type'] == 'Home' or row['Phone 1 - Type'] == 'Work':
                    phone1type = row['Phone 1 - Type']
                else:
                    phone1type = 'Mobile'
                if row['Phone 2 - Value']:
                    if row['Phone 2 - Type'] == 'Home' or row['Phone 2 - Type'] == 'Work':
                        phone2type = row['Phone 2 - Type']
                    else:
                        phone2type = 'Mobile'
                else:
                    phone2type = ''
                name = row['Name']
                phone1 = ''.join([ch for ch in row['Phone 1 - Value'] if ch not in exclude])
                phone2 = ''.join([ch for ch in row['Phone 2 - Value'] if ch not in exclude])
                output.append('{},,,{},{},{},{},,,,,,,,,,,,Canada\n'.format(name, phone1, phone1type, phone2, phone2type))

    with open(sys.argv[2], 'w') as outfile:
        outfile.writelines(output)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        exit(1)

    main()
    exit(0)

