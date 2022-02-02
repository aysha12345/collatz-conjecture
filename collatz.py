import sys

def TNPO(n):
  global sum
  global currentNumber 
  
  if n not in knownNumbers:
    if n == 1:
      sum += 1
      knownNumbers[currentNumber] = sum
      return True
    elif(n % 2) == 0:
      sum += 1
      TNPO(n/2)
    else:
      sum += 1
      TNPO(3*n+1)
  else:
    sum += knownNumbers[n]
    knownNumbers[currentNumber] = sum

s,f=sys.stdin.readline().split()
s=int(s)
f=int(f)
knownNumbers = {}

for i in range(s, f+1):
  sum = 0
  currentNumber = i
  TNPO(i)

print(max(knownNumbers.values()))






#s and f are now integers containing the start and finish values

 #prints the number of runs, change this to be your output
