import json
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port for the server
host = 'localhost'
port = 1234

# Connect to the server
client_socket.connect((host, port))

# Create a JSON object with the values to be divided
data = {"Height": 1080, "Width": 1920}

# Convert the JSON object to a string
json_data = json.dumps(data)

# Send the JSON data to the server
client_socket.send(json_data.encode())

# Receive the response from the server
response = client_socket.recv(1024).decode()

# Parse the JSON response
result_data = json.loads(response)

# Access the results
result1 = result_data["result1"]
result2 = result_data["result2"]

if result1 == result2:
    print("Yes")

# Print the results
print("Result 1:", result1)
print("Result 2:", result2)

# Close the socket
client_socket.close()
