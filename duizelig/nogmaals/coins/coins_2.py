# name of student: Moataz Raji
# number of student: 99035655
# purpose of program: insert money and give change
# function of program: giving the accerucy of the change
# structure of program: that it's easy to read and adjust

toPay = int(float(input('Amount to pay: '))* 100) #convert it to cents in the amount you need to pay
paid = int(float(input('Paid amount: ')) * 100) #convert it to cents in the amount you paid
change = paid - toPay #variable met het van elkaar aftrekken van de bovenstende var

#the variable below ensures that it stays 0 until it counted at the end of the receipt how many coins has been used to return 
coinVijf = 0
coinDrie = 0
coinTwee = 0
coinEen = 0
coinVijftigCent = 0
coinTwintigCent = 0
coinTienCent = 0
coinVijfCent = 0
coinTweeCent = 0
coinEenCent = 0


if change > 0: #If the var is higher then zero
  coinValue = 500 #var value is 500 eu cents
  
  while change > 0 and coinValue > 0: #the beginning of the 2 values stated while there higher then zero
    nrCoinsReturned = 0#this variable is to ensure that if rused in this while that de value is back to 0
    nrCoins = change // coinValue #Devided but round up

    if nrCoins > 0: #if number of coins is higher then 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #print the returen max coin and value of the coins in cents
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #How many coins you put in.
      change -= nrCoinsReturned * coinValue #Subtract the right oppperand from the left and assign it to the return to the left

# comment on code below:
    if coinValue == 500:
        coinVijf += nrCoinsReturned#+= operator add's two values together and assign the resultant value to the variable
        coinValue = 300
    elif coinValue == 300:
        coinDrie += nrCoinsReturned
        coinValue = 200
    elif coinValue == 200:
        coinTwee += nrCoinsReturned
        coinValue = 100
    elif coinValue == 100:
        coinEen += nrCoinsReturned
        coinvalue = 50
    elif coinValue == 50:
        coinVijftigCent += nrCoinsReturned 
        coinValue = 20
    elif coinValue == 20:
        coinTwintigCent += nrCoinsReturned
        coinValue = 10
    elif coinValue == 10:
        coinTienCent += nrCoinsReturned
        coinValue = 5
    elif coinValue == 5:
        coinVijfCent += nrCoinsReturned
        coinValue = 2
    elif coinValue == 2:
        coinTweeCent += nrCoinsReturned
        coinValue = 1
    elif coinValue == 1:
        coinEenCent += nrCoinsReturned
        coinValue = 0


if change > 0: #If the change is higher then zero then return the amount of change other wise stop
    print('Change not returned: ', str(change) + ' cents')#the amount of change that has not been given back
else:
    print(coinVijf, 'of 500 eurocent. ')#The amount of coins that has been used to give the change back
    print(coinDrie, 'of 300 eurocent. ')
    print(coinTwee, 'of 200 eurocent. ')
    print(coinEen, 'of 100 eurocent. ')
    print(coinVijftigCent, 'of 50 eurocent. ')
    print(coinTwintigCent, 'of 20 eurocent. ')
    print(coinTienCent, 'of 10 eurocent. ')
    print(coinVijfCent, 'of 5 eurocent. ')
    print(coinTweeCent, 'of 2 eurocent. ')
    print(coinEenCent, 'of 1 eurocent. ')
    print('done')