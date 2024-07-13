import requests


def testapi():
    CODE = 200
    url = 'https://eng-api-e8wg.onrender.com/docs'
    response = requests.get(url)
    assert response.status_code == CODE


def testdash():
    CODE = 200
    url = 'https://deploy-api-kvp5.onrender.com/'
    response = requests.get(url)
    assert response.status_code == CODE


if __name__ == '__main__':
    testapi()
    testdash()
