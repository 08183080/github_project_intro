import requests

def get_outline(url):
    headers = {'User-Agent':'Mozilla/5.0',
            'Authorization': 'token ef802a122df2e4d29d9b1b868a6fefb14f22b272',
            'Content-Type':'application/json',
            'Accept':'application/json'
            }

    response = requests.get(url, headers=headers)

    return response.json()

if __name__ == '__main__':
    url = 'https://github.com/08183080/be-yourself'
    print(get_outline(url))