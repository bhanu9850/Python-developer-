import socket

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")

            # Handle client request (e.g., file transfer)
            handle_client_request(client_socket)


def handle_client_request(client_socket):
    try:
        # Receive the client's request
        request = client_socket.recv(1024).decode()

        if request == "UPLOAD_REQUEST":
            # Receive the file name from the client
            filename = client_socket.recv(1024)
            print(f"Received filename bytes: {filename}")
            # Receive the file data from the client
            file_data = b''
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file_data += data
            # Save the received file data to a file on the server
            with open(filename, "wb") as file:
                file.write(file_data)
            print(f"File '{filename}' uploaded successfully.")

            # Send confirmation to the client
            client_socket.sendall(b"UPLOAD_SUCCESS")

        elif request == "DOWNLOAD_REQUEST":
            # Receive the requested file name from the client
            filename = client_socket.recv(1024)
            print(f"Received filename bytes: {filename}")
            try:
                # Read the requested file data from the server
                with open(filename, "rb") as file:
                    file_data = file.read()
                # Send the file data to the client
                client_socket.sendall(file_data)
                print(f"File '{filename}' sent successfully.")
            except FileNotFoundError:
                print(f"File '{filename}' not found on the server.")
                # Send error message to the client
                client_socket.sendall(b"FILE_NOT_FOUND")

        else:
            print("Invalid request from client.")

    except Exception as e:
        print("Error handling client request:", e)

    finally:
        # Close the client socket
        client_socket.close()

HOST = 'localhost'
PORT = 45268

start_server(HOST, PORT)
