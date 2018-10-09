import os     # for functions: walk, path.join, remove, path.getsize, path.get[cam]time, mkdir
import shutil # copy, move

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

def CopyPaster(inFrom, inTo):
  print("* Start copy from (" + inFrom + ")")
  print("* In the direcory (" + inTo + ")")
  os.path.join('\'' + inFrom, inTo)  # copy folders into new dir

def RunCp():
  print("*****************************************")
  print("* Hello! Do you want copying your folder?")
  print("* Than Let's go")

  try:
    #  1. show whole
    print("* Write a directory - from: ")
    dir_from = input()
    #show cortege
    ShowCrtg(dir_from, "from")        

    print("* Write a directory - to: ")
    dir_to = input()
    #show cortege
    ShowCrtg(dir_to,"to")

    # 2. Copy
    PrintFrame("Start copy catalog in to")
    CopyPaster(dir_from, dir_to)
  except OSError:
    print("We are have bad news, a directory which you was writed is false...try again!")
    
if __name__ == '__main__':
  RunCp()