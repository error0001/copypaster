'''
Author  : error0001
Version : 0.0.1
Name    : CopyPaster
'''
import os     # for functions: walk, path.join, remove, path.getsize, path.get[cam]time, mkdir
import shutil # copy, move

def CopyFromTo():
  mainDir = input("* Write the MAIN dir:")

  try:
    os.chdir(mainDir)
  except OSError:
    print("* Error of \"write MAIN dir\"")

  fromDir = input("* Write the FROM dir:")
  toDir = input("* Write the TO   dir:")
  try:
    shutil.copytree(fromDir,toDir)
  except OSError:
    print("* Error of \"copytree or writed dirs\"")
    

def RunCp():
  print("**********************************************************")
  print("* ________________________Hello!__________________________")
  print("* This script needed to copy, move rename folders or files")
  print("**********************************************************")
  print("* ______________________Instruction_______________________")
  print("* __________You must write key of concret task____________")
  print("* cft  - Copy From(Write E:\\folder0) To(Write C:\\pd\\ds)")
  print("* none - testing...")
  print("* none - testing...")
  print("**********************************************************")
  
  # Get key 
  inKey = input("* Change the key of work: ") 
  try:
    if inKey == 'cft':
      CopyFromTo() 
  except OSError:
    print('Error input key')

# main
if __name__ == '__main__':
  RunCp()




'''
def PrintFrame(inStr):
  print("_______________________________________")
  print("* " + inStr + " ->")

# void for show cortege
# inDir - a directory, which you are screening
def ShowCrtg(inDir, inAbout):
  PrintFrame("Start show cortege: " + inAbout)
  # !!!WARNING NOT REALIZATION TEST OF DIR
  for inCortege in os.walk(inDir): # walking in the directoryes
    print(inCortege)
  print("* End show cortege")
'''

'''
  try:
    # 1. show whole
    #print("* Write a directory - from: ")
    #dir_from = input()
    #ShowCrtg(dir_from, "from")        
    #
    #print("* Write a directory - to: ")
    #dir_to = input()
    #ShowCrtg(dir_to,"to")

    # 2. Copy
    #PrintFrame("Start copy catalog in to")
    #print("* Write the main catalog: ")
    #main_dir = input()

    #CopyPaster()#main_dir ,dir_from, dir_to) 

  
    #os.chdir('C:\\')

    #shutil.copy('C:\\spam.txt', 'C:\\delicious')
  except OSError:
    print("We are have bad news, a directory which you was writed is false...try again!")
  '''  