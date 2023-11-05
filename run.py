import os
os.system("pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests")
try:
    import XYZ
except:
    exit("Your phone is not 64 bit.")
