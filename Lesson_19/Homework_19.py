import requests

upload_url = 'http://127.0.0.1:8080'

image_path = 'D:\picture_test.jpg'

with open(image_path, 'rb') as image_file:
    files = {'file': image_file}
    response = requests.post(upload_url, files=files)

if response.status_code == 200:
    print("Picture successfully downloaded.")
    file_info = response.json()  # Back to json
    file_url = file_info['file_url']  # Get URL FILE
    file_id = file_info['file_id']  # ID File
    print(f"Link to url: {file_url}")
else:
    print(f"Error Download: {response.status_code}")

# GET
get_file_url = f'https://example.com/get/{file_id}'
get_response = requests.get(get_file_url)

if get_response.status_code == 200:
    print("File link received:")
    print(get_response.json())  # display information about the file
else:
    print(f"Error getting link: {get_response.status_code}")

# DELETE
delete_url = f'https://example.com/delete/{file_id}'
delete_response = requests.delete(delete_url)

if delete_response.status_code == 200:
    print("File successfully delete.")
else:
    print(f"Error delete: {delete_response.status_code}")
