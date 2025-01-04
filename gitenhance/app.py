import getopt, sys

from github.bootstrap import Octokit
from utils.colors import bcolors

# CMD Line Args
arguments_list = sys.argv[1:]
options = "rmph:"
long_options = ["Release", "Merge", "Pull", "Help"]

def print_help():
    print(f"{bcolors.HEADER}-- -- -- -- -- -- -- -- Gitenhance -- -- -- -- -- -- -- -- Help -- -- -- -- -- -- -- -- -- -- -- -- --{bcolors.ENDC}")
    print("To create a new release pass the flag -r or --Release")
    print("To merge your current changes to the destination branch execute:")
    print("gitenhance -m or --Merge <destination_branch>")
    print("To pull the latest changes from remote selected branch run the program with the -p or --Pull flag")
    print("To print this help message again, just use the -h or --Help flag.")
    print("{bcolors.HEADER}-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --{bcolors.ENDC}")

try:
    arguments, values = getopt.getopt(arguments_list, options, long_options)

    for current_argument, current_value in arguments:
        if current_argument in ("-r", "--Release"):
            print("Creating release...")
        elif current_argument in ("-m", "--Merge"):
            print("Merging code...")
        elif current_argument in ("-p", "--Pull"):
            print("Pulling latest changes...")
        elif current_argument in ("-h", "--Help"):
            print_help()

    if len(arguments) <= 0:
        print_help()

except getopt.error as err:
    print(str(err))

