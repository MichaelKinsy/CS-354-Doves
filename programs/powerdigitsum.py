def powerdigitsum(int base, int exp):
  result = math.pow(base, exp)
  sum = 0
  digit = 0
  while(result != 0):
    digit = result%10
    sum += digit
    result = result/10
  return sum
