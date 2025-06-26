def median(input):
  list.sort(input)
  middleIndex = len(input)//2

  if(len(input) % 2 == 0):
    medianValue = (input[middleIndex] + input[middleIndex - 1]) / 2
  else:
    medianValue = input[middleIndex]

  return medianValue

my_list = [0, 1, 2, 3, 4, 5]
print(median(my_list))

