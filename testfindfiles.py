import pathlib
import os

# I want to get all file extensions of '/home/dhjensen/OneDrive/OldHDD' files in all subfiles

OLDHDD_FOLDER = '/home/dhjensen/OneDrive/OldHDD'
DOKS_FOLDER = '/home/dhjensen/OneDrive/OldHDD/Doks'

def get_files_list(path: str):
    files_return = []
    for root, directories, files in os.walk(path):
        for file in files:
            files_return.append(os.path.join(root, file))
    return files_return

EXT_LIST = ['.db', '.mdf', '.sql', '.cfg', '.sch', '.index',
            '.cron', '.asm', '.properties', '.asx', '.txt',
            '.csr', '.SQL', '.vbs', '.csv', '.CSV', '.asp',
            '.alisp', '.pl', '.css', '.php', '.sh', '.pjt',
            '.ini', '.bat', '.js']

files = []
suffix = []
for file in get_files_list(DOKS_FOLDER):
    suf = pathlib.Path(file).suffix
    suffix.append(suf)
    if suf in EXT_LIST:
        files.append(file)

unique = list(set(suffix))

#for ext in unique:
#    print(ext)

for file in files:
    print(file)