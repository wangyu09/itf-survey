import os

assert os.path.isfile("lexiconp.txt"),"Please generate the lexicon.txt before this step!"
assert os.path.isfile("silence_phones.txt"),"Please generate the silence_phones.txt before this step!"

phones = [] 
with open("lexiconp.txt") as fr:
  while True:
    line = fr.readline()
    if line == "":
      break
    line = line.strip().split()
    phones.extend( line[2:] )
phones = sorted(list(set(phones)))

with open("silence_phones.txt") as fr:
  lines = fr.readlines()
  silence_phones = list( map(lambda x:x.strip(), lines) )

with open("nonsilence_phones.txt","w"): pass
with open("nonsilence_phones.txt","a") as fa:
  for phone in phones:
    if phone not in silence_phones:
      fa.write( phone + "\n" )

