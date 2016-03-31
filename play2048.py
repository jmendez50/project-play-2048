#Juan Mendez 
#TODO: Import the module that will allow you to use Selenium
#TODO: Import the module that will allow you to use the up, down, left, and right keys on your keyboard


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def play2048( times ):
    chrome = webdriver.Firefox() #i had to doweload firefox this didnt want to work with chrome
    chrome.get('http://gabrielecirulli.github.io/2048/')
    goes = 0
    web = chrome.find_element_by_tag_name('html')

    for goes in range (times):
        web.send_keys(Keys.UP)
        web.send_keys(Keys.RIGHT)
        web.send_keys(Keys.DOWN)
        web.send_keys(Keys.LEFT)
        goes += 1
    #Was trying to make it run in chrome and i downloaded the chrom tool and all but it didnt work so idk
        
    #TODO: write code in this function that:
    # 1. opens a game of 2048 from the URL: https://gabrielecirulli.github.io/2048/
    # 2. uses the parameter 'times' to determine how many times your code will try to play the game
    # 3. for each 'time', press these keys in this order: UP, RIGHT, DOWN, LEFT
    # 4. print the final score after all tries to the screen 
    
