from selenium import webdriver
from random import randint

letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

driver = webdriver.Chrome("C:/Users/samta/OneDrive/Programacao/Python/chromedriver.exe")
driver.get('https://web.whatsapp.com/')

name = input('Para quem deseja enviar 1000 mensagens? : ')
# name = "Felipe (GEMEOS)"
#msg = input('Enter your message : ')
msg = 1
# count = int(input('Enter the count : '))
count = int(20)

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
    msg+=1