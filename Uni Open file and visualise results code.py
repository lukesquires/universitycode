# So i can use time.sleep
import time

# A function in order for the code to be able to loop
def list_():
    menu = int(input("""***************************************************
Welcome, Please select an option from the list below
1. Visualisation of the text file
2. Add a number to the text file
3. Find the mean and median of the numbers within the text file
***************************************************
"""))
    print ("Loading...")
    time.sleep(2)
    print (" ")

# Option 1 - Visualisation of the text file
    if menu == 1:
        with open('datafile.txt', 'r') as file:
            contents = file.read()
            print(contents)
            exit_question = int(input("""
Choose one of the following:
1.Return to menu
2.Exit Program
"""))

# Option to return to the menu
            if exit_question == 1:
                print (" ")
                list_()
                
# Option to end the code            
            elif exit_question == 2:
                print (" ")
                print ("Thankyou for using the statistic program")

# Option 2 - Adding a number to the list    
    elif menu == 2:
        with open('datafile.txt', 'a') as file:
            add = input("What number would you like to add to the list? ")
            file.write('\n' + add)
            exit_question = int(input("""
Choose one of the following:
1.Return to menu
2.Exit Program
"""))

# Option to return to the menu
            if exit_question == 1:
                print (" ")
                list_()
                
# Option to end the code            
            elif exit_question == 2:
                print (" ")
                print ("Thankyou for using the statistic program")

# Option 3 - Finding the range and mean of the list of numbers    
    elif menu == 3:
        with open('datafile.txt', 'r') as file:
            mean = [float(line.rstrip()) for line in file]

        biggest = min(mean)
        smallest = max(mean)
        print("The range of the numbers in this list is", smallest - biggest)
        print (" ")
        print("The Mean of the numbers in this list is", sum(mean)/len(mean))
        exit_question = int(input("""
Choose one of the following:
1.Return to menu
2.Exit Program
"""))

# Option to return to the menu
        if exit_question == 1:
            print (" ")
            list_()
                
# Option to end the code            
        elif exit_question == 2:
            print (" ")
            print ("Thankyou for using the statistic program")
    
    else:
        list_()
# Recalling the function 
list_()