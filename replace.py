import os
mon_fichier = open("C:/T0.csv", "r")
new_file = open("C:/T1.csv", "w")
for line in mon_fichier:
	new_line = ""
	new_line = line.replace("?","")
	new_file.write(new_line)
mon_fichier.close()
new_file.close()
