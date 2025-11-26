#!/bin/python3

import os
import sys
import time
import argparse
from modules.colour import color
import yt_dlp


parser = argparse.ArgumentParser("python3 downloader.py")

parser.add_argument("--format",help="Download video format",default="video")
parser.add_argument("--link",help="URL to download",default="url")

args=parser.parse_args()

url = args.link
if url == 'None':
    sys.exit()
    
class silentLogger:
    def debug(self,msg):pass
    def warning(self,msg):pass
    def error(self,msg):pass    

def video(url):
    try:
        os.chdir("Downloads")
        
        options = {
    "format": "136+251",
    "outtmpl": "%(title)s.%(ext)s",
    "merge_output_format": "mp4",
    "quiet": True,
    "no_warnings": True,
    "noprogress": True,
    "logger": silentLogger(),

    "http_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": url,
        "X-YouTube-Client-Name": "1",
        "X-YouTube-Client-Version": "2.20240815.00.00"
    },
}
        with yt_dlp.YoutubeDL(options) as ydl:
            print(color.cyan("[+] ")+color.yellow("Downloading 720p resolution"))
            ydl.download([url])
            print(color.green("Successfully downloded !!"))
            sys.exit()
            os.chdir("..")
    except Exception as e_in_720:
            print(color.cyan("[+] ")+color.red(f"Failed\n")+color.cyan("[+] ")+color.red(e_in_720))
            try:
                options={
        "format"  : "135+251",
        "outtmpl" : "%(title)s.%(ext)s",
        "merge_output_format" : "mp4",
        "quiet" : True,
        "no_warnings" : True,
        "noprogress" : True,
        "logger" : silentLogger(),
        
         "http_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": url,
        "X-YouTube-Client-Name": "1",
        "X-YouTube-Client-Version": "2.20240815.00.00",
         },
         
        }
                with yt_dlp.YoutubeDL(options) as ydl:
                    print(color.cyan("[+] ")+color.yellow("Downloading 480p resolution"))
                    ydl.download([url])
                    print(color.green("Successfully downloded !!"))
                    sys.exit()
                    os.chdir("..")         
            except Exception as e_in_480:
                       print(color.cyan("[+] ")+color.red("Failed\n")+color.cyan("[+] ")+color.red(e_in_480))
                       try:
                           options={
                   "format"  : "134+251",
                   "outtmpl" : "%(title)s.%(ext)s",
                   "merge_output_format" : "mp4",
                   "quiet" : True,
                   "no_warnings" : True,
                   "noprogress" : True,
                   "logger" : silentLogger(),
                   
                  "http_headers": {
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                  "Referer": url,
                  "X-YouTube-Client-Name": "1",
                  "X-YouTube-Client-Version": "2.20240815.00.00",
         },
                           }
                           with yt_dlp.YoutubeDL(options) as ydl:
                               print(color.cyan("[+] ")+color.yellow("Downloading 360p resolution"))
                               ydl.download([url])
                               print(color.green("Successfully downloded !!"))
                               sys.exit()
                               os.chdir("..")
                       except Exception as e_in_360:
                           os.chdir("..")
                           print(color.cyan("[+] ")+color.red("Failed\n")+color.cyan("[+] ")+color.red(e_in_360))
                           print(color.cyan('[+] ')+color.red("Unable to download requested resource."))
                           sys.exit()





def audio(url):
    try:
                    os.chdir("Downloads")
                    options={
                   "format"  : "251",
                   "outtmpl" : "%(title)s.mp3",
                   "merge_output_format" : "mp3",
                   "quiet" : True,
                   "no_warnings" : True,
                   "noprogress" : True,
                   "logger" : silentLogger(),
                   
                  "http_headers": {
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                  "Referer": url,
                  "X-YouTube-Client-Name": "1",
                  "X-YouTube-Client-Version": "2.20240815.00.00",
         },
                           }
                    with yt_dlp.YoutubeDL(options) as ydl:
                        print(color.cyan('[+] ')+color.yellow('Downloading audio ...(medium,webm)'))
                        ydl.download([url])
                        print(color.green("Successfully downloded !!"))
                        os.chdir("..")
                        sys.exit()
            
    except Exception as mw_au:
        print(color.cyan('[+] ')+color.red('Failed\n')+color.cyan('[+] ')+color.red(mw_au))
        try:
                   options={
                   "format"  : "140",
                   "outtmpl" : "%(title)s.mp3",
                   "merge_output_format" : "mp3",
                   "quiet" : True,
                   "no_warnings" : True,
                   "noprogress" : True,
                   "logger" : silentLogger(),
                   
                  "http_headers": {
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                  "Referer": url,
                  "X-YouTube-Client-Name": "1",
                  "X-YouTube-Client-Version": "2.20240815.00.00",
         },
                           }
                   with yt_dlp.YoutubeDL(options) as ydl:
                               print(color.cyan('[+] ')+color.yellow('Downloading audio ...(medium,mp4a)'))
                               ydl.download([url])
                               print(color.green("Successfully downloded !!"))
                               os.chdir("..")
                               sys.exit()
        except Exception as mm_au:
                               print(color.cyan('[+] ')+color.red('Failed\n')+color.cyan('[+] ')+color.red(mm_au))
                               
                               try:
                                   options={
                    "format"  : "249",
                    "outtmpl" : "%(title)s.mp3",
                    "merge_output_format" : "mp3",
                    "quiet" : True,
                    "no_warnings" : True,
                    "noprogress" : True,
                    "logger" : silentLogger(),
                    "http_headers": {
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                  "Referer": url,
                  "X-YouTube-Client-Name": "1",
                  "X-YouTube-Client-Version": "2.20240815.00.00",
         },
                           }
                                   with yt_dlp.YoutubeDL(options) as ydl:
                                       print(color.cyan('[+] ')+color.yellow('Downloading audio ...(low,webm)'))
                                       ydl.download([url])
                                       print(color.green("Successfully downloded !!"))
                                       os.chdir("..")
                                       sys.exit()
                               except Exception as lw_au:
                                   print(color.cyan('[+] ')+color.red("Failed\n")+color.cyan('[+] ')+color.red(lw_au))
                               try:
                                   options={
                   "format"  : "139",
                   "outtmpl" : "%(title)s.mp3",
                   "merge_output_format" : "mp3",
                   "quiet" : True,
                   "no_warnings" : True,
                   "noprogress" : True,
                   "logger" : silentLogger(),
                   
                  "http_headers": {
                  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                  "Referer": url,
                  "X-YouTube-Client-Name": "1",
                  "X-YouTube-Client-Version": "2.20240815.00.00",
         },
                           }
                                   with yt_dlp.YoutubeDL(options) as ydl:
                                       print(color.cyan('[+] ')+color.yellow('Downloading audio ...(low,mp4a)'))
                                       ydl.download([url])
                                       print(color.green("Successfully downloded !!"))
                                       os.chdir("..")
                                       sys.exit()
                               except Exception as lm_au:
                                   print(color.cyan('[+] ')+color.red('Failed\n')+color.cyan('[+] ')+color.red(lm_au))
                                   print(color.cyan('[+] ')+color.red("Unable to download"))
                                   os.chdir('..')
                                   sys.exit()
                                   
                               
        
def home():
    print(color.cyan("\n[+] ")+color.yellow("Checking..."))
    try :
        title = os.popen(f"yt-dlp --get-title {url}").read().strip()
        print(color.cyan('[+] ')+color.green(f"Title : {title}"))
        while True:
               if args.format == "video":
                   video(url)
               elif args.format == "audio":
                   audio(url)
               else:
                   print(color.red("Enter a valid option."))
                   sys.exit()
    except Exception as err_at_title :
             print(color.cyan("[")+color.cyan('+')+color.cyan('] ')+color.red("Check URL and internet connection !"))
             
             
            
    
if __name__ == '__main__':
    home()                                                   
