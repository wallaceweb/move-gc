# move-gc
Move gamecube iso and ciso files to be in Nintendont configuration using python3

**Nintendont has issues with some ciso files. This program will not fix/reconfigure files in a way that will make non-working ciso files work with Nintendont. I merely added ciso functionality to the program as I have seen others online mention they were able to get ciso files to work properly**

INFO-
This repo has 2 files, the original move-gc.py file and an executable file that should work without needing to install Python3
This program creates a /games directory, then renames the .iso OR .ciso files as game.iso or game.ciso respectively. I could've done a bit more work and just learned how to copy the files and then rename, but got a bit stuck. If anyone has tips let me know!

**WARNING - PLEASE MANUALLY BACK UP GAMES FIRST
AND ISOLATE THE PROGRAM FROM ALL OTHER FILES/FOLDERS OTHER THAN GC ISO AND CISO FILES
THIS PROGRAM RENAMES AND MOVES FILES MANUALLY WITHOUT COPYING
IF YOU HAVE ANY NON GC ISO OR CISO FILES, THEY WILL ALSO BE MOVED**

Usage-

Executable:
1. Put executable move-gc file in a new folder
2. Put all gamecube files in the same folder
3. Open up a terminal window (CMD, powershell, bash, zsh etc)
4. Change your directory to the new folder
  If you need help doing this, might need to look up a tutorial
5. Run the program by typing the program's name

  Windows:
    move-gc

  Linux:
    sudo chmod +x move-gc
    ./move-gc

6. Follow the steps listed on screen
    
Python file:
1. Install python3
2. Follow above listed steps, except when getting to running the program, type

  Windows:
    python move-gc.py

  Linux:
    python3 move-gc.py

3. Follow listed steps


Sorry if everything is a bit of a mess! Pretty new to programming but was excited to share this utility that I made. I'll try to help if anyone needs it!
