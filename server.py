SERVER CODE: 
import socket 
 
# Set up a TCP/IP socket sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
 
# Define the server address and port server_address = ('localhost', 10000) 
 
# Bind the socket to the server address and port sock.bind(server_address) 
 
# Listen for incoming connec ons 
sock.listen(1) 
 
# Define the food items and their prices food_items = {'pizza': 10, 'burger': 8, 'fries': 4, 'soda': 2,'masala dosa':20} def calculate_cost(order): 
    total_cost = 0     for item, quan ty in order.items(): 
        total_cost += food_items.get(item, 0) * quan ty     return total_cost 
 
# Wait for a connec on print('Wai ng for a connec on...') connec on, client_address = sock.accept() 
 
try: 
    # Receive the food order from the client     data = connec on.recv(1024).decode()     order = eval(data) # convert the string to a dic onary 
 
    # Calculate the total cost of the order     total_cost = calculate_cost(order) 
 
    # Send the total cost back to the client     connec on.sendall(str(total_cost).encode()) 
 
    # CLOSE the connec on     connec on.close()     sock.close() 
