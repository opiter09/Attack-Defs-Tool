binn2 = open("0.bin", "rb")
bytE = binn2.read()
text = open("ff1_vivoNames.txt", "rt").read()

import os
try:
    os.mkdir("vivoFiles")
except OSError as error:
    pass
        
for i in range(116):
    oldOffset = bytE[(48 + (i * 4)):(52 + (i * 4))]
    newOffset = bytE[(52 + (i * 4)):(56 + (i * 4))]
    if (i == 115):
        newOffset = os.stat("0.bin").st_size
        newOffset = newOffset.to_bytes(4, "little")
    
    newFile = open("vivoFiles/" + text.split("\n")[i] + "_" + str(i + 1) + ".bin", "wb")
    newFile.write(bytE[int.from_bytes(oldOffset, "little"):int.from_bytes(newOffset, "little")])
    newFile.close()
    
