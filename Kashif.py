import os,platform
os.system('git pull')
 
kashif=platform.architecture()[0]
if kashif=="32bit":
    print('Sorry 32 Bit Not Supported...')
elif kashif=="64bit":
    __import__("Kashif64")
