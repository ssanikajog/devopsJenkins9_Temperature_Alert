import sys
if len(sys.argv) == 2:
  temp = int(sys.argv[1])

else:
  temp = 45

if temp < 15:
  print("Cold")
elif temp > 15 and temp < 30:
  print("Normal")
if temp > 30:
  print("Hot")
