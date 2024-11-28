'''
. Real-World Python Dictionary Applications
Objective: The aim of this assignment is to reinforce your understanding and application of Python dictionaries, nested collections, 
and dictionary methods.

Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. 
Your task is to update this menu based on given instructions

Problem Statement: Given the initial menu:'''
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

#  Add a new category called "Beverages" with at least two items.
restaurant_menu['Beverages'] = {"Coke": 3.50, "Juice":4.25}
print(restaurant_menu)
# - Update the price of "Steak" to 17.99.
# restaurant_menu.update({"Main Course":{"Steak": 17.99, "Salmon": 13.99}})
restaurant_menu["Main Course"]["Steak"] = 17.99
print(restaurant_menu)
# - Remove "Bruschetta" from "Starters". 
del restaurant_menu["Starters"]["Bruschetta"]
print(restaurant_menu)

'''
2. Python Programming Challenges for Customer Service Data Handling
Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and 
loops by creating a system to track customer service tickets.

Problem Statement: Develop a program that:

Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry.

Example ticket structure:

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}
'''
service_tickets = {
    "Ticket1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

count = 3
def open_ticket(customer, issue, status):
    global count
    service_tickets["Ticket" + str(count)] = {"Customer": customer, "Issue": issue, "Status": status}
    count = count + 1
    print(service_tickets) 
    # (f"Ticket{count-1} added succesfully") 

def update_ticket():
    ticket_number = input("What is the ticket number?")
    service_tickets["Ticket" + ticket_number]["Status"] = input("Enter open/closed. ")
    print(service_tickets)
    
"Display all tickets or filter by status."
def display_tickets(service_tickets):
    for ticket in service_tickets:  
        print(ticket, service_tickets[ticket])

def filter_status():
   status = input("Enter open or closed: ")
   for ticket in service_tickets:
       if service_tickets[ticket]["Status"] == status:
           print(ticket, service_tickets[ticket])
                            
while True:
    print("\nCustomer Service Ticket Tracker")
    print("1: Open New Ticket\n2: Update Ticket status\n3: Display All Tickets or Filter by Status\n4: Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        customer = input("Enter Name: ")
        issue = input("Enter Issue: ")
        status = input("Enter Status: ")
        open_ticket( customer, issue, status)
    elif choice == '2':
        update_ticket()
    # Display all tickets or filter by status
    elif choice == '3':
        
        ticket = input("Do you want to display all tickets or filter by status ? Enter Display/Filter: ")
        # print(ticket.upper())
        if ticket.upper() == "Display".upper():# or ticket == "display":
            display_tickets(service_tickets)
        elif ticket.upper() == "Filter".upper(): # or ticket == "filter": 
            filter_status()
        #  status = input("Enter Status: ")
        #     for ticket in service_tickets:
        #         if service_tickets[ticket]["Status"] == status:
        #             print(ticket, service_tickets[ticket])
        else:
            print("You did not enter display or filter")
                  
        # print(f"This is a Key{key}")  
        # print(f"This is a Value{value}") 
        
    # service_tickets = {
    # "Ticket1": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    # "Ticket2": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    
    elif choice == '4':
        print("Exiting system.")
        break
        print()  

        display_tickets(service_tickets)
         

        
       

    