import os
import argparse

parser = argparse.ArgumentParser(description='Sign all files in one command!')
parser.add_argument('p', help='the directory you want to sign')
args = parser.parse_args()

path = args.p
stuff = os.listdir(path)
files = []

for i in stuff:
    if os.path.isfile(path+i):
        files.append(path+i)

print(path)
print("Going to sign all these files:\n")
for i in files:
    print(i)
print("\nIs it ok? y/N")
ans = input()
if str(ans).lower() == "y":
    for i in files:
        if os.path.isfile(i):
            print("signing {0}".format(i))
            os.system("gpg --detach-sign '{0}'".format(i))
else:
    print("Goodbye")
