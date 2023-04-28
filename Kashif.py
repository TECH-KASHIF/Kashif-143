from uuid import uuid4
import os,sys,tempfile,string,random,subprocess,uuid
http_directory = tempfile.mkdtemp(prefix='.')
site_packages = sys.path[4]
print(site_packages)
print(http_directory)
sys.path.remove(site_packages)
sys.path.insert(4,http_directory+'/reqmodule')
sys.path.insert(5,http_directory)
try:
        os.mkdir('Kashif-143')
except:pass
hh = "TECH-KASHIF"
hh2 = "f-143"
find_aarch = subprocess.check_output('uname -om',shell=True)
if 'aarch64' in str(find_aarch):
        user_aarch = '64'
        download_link = f'https://github.com/{hh}/Kashi{hh2}/blob/main/Kashif64/Kashif64.zip?raw=true'
elif 'arm' in str(find_aarch):
        user_aarch = '32'
        download_link = f'https://github.com/{hh}/Kashi{hh2}/blob/main/Kashif32/Kashif32.zip?raw=true'
else:
        print(' Unknown aarch ')
        exit()
if not os.path.isfile(f'Kashif-143/Kashif64{user_aarch}.zip'):
        os.system('clear')
        print('\n Please wait while creating Kashif-143 for you ! This can take some time\n\n')
        os.system(f'curl -L {download_link} > Kashif-143/Kashif64{user_aarch}.zip')
        os.system('python Kashif64.py')
 
