from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def checkAvailability(name):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    url = 'https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={}'.format(name)

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    element = driver.find_element_by_xpath('//*[@id="exact-match"]/div/div/div/div')

    dataCy = element.get_attribute('data-cy')

    if dataCy == 'flattened-taken-exact':
        available = False
        premium = False
        domainName = driver.find_element_by_xpath('//*[@id="exact-match"]/div/div/div/div/div[1]/div[1]/span').text
    elif dataCy == 'celebrate-exact-match':
        available = True
        premium = False
        domainName = driver.find_element_by_xpath('//*[@id="exact-match"]/div/div/div/div/div/p').text
    else:
        available = True
        premium = True
        domainName = driver.find_element_by_xpath('//*[@id="exact-match"]/div/div/div/div/div[2]/div[1]/div[1]/span/span').text

    return available, premium, domainName, url