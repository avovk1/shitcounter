out = ""
with open("data.txt", "rt", encoding="UTF-8") as file:
 for line in file.readlines():
  line = line.split(";")
  out = out + line[0] + ";" + str(int(line[1][:-1])+8600) + "\n"
with open("data.txt", "wt", encoding="UTF-8") as file:
 file.write(out)
