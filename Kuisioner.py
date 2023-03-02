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
VM041103 - Matematika 1   				#matakuliah > option:nth-child(2)
VM041104 - Standar Internasional dan K3             
VM041105 - Sistem Pengukuran
VM041106 - Mekanika Statika
VM041107 - Ilmu Material
VM041108 - Rangkaian Listrik 1
VM041109 - Praktikum Sistem Pengukuran
VM041110 - Praktikum Rangkaian Listrik 1
VM041111 - Workshop Gambar Teknik 
VM041112 - Workshop Pemrograman 1        
VM041201 - Agama        
VM041202 - Konsep dan Wawasan Teknologi        
VM042101 - Matematika 2        
VM042102 - Perancangan Mekanika        
VM042103 - Mekanika Dinamika        
VM042104 - Rangkaian Listrik 2        
VM042105 - Elektronika Analog 1        
VM042106 - Elektronika Digital 1        
VM042107 - Elektronika Analog 1        
VM042107 - Rangkaian Listrik 2        
VM042108 - Praktikum Elektronika Digital 1        
VM042109 - Workshop Gambar Mesin        
VM042110 - Bengkel Manufaktur 1        
VM042111 - Workshop Pemograman 2        
VM043101 - Kendali Otomatis 1        
VM043102 - Matematika 3        
VM043103 - Mekanika Getaran        
VM043104 - Elektronika Analog 2        
VM043105 - Elektronika Digital 2        
VM043106 - Sistem Mikroprosesor        
VM043107 - Praktikum Sistem Mikroprosesor        
VM043108 - Praktikum Kendali Otomatis 1        
VM043109 - Elektronika Analog 2        
VM043109 - Elektronika Digital 2        
VM043110 - Workshop Bengkel Elektronika        
VM043111 - Workshop Bengkel Manufaktur 2        
VM043112 - Workshop Pemograman 3        
VM044101 - Robotika 1        
VM044102 - Kendali Otomatis 2        
VM044103 - Mekanika Fluida        
VM044104 - Instalasi Industri        
VM044105 - Elektronika Daya        
VM044106 - Mikrokontroler dan Sistem Antarmuka        
VM044107 - Kendali Otomatis 2        
VM044107 - Robotika 1        
VM044108 - Praktikum Mikrokontroler dan Sistem Antarmuka        
VM044109 - Elektronika Daya        
VM044109 - Instalasi Industri        
VM044110 - Workshop CNC1        
VM044111 - Workshop Pengolahan Sinyal        
VM044112 - Workshop Metode Numerik               

asyncio.get_event_loop().run_until_complete(main())
