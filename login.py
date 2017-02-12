from bs4 import BeautifulSoup
import requests
import os,re,time
from selenium import webdriver


# driver = webdriver.Chrome()
# url = 'http://www.jianshu.com/writer#/notebooks/9768467/notes/9095260'
# driver.get(url)
# time.sleep(35)
# cook = driver.get_cookies()
# print(cook)
# time.sleep(35)

# PhantomJS
driver = webdriver.Chrome()
url = 'http://www.jianshu.com/writer#/notebooks/9768467/notes/9095260'

driver.get(url)
time.sleep(1)


cook = [{'name': '_session_id', 'httpOnly': True, 'path': '/', 'secure': False, 'domain': 'www.jianshu.com', 'value': 'Q3lqdnRnNjRFMWN4aFB1K3F1WjAxcEhWWFYxYzdPMU5VYnJBcWdPU0NFZ2RqSGlPbHFBTWtLS0JzZktvK1lVMkJHelNUTXJPV2tXem1YQ0k0RkYrTkFacld4bEtrV2lkdjZkTkdGVFh2d3VJaG5EVUNnN0lYeWh0UzNxMDVnWENqNnpyUmJmU3pvRVcyRnpsZXdFN0ppY1pDSDI4d2pDaGdhaVVMYlhRNG5jVHlTMkw1NDUwcm1BZkpvbjE2TURTaFdGaFAxaXY0R3NxUWVRcDNvTnpVZFpBNTVmVkxjV2VOeXNtUk9hRzRqZ0o2MDE5QXNkQlVIMWhtQXBnSGdRQmZJRmV3ZnhQSXpDNFNiS0dEQkYvVXEzdFR3SjVTNVA4dmttVTVRYlUvZjdjeDJpSDAvQ3FRWjZFZkxyaVJQRTdJVWNXa3VXMW45OG12a2RYRVdCenJlWGVFL2FYdzZ4NmFZbGxOYWZ4MEJTamptemdIeWhCbnVjRnpncnNYYUlZMjBKaFMrTHpwS1U3bzFnT21vRVoxRFhwODIrOStKK3U2V2VmaTJ5SlgzdHVoMFgzQlROa3Q5NHEzZ2lFa3d6Z2pCa2xyVlY0dE1USW1mSzJHRDRXamc9PS0tWS9yMUVIeUdidTRXWCsxdnNzdjJ6dz09--b92461cd672231b18d47c777d1eb324edeabb839'}, {'expiry': 1549886122, 'httpOnly': False, 'path': '/', 'secure': False, 'name': '_ga', 'domain': '.jianshu.com', 'value': 'GA1.2.995309512.1486814105'}, {'expiry': 1502538922, 'httpOnly': False, 'path': '/', 'secure': False, 'name': 'CNZZDATA1258679142', 'domain': 'www.jianshu.com', 'value': '470763093-1486812348-%7C1486812348'}, {'expiry': 1488023721.416068, 'httpOnly': True, 'path': '/', 'secure': False, 'name': 'remember_user_token', 'domain': 'www.jianshu.com', 'value': 'W1szNDI2ODUyXSwiJDJhJDEwJHJHZ3VaR0kwQzduYTMxMjUuS3FrYU8iLCIxNDg2ODE0MDMwLjM0Mjc3MzIiXQ%3D%3D--52f9ed6df2226af633ad5172926cb25f6ad7dfdc'}, {'expiry': 1486814705, 'httpOnly': False, 'path': '/', 'secure': False, 'name': '_gat', 'domain': '.jianshu.com', 'value': '1'}]

driver.delete_all_cookies()
for cookx in cook:
    driver.add_cookie(cookx)

driver.get(url)
time.sleep(10)

aa = driver.page_source
print(aa)
time.sleep(89)
