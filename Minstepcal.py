
class minstepcal:                       #class name
    def makeProductOne(arr, N):         #making function that will return number of steps
        step=0                          #variable initialization to store the count of number of steps
        neg=0                           #negative counter to store value of negative counter in the array
        zcount=0                        #variable initialization to store value of zero count in the array
        for num in arr:                 #for loop to parse all the elements of the array through it and get the step count
            if num<=0:              
                neg+=1
        for num in arr:
                if num==0 :
                    step+=1
                    zcount+=1
                    num=num+1
                elif num<-1:
                    step=step-num-1
                elif num>1:
                    step=step+num-1
        if neg%2==0:                    #now we add nothing to step if number of negative numbers are odd 
            return step
        if neg%2!=0 and zcount%2!=0:    #adding one to step counter in case negative number are odd and there is a zero as it can easily become -1 to turn product into -1
            return step+1  
        if neg%2!=0 and zcount==0:      #adding step counter by 2 in case there is no zero present and negative numbers are odd because then we will need to turn -1 to 1 which will take two steps
            
            return step+2
    print("This program prints the number of steps required to make the product of the input array equal to 1 ")
    n= int(input("Please enter number of elements in the array: "))#asking user for number of elements in the array
    lst=[]
    for i in range(0,n):
        ele= int(input("Please enter number {}: ".format(i+1)))    #asking user for all the elements in the array by using for loop
        lst.append(ele)
    print("Input array was {}".format(lst))                        #Printing user inputted array for  reference 
    abc=makeProductOne(lst,n)                                      #abc is initalized and it store the answer of number of steps returned by makeProductOne() 
    print("The minimum number of steps required to make the product of elements in the input array equal to 1 is {}".format(abc)) #Printing the answer of the program
    print("Thanks for running the program\n********RAHUL SHUKLA********")
    
    
        
