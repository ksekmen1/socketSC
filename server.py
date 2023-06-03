import json
import socket


def handle_client(client_socket):
    # Receive data from the client
    json_data = client_socket.recv(1024).decode()

    # Parse the JSON data
    data = json.loads(json_data)

    # Access the values
    value1 = data["Height"]
    value2 = data["Width"]

    # Perform the divisions
    result1 = value1 / 9
    result2 = value2 / 16
    # Create a JSON response with the results

    response = json.dumps({"result1": result1, "result2": result2})

    # Send the response back to the client
    client_socket.send(response.encode())

    # Close the client socket
    client_socket.close()


# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port for the server
host = 'localhost'
port = 1234

# Bind the socket to the host and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)
print(f"Server listening on {host}:{port}")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    # Handle the client request
    handle_client(client_socket)
