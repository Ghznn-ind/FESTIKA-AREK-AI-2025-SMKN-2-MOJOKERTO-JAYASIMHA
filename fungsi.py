import time
import os
import sys

def countdown_kuis():
    for detik in range(3,0,-1):
        output = f"\rKuis dimulai {detik} detik lagi"
        print(output, end='')
        sys.stdout.flush() 
        time.sleep(1)

def else_countdown():
    os.system('cls')
    print("Input tidak valid, coba lagi...")
    time.sleep(1.8)

if __name__ == "__main__":
    from main import menu
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