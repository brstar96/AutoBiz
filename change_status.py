# from selenium.common.exceptions import NoSuchElementException
from datetime import date
import json
import os

# change slack status icon. 
# if failed to change status, send message to slack

try:
  from selenium import webdriver
  options = webdriver.ChromeOptions()
  options.add_argument('--headless')
  options.add_argument('--no-sandbox')
  options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome('./chromedriver', options=options)
  print(driver)

  driver.get('http://naver.com')
  driver.implicitly_wait(3)
  driver.get_screenshot_as_file('naver_main_headless.png')


  # options = webdriver.ChromeOptions()
  # options.add_argument("start-maximized")
  # options.add_argument("lang=ko_KR")
  # options.add_argument('headless')
  # options.add_argument('window-size=1500,1200')
  # options.add_argument("disable-gpu")
  # options.add_argument("--no-sandbox")

  # driver = webdriver.Chrome(executable_path='chromedriver', options=options)
  # driver.implicitly_wait(3)
  # print('a')
  # with open('users.json') as json_file:
  #   users = json.load(json_file)

  # datenow = date.today().strftime("%y%m%d")
  
  # project_dir = os.path.dirname(os.path.abspath(__file__))
  
  for i in users:
    print(i)
    driver.get(i['url']) # access url

    # try:
    #   driver.find_element_by_class_name("ui-dialog-titlebar-close").click()
    # except NoSuchElementException:
    #   pass

    # driver.find_element_by_id('rspns011').click()
    # driver.find_element_by_id('rspns02').click()
    # driver.find_element_by_id('rspns070').click()
    # driver.find_element_by_id('rspns080').click()
    # driver.find_element_by_id('rspns090').click()

    # driver.find_element_by_id('btnConfirm').click()

    # driver.save_screenshot(f"{project_dir}/images/{datenow}-{i['no']}.png")

except Exception as e:
  print(e)
#   # TODO: slack notification if error
#   # TODO: print('크론잡 실행 실패, 수동으로 상메 변경해주세요.')
#   driver.quit()

# finally:
#   print("finish all self check")
#   driver.quit()