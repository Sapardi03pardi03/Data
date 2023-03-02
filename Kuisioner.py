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
        'slowMo': 5
    })
    page = await browser.newPage()
    await page.goto(URL + login)
    await page.type('#username', usr,{'delay': 15})
    await page.type('#password', pwd,{'delay': 15})
    await page.keyboard.press('Enter')
    await page.waitForNavigation()
    await page.waitFor(500)
    await page.goto(URL + logbook)

    await page.click('#jam_mulai')
    await page.waitForNavigation()
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

    await page.type('#kegiatan', kata,{'delay': 5})
    await page.waitFor(1000)

    await page.click('#matakuliah > option:nth-child(2)')
    await page.waitFor(100000)

    # SesKul = input("Apakah Sesuai Kuliah ? [Y/N]")
    # if SesKul == 'Y' or SesKul == 'y':
    #     await page.click('#sesuai_kuliah1')
    #     await page.waitFor(10000)
    # elif SesKul == 'N' or SesKul == 'n':
    #     await page.click('#sesuai_kuliah2')
    #     await page.waitFor(10000)



    # await page.click('#matakuliah')
    # print("\n\n List Mata Kuliah ")
    # print(" 1.  VM041103 - Matematika 1 ")
    # print(" 2.  VM041104 - Standar Internasional dan K3")
    # print(" 3.  VM041105 - Sistem Pengukuran")
    # print(" 4.  VM041104 - Standar Internasional dan K3")
    # print(" 5.  VM041103 - Matematika 1 ")
    # print(" 6.  VM041104 - Standar Internasional dan K3")
    # print(" 7.  VM041103 - Matematika 1 ")
    # print(" 8.  VM041104 - Standar Internasional dan K3")
    # print(" 9.  VM041103 - Matematika 1 ")
    # print(" 10. VM041104 - Standar Internasional dan K3")
    # print(" 11. VM041103 - Matematika 1 ")
    # print(" 12. VM041104 - Standar Internasional dan K3")
    # print(" 13. VM041103 - Matematika 1 ")
    # print(" 14. VM041104 - Standar Internasional dan K3")
    # print(" 15. VM041103 - Matematika 1 ")
    # print(" 16. VM041104 - Standar Internasional dan K3")


    # elements = await page.querySelectorAll('body')
    # for element in elements:
    #     content = await page.evaluate('(element) => element.innerHTML', element)
    #     soup = BeautifulSoup(content, 'html.parser')
    #     print(soup.prettify())

    # await browser.close()


asyncio.get_event_loop().run_until_complete(main())
