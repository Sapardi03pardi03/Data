import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
import time

URL = 'https://online.mis.pens.ac.id/'
login = 'index.php?Login=1&halAwal=1'
logbook = 'mEntry_Logbook_KP1.php'

usr = 'madeadit23@me.student.pens.ac.id'
pwd = 'TheDark12345'
JamMulai = '08:00'
JamSelesai = '17:00'
kata = 'melakukan pengambilan data Cycle dan perubahan program dari RTC untuk menampilkan di halaman login agar nantinya dapat dengan mudah di screp datanya dan di olah menjadi ke digital untuk switch tombol dan perhitungan Cycling nya'


async def main():
    browser = await launch({
        'headless': False,
        'slowMo': 20
    })
    page = await browser.newPage()
    await page.goto(URL + login)
    await page.type('#username', usr)
    await page.type('#password', pwd)
    await page.keyboard.press('Enter', {'delay': 900})
    await page.waitForNavigation()
    await page.waitFor(500)
    await page.goto(URL + logbook)

    await page.click('#jam_mulai')
    await page.keyboard.down('Control')
    await page.keyboard.press('KeyA')
    await page.keyboard.press('Backspace')
    await page.keyboard.up('Control')

    await page.type('#jam_mulai', JamMulai)
    await page.waitFor(1000)

    await page.click('#jam_selesai')
    await page.keyboard.down('Control')
    await page.keyboard.press('KeyA')
    await page.keyboard.press('Backspace')
    await page.keyboard.up('Control')

    await page.type('#jam_selesai', JamSelesai)
    await page.waitFor(1000)

    await page.click('#kegiatan')
    await page.keyboard.down('Control')
    await page.keyboard.press('KeyA')
    await page.keyboard.press('Backspace')
    await page.keyboard.up('Control')

    await page.type('#kegiatan', kata)
    await page.waitFor(1000)
    await page.click('#sesuai_kuliah1')
    await page.waitFor(10000)

    elements = await page.querySelectorAll('body')
    for element in elements:
        content = await page.evaluate('(element) => element.innerHTML', element)
        soup = BeautifulSoup(content, 'html.parser')
        print(soup.prettify())

    # await browser.close()


asyncio.get_event_loop().run_until_complete(main())
