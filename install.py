#!/bin/python3

import subprocess
import os
from modules.colour import color

os.system('bash templates/banner.sh')
print(color.cyan('[+] '),end = '')
print(color.red('Ensure run this file as root\n'))
venv = str(input(color.cyan('[+] ')+color.blue('Setup a virtual environment (y/n) : '))) or "continue"

if venv.lower() == "n":
    print(color.cyan('[+] ')+color.green('Virtual environment setup skipped '))
    xyz = str(input(color.blue('Press enter to continue...')))
else:
    try:
            print(color.cyan('\n[+] ')+color.yellow('Installing python3-venv'))
            result = subprocess.run(
            ["sudo","apt","install","python3-venv","-y"],
            stdout = subprocess.DEVNULL,
            stderr = subprocess.PIPE,
            text = True,
           check = True
         )
            print(color.green('[✓] ')+color.green('python3-venv successfully installed'))
            try:
                print(color.cyan('[+] ')+color.yellow('Creating virtual environment...'))
                result = subprocess.run(
    ["python3","-m","venv","DownVid"],
    stdout = subprocess.DEVNULL,
    stderr = subprocess.PIPE,
    text = True,
    check = True
    )
                print(color.green('[✓] ')+color.green('Environment cretaed'))
                try :
                    cwd = os.getcwd()+"/DownVid/bin/activate"
                    print(color.cyan('\n[+] ')+color.yellow('Activating...'))
                    result = subprocess.run(
    ["source",cwd],
    stdout = subprocess.DEVNULL,
    stderr = subprocess.PIPE,
                text = True,
                check = True
    )
                    print(color.green('[✓] ')+color.green('Environment activated '))
                    abc = str(input(color.blue('\nPress enter to continue...')))
                except subprocess.CalledProcessError as e :
                    print(color.cyan('[+] ')+color.red('Update Failed '))
                    print(color.red('Error : \n')+e.stderr)
                    abc = str(input(color.blue('\nPress enter to continue...')))
                    
            except subprocess.CalledProcessError as e :
                print(color.cyan('[+] ')+color.red('Failed : try manually'))
                print(color.red('Error : \n')+e.stderr)
                abc = str(input(color.blue('\nPress enter to continue...')))
    
    
    
    except subprocess.CalledProcessError as e :
        print(color.cyan('[+] ')+color.red('Installation Failed '))
        print(color.red('Error :  \n')+e.stderr)
        abc = str(input(color.blue('\nPress enter to continue...')))
        
        
          

os.system('bash templates/banner.sh')
print(color.cyan('[+] ')+color.green('Installation started'))
try:
    print(color.cyan('\n[+] ')+color.yellow('Updating System...'))
    result = subprocess.run(
    ["sudo","apt","update","-y"],
    stdout = subprocess.DEVNULL,
    stderr = subprocess.PIPE,
    text = True,
    check = True
    )
    print(color.green('[✓] ')+color.green('System Successfully Updated'))
except subprocess.CalledProcessError as e :
    print(color.cyan('[+] ')+color.red('Update Failed '))
    print(color.red('Error : \n')+e.stderr)
    
try:
    print(color.cyan('\n[+] ')+color.yellow('Upgrading System...'))
    result = subprocess.run(
    ["sudo","apt","upgrade","-y"],
    stdout = subprocess.DEVNULL,
    stderr = subprocess.PIPE,
    text = True,
    check = True
    )
    print(color.green('[✓] ')+color.green('System Successfully Upgraded'))
except subprocess.CalledProcessError as e :
    print(color.cyan('[+] ')+color.red('Upgrade Failed '))
    print(color.red('Error : \n')+e.stderr)
    
try:
    print(color.cyan('\n[+] ')+color.yellow('Installing python3-pip...'))
    result = subprocess.run(
    ["sudo","apt","install","python3-pip","-y"],
    stdout = subprocess.DEVNULL,
    stderr = subprocess.PIPE,
    text = True,
    check = True
    )
    print(color.green('[✓] ')+color.green('python3-pip Successfully installed'))
except subprocess.CalledProcessError as e :
    print(color.cyan('[+] ')+color.red('Installation Failed '))
    print(color.red('Error : \n')+e.stderr)  
    print(color.cyan('[+] ')+color.yellow('Try to install manually (ex - apt install python3-pip or apt install python3-pip3)'))            
    
try:
    print(color.cyan('\n[+] ')+color.yellow('Installing yt-dlp...'))
    result = subprocess.run(
    ["sudo","apt","install","yt-dlp","-y"],
    stdout = subprocess.DEVNULL,
    stderr = subprocess.PIPE,
    text = True,
    check = True
    )
    print(color.green('[✓] ')+color.green('yt-dlp Successfully installed'))
except subprocess.CalledProcessError as e :
    print(color.cyan('[+] ')+color.red('Installation Failed '))
    print(color.red('Error : \n')+e.stderr)  
    print(color.cyan('[+] ')+color.yellow('Try to install manually(ex - pip install yt-dlp)\nor create a virtual environment'))          


    
    
try:
    print(color.cyan('\n[+] ')+color.yellow('Installing ffmpeg...'))
    result = subprocess.run(
    ["sudo","apt","install","ffmpeg","-y"],
    stdout = subprocess.DEVNULL,
    stderr = subprocess.PIPE,
    text = True,
    check = True
    )
    print(color.green('[✓] ')+color.green('ffmpeg Successfully installed'))
except subprocess.CalledProcessError as e :
    print(color.cyan('[+] ')+color.red('Installation Failed '))
    print(color.red('Error : \n')+e.stderr)  
    print(color.cyan('[+] ')+color.yellow('Try to install manually (ex - apt install ffmpeg)'))          
    