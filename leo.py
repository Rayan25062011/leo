import time
import sys
import subprocess
import time
import os
from core.exceptions import *
from rich.console import Console
from core.security import secure

console = Console()
verbose = False
cddir = ""

red = "\033[31m"
blue = "\033[34m"
bold = "\033[1m"
reset = "\033[0m"
green = "\033[32m"
yellow = "\033[33m"

username = os.getlogin()
secure(username)

def p(string, delay):
    sys.stdout.write(string+"... ")
    time.sleep(delay)
    sys.stdout.write("Done\n")


def _handle_output(process):
    print(process.stdout)
    print(process.stderr)

def _kill(process):
    subprocess.kill(process)

def _communicate(process):
    process = subprocess.communicate(process)
    if process:
        return 0
    else:
        console.log("Communication with process failed, try starting the thread")
        return 1


while True:
    if cddir == "":
        leo = input(f"~{blue} @{reset} ")
    else:
        leo = input(f"~/{cddir}{blue} @{reset} ")


    if leo == "quit":
        break

    elif leo == "":
        pass
    elif leo == "!verbose":
        if verbose == False:
            verbose = True
    elif leo == "!!verbose":
        if verbose == True:
            verbose = False
    elif leo == "stop":
        p("Shutting down leo", 0.9)
        verbose = False
        username = ""
        cddir = ""
        break
    else:
        try:
            if "cd" in leo:
                os.system(leo)
                org1 = leo
                spl1 = "cd"
                resl = org1.split(spl1)[1]
                cddir = resl
                cddir = cddir.translate({ord(' '): None})
                if "cd" == leo:
                    cddir = ""
            else:
                result = subprocess.run([leo], capture_output=True, text=True, check=True)
                if verbose == True:
                    print(result)
                _handle_output(result)
            if verbose == True:
                console.log(result)

        except Exception as e:
            console.log("Command "+"'"+leo+"'"+" is invalid")
    