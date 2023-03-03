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

expect_value = '26111'

expect_value1 = '26105'     #Matematika 1
expect_value2 = '26106'     #Standar Internasional dan K3
expect_value3 = '26107'     #Sistem Pengukuran
expect_value4 = '26108'     #Mekanika Statika
expect_value5 = '26109'     #Ilmu Material
expect_value6 = '26110'     #Rangkaian Listrik 1
expect_value7 = '26111'     #Praktikum Sistem Pengukuran
expect_value8 = '26112'     #Praktikum Rangkaian Listrik 1
expect_value9 = '26113'     #Workshop Gambar Teknik
expect_value10 = '26114'    #Workshop Pemrograman 1
expect_value11 = '26103'    #Agama
expect_value12 = '26104'    #Konsep dan Wawasan Teknologi
expect_value13 = '26589'    #Matematika 2
expect_value14 = '26591'    #Perancangan Mekanika
expect_value15 = '26590'    #Mekanika Dinamika
expect_value16 = '26583'    #Rangkaian Listrik 2
expect_value17 = '26586'    #Elektronika Analog 1
expect_value18 = '26582'    #Elektronika Digital 1
expect_value19 = '26587'    #Elektronika Analog 1  
expect_value20 = '26581'    #Rangkaian Listrik 2
expect_value21 = '26585'    #Praktikum Elektronika Digital 1
expect_value22 = '26584'    #Workshop Gambar Mesin
expect_value23 = '26588'    #Bengkel Manufaktur 1
expect_value24 = '26592'    #Workshop Pemograman 2
expect_value25 = '27553'    #Kendali Otomatis 1
expect_value26 = '27554'    #Matematika 3
expect_value27 = '27559'    #Mekanika Getaran
expect_value28 = '27557'    #Elektronika Analog 2
expect_value29 = '27558'    #Elektronika Digital 2
expect_value30 = '27565'    #Sistem Mikroprosesor
expect_value31 = '27562'    #Praktikum Sistem Mikroprosesor
expect_value32 = '27563'    #Praktikum Kendali Otomatis 1
expect_value33 = '27560'    #Elektronika Analog 2
expect_value34 = '27561'    #Elektronika Digital 2
expect_value35 = '27556'    #Workshop Bengkel Elektronika
expect_value36 = '27564'    #Workshop Bengkel Manufaktur 2
expect_value37 = '27555'    #Workshop Pemograman 3
expect_value38 = '27905'    #Robotika 1
expect_value39 = '27901'    #Kendali Otomatis 2
expect_value40 = '27902'    #Mekanika Fluida
expect_value41 = '27903'    #Instalasi Industri
expect_value42 = '27909'    #Elektronika Daya
expect_value43 = '27900'    #Mikrokontroler dan Sistem Antarmuka
expect_value44 = '27913'    #Kendali Otomatis 2
expect_value45 = '27907'    #Robotika 1
expect_value46 = '27912'    #Praktikum Mikrokontroler dan Sistem Antarmuka
expect_value47 = '27910'    #Elektronika Daya
expect_value48 = '27908'    #Instalasi Industri
expect_value49 = '27904'    #Workshop CNC1
expect_value50 = '27906'    #Workshop Pengolahan Sinyal
expect_value51 = '27911'    #Workshop Metode Numerik

async def main():
    browser = await launch({
        'headless': False,
        'slowMo': 5
    })
    contex = await browser.createIncogniteBrowserContext()
    page = await contex.newPage()
    await page.goto(URL + login)
    await page.type('#username', usr,{'delay': 10})
    await page.type('#password', pwd,{'delay': 10})
    await page.click('.btn-submit')
    await page.waitFor(500)
    await page.goto(URL + logbook)
    await page.waitFor(5000)

    ##Opsi JAM Mulai
    await page.click('#jam_mulai')
    await page.keyboard.down('Control')
    await page.keyboard.press('KeyA')
    await page.keyboard.press('Backspace')
    await page.keyboard.up('Control')
    await page.type('#jam_mulai', JamMulai)
    await page.waitFor(1000)

    ##Opsi Jam Selesai
    await page.click('#jam_selesai')
    await page.keyboard.down('Control')
    await page.keyboard.press('KeyA')
    await page.keyboard.press('Backspace')
    await page.keyboard.up('Control')
    await page.type('#jam_selesai', JamSelesai)
    await page.waitFor(1000)

    #Opsi Kegiatan
    await page.click('#kegiatan')
    await page.keyboard.down('Control')
    await page.keyboard.press('KeyA')
    await page.keyboard.press('Backspace')
    await page.keyboard.up('Control')
    await page.type('#kegiatan', kata,{'delay': 5})
    await page.waitFor(1000)

    ##Opsi Sesuai Kuliah Ya Atau Tidak
    SesKul = input("Apakah Sesuai Kuliah ? [Y/N] : ")
    if SesKul == 'Y' or SesKul == 'y':
        await page.click('#sesuai_kuliah1')
        await page.waitFor(500)
    elif SesKul == 'N' or SesKul == 'n':
        await page.click('#sesuai_kuliah2')
        await page.waitFor(500)

    ##Opsi Matakuliah yg dipilih
    print("\n\n List Mata Kuliah ")
    print(" 1.      VM041103 - Matematika 1 ")
    print(" 2.      VM041104 - Standar Internasional dan K3")
    print(" 3.      VM041105 - Sistem Pengukuran")
    print(" 4.      VM041106 - Mekanika Statika        ")
    print(" 5.      VM041107 - Ilmu Material   ")
    print(" 6.      VM041108 - Rangkaian Listrik 1   ")
    print(" 7.      VM041109 - Praktikum Sistem Pengukuran   ")
    print(" 8.      VM041110 - Praktikum Rangkaian Listrik 1 ")
    print(" 9.      VM041111 - Workshop Gambar Teknik ")
    print(" 10.     VM041112 - Workshop Pemrograman 1  ")
    print(" 11.     VM041201 - Agama  ")
    print(" 12.     VM041202 - Konsep dan Wawasan Teknologi ")
    print(" 13.     VM042101 - Matematika 2 ")
    print(" 14.     VM042102 - Perancangan Mekanika")
    print(" 15.     VM042103 - Mekanika Dinamika   ")
    print(" 16.     VM042104 - Rangkaian Listrik 2        ")
    print(" 17.     VM042105 - Elektronika Analog 1  ")
    print(" 18.     VM042106 - Elektronika Digital 1 ")
    print(" 19.     VM042107 - Elektronika Analog 1   ")
    print(" 20.     M042107  - Rangkaian Listrik 2 ")
    print(" 21.     VM042108 - Praktikum Elektronika Digital 1 ")
    print(" 22.     VM042109 - Workshop Gambar Mesin    ")
    print(" 23.     VM042110 - Bengkel Manufaktur 1  ")
    print(" 24.     VM042111 - Workshop Pemograman 2    ")
    print(" 25.     VM043101 - Kendali Otomatis 1  ")
    print(" 26.     VM043102 - Matematika 3   ")
    print(" 27.     VM043103 - Mekanika Getaran    ")
    print(" 28.     VM043104 - Elektronika Analog 2   ")
    print(" 29.     VM043105 - Elektronika Digital 2  ")
    print(" 30.     VM043106 - Sistem Mikroprosesor  ")
    print(" 31.     VM043107 - Praktikum Sistem Mikroprosesor ")
    print(" 32.     VM043108 - Praktikum Kendali Otomatis 1   ")
    print(" 33.     VM043109 - Elektronika Analog 2      ")
    print(" 34.     VM043109 - Elektronika Digital 2   ")
    print(" 35.     VM043110 - Workshop Bengkel Elektronika  ")
    print(" 36.     VM043111 - Workshop Bengkel Manufaktur 2   ")
    print(" 37.     VM043112 - Workshop Pemograman 3     ")
    print(" 38.     VM044107 - Robotika 1         ")
    print(" 39.     VM044102 - Kendali Otomatis 2 ")
    print(" 40.     VM044103 - Mekanika Fluida   ")
    print(" 41.     VM044104 - Instalasi Industri  ")
    print(" 42.     VM044105 - Elektronika Daya   ")
    print(" 43.     VM044106 - Mikrokontroler dan Sistem Antarmuka  ")
    print(" 44.     VM044107 - Kendali Otomatis 2 ")
    print(" 45.     VM044107 - Robotika 1             ")
    print(" 46.     VM044108 - Praktikum Mikrokontroler dan Sistem Antarmuka   ")
    print(" 47.     VM044109 - Elektronika Daya    ")
    print(" 48.     VM044109 - Instalasi Industri  ")
    print(" 49.     VM044110 - Workshop CNC1     ")
    print(" 50.     VM044111 - Workshop Pengolahan Sinyal   ")
    print(" 51.     VM044112 - Workshop Metode Numerik")


    kuliahmata = input("Masukan Jenis Matakuliah[1 - 16]: ")


    # tag_element = await page.querySelector('#matakuliah')
    # options_text = await tag_element.querySelectorAllEval(
    #     'option',
    #     'options => options.map(option => option.value)'
    # )
    # if expect_value in options_text:
    
    await page.querySelectorEval('#matakuliah', f'element => element.value = "{expect_value}"')
    # await page.querySelectorEval('#matakuliah', 'element => element.value')

    #Opsi Setuju
    await page.click('#Setuju')

    #Opsi Simpan
    await page.click('input[value="Simpan"]')
    await page.waitFor(100000)




    # elements = await page.querySelectorAll('body')
    # for element in elements:
    #     content = await page.evaluate('(element) => element.innerHTML', element)
    #     soup = BeautifulSoup(content, 'html.parser')
    #     print(soup.prettify())

    # await browser.close()


asyncio.get_event_loop().run_until_complete(main())
