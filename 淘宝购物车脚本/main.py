import datetime #模坎
# now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
import time
#全自动化Python代码操作
from selenium import webdriver
import win32com.client
from selenium.webdriver.common.by import By
from mail import sendMail
from datetime import datetime, timedelta

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# kill_time = "2023-9-16 11:00:00.00000000"
wtools = webdriver.Chrome()

wtools.get("https://www.taobao.com")
time.sleep(5)
wtools.find_element(By.LINK_TEXT, "亲，请登录").click()

# print("请尽快扫码登录")
time.sleep(15)
wtools.get("https://cart.taobao.com/cart.htm")
time.sleep(3)

checktime2 = datetime.now()

while True:
    try:
        wtools.find_element(By.XPATH, '//*[@id="J_Item_5149874782549"]/ul/li[5]/div/div/div[1]/a[2]').click()
        stock_num1 = wtools.find_element(By.XPATH, '//*[@id="J_Item_5149874782549"]/ul/li[5]/div/div/div[1]/input')
        stock_name1 = wtools.find_element(By.XPATH, '//*[@id="J_Item_5149874782549"]/ul/li[2]/div/div[2]/div[1]/a')
        # print(stock_text.get_attribute('value'))
        if int(stock_num1.get_attribute('value')) == 1 : 
            # sendMail(stock_name1.get_attribute('value'), "jdsxjh@126.com")
            main_content = '''代码就是这么多
                            是不是很简单。
                            ok了家人们,记得点一个赞。
                            '''
            sendMail(main_content, "jdsxjh@126.com")
            
        else :
            while int(stock_num1.get_attribute('value')) > 1 :
                wtools.find_element(By.XPATH, '//*[@id="J_Item_5149874782549"]/ul/li[5]/div/div/div[1]/a[1]').click()
                stock_num1 = wtools.find_element(By.XPATH, '//*[@id="J_Item_5149874782549"]/ul/li[5]/div/div/div[1]/input')
            time.sleep(5)

        wtools.find_element(By.XPATH, '//*[@id="J_Item_5137025670206"]/ul/li[5]/div/div/div[1]/a[2]').click()
        stock_num2 = wtools.find_element(By.XPATH, '//*[@id="J_Item_5137025670206"]/ul/li[5]/div/div/div[1]/input')
        stock_name2 = wtools.find_element(By.XPATH, '//*[@id="J_Item_5137025670206"]/ul/li[2]/div/div[2]/div[1]/a')
        if int(stock_num2.get_attribute('value')) == 1 : 
            if datetime.now() >= checktime2:
                main_content = stock_name2.text + "库存仅剩最后一件，及时购买"
                print(stock_name2.text)
                sendMail(main_content, "jdsxjh@126.com")
                checktime2 = datetime.now() + timedelta(weeks=1)

        else :
            while int(stock_num2.get_attribute('value')) > 1 :
                wtools.find_element(By.XPATH, '//*[@id="J_Item_5137025670206"]/ul/li[5]/div/div/div[1]/a[1]').click()
                stock_num2 = wtools.find_element(By.XPATH, '//*[@id="J_Item_5137025670206"]/ul/li[5]/div/div/div[1]/input')
            time.sleep(5)
            
    
    except Exception as e:
        print(e)
        break


