This script is meant to take Box Data Reports generated by PKHex and filter out unnessary fields for ease of use.

This script requires Python3 and PKHex to be installed on your machine.

You can get Python at https://www.python.org/downloads/
You can learn more about, and download PKHex at https://projectpokemon.org/home/files/file/1-pkhex/

---------How to Use----------

Dump your save and load it into PKHex.
Within PKHex access Tools-> Data -> Box Data Report
Exit the report and you'll be presented with an option to save as a CSV. It is recommended to rename this file.
Copy/move the .csv file to the "input" folder. You may repeat these steps for any number of .csv files.
Open your terminal, navigate to the scripts directory and run the following command ```python pkmncsvconversion.py ```

You can find the modified .csv files in the "output" folder. The original files have been moved to the "completed" folder to prevent them from being ran again.


----------Modifying the "Position" field-------
This field includes more information than is necessary. By default, this script with modify the output data so that it only shows box/party location and position. You can output the original data by commenting out the notated code in the script. Be sure the uncomment the noted line of code, otherwise nothing will write to the output file.


----------Modifying the fields----------

Be default, this script is set up to provide easy access to pokemon's IV and EV values. This script can be modified to add or remove fields as the user sees fit.

Access the script and modify the "fieldnames" list.
Learn about Python lists at https://www.w3schools.com/python/python_lists.asp

A list of fields can be found below. The order in which they appear in the source code will be the order in which they output to the .csv file.

Position
Nickname
Species
Nature
Gender
ESC
HP_Type
Ability
Move1
Move2
Move3
Move4
HeldItem
HP
ATK
DEF
SPA
SPD
SPE
MetLoc
EggLoc
Ball
OT
Version
OTLang
Legal
EC
PID
IV_HP
IV_ATK
IV_DEF
IV_SPA
IV_SPD
IV_SPE
EXP
Levle
EV_HP
EV_ATK
EV_DEF
EV_SPA
EV_SPD
EV_SPE
Cool
Beauty
Cute
Smart
Tough
Sheen
NotOT
AbilityNum
GenderFlag
Form
PokerusStrain
PokerusDays
MetLevel
OriginalTrainerGender
FatefulEncounter
IsEgg
IsNicknamed
IsShiny
TID16
SID16
TSV
Move1_PP
Move2_PP
Move3_PP
Move4_PP
Move1_PPUp
Move2_PPUp
Move3_PPUp
Move4_PPUp
Relearn1
Relearn2
Relearn3
Relearn4
Checksum
Friendship
EggYear
EggMonth
EggDay
MetYear
MetMonth
MetDay
# PKHex-csv-conversion
