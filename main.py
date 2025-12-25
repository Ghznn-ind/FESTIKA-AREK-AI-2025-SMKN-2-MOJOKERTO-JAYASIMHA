import os
import sys
from fungsi import else_countdown as invalid_input
import story_mode as sm
import quiz
import explore

# Menu Utama
def menu():
    os.system('cls')
    while True:
        print("╔══════════════════════════════════════════════╗")
        print("║     🌟 SELAMAT DATANG DI PETUALANGAN! 🌟     ║")
        print("╠══════════════════════════════════════════════╣")
        print("║  1. Quiz 📜         → Uji kepintaranmu       ║")
        print("║  2. Story Mode 🚂   → Ikuti ceritanya!       ║")
        print("║  3. Explore 🧭      → Jelajahi dunia!        ║")
        print("║  0. Keluar ⬅️       → Sampai jumpa!           ║")
        print("╚══════════════════════════════════════════════╝\n")
        
        main_klik = input("Pilih (0-2): ")
        if main_klik == "1":
            quiz.menu_quiz()
        elif main_klik == "2":
            sm.menu_utama()
        elif main_klik == "3":
            explore.main_loop()
        elif main_klik == "0":
            os.system('cls')
            print("\n╔═════════════════════════════════════════╗")
            print("║           🦊 SI JATIM PAMIT!            ║")
            print("╠═════════════════════════════════════════╣")
            print("║ Terima kasih, Petualang Cilik!          ║")
            print("║ Kamu hebat hari ini! 🌟                 ║")
            print("║ Sampai jumpa di petualangan berikutnya! ║")
            print("║ Si Jatim akan menunggumu lagi~ 😄       ║")
            print("╚═════════════════════════════════════════╝\n")
            sys.exit()
        else:
            invalid_input()
            os.system('cls')
            continue

# Menjalankan Program
if __name__ == "__main__":
    os.system('cls')
    print("\n╔══════════════════════════════════════════════╗")
    print("║           🌟 NGULIK SI JATIM 🌟              ║")
    print("║==============================================║")
    print("║  Selamat datang, Petualang Cilik!            ║")
    print("║  Di sini kamu bisa menjelajahi Jawa Timur,   ║")
    print("║  bertemu tempat-tempat seru, menjawab kuis,  ║")
    print("║  dan mengumpulkan pengalaman baru!           ║")
    print("║                                              ║")
    print("║  Siap berangkat? Ayo kita mulai! 🚀          ║")
    print("╚══════════════════════════════════════════════╝")
    input("👉 Tekan ENTER untuk mulai petualangan! ")
    menu()