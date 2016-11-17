#!/usr/bin/python3
import sys
big_table = {}         # The data store
col_names = ['row-id'] # An index of all column names

# Start with a fixed column named row-id:
print("Enter row-id, or just hit ENTER to stop adding data: ")
while True:
    input_data = sys.stdin.readline().strip()
    if len(input_data) == 0:
        print("Nothing entered, ending data entry loop")
        break

    # Create a new row object, that's a dictionary, with one entry for
    # mandatory row-id
    row = {'row-id': input_data}

    print("Enter column name (just press ENTER to end row data entry): ")

    while True:
        # Get another input record
        colname = sys.stdin.readline().strip()

        if len(colname) == 0:
            print("Completed row '{0}'".format(row['row-id']))
            big_table[row['row-id']] = row
            break

        print("Enter column value (just press ENTER for no value): ")
        input_data = sys.stdin.readline().strip()
        if len(input_data) > 0:
            row[colname] = input_data
            if colname not in col_names:
                col_names.append(colname)
        print("Enter column name (just press ENTER to end row data entry): ")

    print("Enter row-id, or just hit ENTER to stop adding data: ")

print(big_table)

print("\n" + '\t'.join(col_names))
for r in big_table:
    s = ''
    for c in col_names:
        if c in big_table[r]:
            s = s + big_table[r][c] + '\t'
        else:
            s = s + '\t'

    print(s)
