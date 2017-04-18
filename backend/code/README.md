# FPS_utep-sp17
UTEP CS4311 Spring 2017 capstone: FPS
@author Mahdokht (Michelle) Afravi
@modified 04-18 T

## Organization and Delegation
Each directory is the directory on which you will be working, i.e., they are labeled by YOUR NAME. Please DO NOT work on another directory within your branch (see below).

## Instructions for Development
### 1. Installation
Download Anaconda for your machine to install the package for Python development. Choose the Python 3.6 Download for your machine:
  - https://www.continuum.io/downloads
### 2. Development
The following sections describe how to develop on your branch of the Git repository (General). The next section (Deadlines) outlines by which days your tasks must be completed so that I may integrate. The last section (Git Help) offers solutions to handle Git operations.
#### General
After installing, you can develop in the command line (iPython console) or develop in the GUI version (Spyder). Note: each class you work on has the documentation (comments/protocols) for classes and methods.
##### Documentation
Please, GET INTO THE HABIT OF COMMENTING and using TODOS or FIXMES. This will help GREATLY (not just me, but also yourself!). <br />
Use the following design for your documentation in Python:
  - type '#' to comment a single line
  - type '"""' around a block of code to comment it out <br />
At the top of every file, please note that you have modified the file with the date and your name in this design:
  - """ <br />
       ... <br />
       @modified MM-DD Weekday by <your_name> <br />
	   Short description of what was modified. <br />
    """ <br />
For me on this file (if it had been written in a Python file), this would look like:
  - """ <br />
       ... <br />
	   @modified 04-18 T by mafravi <br />
	   Added delegations and schedules. <br />
    """
##### Keep Working
It's almost over guys, let's end strong by getting this project done for the team!
### What to Submit
In every commit, submit all of your work, including your tests (this could be in a .txt document or even a Python unit test file). I need to know how you tested your work.
### Deadlines (by midnight)
Please adhere to these deadlines to allow time for me to merge everything together. DO NOT EVER MERGE.
#### 05/03 Wednesday
Integration. Delegations of work TBD through our weekly meetings.
#### 04/28 Friday
By this day, all of your classes fully implemented and tested. Message me which ones you have submitted to your branch so that I may check.
#### 04/24 Monday
By this day, have at least two (2) classes fully implemented and tested. Message me which ones you have submitted to your branch so that I may check.
#### 04/21 Friday
By this day, have at least one (1) class fully implemented and tested. Message me which ones you have submitted to your branch so that I may check.
#### 04/18 Tuesday
By this day, clone and create your branches in your system. Message me directly for help!
### Git Help
#### Cloning
You should have already received a link to add this repository to your Git account as a Collaborator (it's the only way you can see this page). Clone to your system by:
  - navigating to the directory you want to develop within in your command line (for me, it is in the path: C:\Users\mmafr\Documents\Skool\)
  - typing in the command line: git clone https://github.com/mahdafr/legac_fps.git
  - navigating next to this directory in the command line (for me, it is: C:\Users\mmafr\Documents\Skool\legac_fps)
  - you should see everything in the origin branch now (everything that is on the website)
#### Branches
Create a branch FROM this repository. You will name it <your_first_name> or <your_utep_username> (e.g., Michelle creates a branch called michelle OR mafravi). Do this on the command line by:
  - navigating to the legac_fps directory in your command line (for me, it is in the path: C:\Users\mmafr\Documents\Skool\legac_fps)
  - typing in the command line: git checkout -b <your_name> (for me, this could be: git checkout -b michelle OR git checkout -b mafravi)
  - copying everything into your branch by typing in the command line: git pull
#### Committing and Pushing
Please get into the habit of doing this after every day of your work to not only track your progress, but also have a backup baseline for you to refer. <br />
NEVER MERGE - this will be my job to handle merges and their conflicts (if any). The only commands you need to worry about for your development are:
  - git status
    This will tell you which files you have modified that ARE NOT already committed to the repository. Do this before 'git add .' to be sure of everything.
  - git add .
    This will add all your edited files to be ready for pushing to the git repository. Do this before 'git commit -m "..."'.
  - git commit -m "<useful message here>"
    This will collect all your modifications to be added to your branch on the git repository. Make sure of this by reading the next line after hitting ENTER, it should say something like "on git branch origin/<your_name>" or so. Do this before 'git push'.
  - git push
    This will collect everything to be added to the git repository on your branch only. Do this last. You have submitted your work to your branch for me to check out.
If you need anything else, ASK ME. I am here to help with this assignment!