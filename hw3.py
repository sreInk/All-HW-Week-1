import os
import platform

def shutdown_pc():
  
    if platform.system() == "Windows":
        os.system("shutdown /s /t 1")  
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        os.system("shutdown now") 
    else:
        print("Unsupported operating system.")

shutdown_pc()
