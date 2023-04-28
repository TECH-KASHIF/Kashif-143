#coding=utf-8
import os,sys,subprocess
py_ver = subprocess.check_output('python -V',shell=True)
if '3.10' in str(py_ver):
    os.system('pkg upgrade python -y')
    os.system('python Kashif.py')
else:pass
current_os=subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(current_os):
    if not os.path.isfile('Kashif-143'):
        os.system('curl -L https://github.com/TECH-KASHIF/Kashif-143/blob/main/Kashif64?raw=true > Kashif64.py')
        os.system('chmod 777 Kashif-143')
        os.system('./Kashif64')
    else:
        os.system('./Kashif64')
elif 'arm' in str(current_os):
    if not os.path.isfile('Kashif64'):
        os.system('curl -L https://github.com/TECH-KASHIF/Kashif-143/blob/main/Kashif64.cpython-311.so?raw=true > Kashif64')
        os.system('chmod 777 Kashif-143')
        os.system('./Kashif64')
    else:
        os.system('./Kashif64')
else:
    print('\n  Unknown device, aarch or os found, contact author.')
    os.sys.exit()
