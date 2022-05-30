from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

import os

gauth = GoogleAuth()
print('Linha 1')
gauth.LocalWebserverAuth()
print('Linha 2')
drive = GoogleDrive(gauth)
print('linha 3')
path = r"Drive"
print('Linha 4')
print('antes do for')

for x in os.listdir(path):
    f = drive.CreateFile({'title': x})
    f.SetContentFile(os.path.join(path, x))
    f.Upload()
    f = None
