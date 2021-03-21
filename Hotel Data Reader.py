#importing csv module and reader function in order to facilitate csv file reading
import csv
from csv import reader

#user input asking begins here

#Getting user generated input for state,cost or ratings, and the operation whether highest,cheapest or average and displaying invalid input until correct data is entered.
#Also doing error checking with help of while loop to check if correct data is entered


while True:     #first while loop for asking state from the user 
	state_inp=input("What is the state: ")                  #state_inp for user input of value of state
	if state_inp.lower() in ('maharashtra','karnataka','tamilnadu'):                        #checking if correct state is entered after turning it it lowercase to prevent exceptions
		break                                           #exiting loop if correct state is entered
	print("!! INVALID INPUT!!")                             #printing error message
while True:     #second while loop asking user for cost or ratings
	cost_rating=input("Cost or Rating: ")                   #asking user cost or ratings
	if cost_rating.lower() in ('cost','rating'):            #checking if user entered information is valid or not after turning it into lower case so that exceptions do not happen
		break                                           #exiting while loop if correct information is entered
	print("!! INVALID INPUT !!")                            #printing error message
while True:     #third while loop asking user for desired operation of highest,cheapest or average
	oper_inp=input('Operation:')                            #asking user for his/her desired operation
	if oper_inp.lower() in ('highest','cheapest','average'):#checking if user entered information is correct after turning into lower case to prevent exceptions
		break                                           #exiting while loop if correct information is entered
	print("!! INVALID INPUT!!")                             #printing error message




state=state_inp.capitalize()                                    #we are capitalizing variable received from state because in our csv file the data is of first letter capital 
cost_rating_lc=cost_rating.lower()                              #cost or rating variable is turned to lower case to facilitate checking what user has input
oper= oper_inp.lower()                                          #same is done for operation input

#csv reading begins here
#we are now loading our csv file into the program and then opening it and making a nested list /list_all/ to store complete csv information

with open('hotels.csv','r') as read_obj:                        #loading hotel.csv into program
	csv_reader = reader(read_obj)                           #csv_reader will help us create nested list /list_all/
	list_all= list(csv_reader)                              #list_all stores complete csv information

#list_all processing begins here

cnt=1                                                           #this variable help in stopping the execution of following while loop by keeping count                                                         
cost=[]
rating=[]                                                       #creating an empty list for rating[] which will be appended later
hotel_code=[]
def cal(count,str):                                             #this function cal will create individual lists out of the nested lists using while loop. This function will be called later
                                                                #it calls the state input by user
        x=(len(list_all))                                       #x stores length of the nested list  
        while True:                                             #while loop for creating separate lists out of the nested list
                if list_all[count][2]== str:                    #in following lines of codes rating,hotel_code and cost which are empty lists are appended by relevant state's data 
                        hotel_code.append(list_all[count][1])
                        cost.append(list_all[count][3])
                        rating.append(list_all[count][4])
                count+=1
                if count+1>x:
                        break
cal(cnt,state)                                                  #cal is now called with cnt and state as parameters
cost=list(map(float,cost))                                      #turning list cost into integer list with help of map function
rating=list(map(float,rating))                                  #turning list rating into integer list with help of map function
minpos =0                                                       #variable initialization to store position of cheapest cost or rating in the list
maxpos=1                                                        #variable initializatoin to store postion of highest cost or rating in the list
def average(lst1):                                              #this function is for calcuating average
        avvg =sum(lst1)/len(lst1)
        return round(avvg,1)                                    #returning average so that it can be printed later
def cheapest(lst2):                                             #function calculating the index at which cheapest rating or cost is present 
        return lst2.index(min(lst2))                            #return the index at which the cheapest rating/cost is present
def highest (lst3):                                             #function calculating the index at which highest rating or cost is present
        return lst3.index(max(lst3))                            #return the index at which the highest rating/cost is present
        
#checking if average is entered as operation by user if yes then check cost or rating and then print relevant information

if oper == 'average':                                           
        if cost_rating_lc == 'cost':                            #if cost is entered parse cost through average function otherwise we parse rating through it
                 avg = average(cost)
                 print("Average cost of Hotel in {} is Rs.{}".format(state,avg))                        #printing relevant output using format() function 
        else:
                avg=average(rating)
                print("Average rating of Hotel in {} is {}".format(state,avg))                          #printing relevant output using format() function 

#checking if cheapest is entered as operation by user if yes then check cost or rating and then print relevant information

if oper== 'cheapest':
        if cost_rating_lc=='cost':                              #if cost is entered we will parse cost through cheapest otherwise parse rating through cheapest function
                
                minpos=cheapest(cost)                           #get returned value of index from cheapest function we use this value to print relevant output
                print("Hotel with cheapest price in {} is {} with price {}".format(state,hotel_code[minpos],cost[minpos]))              #printing relevant output using format() function 
        else:
                minpos=cheapest(rating)                         #get returned value of index from cheapest function we use this value to print relevant output
                print ("Hotel with lowest rating in {} is {} with rating {}".format(state,hotel_code[minpos],rating[minpos]))           #printing relevant output using format() function 

#checking if  highest is entered as operation by user if yes then check cost or rating and then print relevant information

if oper=="highest":
        if cost_rating_lc=='cost':                              #if cost is entered we will parse cost through highest otherwise parse rating through highest function
                maxpos=highest(cost)                            #get returned value of index from highest function we use this value to print relevant output
                print ("Hotel with highest price in {} is {} with price {}".format(state,hotel_code[maxpos],cost[maxpos]))#printing relevant output using format() function 
        else:
                maxpos=highest(rating)                          #get returned value of index from highest function we use this value to print relevant output
                print("Hotel with highest rating in {} is {} with price {}".format(state,hotel_code[maxpos],rating[maxpos]))            #printing relevant output using format() function 
print("Thanks for running the program")                         #printing thankyou message
print("**************PROGRAM MADE BY RAHUL SHUKLA FOR INKOOP************** \nEmail: shuklarahul834@gmail.com ")#Printing build data for convenience

                

        

	




