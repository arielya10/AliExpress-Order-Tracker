from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from forex_python.converter import CurrencyRates
import time

cr=CurrencyRates()

#Login
def login():
    while True:
        user_email=input("Enter your mail: ")
        user_password=input("Enter your password: ")
        email = driver.find_element(By.ID, 'fm-login-id')
        email.clear()
        email.send_keys(user_email)
        password = driver.find_element(By.ID, 'fm-login-password')
        password.clear()
        password.send_keys(user_password)
        driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/button[2]').click()
        time.sleep(5)
        try:
            driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div/div/button[2]').click()
            print("Your account name or password is incorrect.")
            driver.close()
            driver.quit()
            exit()
        except Exception:
            driver.maximize_window()
            break


#Showing all the items
def show_all_orders(flag):
    while True:
        try:
            view_orders = wait.until(EC.visibility_of_element_located((By.XPATH,f'//*[@id="root"]/div/div[2]/div[{flag}]/button/span')))
            driver.execute_script("arguments[0].click();", view_orders)
        except Exception:
            break

#counting orders

def get_orders(flag):
    i = 1
    counter=1
    total_price = 0
    tab="My orders"
    span="span"
    if flag==2:
        tab= "Deleted orders"
        span="label/span[2]"
    while True:
        try:

            #getting status {Finished , Awaiting delivery} ,refundable status {Closed, Cancelled}
            status = driver.find_element(By.XPATH,f'//*[@id="root"]/div/div[2]/div[{flag}]/div/div[{i}]/div[1]/div[1]/{span}')
            status =status.text
            if status == "Finished" and status != "Awaiting delivery":

                #getting item price
                order =driver.find_element(By.XPATH,f'//*[@id="root"]/div/div[2]/div[{flag}]/div/div[{i}]/div[3]/div[2]/div[1]/span')
                driver.execute_script("arguments[0].scrollIntoView();", order)
                order =order.text

                #checking currency
                if order.find('₪') != -1:
                    order = order.replace('Total: ₪ ', '')
                    price=float(order)
                    price = cr.convert('ILS', 'USD', price)
                else:
                    order = order.replace('Total: US $', '')
                    price=float(order)

                #summing total price
                counter += 1
                total_price += price
                print(f"({tab})({status}) Total money spent: {total_price:.2f}$, Price: {price:.2f}$, (index: {counter})\n")
            i+=1
        except Exception:
            break
    print(f"Total money spent in {tab}: {total_price:.2f}$\n")
    print(f"{counter} items bought...\n")
    return total_price,counter



#URL
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.minimize_window()
driver.get('https://www.aliexpress.com/p/order/index.html')
wait = WebDriverWait(driver, 5)

#login
login()

#Getting my orders
show_all_orders(2)
sum_my_orders=get_orders(1)

#Getting deleted orders
deleted_orders = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="root"]/div/div[1]/div[1]/div[2]')))
driver.execute_script("arguments[0].click();", deleted_orders)
show_all_orders(3)
sum_deleted_orders=get_orders(2)


print(f"Total money spent in Aliexpress: {sum_my_orders[0] + sum_deleted_orders[0]:.2f}$")
print(f"{sum_my_orders[1] + sum_deleted_orders[1]} items bought.....")
driver.close()
driver.quit()



