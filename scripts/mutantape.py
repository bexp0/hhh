from selenium import webdriver
import wget

base_url = "https://opensea.io/assets/0x60e4d786628fea6478f785a6d7e704777c86a7c6/"
driver = webdriver.Chrome()

for each in range(10000):
    driver.get(base_url + str(each))
    img_src = driver.find_element_by_xpath("//*[@id='main']/div/div/div/div[2]/div/article/div/div/div/div/img").get_attribute("src")
    if img_src is not None:
        wget.download(img_src, str(each) + ".png")

driver.close()