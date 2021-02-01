import numpy as np

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

feat = {}
with open("mfcc.txt") as fr:
  while True:
    one = read_one_matrix(fr)
    if not one:
      break
    else:
      feat[one[0]] = one[1]

print(feat)