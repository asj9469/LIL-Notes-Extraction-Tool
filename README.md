# Linked In Learning Annotation Extraction Tool 
<img align="right" src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">

## Brief Description:
A python-based tool that extracts and organizes annotations from [Linked In Learning (LIL)](https://www.linkedin.com/learning) notebooks in a more readable format (.txt, .md, .docx).

## Background:
- The exported notebook from LIL includes formatting and details such as time stamps of the location of which the note was taken.
- Although the included details may be helpful when referring back to the video, it adds unnecessary challenges to students who try to study with the annotations only and/or merge them with other study materials

## What Does This Tool Do?
- Takes in the original .txt file downloaded directly from [Linked In Learning](https://www.linkedin.com/learning) as an input
- Provides user the option to pick from different output formats (.txt, .md, .docx)
- "Cleans up" the original text file into a more readable and organized structure
- Filters out necessary information (course title, chapter, video title, and annotations) and adds to the new output file
- Creates a new file if user chooses to create a file that does not previously exist / replaces the file if it exists

\* _the notes' organization is based on my personal note taking style (including the color in the .docx file), so feel free to edit the code and customize it!_

## How Do I Run This???
1. Download the zip file or clone the repo
    - Click the green button that says "<> Code" to view these download options
    - Extract the folder if you downloaded the zip file
2. If you are on Windows:
    - run the .exe file included in the 
3. If you're on mac and have python and an IDE (e.g. VS Code)
    - Open the extracted folder on your IDE of choice
    - Navigate to the "functions.py" file and execute the code

## Demo
### Option 1: Export as Text File (.txt)

https://user-images.githubusercontent.com/79544046/229377404-c2f73f66-bd16-44b2-8587-feee5b5cf438.mp4

### Option 2: Export as Mardown File (.md)

https://user-images.githubusercontent.com/79544046/229403567-a87671b0-5c47-42d3-b030-e9574b61df0a.mp4

### Option 3: Export as Microsoft Word Document File (.docx)

https://user-images.githubusercontent.com/79544046/229377422-d94bf5d8-50f7-4682-b8a7-96ee06a10020.mp4

