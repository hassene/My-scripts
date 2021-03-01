#====================================================================================
#FileName    : codeParser.py
#Description : Python script to analyse code
#Author      : Hassene ELHABIBI <elhabibi.hassene@gmail.com>
#date        : 28 February 2021
#====================================================================================

import os
import sys
import csv

def ask_user():
   """
   Description: this function will ask the user if he want to tray to enter a valid choise or not (Y/N).
   To conitune, please tape "q".
   """       
   check = str(input("Do You Want To Try Again  ? (Y/N): ")).lower().strip()
   try:
       if check[0] == 'y':
           return True
       elif check[0] == 'n':
           return False
       else:
           print('Invalid Input')
           return ask_user()
   except Exception as error:
       print("Please enter valid inputs")
       print(error)
       return ask_user()

def maketempfile(dir_name,base_filename,filename_suffix):
   """
   inputParm: dir_name       : directory where the file will be added
              base_filename  : the name of the file
              filename_suffix: file extension 
   Description: this function will create a temporary file.
   To conitune, please tape "q".
   """
   file_path = os.path.join(dir_name, '.'.join((base_filename, filename_suffix)))
   if not os.path.exists(file_path):
      os.mknod(file_path)
      return file_path
   else:
      return None

def maketempDir(current_path):
   """
   inputParm: Current_path => path that will parsed
   Description: this function will create a temporary directory.
   Return: dirNam => None: if the creation the directory failed
                     Path: the directory path if the successfully created
   To conitune, please tape "q".
   """    
   FolderName = 'tempDir'
   dirName = os.path.join(current_path,FolderName)
   try:
       os.makedirs(dirName)
   except OSError:
       print(("Creation of the directory %s failed" % dirName))
       dirName = None
   else:
       print ("Successfully created the directory %s " % dirName)
   return(dirName)

def SearchKeyWordInLines(file_name,keyWord):
    """ 
    inputParm: file_name : file to be parsed
                keyWord  : Key word to search for
    Description: this function will check if any line in the file contains given string.
    Return: research result ( found (True/False))
    To conitune, please tape "q".
     """
    keyWordFound = False
    with open(file_name, encoding="utf8", errors='ignore') as read_obj:
        count = 0
        # Read all lines in the file one by one
        for line in read_obj:
            count +=1
            # For each line, check if line contains the string
            if keyWord in line:
                #print(f'line {count}: {line}')
                keyWordFound = True
            else:
                continue
        return keyWordFound

def SearchKeyWordInWords(file_name,keyWord):
    """ 
    inputParm: file_name : file to be parsed
                keyWord  : Key word to search for
    Description: this function will check if any line in the file contains given string.
    Return: research result ( found (True/False))    
    """
    keyWordFound = False    
    # Open the file in read only mode
    with open(file_name, encoding="utf8", errors='ignore') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            for word in line:
                # For each line, check if line contains the string
                if keyWord in word:
                    #print(f'Word: {word}')
                    keyWordFound = True 
                else:
                    continue
        return keyWordFound                 

def parseDirectory(Current_path,keyWord):
   """
   inputParm: Current_path => path that will parsed
              keyWord      => key word to search
   Description: this function will print all folders, subfolders and filenames found in the current path
                excluding the folders, subfolders and filename which start with a dot.
   To conitune, please tape "q".
   """
   print(f"the directory which it will be parsed is {Current_path}")
   for folderName, subfolders, filenames in os.walk(Current_path):
      if str(os.path.basename(folderName)).startswith('.'):
         continue
      else:
         print("the current folder is "+ folderName)
         for subfolder in subfolders:
            if str(subfolder).startswith('.'):
               subfolders.remove(subfolder)
            else:
               print("SUBFOLDER of "+ folderName + ":" + subfolder)             
         for filename in filenames:
            if str(filename).startswith('.'):
               filenames.remove('filename')
            else: 
               print("File Inside" + folderName + ":" + filename)
               print("Search a keyword in a line")
               SearchKeyWordInLines(filename,keyWord)
               print("Search a keyword in a word")
               SearchKeyWordInWords(filename,keyWord)
               #FileObj=open(filename,'r')
               #lines = FileObj.readlines()
               #count = 0
               #for line in lines:
                    #count += 1
                    #print(f'line {count}: {line}') 

def getStaticArch(working_dir):
   """
   inputParm: Current_path => path that will parsed
   Description: this function will analyse the static architecture by:
                - Parsing the project structure
                - get all folders, subfolders and filenames found in the current path
                  excluding the folders, subfolders and filename which start with a dot.
                - write them to a cvs file
   To conitune, please tape "q".
   """
   current_path = os.getcwd()
   dir_name = maketempDir(current_path)
   if dir_name != None:
       csvFile = maketempfile(dir_name,"AnalysisResult","csv")
       if csvFile != None:
           csvFileObj = open(csvFile, 'w', newline='')
       else:
           sys.exit("Failed to create a csv file!")     
   csvWriter = csv.writer(csvFileObj)
   csvWriter.writerow(["Directory", "Folder", "fileName", "File_Sufix"])
   print(f"the directory which it will be parsed is {working_dir}")
   for folderName, subfolders, filenames in os.walk(working_dir):
      if str(os.path.basename(folderName)).startswith('.'):
         continue
      else:
         #csvWriter.writerow([folderName])
         for subfolder in subfolders:
            if str(subfolder).startswith('.'):
               subfolders.remove(subfolder)
         for filename in filenames:
            if str(filename).startswith('.'):
               filenames.remove(filename)      
      csvWriter.writerow([folderName,subfolders,filenames])
   csvFileObj.close()

def searchForData(working_dir,keyWord):
   """
   inputParm: working_dir : path that will parsed
              keyWord     : Key word to searched for
   Description: this function will search for datas by:
                - Parsing the code in the current path
                  excluding the folders, subfolders and filename which start with a dot.
                - get all datas which contain a keyword
                - write them to a cvs file
   To conitune, please tape "q".
   """
   print("Implementation of this function is ongoing !")
   current_path = os.getcwd()
   dir_name = maketempDir(current_path)
   if dir_name != None:
      csvFile = maketempfile(dir_name,"AnalysisResult","csv")
      ReadeMeFile = maketempfile(dir_name,"ReadMe","txt")
      if csvFile != None:
         if ReadeMeFile == None:
            sys.exit("Failed to create a ReadMe files")
      else:
         sys.exit("Failed to create csv file!")
   else:
      sys.exit("Failed to create temp directory!")  
   
   ReadeMeFileObj = open(ReadeMeFile,"a")
   ReadeMeFileObj.write("Search for data which contain the keyword " + keyWord + " in files under the path " + working_dir)
   ReadeMeFileObj.write("For more details, please check the file" + csvFile + "\n")
   csvFileObj = open(csvFile, 'w', newline='')
   csvWriter = csv.writer(csvFileObj)
   csvFileObj.close()
   ReadeMeFileObj.close()
    
def searchForAPI(working_dir,keyWord):
   """
   inputParm: working_dir : path that will parsed
              keyWord     : Key word to searched for
   Description: this function will search for APIs by:
                - Parsing the code in the current path
                  excluding the folders, subfolders and filename which start with a dot.
                - get all APIs which contain a keyword
                - write them to a cvs file
   To conitune, please tape "q".
   """
   current_path = os.getcwd()
   dir_name = maketempDir(current_path)
   if dir_name != None:
      csvFile = maketempfile(dir_name,"AnalysisResult","csv")
      ReadeMeFile = maketempfile(dir_name,"ReadMe","txt")
      if csvFile != None:
         if ReadeMeFile == None:
            sys.exit("Failed to create a ReadMe files")
      else:
         sys.exit("Failed to create csv file!")
   else:
      sys.exit("Failed to create temp directory!")
   ReadeMeFileObj = open(ReadeMeFile,"a")
   ReadeMeFileObj.write("Search for APIs which contain the keyword " + keyWord + " in files under the path " + working_dir)
   ReadeMeFileObj.close()
      
def searchForTypeDef(working_dir,keyWord):
   """
   inputParm: working_dir : path that will parsed
              keyWord     : Key word to searched for
   Description: this function will search for type definition by:
                - Parsing the code in the current path
                  excluding the folders, subfolders and filename which start with a dot.
                - get all types defintion which contain a keyword
                - write them to a cvs file
   To conitune, please tape "q".
   """
   current_path = os.getcwd()
   dir_name = maketempDir(current_path)
   if dir_name != None:
      csvFile = maketempfile(dir_name,"AnalysisResult","csv")
      ReadeMeFile = maketempfile(dir_name,"ReadMe","txt")
      if csvFile != None:
         if ReadeMeFile == None:
            sys.exit("Failed to create a ReadMe files")
      else:
         sys.exit("Failed to create csv file!")
   else:
      sys.exit("Failed to create temp directory!")
   ReadeMeFileObj = open(ReadeMeFile,"a")
   ReadeMeFileObj.write("Search for type definition which contain the keyword " + keyWord + " in files under the path " + working_dir)
   ReadeMeFileObj.write("For more details, please check the file" + csvFile + "\n")
   csvFileObj = open(csvFile, 'w', newline='')
   csvWriter = csv.writer(csvFileObj)
   csvFileObj.close()
   ReadeMeFileObj.close()
   
def SearchForFile(working_dir,keyWord):
   """
   inputParm: working_dir : path that will parsed
              keyWord     : Key word to searched for
   Description: this function will search for Files by:
                - Parsing the code in the current path
                  excluding the folders, subfolders and filename which start with a dot.
                - get all files name which contain a keyword
                - write them to a cvs file
   To conitune, please tape "q".
   """
   current_path = os.getcwd()
   dir_name = maketempDir(current_path)
   if dir_name != None:
      csvFile = maketempfile(dir_name,"AnalysisResult","csv")
      ReadeMeFile = maketempfile(dir_name,"ReadMe","txt")
      if csvFile != None:
         if ReadeMeFile == None:
            sys.exit("Failed to create a ReadMe files")
      else:
         sys.exit("Failed to create csv file!")
   else:
      sys.exit("Failed to create temp directory!")
   ReadeMeFileObj = open(ReadeMeFile,"a")
   ReadeMeFileObj.write("Search for files which contain the keyword " + keyWord + " under the path " + working_dir + "\n")
   csvFileObj = open(csvFile, 'w', newline='')
   csvWriter = csv.writer(csvFileObj) 
   FileFoundNb = 0
   #Parsing the code
   for folderName, subfolders, filenames in os.walk(working_dir):
      if str(os.path.basename(folderName)).startswith('.'):
         continue
      else:
         for filename in filenames:
            if str(filename).startswith('.'):
               filenames.remove(filename)
            else:
               if keyWord.lower() in filename.lower():
                  FileFoundNb +=1
                  csvWriter.writerow([folderName,filename])          
   if FileFoundNb !=0:
       ReadeMeFileObj.write(str(FileFoundNb) + " File is found, for more details please check the file" + csvFile + "\n")  
   csvFileObj.close()
   ReadeMeFileObj.close()

def SearchForEntryPoint(working_dir):
   """
   inputParm: working_dir : path that will parsed
              keyWord     : Key word to searched for
   Description: this function will search for the program entry point by:
                - Parsing the code in the current path
                  excluding the folders, subfolders and filename which start with a dot.
                - get all possible entry point in the code (search the keyword ENTRY)
                - write them to a cvs file
   To conitune, please tape "q".
   """
   print("Implementation of this function is ongoing !")
   current_path = os.getcwd()
   dir_name = maketempDir(current_path)
   if dir_name != None:
      csvFile = maketempfile(dir_name,"AnalysisResult","csv")
      ReadeMeFile = maketempfile(dir_name,"ReadMe","txt")
      if csvFile != None:
         if ReadeMeFile == None:
            sys.exit("Failed to create a ReadMe files")
      else:
         sys.exit("Failed to create csv file!")
   else:
      sys.exit("Failed to create temp directory!")  
   ReadeMeFileObj = open(ReadeMeFile,"a")
   ReadeMeFileObj.write("Search for the program entry point in files under the path " + working_dir + "\n")
   csvFileObj = open(csvFile, 'w', newline='')
   csvWriter = csv.writer(csvFileObj)
   EntryPointFoundNb = 0
   #Parsing the code
   for folderName, subfolders, filenames in os.walk(working_dir):
      if str(os.path.basename(folderName)).startswith('.'):
         continue
      else:
         for filename in filenames:
            if str(filename).startswith('.'):
               filenames.remove(filename)
            else:
               file_path = os.path.join(folderName, filename)
               with open(file_path, encoding="utf8", errors='ignore') as read_obj:
                  for line in read_obj:
                     if line.startswith('ENTRY('):
                        EntryPointFoundNb +=1
                        csvWriter.writerow([folderName,filename])
                     else:
                        continue                     
   if EntryPointFoundNb !=0:
       ReadeMeFileObj.write(str(EntryPointFoundNb) + " entry point is found, for more details please check the file" + csvFile + "\n")
   csvFileObj.close()
   ReadeMeFileObj.close()
   
            
def GetAnalysisType(working_dir):
    """
    Description: this function will get the type of analysis to be done.
    To conitune, please tape "q".
    """
    ListOfAnalysis = [1,2,3,4,5]
    while True:
        AnalysisType = int(input("""Please choose the analyse to be done
        in the following list:
        #1.Search for a data
        #2.Search for an API
        #3.Search for a type definition
        #4.Search for fileName with keyword in the title
        #5.Search for the program entry point
        Analysis Type: """))
        if AnalysisType in ListOfAnalysis:
            if AnalysisType == 1:
                print("You choosen to search for a data")
                keyWord = str(input("Please Enter the key word to search:"))
                searchForData(working_dir,keyWord)
                break
            elif AnalysisType ==2:
                print("Your choosen to search for an API")
                keyWord = str(input("Please Enter the key word to search:"))
                searchForAPI(working_dir,keyWord)                
                break
            elif AnalysisType ==3:
                print("Your choosen to search for a type definition")
                keyWord = str(input("Please Enter the key word to search:"))
                searchForTypeDef(working_dir,keyWord)                             
                break
            elif AnalysisType ==4:
                print("Your choosen to search for a file with a keyword in the filename")
                keyWord = str(input("Please Enter the key word to search:"))
                SearchForFile(working_dir,keyWord)
                break                
            else:
                print("Your choosen to search for the progrm entry point ")
                SearchForEntryPoint(working_dir)
                break
        else:
            print("Wrong Choise!")
            if  ask_user() == False:
                break
            else:
                continue

def GetActionToDo():
    """
    Description: this function will get the action to be done.
    To conitune, please tape "q".
    """
    ListOfAction = [1,2]
    while True:
        ActionType = int(input("""Please choose what you want to do
        from the following list:
        #1.Analyse the code structue
        #2.Analyse the code content

        Analysis Type: """))

        if ActionType in ListOfAction:
            if ActionType == 1:
                print("You need to analyse the code struture")
                workingDir = getWorkingDir()
                getStaticArch(workingDir)
                break
            else:
                print("Your choosen to analyse the code")
                workingDir = getWorkingDir()
                GetAnalysisType(workingDir)                
                break
        else:
            print("Wrong Choise!")
            if  ask_user() == False:
                break
            else:
                continue
            
def getWorkingDir():
    """
    Description: this function will get the working directory.
    Return: the working dircctory
    To conitune, please tape "q".
    """   
    workingDir = str(input("Please Enter the working directory:"))
    return workingDir

def main():
    GetActionToDo()

if __name__ == "__main__":
    main()
