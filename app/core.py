import subprocess
import os
import json

# create current work path using the current directory
# script_path = "{}".format(__file__)
script_path = os.getcwd()+'\\app\\file.ps1'

# run subprocess with the param to generate the file
json_result = subprocess.run(["powershell.exe", "-File", script_path, 'Security'], stdout = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines = True)

# accept the param from the form

# print(json_result.stdout)
# print(json_result.stderr)

f = open('app/sample.json', 'w')
f.write(json_result.stdout)

# with open('app/sample.json', 'w', encoding='utf-8') as f:
#     json.dump(json_result.stdout, f, ensure_ascii=False, indent=4)