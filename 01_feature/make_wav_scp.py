import os,glob

PWD = os.path.abspath(".")
result = {}
for filePath in glob.glob(os.path.join(PWD,"*.wav")):
  ID = os.path.basename(filePath).split(".")[0]
  result[ID] = filePath

with open("wav.scp","w"):pass
with open("wav.scp","a") as fa:
  for key,value in result.items():
    fa.write( key + " " + value + "\n" )
