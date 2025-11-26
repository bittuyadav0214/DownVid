#!/bin/python3

import sys
import os
import subprocess
import time
from modules.colour import color

try:
    os.mkdir("Downloads")
except:
    pass
os.system("bash templates/banner.sh")
print(color.cyan(' [•] ')+color.yellow("Update tool regularly to avoid errors !! \n "))
update = str(input(color.blue("Press any key to update or enter to skip and continue... "))) or False
if update:
    try:
        print(color.cyan('\n[^°^] ')+color.yellow('Updating system...'))
        result = subprocess.run(
        ["apt","update","-y"],
        stdout = subprocess.DEVNULL,
        stderr = subprocess.PIPE,
        text = True,
        check = True
        )
        print(color.green("[✓] System Successfully updated"))
    except subprocess.CalledProcessError as e:
        print(color.red('[+] Update Failed'))
        print(color.cyan("[+] ")+color.red('Error : \n'))
        print(color.red(e.stderr))
        
    try:
        print(color.cyan('\n[^°^] ')+color.yellow('Updating yt-dlp...'))
        result = subprocess.run(
        ["yt-dlp","-U"],
        stdout = subprocess.DEVNULL,
        stderr = subprocess.PIPE,
        text = True,
        check = True
        )
        print(color.green("[✓] yt-dlp Successfully updated"))
    except subprocess.CalledProcessError as e:
        print(color.red('[+] Update Failed'))
        print(color.cyan("[+] ")+color.red('Error : \n')+e.stderr)        
        
    try:
        print(color.cyan('\n[^°^] ')+color.yellow('Updating tool...'))
        result = subprocess.run(
        ["git","pull"],
        stdout = subprocess.DEVNULL,
        stderr = subprocess.PIPE,
        text = True,
        check = True
        )
        print(color.green("[✓] Tool Successfully updated"))
    except subprocess.CalledProcessError as e:
        print(color.red('[+] Update Failed'))
        print(color.cyan("[+] ")+color.red('Error : \n')+e.stderr)        
       
    AfterUpdate = str(input(color.blue('\nPress enter to continue...')))    
    
os.system("bash templates/banner.sh")    

def home():
    print(color.blue('  [')+color.cyan('+')+color.blue(']')+color.yellow(" Choose the format :-\n"))
    print(color.blue('  [')+color.red('+')+color.blue(']')+color.cyan(" 1.Video"))
    print(color.blue('  [')+color.red('+')+color.blue(']')+color.cyan(" 2.Audio"))
    print(color.blue('  [')+color.red('+')+color.blue(']')+color.cyan(" 3.Exit"))
    
    
    
    while True:
        dec = str(input(color.green(" \nSelect your option : ")))
        
        
        if dec == "1":
            url = str(input(color.green("Enter URL : "))) or "None"
            init = True
            while True:
                try:
                    if init :
                        result = os.system(f"python3 downloader.py --format video --link {url}")
                        init = False
                    else:
                        url = str(input(color.green("Enter URL or press enter for main menu : ")) or "back")
                        
                        if url == "back":
                            break
                        else:
                            os.system(f"python3 downloader.py --format video --link {url}")
                    
                    
                except Exception as e:
                    print(e)
                    
                    
                    
        elif dec == "2":
                url = str(input(color.green("Enter URL : "))) or "None"
                init = True
                while True:
                    try:
                        if init :
                            os.system(f"python3 downloader.py --format audio --link {url}")
                            init = False
                        else:
                            url = str(input(color.green("Enter URL or press enter for main menu : ")) or "back")
                        
                            if url == "back":
                                break
                            else:
                                os.system(f"python3 downloader.py --format audio --link {url}")
                    
                    
                    except Exception as e:
                        print(e)
                
                
                
        elif dec == "3":
                    print(color.red("Exiting..."))
                    time.sleep(1)
                    sys.exit()
                    
                    
                    
        else:
                    print(color.red("Please enter valid option."))
                    
                    
                    
if __name__ == "__main__":
    home()        
