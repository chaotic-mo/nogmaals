#  nums = [1, 2, 3, 4, 5, 6]
#  i_nums = iter(nums)

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break

answer = ''
count = 0

while answer != 'quit':
    answer =  input('{}x gevraagd, nu dan?'.format(count))
    count += 1
