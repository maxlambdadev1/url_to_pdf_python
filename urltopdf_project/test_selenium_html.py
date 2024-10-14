import pdfkit  
  
# configuring pdfkit to point to our installation of wkhtmltopdf  
config = pdfkit.configuration(wkhtmltopdf = r"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")  

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc 

# driver = uc.Chrome()

# options = {
#     'header-html' : 'header.html'
# }
# wf = open('result1.txt', 'w')

# ################# getting next url from entering the url ###############
# main_url = 'https://alchemix-finance.gitbook.io/user-docs'
# selector = 'nav a' 
# main_url = 'https://docs.frax.finance'
# selector = 'nav a' 
# main_url = 'https://docs.mstable.org'
# # selector = 'nav a'
# main_url = 'https://sommelier-finance.gitbook.io/'
# selector = 'nav a'


# driver.get(main_url)
# # element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body')))
# # html = element.get_attribute('innerHTML')
# # wf.write(html)
# html_content = driver.page_source
# # Save the HTML content to a file
# with open("page.html", "w", encoding="utf-8") as file:
#     file.write(html_content)

# # pdfkit.from_file('page.html', 'output.pdf', configuration=config)
# from weasyprint import HTML
# # Convert HTML file to PDF
# HTML('page.html').write_pdf('output.pdf')


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

# Call the function with the URL and output path
url = 'https://docs.aztec.network/'
output_path = 'output.pdf'

# Run the function in an event loop
asyncio.get_event_loop().run_until_complete(save_page_as_pdf(url, output_path))

# driver.get(main_url)
# elems = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
# elem = elems[0]
# url=elem.get_attribute('href')

# endFlag = 0
# number = 0
# file_arr = []

# while endFlag < 1:
#     filename = 'temp/' + str(number) + '.pdf' 
#     file_arr.append(filename)
#     print(url) 
#     pdfkit.from_url(url, filename,  configuration = config)
        
#     driver.get(url)
#     elems = WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, selector)))
#     length = len(elems)

#     i = 0
#     for elem in elems:
#         i = i + 1
#         if (elem.get_attribute('href') == url):
#             break

#     if (i < length):
#         elem = elems[i]           
#         url = elem.get_attribute('href')
#     else:
#         endFlag = 1
    
#     number = number + 1

##################  get from all href list ############
# main_url = 'https://docs.balancer.fi/'
# selector = '.sidebar-items li > a' 

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
#         pdfkit.from_url(url, filename,  configuration = config)
            
#     number = number + 1

#########  concate all files to one.################
# from PyPDF2 import PdfMerger

# pdf_merger = PdfMerger()

# file_arr = ['0.pdf','1.pdf','2.pdf','3.pdf','4.pdf','5.pdf','6.pdf','7.pdf','8.pdf','9.pdf','10.pdf','11.pdf','12.pdf','13.pdf','14.pdf','15.pdf','16.pdf','17.pdf','18.pdf','19.pdf','20.pdf','21.pdf','22.pdf','23.pdf','24.pdf','25.pdf','26.pdf','27.pdf','28.pdf','29.pdf','30.pdf','31.pdf','32.pdf','33.pdf','34.pdf','35.pdf'
#             ,'36.pdf','37.pdf','38.pdf','39.pdf','40.pdf','41.pdf','42.pdf','43.pdf','44.pdf','45.pdf','46.pdf','47.pdf','48.pdf','49.pdf','50.pdf','51.pdf','52.pdf','53.pdf']

# for file in file_arr:
#     pdf_merger.append(file)


# # Remove 'https://'
# output_file = 'aaa' + '.pdf'

# pdf_merger.write(output_file)
# pdf_merger.close()

# #delete all files
# import os

# for fileurl in file_arr:
#     os.remove(fileurl)

# driver.close()