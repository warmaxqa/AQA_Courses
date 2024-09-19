import requests
import os

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

params = {
    'sol': 1000,  # day mission
    'camera': 'fhaz',  # camera first plan
    'api_key': 'DEMO_KEY'  # public key
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    photos = data['photos']

    if photos:
        for i, photo in enumerate(photos):
            img_url = photo['img_src']
            img_response = requests.get(img_url)

            if img_response.status_code == 200:
                img_filename = f'mars_photo{i + 1}.jpg'
                with open(img_filename, 'wb') as file:
                    file.write(img_response.content)
                print(f'Photo {img_filename} saved.')
            else:
                print(f'Failed to upload photo {i + 1}')
    else:
        print('Photo behind the title not found.')
else:
    print(f'Error request: {response.status_code}')
