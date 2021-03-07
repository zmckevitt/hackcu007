import sys
import subprocess

uname = sys.argv[1]
pword = sys.argv[2]
time = sys.argv[3]

output = "{Uname: " + uname + ", Pword: " + pword + ", time: " + time + "}"

string_out = uname + "\n" + pword + "\n" + str(time) + "\n"
f = open("txt_files/testfile.txt", "w")
f.write(string_out)
f.close()
print(output)