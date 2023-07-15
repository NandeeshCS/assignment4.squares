#Sample List: [4, 5, 2, 9]
#Square the elements of the list:
#[16, 25, 4, 81]
def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements of the said list using map():")
print(list(result))