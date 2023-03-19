## import needed modules

from pathlib import Path
import shutil

## set up variables

isofile = Path('.').glob('*.iso')
cisofile = Path('.').glob('*.ciso')
games = Path('games')

## define copyiso and copyciso command
## creates games folder, renames iso or ciso file then moves it to created folder

def copyiso():
    games.mkdir(exist_ok = True)
    for file in isofile:
        print(file)
        pre = file.stem
        print('Creating folder for: ' + pre)
        Path(pre).mkdir()
        print('Renaming to game.iso')
        file.rename('game.iso')
        print('Moving to ' + pre)
        shutil.move('game.iso', pre)
        shutil.move(pre, games)

def copyciso():
    games.mkdir(exist_ok = True)
    for file in cisofile:
        print(file)
        pre = file.stem
        print('Creating folder for: ' + pre)
        Path(pre).mkdir()
        print('Renaming to game.ciso')
        file.rename('game.ciso')
        print('Moving to ' + pre)
        shutil.move('game.ciso', pre)
        shutil.move(pre, games)

## Warnings

print('WARNING - PLEASE MANUALLY BACK UP GAMES FIRST')
print('AND ISOLATE THE PROGRAM FROM ALL OTHER FILES/FOLDERS OTHER THAN GC ISO AND CISO FILES')
print('THIS PROGRAM RENAMES AND MOVES FILES MANUALLY WITHOUT COPYING')
print('IF YOU HAVE ANY NON GC ISO OR CISO FILES, THEY WILL ALSO BE MOVED')

## input and such

print('If you have read the previous warning, please type filetype of gc iso (.ciso or .iso).')
filetype = input()

if filetype == 'iso' or filetype == '.iso':
    print('Please put all gamecube .iso files in the same directory as this program, then type Y when ready.')
    accept = input()
    if accept == 'Y' or accept == 'y':
        copyiso()
        print('Games moved over in .iso format. Have a nice day :)')
    else:
        print('Cancelled.')

elif filetype == 'ciso' or filetype == '.ciso':
    print('Please put all gamecube .ciso files in the same directory as this program, then type Y when ready.')
    accept = input()
    if accept == 'Y' or accept == 'y':
        copyciso()
        print('Games moved over in .ciso format. Have a nice day :)')
    else:
        print('Cancelled.')

else:
    print('Unrecognized filetype.')
