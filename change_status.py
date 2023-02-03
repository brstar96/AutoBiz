# change slack status icon. 
# if failed to change status, send personal DM via slack

import os
import chromedriver_autoinstaller
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver as wd
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
    print(str1)
    print(str2)
    print(str1[0:2])
    print(str2[0:2])
    
    driver.implicitly_wait(3)
    driver.get('https://synergyai-lab.slack.com/?redir=%2Fgantry%2Fclient')
    driver.implicitly_wait(3)
    driver.get_screenshot_as_file('./screenshots/main_headless.png')


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
  
  # for i in users:
  #   print(i)
  #   driver.get(i['url']) # access url

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
  # TODO: slack notification if error
  # TODO: print('크론잡 실행 실패, 수동으로 상메 변경해주세요.')
  driver.quit()
finally:
  print("finish change all slack status")
  # driver.quit()