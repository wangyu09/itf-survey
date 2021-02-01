import numpy as np
from collections import namedtuple 

def read_one_matrix(fr):

  header = fr.readline()
  if header == "":
    return False
  header = header.strip()
  assert header.endswith("[")
  ID = header.split()[0]
  matrix = []
  while True:
    line = fr.readline().strip().split()    
    if line[-1] == "]":
      matrix.append( line[:-1] )
      break
    else:
      matrix.append( line )
  
  return ID, np.array(matrix,dtype="float32")

def read_one_vector(fr):

  line = fr.readline()
  if line == "":
    return False
  line = line.strip().split()
  
  return line[0],np.array(line[1:],dtype="int32")

feat = {}
with open("fbank.txt") as fr:
  while True:
    one = read_one_matrix(fr)
    if not one:
      break
    else:
      feat[one[0]] = one[1]

ali = {}
with open("pdf_ali.txt") as fr:
  while True:
    one = read_one_vector(fr)
    if not one:
      break
    else:
      ali[one[0]] = one[1]

dataset = []
T = namedtuple("Frame",["fbank","pdfID"])
for uttID in feat.keys():
  if uttID in ali.keys():
    uttFeat = feat[uttID]
    uttAli = ali[uttID]
    assert len(uttFeat) == len(uttAli), "Frames does not match!"
    for f,a in zip(uttFeat,uttAli):
      dataset.append( T(f,a))

print(len(dataset))
print(dataset[0])

