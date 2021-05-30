# import Library selenium dan json
from selenium import webdriver
import json

# koneksi dengan laman web
web = webdriver.Chrome()
web.get('https://prak3pwl-silenium.herokuapp.com/')

# koneksi dengan file json
with open('data.json') as f:
    data = json.load(f)

for state in data['test_case']:
    username = state['data']['username']
    usernameInput = web.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/input')
    usernameInput.send_keys(username)

    password = state['data']['password']
    passwordInput = web.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/input')
    passwordInput.send_keys(password)

    validasi = state['data']['validasi']
    validasiInput = web.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/input')
    validasiInput.send_keys(validasi)

    button = web.find_element_by_xpath('/html/body/div/div[2]/div/div[4]/div/button')
    button.click()

    hasil = web.find_element_by_xpath('/html/body/div/div[2]/div/p[4]')
    if(hasil.text == state['expected']):
        print("berhasil")
    else:
        print("gagal")

    # mengkosongkan text field
    usernameInput.clear()
    passwordInput.clear()
    validasiInput.clear()