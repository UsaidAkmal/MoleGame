import random #import artinya mengambil dan random adalah sebuah library
import pprint
import io

hello_massage='WELCOME TO THE GAMES'
spasi=' '
bentuk_goa = '''
   ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗
   ║     ║ ║     ║ ║     ║ ║     ║ ║     ║ ║     ║ ║     ║
   ║     ║ ║     ║ ║     ║ ║     ║ ║     ║ ║     ║ ║     ║
   ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝
'''
goa_kosong = [''.join(bentuk_goa)] * 20 # ini tetap harus kosong


# Tentukan posisi cuypy secara acak
posisi_cuypy = random.randint(1, 20)

goa=goa_kosong.copy() #ini tempat baru buat CUYPY

# Memperbanyak lubang goa dengan membuat tampilan rapih
goa[posisi_cuypy - 1] ='''
   ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗ ╔═════╗
   ║(•◡•)║ ║     ║ ║     ║ ║     ║ ║(•◡•)║ ║     ║ ║     ║
   ║ ; ; ║ ║     ║ ║     ║ ║     ║ ║ ; ; ║ ║     ║ ║     ║
   ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝ ╚═════╝
'''

tampilan_goa = '   '.join(goa_kosong)

# Menangkap output pprint ke dalam string
output = io.StringIO()
pprint.pprint(goa, stream=output)
formatted_goa = output.getvalue()  # Mengambil hasil sebagai string


# nomor_saya=4

print('''
    _________________________________________________
    |                                               |\
    |  █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█   ▀█▀ █▀█        |█\
    |  ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█   ░█░ █▄█        |██|
    |                                               |██|
    |  █▀▀ █░█ █▄█ █▀█ █▄█   █▀▀ ▄▀█ █▀▄▀█ █▀▀ █▀   |██|
    |  █▄▄ █▄█ ░█░ █▀▀ ░█░   █▄█ █▀█ █░▀░█ ██▄ ▄█   |██|
    |                                               |██|
    |  BY BANG DEA_AFRIZAL,modified from OxCircuitz |██|
    |_______________________________________________|██|
    \████████████████████████████████████████████████\█|
     \________________________________________________\|

      ''')
# if nomor_saya == 4: #ini adalah sebuah kondisi dibaca dengan jika var nomer_saya sama dengan 4, maka
#     print('KAMU BENAR NOMOR SAYA ADALAH',nomor_saya) #cetaklah string berikut
# else: #namun jika tidak, maka
#     print('KAMU SALAH !!!') #cetaklah string berikut
nama_user = input("[+] MASUKKAN NAMA KAMU: ")
print(hello_massage + ' ' + nama_user + '!!!' + f'''

   _____________________________________________________________________________
   |                                                                           |\
   | UNTUK MEMULAI GAMENYA KAMU DAPAT MEMPERHATIKAN LUBANG-LUBANG DIBAWAH,     |█|
   | KAMU HARUS MENEMUKAN 2 TIKUS TANAH YANG SEDANG                            |█|
   | BERSEMBUNYI DI BAWAH LUBANG LUBANG INI                                    |█|
   | Cobalah untuk teliti                                                      |█|
   | Dan jangan menebak-nembak !!!                                             |█|
   |                                                                           |█|
   |___________________________________________________________________________|█|
   \█████████████████████████████████████████████████████████████████████████████|


   _________________________________________________
   |                                               |\
   |   █▀▀ █░█ █▄█ █▀█ █▄█   █░█ █▀█ █░░ █▀▀ █▀    |█
   |   █▄▄ █▄█ ░█░ █▀▀ ░█░   █▀█ █▄█ █▄▄ ██▄ ▄█    |█
   |_______________________________________________|█
   |   find a cuypy, and see what happens          |█
   |_______________________________________________|█
   \█████████████████████████████████████████████████


   {tampilan_goa}


    ''')


pilihan_user= int(input("menurut kamu di BARIS lubang yang mana CUYPY berada? [1,2,3,4,5,6,..]? "))  #jika kita menggunakan function input maka nilai yang di input oleh user formatnya adalah string.

# function konfirmasi input user
konfirmasi_user=input(f'''

          |█|  ⭕ K O N F I R M A S I
          |█|
          |█|  F O K U S
          |█|  APAKAH KAMU YAKIN,BAHWA CUYPY BERADA DI BARIS {pilihan_user} ?
          |█|  kalo salah nanti di ledekin developernya lhoo, kamu milih BARIS KE {pilihan_user},yakin?
          |█|
          |█|

          |█|===> [+] JAWABAN KAMU,[Y/n]:
                      ''').lower()
# function kondisi /n
if konfirmasi_user == "n":
    print(f"YAHHH {nama_user} CUPUUU,KAMU HARUS-nya YAKIN !!!")
    exit()
# function kondisi /Y
elif konfirmasi_user == "y":
    if pilihan_user == posisi_cuypy:
        print (f'''

        {formatted_goa},


         ⢀⣴⠶⢶⣄⣀⣀⣤⣴⠶⣦⡀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⠀⠀⠀⠀
    ⠀⠀⠀⢀⣼⡟⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠈⣷⡀⠀⠀
    ⠀⠀⠀⣾⠁⠀⠀⣠⡾⠛⠉⠉⠉⠉⠉⠙⢿⣄⠹⣧⠀⠀
    ⠀⠀⠀⡇⠀⠀⠀⡏⠀⣀⣀⣀⠀⠀⠀⠀⠀⢻⡄⢸⡇⠀
    ⠀⠀⠀⡇⠀⠀⠀⡇⠀⠈⠉⠉⠁⠀⣀⣀⣀⡼⠁⢸⡇⠀
    ⠀⠀⠀⣷⡀⠀⠀⠈⠳⢦⣤⣤⣤⡾⠛⠉⠁⠀⠀⣼⠇⠀
    ⠀⠀⠀⠈⠻⣦⣄⣀⣀⣀⣀⣀⣀⣤⣶⣶⣶⣶⡾⠋⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀YAHHH AKU KETAUAN :(, {nama_user} KAMU HACKER YA ?⠀⠀⠀⠀⠀⠀⠀⠀
                    TADI AKU NGUMPET DI : DI BARIS LUBANG {posisi_cuypy}
                    kamu tadi milih BARIS lubang yang {pilihan_user} KANNNNN
                    AKU JADI MALU o_o

            ''')
    else:
        print(f'''

        {formatted_goa},


           ⢀⣠⣤⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⣠⡾⠛⠉⠁⠀⠀⠈⠙⠷⣄⠀⠀⠀⠀⠀
    ⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀
    ⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀
    ⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣧⠀
    ⢀⡟⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⢻⡄
    ⢸⡇⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⣷
    ⠘⣧⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⣶⣤⡀⠀⠀⠀⠀⣰⡟
    ⠀⠈⢳⣄⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⣰⡿⠁
    ⠀⠀⠀⠙⢷⣤⣀⠀⠈⠉⠉⠉⠉⠉⠁⠀⣀⣴⠟⠁⠀
    ⠀⠀⠀⠀⠀⠀⠉⠛⠶⢤⣤⣤⣤⣶⠶⠟⠋⠁⠀⠀⠀

                KAMU SALAH,
            KAMU BUKAN HACKER :(

            CUYPY ADA DI BARIS LUBANG {posisi_cuypy}
            KAMU MILIH BARIS LUBANG {pilihan_user}
            {nama_user} KAMU CUPU ULANG LAGI SANA !!!!

            ''')

else:
    print(f'''




          |█|  ⭕ W A R N I N G
          |█|
          |█|  INI USER NGINPUT APAAN KOCAK!!!
          |█|  {nama_user} SEPERTINYA KAMU LELAH, BERISTIRAHAT LAH!!!!
          |█|
          |█|

          |█|===> [+] ANOMALI INPUT DETECTED [{konfirmasi_user}] ULANG GAME DARI AWAL, DAN MASUKAN INPUT SESUAI OPSI!


          ''')

    exit()
         # selain dari kondisi ttersebut maka lanjutkan program
respon_pengguna=input("MASUKAN UNTUK DEVELOPER ?")

print(f'''

    |████████████████████████████████████████████████████████████████
    |█|
    |█|  {respon_pengguna}
    |█|
    |█|
    |█| TERIMAKSIH {nama_user} TELAH BERKONTRIBUSI :)
    |█|
    |█| tiada yang sempurna di dunia ini, kita harus terus berkembang
    |█| seperti layaknya game CUYPYGAMES ini,akan selalu dikembangkan oleh sang developer.
    |█|
    |█| message from creator @deaAfrizal_ and modifier @usaidAkmal_
    |█|
    |█|
    |███████████████████████████████████████████████████████████████

      ''')