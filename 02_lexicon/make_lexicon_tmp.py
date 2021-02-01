words = {}
with open("wordslist.txt") as fr:
  words = dict((x.strip(),None) for x in fr.readlines())

with open("pronunciation.txt") as fr:
  while True:
    line = fr.readline()
    if line == "":
      break
    line = line.strip().split(maxsplit=1)
    if line[0] in words.keys():
      words[line[0]] = line[1]

with open("lexicon_tmp.txt","w"):pass
with open("lexicon_tmp.txt","a") as fa:
  for key,value in words.items():
    if value:
      fa.write( key + " " + value + "\n" )


