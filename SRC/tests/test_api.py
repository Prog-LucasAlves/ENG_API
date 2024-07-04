import requests


def testapi():
    CODE = 200
    url = 'https://eng-api-e8wg.onrender.com/docs'
    response = requests.get(url)
    print(response.text)
    assert response.status_code == CODE


if __name__ == '__main__':
    testapi()
