# name of student: Moataz Raji
# number of student: 99035655
# purpose of program: insert money and give change
# function of program: giving the accerucy of the change
# structure of program: that it's easy to read and adjust

toPay = int(float(input('Amount to pay: '))* 100) #convert it to cents in the amount you need to pay
paid = int(float(input('Paid amount: ')) * 100) #convert it to cents in the amount you paid
change = paid - toPay #variable met het van elkaar aftrekken van de bovenstende var

if change > 0: #If the var is higher then zero
  coinValue = 50 #var value is 50
  
  while change > 0 and coinValue > 0: #the beginning of the 2 values stated while there higher then zero
    nrCoins = change // coinValue #delen maar afgerond

    if nrCoins > 0: #if number of coins is higher then 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #print the returen max coin and value of the coins in cents
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #How many coins you put in.
      change -= nrCoinsReturned * coinValue #Subtract the right oppperand from the left and assign it to the return to the left

# comment on code below: 
    if coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: #If the change is higher then zero then return the amount of change other wise stop
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')