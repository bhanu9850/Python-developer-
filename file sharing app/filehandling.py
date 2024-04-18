import socket


def upload_file(filename, server_address, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_address, port))
            with open(filename, 'rb') as file:
                file_data = file.read()
            s.sendall(file_data)
        print("File uploaded successfully.")
    except Exception as e:
        print("Error uploading file:", e)


def download_file(filename, server_address, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_address, port))
            s.sendall(b"DOWNLOAD_REQUEST")
            with open(filename, 'wb') as file:
                while True:
                    data = s.recv(1024)
                    if not data:
                        break
                    file.write(data)
        print("File downloaded successfully.")
    except Exception as e:
        print("Error downloading file:", e)
