file = open("lista.txt",'r')
links = file.readlines()

for k in links:
    driver = webdriver.Firefox()
    driver.get(k[:-1])
    driver.save_full_page_screenshot("%d.png")
    driver.close()
