# change slack status icon. 
# if failed to change status, send personal DM via slack

import os, random, time, pyperclip, pyautogui
import chromedriver_autoinstaller
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# for ubuntu CLI: https://somjang.tistory.com/entry/Ubuntu-Ubuntu-%EC%84%9C%EB%B2%84%EC%97%90-Selenium-%EC%84%A4%EC%B9%98%ED%95%98%EA%B3%A0-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0


os.makedirs('./screenshots', exist_ok=True)

try:
  from selenium import webdriver
  options = webdriver.ChromeOptions()
  # options.add_argument('headless')
  options.add_argument("lang=ko_KR")
  options.add_argument('window-size=1500,1200')
  options.add_argument("disable-gpu")
  options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

  try:
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
  except Exception as e:
    print(e)
    path = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(path, options=options)
  except Exception as e:
    print(e)
    driver = webdriver.Chrome(r"./chromedriver_mac64", options=options)  
  finally:
    str1 = driver.capabilities['browserVersion']
    str2 = driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
    print(f'Browser Version: {str1}, ChromeDriver Version: {str2}') 

    driver.implicitly_wait(0.2)
    driver.get('https://dashboard.wantedspace.ai/auth/email?redirect=/auth')
    id = driver.find_element_by_xpath('//*[@id="join"]/div[1]/div/div/div[1]/div[2]/div/input')
    time.sleep(1)
    id.send_keys('brstar96@synergyai.co')
    time.sleep(random.uniform(1,3))
    next_btn1 = driver.find_element_by_xpath('//*[@id="join"]/div[1]/div/div/div[2]/div[2]/button').click()
    time.sleep(random.uniform(2,4))
    pw = driver.find_elements_by_css_selector('#join > div.flex-wrap > div > div > div.card-body > div:nth-child(2) > div > input')[0]
    pw.click()
    actions_pw = webdriver.ActionChains(driver).send_keys_to_element(pw, '???').send_keys(Keys.ENTER)
    actions_pw.perform()
    time.sleep(random.uniform(3,5))
    
    # 결재 페이지로 이동
    driver.get('https://dashboard.wantedspace.ai/approval/sent')
    driver.implicitly_wait(10)
    write_request_btn = driver.find_element(By.CSS_SELECTOR, '#ct > div > div:nth-child(4) > div.display-flex > button')
    actions_request_btn = webdriver.ActionChains(driver).move_to_element(write_request_btn).click(write_request_btn).perform()
    time.sleep(random.uniform(2,4))
    request_template_btn = driver.find_element(By.CSS_SELECTOR, '#modal5 > div > div > div.modal-body > div > table > tbody > tr:nth-child(7) > td')
    actions_request_template_btn = webdriver.ActionChains(driver).move_to_element(request_template_btn).click(request_template_btn).perform()
    time.sleep(random.uniform(2,4))

    # 결재 요청 내용 입력 
    txt = '기간: 2023년 1월 30일 ~ 2023년 2월 3일 근무시간: 오전 7시 ~ 오후 4시'
    request_txt = driver.find_element_by_css_selector('#wrap > div:nth-child(3) > div > div.sc-cUEOzv.fVNCMH > div.sc-eeMvmM.glqOYO > div > div:nth-child(3) > div > div > div > div.fr-wrapper > div > p:nth-child(2)')
    request_txt.click()
    time.sleep(1)
    request_txt.send_keys(Keys.ENTER)
    time.sleep(1)
    actions_request_txt = webdriver.ActionChains(driver).send_keys_to_element(request_txt, txt).perform()

    # driver.save_screenshot(f"{project_dir}/images/{datenow}-{i['no']}.png")

except Exception as e:
  print(e)
  # TODO: slack notification if error
  # TODO: print('크론잡 실행 실패, 수동으로 상메 변경해주세요.')
  driver.quit()
finally:
  print("finish change all slack status")
  # driver.quit()