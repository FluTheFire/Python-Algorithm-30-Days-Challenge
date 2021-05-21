def arrangeCoins(n):
  current = n
  row = 1
  
  while current > 0:
    current = current - row
    if current < 0:
      break
    else:
      row = row + 1
  
  return row - 1

print(arrangeCoins(5))