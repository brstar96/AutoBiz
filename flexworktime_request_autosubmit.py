import os, random, time
from pytz import timezone
from datetime import datetime, timedelta
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# for ubuntu CLI: https://somjang.tistory.com/entry/Ubuntu-Ubuntu-%EC%84%9C%EB%B2%84%EC%97%90-Selenium-%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0

os.makedirs('./screenshots', exist_ok=True)
debug = True
now = datetime.now(timezone('Asia/Seoul'))
days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
today = datetime.today().weekday()
print('today is {}, debug: {}'.format(days[today], debug))
formattedDateToday = now.strftime("%Y%m%d_%H%M%S")
ID_MGL = os.environ.get('ID_MGL')
PW_MGL = os.environ.get('PW_MGL')

if today == 4:
  monday = now + timedelta(days=3)
  friday = monday + timedelta(days=4)
  workingday = '{} ~ {}'.format(monday.strftime('%Y년 %m월 %d일'), friday.strftime('%Y년 %m월 %d일'))
else:
  if debug == True:
    print('debug mode')
    now = now + timedelta(days=2)
    monday = now + timedelta(days=3)
    friday = monday + timedelta(days=4)
    workingday = '{} ~ {}'.format(monday.strftime('%Y년 %m월 %d일'), friday.strftime('%Y년 %m월 %d일'))
    print(workingday)
  else:
    print('Not Friday')
    raise Exception('Not Friday')

try:
  from selenium import webdriver
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument("lang=ko_KR")
  chrome_options.add_argument('window-size=1500,1200')
  chrome_options.add_argument("disable-gpu")
  chrome_options.add_argument('--disable-dev-shm-usage')
  chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

  try:
    driver = webdriver.Chrome('./chromedriver_mac64')
    print('use project driver')
  except Exception as e:
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    print('use ChromeDriverManager')
  except Exception as e:
    print('Error!! - ', e)
    import chromedriver_autoinstaller
    path = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(path, chrome_options=chrome_options)
    print('use chromedriver_autoinstaller')
  else:
    print('Driver Loaded!')
    str1 = driver.capabilities['browserVersion']
    str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
    print(f'Browser Version: {str1}, ChromeDriver Version: {str2}') 

    driver.implicitly_wait(0.2)
    driver.get('https://dashboard.wantedspace.ai/auth/email?redirect=/auth')
    id = driver.find_element_by_xpath('//*[@id="join"]/div[1]/div/div/div[1]/div[2]/div/input')
    time.sleep(1)
    id.send_keys(ID_MGL) # ID_MGL
    time.sleep(random.uniform(1,3))
    next_btn1 = driver.find_element_by_xpath('//*[@id="join"]/div[1]/div/div/div[2]/div[2]/button').click()
    time.sleep(random.uniform(2,4))
    pw = driver.find_elements_by_css_selector('#join > div.flex-wrap > div > div > div.card-body > div:nth-child(2) > div > input')[0]
    pw.click()
    actions_pw = webdriver.ActionChains(driver).send_keys_to_element(pw, PW_MGL).send_keys(Keys.ENTER) # PW_MGL
    actions_pw.perform()
    driver.implicitly_wait(1)
    time.sleep(random.uniform(3,5))
    
    # 결재 페이지로 이동
    driver.get('https://dashboard.wantedspace.ai/approval/sent')
    driver.implicitly_wait(1)
    write_request_btn = driver.find_element(By.CSS_SELECTOR, '#ct > div > div:nth-child(4) > div.display-flex > button')
    actions_request_btn = webdriver.ActionChains(driver).move_to_element(write_request_btn).click(write_request_btn).perform()
    driver.implicitly_wait(1)
    time.sleep(random.uniform(2,4))
    request_template_btn = driver.find_element(By.CSS_SELECTOR, '#modal5 > div > div > div.modal-body > div > table > tbody > tr:nth-child(7) > td')
    actions_request_template_btn = webdriver.ActionChains(driver).move_to_element(request_template_btn).click(request_template_btn).perform()
    driver.implicitly_wait(1)
    time.sleep(random.uniform(2,4))

    # 결재 요청 내용 입력 
    txt = '\n\n기간: {} \n근무시간: 오전 7시 ~ 오후 4시'.format(workingday)
    time.sleep(3)
    application_form = driver.find_element(By.CSS_SELECTOR, '#wrap > div:nth-child(3) > div > div.sc-lbVpMG.ieOMJV > div.sc-gScZFl.cyBdCS > div > div:nth-child(3) > div > div > div > div.fr-wrapper > div')
    
    application_form_location = application_form.location
    application_form_ac = webdriver.ActionChains(driver) 
    application_form_ac.move_to_element(application_form).move_by_offset(10, 10).click().send_keys(txt).perform()

    print('Add txt done! \n Added text: {}'.format(txt))
    time.sleep(random.uniform(2,4))
    
    # 결재 상신 
    if debug == False:
      confirm_btn = driver.find_elements_by_xpath('//*[@id="wrap"]/div[3]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/button[2]')[0]
    else:
      confirm_btn = driver.find_elements_by_xpath('//*[@id="wrap"]/div[3]/div/div[2]/div[2]/div/div[6]/div[2]/div[2]/button[1]')[0]

    confirm_btn.click() 

    time.sleep(1)

    print('결재 상신 완료!')
    driver.save_screenshot(f"./screenshots/{formattedDateToday}.png")
    driver.quit()
    print('크론잡 실행 완료, 스크린샷 저장: ', f"./screenshots/{formattedDateToday}.png")

except Exception as e:
  print(e)
  driver.quit()
  raise Exception('Failed to run cronjob. It may be because of the chromedriver error.')
finally:
  print("finish change all slack status")
  driver.quit()