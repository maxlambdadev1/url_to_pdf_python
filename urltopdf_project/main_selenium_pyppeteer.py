import pdfkit  
  
# configuring pdfkit to point to our installation of wkhtmltopdf  
config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc 

import time

driver = uc.Chrome()

options = {
    # 'header-html' : 'header.html'
    'user-style-sheet' : 'custom.css'
}

################# getting next url from entering the url ###############
main_url = 'https://alchemix-finance.gitbook.io/user-docs/'
selector = 'nav a' 
options = {
    'user-style-sheet' : 'custom.alchemix-finance.gitbook.io.css'
}
# main_url = 'https://docs.frax.finance'
# selector = 'nav a' 
# options = {
#     'user-style-sheet' : 'custom.docs.frax.finance.css'
# }
# main_url = 'https://docs.mstable.org'
# selector = 'nav a'
# options = {
#     'user-style-sheet' : 'custom.docs.mstable.org.css'
# }
# main_url = 'https://sommelier-finance.gitbook.io/sommelier-documentation/introduction/what-is-sommelier'
# selector = 'nav a'
# options = {
#     'user-style-sheet' : 'custom.sommelier-finance.gitbook.io.css'
# }
# main_url = 'https://docs.pooltogether.com/welcome/master'
# selector = 'nav a'
# options = {
#     'user-style-sheet' : 'custom.docs.pooltogether.com.css'
# }
# main_url = 'https://docs.aztec.network'
# selector = 'aside nav li a'
# options = {
#     'user-style-sheet' : 'custom.docs.aztec.network.css'
# }
# main_url = 'https://docs.morpho.org/start-here/homepage'
# selector = '.gitbook-root .css-175oi2r.r-1yzf0co.r-1sc18lr a'
# options = {
#     'user-style-sheet' : 'custom.docs.morpho.org.css'
# }
first_string = main_url[:20]

driver.get(main_url)
elems = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
elem = elems[0]
url=elem.get_attribute('href')

endFlag = 0
number = 0
file_arr = []

import asyncio
from pyppeteer import launch

async def save_page_as_pdf(url, output_path):
    # Launch headless Chrome browser
    browser = await launch()
    page = await browser.newPage()

    # Go to the desired URL
    await page.goto(url)

    # Set PDF options
    pdf_options = {
        'path': output_path,
        'format': 'A4',
        'margin' : {
            'top' : '0.5in',
            'bottom' : '0.5in',
            'left' : '0.25in',
            'right' : '0.25in'
        }
    }

    # Save page as PDF
    # await asyncio.sleep(15) 
    await page.pdf(pdf_options)

    # Close the browser
    await browser.close()


while endFlag < 1:
    filename = 'temp/' + str(number) + '.pdf' 
    file_arr.append(filename)
    # Run the function in an event loop
    asyncio.get_event_loop().run_until_complete(save_page_as_pdf(url, filename))
    # print(url) 
    # pdfkit.from_url(url, filename, options=options, configuration = config)
        
    driver.get(url)
    elems = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
    length = len(elems)

    i = 0
    j = 0
    for elem in elems:
        i = i + 1
        if (url == 'https://docs.morpho.org/governance/organization/multisigs-and-addresses' and elem.get_attribute('href') == url) :
            j = j + 1
            if (j > 1) : 
                break
        if (elem.get_attribute('href') == url and url != 'https://docs.morpho.org/governance/organization/multisigs-and-addresses'):
            break

    if (i < length):
        elem = elems[i]
        prev_url =  url          
        url = elem.get_attribute('href')

        while url.find('#') >= 0 or prev_url == url:
            elem.click()
            time.sleep(1)
            elems = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
            length = len(elems)
            i = i + 1
            if (i < length) :
                elem = elems[i]
                prev_url = url
                url = elem.get_attribute('href')
        while url.find(first_string) < 0 : #for external link
            i = i + 1
            if (i >= length) : 
                endFlag = 1
                break
            elem = elems[i]
            prev_url = url
            url = elem.get_attribute('href')
            if (prev_url.find(first_string) < 0 and url == 'https://docs.morpho.org/governance/organization/multisigs-and-addresses') :
                url = prev_url
        if (i >= length) :
            endFlag = 1
        if (url.find('discord') >= 0) :  ### for external link
            endFlag = 1
    else:
        endFlag = 1
    
    number = number + 1

#################  get from all href list ############
# main_url = 'https://docs.balancer.fi'
# selector = '.sidebar-items li > a'
# options = {
#     'user-style-sheet' : 'custom.docs.balancer.fi.css'
# }
# main_url = 'https://docs.yearn.finance/getting-started/intro'
# selector = 'aside nav a'
# options = {
#     'user-style-sheet' : 'custom.docs.yearn.finance.css'
# }

# driver.get(main_url)
# elems = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
# length = len(elems)

# number = 0
# file_arr = []

# while number < length:
#     elem = elems[number]           
#     url = elem.get_attribute('href')

#     if url != None and url.find('#') < 0 :
#         filename = 'temp/' + str(number) + '.pdf' 
#         file_arr.append(filename)
#         print(url) 
#         pdfkit.from_url(url, filename, options=options,  configuration = config)
            
#     number = number + 1

#########  concate all files to one.################
from PyPDF2 import PdfMerger

pdf_merger = PdfMerger()

for file in file_arr:
    pdf_merger.append(file)


# Remove 'https://'
url_without_http = main_url.replace('https://', '')
# Replace '/' with '_'
modified_url = url_without_http.replace('/', '_')
output_file = modified_url + '.pdf'

pdf_merger.write(output_file)
pdf_merger.close()

#delete all files
import os

for fileurl in file_arr:
    os.remove(fileurl)

driver.close()