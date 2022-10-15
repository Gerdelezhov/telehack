from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def scr_f(url):
    filePath = __file__
    less_filePath = filePath.rstrip(r"project\scr.py")
    less_filePath1 = less_filePath + '\scr\geckodriver.exe'
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(options=options,
    executable_path=less_filePath1)
    browser.maximize_window()
    browser.get(url)

    url1 = url.lstrip(r"https://")
    print(url1)
    browser.save_screenshot(url1+r'.png')
    browser.quit()