from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


options = webdriver.ChromeOptions()
options.headless = True
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=options)

def submit_adrs(adrs):
    browser.get('https://docs.google.com/forms/d/e/1FAIpQLScmbcXs6qF7BXESqeFKKmmsEkcStYoaCar_9hIG-ILFiT1CFw/viewform')

    sleep(3)

    checkboxes = browser.find_elements(By.CSS_SELECTOR, 'div[role="checkbox"]')

    for i in checkboxes:
        i.click()

    next_button = browser.find_element(By.CSS_SELECTOR, 'div[jsname="OCpkoe"]')
    next_button.click()

    adrs_input = browser.find_element(By.CSS_SELECTOR, 'input[jsname="YPqjbf"]')

    adrs_input.clear()
    adrs_input.send_keys(adrs)

    submit_button = browser.find_element(By.CSS_SELECTOR, 'div[jsname="M2UYVd"]')

    # submit_button.click()

    with open('done.txt', 'a') as f:
        f.write(f'{adrs}\n')
        print(f'{adrs} done.')

with open('wl.txt', 'r') as f:
    all_wallets = f.read().splitlines()

    with open('done.txt', 'r') as d:
        done_wallets = d.read().splitlines()

        for wl in all_wallets:
            if wl not in done_wallets:
                submit_adrs(wl)
                sleep(60 * 12)
            else:
                print(f'{wl} is already done, skipping...')