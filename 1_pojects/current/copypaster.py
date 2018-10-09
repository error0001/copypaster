import os

def RunCp():
  print("***************************************")
  print("Hello! Do you want copying your folder?")
  print("Than Let's go")
  try:
    print("Write a directory - from: ")
    from_dir = input()  # get dir
    print("***************************************")
    for crtgs in os.walk(from_dir):  # Generate a cortages
	    print (crtgs)                  # and print whole
    print("***************************************")
    #print("Write a directory - to  : ")
    #to_dir = input()
    #print("Nice! Please wait, the copypaster is working...")
    
  except OSError:
    print("We are have bad news, a directory which you was writed is false...try again!")
    
if __name__ == '__main__':
  RunCp()