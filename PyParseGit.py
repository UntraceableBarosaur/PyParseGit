# Owen Cody, 3-09-2018, Python

# Overview :
# PyParseGit was created as a GUI program to parse a CSV file for an
# entry and print the entry out to the GUI in a simple fashion

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#   INITIAL APPLICATION SETUP:

# Importing our necessary packages
from tkinter import *
from tkinter import ttk
import csv
import os
import sys

# Insert the path to the CSV file here
global csvPathVar
csvPathVar = 'Stored_Data.csv'

#Git VARIABLES
branch      =   "UntraceableBarosaur/PyParseGit.git"
PyParsePath  =  os.path.dirname(os.path.realpath("PyParseGit.py"))
pull        =   "git pull https://github.com/"

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#    GIT PULL FUNCTION:

# Do a git pull on startup
gitPull(branch,PyParsePath)

def gitPull(branch,PyParsePath):
    os.chdir(PyParsePath) # Specifying the path where the cloned project has to be copied
    try:
        os.system(pull+branch) # Pulling
    except RuntimeError:
        print("Pulling Failed")
    print("Pulling Successful")

def gitUpdate(*args):
    try:
        gitPull(branch,PyParsePath)
    except RuntimeError:
        returnTerm.set("An error occured during the git pull")
    returnTerm.set("The git pull has been successful")

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#    CSV SEARCHING FUNCTION:

#Define our CSV search function
def searchCSV(*args):

    # Formats our output string variable to pool text results
    saveTerm = "['What','When','Where','Who']\n"
    # Open RomanTerms.csv using the CSV module and sets to read mode
    with open(csvPathVar, 'r') as Terms:
        # Set the csv to the matrix variable reader
        reader = csv.reader(Terms)
        # Get the search term from the entry field
        checkinput = str(searchTerm.get())

        # Incriment through the Rows
        for row in reader:
            # Incriment through the fields in each row
            for field in row:
                # Check each field for the string from the entry field
                if field == checkinput:
                    # If matching field is found, add it to our output variable
                    # Also add a newline between responses
                    saveTerm = saveTerm + "\n" + str(row)

        # Check to see if any results were found
        if saveTerm == "['What','When','Where','Who']\n":
            # If not set the saved term to No Search Results Found
            saveTerm = "No Search Results Found"
        # Set the string returnTerm to the output variable saveTerm
        returnTerm.set(saveTerm)

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#    GUI SETUP STAGE:


# Initialize funtion TK() as root instead of using Tk(title("sample"))
root = Tk()
# Title the window
root.title("PyParseTGT")

# Setup the basic window
mainframe = ttk.Frame(root, padding="3 3 12 12")
# Set numbers of Rows and Columns
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# Set organizational weights
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#    CREATE GUI DATA STORAGE VARIABLES:


# Setup the searchTerm variable to read from the entry
searchTerm = StringVar()
# Setup the returnTerm variable to give the results to the Label
returnTerm = StringVar()

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#    CONFIGURE THE WIDGETS:


# Setup the Entry field as 25 characters long, and write to searchTerm
searchTerm_entry = ttk.Entry(mainframe, width=25, textvariable=searchTerm)
# Also stick the field to the window's North West and East sides
searchTerm_entry.grid(column=1, row=1, sticky=(N, W, E))

# Setup the search Button and have it run the function searchCSV when clicked
ttk.Button(mainframe, text="Search", command=searchCSV).grid(column=2, row=1, sticky=(N, W, E))

# Setup the git pull Button and have it run the function searchCSV when clicked
ttk.Button(mainframe, text="Github Pull", command=gitUpdate).grid(column=2, row=2, sticky=(E, S))

# Setup the data return Label on row 2 and stick to the window's bottom
ttk.Label(mainframe, textvariable=returnTerm).grid(column=1, row=2, sticky=(W, S, E))

"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#    FINISHING TOUCHES:


# Adds padding between and on the sides of the modules
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# Starts the cursor in the search field
searchTerm_entry.focus()

# Allows for the "Enter" key to run the search function
root.bind('<Return>', searchCSV)

# Enter the event loop
root.mainloop()
