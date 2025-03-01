"""This script will iterate through any number of CSV files generated from PKHex box data reports and output a modified CSV file with only specified fields.

Note: This has only been tested with gen3-6 but should also work for later gens. Refer to the readme for instructions.
"""

import csv
from os import listdir
from pathlib import Path

csv_files = listdir(r'input')

INPUT_PATH = r'input\\'
OUTPUT_PATH = r'output\\'
COMPLETED_PATH= r'completed\\'

for file in csv_files:
    with open(f'{INPUT_PATH}{file}', mode='r', encoding='utf-8') as csvfile:

        csv_reader = csv.DictReader(csvfile)
        modified_csv = f'MODIFIED - {file}'
        output_file = open(f'{OUTPUT_PATH}{modified_csv}', 'x', encoding='utf-8')

        with open(f'{OUTPUT_PATH}{modified_csv}', 'w', newline='', encoding='utf-8') as newfile:


            # Modify this list to change the output file's columns.
            # Refer to the readme for a list of fields.
            fieldnames = [
              'Position', 'Species',  'Nickname', 'Nature', 'IV_HP',
              'IV_ATK', 'IV_DEF', 'IV_SPA', 'IV_SPD', 'IV_SPE',
              'EV_HP', 'EV_ATK', 'EV_DEF', 'EV_SPA', 'EV_SPD', 'EV_SPE'
              ]

            csv_writer = csv.DictWriter(newfile, fieldnames=fieldnames)
            csv_writer.writeheader()

            for row in csv_reader:
                rowdict = {}
                for item in fieldnames:
                    
                    ######## Comment out the following lines to output original Position data ########
                    if item == "Position":
                        position = row[item].split('@').pop(1).split(' ')
                        if len(position[3]) == 4:
                            position[3] = ''
                        rowdict[item] = f'{position[1]} {position[2]} {position[3]}'
                    else:
                        rowdict[item] = row[item]
                    #################################################################################
                    #rowdict[item] = row[item]    # Uncomment this line to output original Position data
                csv_writer.writerow(rowdict)

        output_file.close()
        csvfile.close()
        Path(f'{INPUT_PATH}{file}').rename(f'{COMPLETED_PATH}{file}')
