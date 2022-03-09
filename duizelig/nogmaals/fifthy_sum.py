# answer = ''
# count = 0

# while answer != 'quit':
#     answer =  input('{}x gevraagd, nu dan?'.format(count))
#     count += 1
#     if count >= 1001:
#         print("done")
#         break

count = 50
totaal = count

while totaal < 1000:
    count += 1
    totaal += count
    print(totaal)