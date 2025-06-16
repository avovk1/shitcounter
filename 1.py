from time import time
from subprocess import run
from os import name
structure = "Чекаю {} день {}\n"
out = ""
t = int(time())
with open("data.txt", "rt", encoding="UTF-8") as file:
 for entry in file.readlines():
  entry = entry.replace("\n", "").split(";")
  out = out+structure.format(entry[0], (t-int(entry[1]))//86400)
print(out)
if name == "posix":
 os = run(["uname", "-o"], capture_output=True, text=True).stdout.replace("\n", "")
 if os == "GNU/Linux":
  try:
   run("echo \"{}\" | xclip -sel clip".format(out), shell=True)
  except:
   print("Install xclip package, or tell dev to implement another.")
   exit(1)
  print("Copied into clipboard!")
 elif os == "Android":
  try:
   run("echo \"{}\" | termux-clipboard-set".format(out), shell=True)
  except:
   print("Install termux-api package")
   exit(1)
  print("Copied into clipboard!")
 else:
  print("Unsupported POSIX-like OS (termorairly). This is output of \"uname -o\" - {}. Send it to dev to fix.".format(os))
  exit(1)
elif name == "nt":
 run("echo \"{}\" | clip".format(out), shell=True)
 print("Copied into clipboard!")
else:
 print("Unsupported kernel (temporairly). This is output of \"os.name\" - {}. Send it to dev to fix.".format(name))
 exit(1)
