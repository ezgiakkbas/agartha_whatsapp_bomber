from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
while True:
    print("**********AGARTHA WHATSAPP SELENIUM DENEME************")
    print("**********WHATSAPP BOMBER************")

    try:
        name = input('Kullan�c� veya Grup Ad� Yaz : ')
    except:
            print("Hata Olu�tu")
            name = input('Kullan�c� veya Grup Ad� Yaz : ')
    try:
        msg = input('Mesaj�n� Yaz : ')
    except:
        print("Bir hata olu�tu")
        msg = input('Mesaj�n� Yaz : ')
    try:
        count = int(input('Ka� Adet G�nderilsin : '))
    except: 
        print("Hata Olu�tu")
        count = int(input('Ka� Adet G�nderilsin : '))
        
    input('G�ndermek ��in Bas�n�z')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()