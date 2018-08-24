from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://qa-admin.dr-elephant.com/")
driver.execute_script('sessionStorage.setItem("access_token", "qVWrh0tOO_TeKQRhCoV6HSZHq3NhIlqXb5j9xfL\
6NHUJZyyjmeNpd82OUJm3q1XAvxctz5RYMp_bD8QIk13_f2euascT8BNSnPLoiw61tfQh7Y3yG8SQbM5DcpU2qFxsw0Cryi36KKRnm\
WSVdpPsK7Ypxgiq6JjK-W-MP2fgIZVTCP1SPPOJMrnxg__k1W_dtAGpwhcrt1ZImwNlvMEG6ghELlyx4EJJ_6UlLJkX78g4luB2K9M\
dB9GomazRQzLdX0wRbTCvai8ozM-GoCprCq1xvomjafzr5jjPq6QO8arKJ-DLXrwcKGzgf4PrfNVcmH7aHmA2H0gep5q5VMrfwN5tR\
XSX9r47evpZsr3nQ9vEAvHROWZQN7Y2FRKhsYxHMyP8YvhzV0dEBmm8STXO2EcQO8dB6lX8oBCkrVqt44WU-huqKBm8-A9Rx7_2bj1\
m9mv0B-OXk8c8FBZowdmJgocPJtzf7V9rSnxFpNr8uDA_3KTx76JM2pP7f8ZiXhjh-46Ma5_jmSP4KsHDTEUZWZB3ot6bZFjNO73We\
sw1Wv8baMgDsStE3mk33jY4-in_-Fw8cwXi-YNVci2hxd6-1w");')
driver.execute_script('sessionStorage.setItem("userName", "testadmin");')
driver.execute_script('sessionStorage.setItem("userId", "fc6b16e0-5427-4edc-b8ee-862fc5aa8455");')
driver.execute_script('sessionStorage.setItem("roleName", "6");')

driver.get("https://qa-admin.dr-elephant.com/slide")
driver.refresh()
