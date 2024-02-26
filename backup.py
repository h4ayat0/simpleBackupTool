from os import mkdir
from shutil import copytree
from datetime import datetime

backupFolder = 'C:/Users/Hayato/Downloads/t'
saveFolder = 'C:/Users/Hayato/Downloads/t/teste dummy'

backup = datetime.today().strftime('%Y-%m-%d %H-%M-%S')
backup = f'{backupFolder}/{backup}'
print(backup)

copytree(saveFolder, backup)
