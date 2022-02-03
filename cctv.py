import os,sys,time

def khamdihi_ganteng():
    os.system('clear')
    coli()
    print(' [01] Ambi link cctv publik')
    print(' [02] Mulai akses cctv ')
    print(' [00] Keluar/exit')
    khamdihi()

def coli():
    print('''\x1b[1;97m
  ______  ______  _______  ___ ___
 |      ||      ||_     _||   |   | || Author : Khamdihi xd
 |   ---||   ---|  |   |  |   |   | || Wa     : 83146061814
 |______||______|  |___|   \_____/  || Yt     : DIHI IT
 ''')

def khamdihi():
    khamdihi = input('\n [+] Chose menu : ')
    if khamdihi =='':
       print('\n [×] Silakan pilih salah satu menu')
       memek = input(' [ enter ] ')
       khamdihi_ganteng()
    elif khamdihi in ['1','01']:
       print('\n [01] http://119.2.50.116:90/#view')
       print(' [02] http://119.2.50.116:84/view/viewer_index.shtml?id=1183')
       print(' [03] http://202.150.130.137:88/control/userimage.html')
       print(' [04] http://152.26.8.85/view/index.shtml')
       print(' [05] http://103.217.216.198:8001/#view')
       print(' [06] http://103.217.216.197:8001/#view')
       print(' [07] http://103.52.16.102:82/live/index.html?Language=0')
       print(' [08] http://202.52.50.183:8001/#view')
       print(' [09] http://103.217.216.198:8000/#view')
       print(' [10] http://119.252.169.189:82/mobile.htm')
       print(' [11] http://119.252.169.189:84/')
       print(' [12] http://103.119.145.26:8001/live/index.html?Language=0')
       print(' [13] http://36.91.83.73:8081/')
       print(' [14] http://119.252.169.189:85/')
       print(' [05] http://103.245.19.243/live/index.html?Language=0')
       print('\n -->  Salin salah satu link di atas  ')
       input(' --> enter  ');khamdihi_ganteng()
    elif khamdihi in ['2','02']:
       kontol = input(' [✓] masukan link cctv : ')
       os.system('xdg-open '+kontol)
       if kontol =='':
          print(' [×] Ups kamu tidak memilih link')
          input('\n --> Enter');khamdihi_ganteng()
       colmek = input(' [?] Mau akses lagi gak y/t : ')
       if colmek == 'y':
          khamdihi_ganteng()
       elif colmek in ['t','T']:
          exit()
    elif khamdihi in ['0','00']:
       exit()
    else:
       print('\n [ tidak ada di menu ] ');khamdihi_ganteng()

if __name__ == '__main__':
   os.system('clear')
   print(' [×] Untuk mengakses cctv pilih dulu menu [1] ')
   print(' [+] Lalu salin link cctvnya ')
   print(' [×] Baru pilih nomer [2] ')
   print(' [×] lalu buka di chrome ')
   input(' ---> Press enter ')
   os.system('xdg-open https://youtube.com/channel/UCOqxx2kjYPypVct2l81Y1Jw')
   khamdihi_ganteng()
