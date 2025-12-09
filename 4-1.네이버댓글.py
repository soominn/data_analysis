import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
# driver.get('https://comic.naver.com/webtoon/detail?titleId=845271&no=2&week=mon')
driver.get('https://comic.naver.com/webtoon/detail?titleId=776601&no=178&week=fri')
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')

xpath = '/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/ul/li'
best_comment_elements = driver.find_elements(By.XPATH, xpath)
for li in best_comment_elements:
    try:
        #'/div[1]/div[2]/div/p'
        comment_p = li.find_element(By.XPATH, './div[1]/div[2]/div/p')
        comment_text = comment_p.text.strip()
        print(comment_text)
        print('-' * 30)
    except Exception as e:
        print(e)

driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div/div[5]/div[1]/div[3]/div/section/div[4]/button[2]').click()

time.sleep(1)

print('***** 전체 댓글 *****')
all_comment_elements = driver.find_elements(By.XPATH, xpath)
for li in all_comment_elements:
    try:
        comment_p = li.find_element(By.XPATH, './div[1]/div[2]/div/p')
        comment_text = comment_p.text.strip()
        print(comment_text)
        print('-' * 30)
    except NoSuchElementException as e:
        comment_p = li.find_element(By.XPATH, './p')
        comment_text = comment_p.text.strip()
        print(comment_text)
        print('-' * 30)
    except Exception as e:
        print(e)

time.sleep(1)