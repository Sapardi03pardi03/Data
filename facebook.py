import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import time

urlgroup = 'https://www.facebook.com/groups/499986941509989'
login = 'https://www.facebook.com/'
mail = 'sapardi03pardi03@gmail.com'
paswd = 'Bukalapak12345'


async def main():
    browser = await launch({
        'headless': False
    })
    contex = await browser.createIncogniteBrowserContext()
    page = await contex.newPage()
    await page.goto(login)
    await page.type('#email', mail, {'delay': 15})
    await page.type('#pass', paswd, {'delay': 15})
    await page.keyboard.press('Enter')
    await page.waitForNavigation()
    await page.waitFor(1000)
    await page.goto(urlgroup)
    await page.waitFor(1000)
    elements = await page.querySelectorAll('body')

    for element in elements:
        content = await page.evaluate('(element) => element.innerHTML', element)
        soup = BeautifulSoup(content, 'html.parser')
        tes = soup.find('# jsc_c_2g > div:nth-child(1) > div:nth-child(1)')
        # print(soup.prettify())



    # await page.evaluate("""{window.scrollBy(0, document.body.scrollHeight);}""")
    await page.waitFor(20000)

asyncio.get_event_loop().run_until_complete(main())

