import os
from time import sleep


a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print(a+'\t  Enable Extra Keys on Termux ')
print(b+'\t  Web : inovasikecilku.my.id')
print(a+'+'*48)
print('\nProses..')
sleep(1)
print(b+'\n[!] Memasukan keys tambahan')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(b+'[!] harap tunggu')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close()
sleep(1)
os.system('termux-reload-settings')
print(a+'[!] Berhasil !!')
