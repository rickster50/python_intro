tickets = input("How many tickets would you like?")
if tickets.isdigit(): #I put this here because the program gives an error message if something that isn't a number is entered
    number_of_tickets = int(tickets) + 1 #+1 because range stop number is exclusive so the loop finishes at stop - 1  
    for count in range(1,number_of_tickets): #default step is one
        print("Ticket Number "+str(count)+ " Booked")
else: 
    print(tickets + " is not a number")

