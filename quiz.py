import os
import time
import random
from fungsi import countdown_kuis as countdown
from fungsi import else_countdown as invalid_input

# Variabel Best Score
best_score = {
    "1": {"1": 0, "2": 0, "3": 0},
    "2": {"1": 0, "2": 0, "3": 0},
    "3": {"1": 0, "2": 0, "3": 0},
    "4": {"1": 0, "2": 0, "3": 0}
}

# Menu Trivia
def menu_quiz():
    os.system('cls')
    while True:
        print("╔════════════════════════════════════════╗")
        print("║         🦊 MENU PERMAINAN 🦊           ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1. Mulai 🏁       → Ayo bermain!       ║")
        print("║ 2. Lihat Skor 🏆  → Cek kemampuanmu!   ║")
        print("║ 0. Kembali ⬅️      → Balik dulu yuk!    ║")
        print("╚════════════════════════════════════════╝")

        menu_klik = input("Pilih (0-3): ")      
        if menu_klik == "1":
            mulai()
        elif menu_klik == "2":
            lihat_skor()
        elif menu_klik == "0":
            import main
            os.system('cls')
            main.menu()
        else:
            invalid_input()
            os.system('cls')
            continue

# Mulai dan cabangnya
def mulai():
    os.system('cls')
    while True:
        print("╔════════════════════════════════════════╗")
        print("║     🦊 SI JATIM: PILIH QUIZ! 🦊        ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1. Budaya 👺        → Kenali tradisi!  ║")
        print("║ 2. Bentang Alam ⛰️  → Jelajah alam!     ║")
        print("║ 3. Wilayah 🗺️        → Temukan daerah!  ║")
        print("║ 4. Makanan 🍗        → Cari kuliner!   ║")
        print("║ 0. Kembali ⬅️        → Mundur dulu~     ║")
        print("╚════════════════════════════════════════╝")

        permainan_klik = input("Pilih Permainan (0-4): ")
        if permainan_klik in ("1","2","3","4"):
            permainan = permainan_klik

            difficulty = tingkat_kesulitan()
            if difficulty is None:
                continue

            banyak_soal = jumlah_soal()
            if banyak_soal is None:
                continue

            cabang_soal(permainan,difficulty,banyak_soal)
            break

        elif permainan_klik =="0":
            os.system('cls')
            break
        else:
            invalid_input()
            os.system('cls')
            continue

# Fungsi difficulty
def tingkat_kesulitan():
    os.system('cls')
    while True:
        print("╔════════════════════════════════════════╗")
        print("║     🦊 SI JATIM: PILIH KESULITAN! 🦊   ║")
        print("╠════════════════════════════════════════╣")
        print("║ 1. Mudah 😊        → Santai saja~      ║")
        print("║ 2. Normal 😐       → Lumayan menantang ║")
        print("║ 3. Susah 😠        → Siap jadi pro?    ║")
        print("║ 0. Kembali ⬅️       → Mundur dulu~      ║")
        print("╚════════════════════════════════════════╝")

        tingkat_kesulitan_klik = input("Pilih Tingkat Kesulitan (0-3): ")
        if tingkat_kesulitan_klik in ("1","2","3"):
            return tingkat_kesulitan_klik
        elif tingkat_kesulitan_klik =="0":
            os.system('cls')
            return None
        else:
            invalid_input()
            os.system('cls')
            continue

# Fungsi jumlah soal
def jumlah_soal():
    os.system('cls')
    while True:
        print("╔══════════════════════════════════════╗")
        print("║     🦊 SI JATIM: PILIH JUMLAH! 🦊    ║")
        print("╠══════════════════════════════════════╣")
        print("║ 1. 10 Soal        → Cepat & seru!    ║")
        print("║ 2. 15 Soal        → Cukup menantang  ║")
        print("║ 3. 20 Soal        → Petualang hebat! ║")
        print("║ 4. 30 Soal        → Tantangan besar! ║")
        print("║ 0. Kembali ⬅️      → Mundur dulu~     ║")
        print("╚══════════════════════════════════════╝")

        jumlah_soal_klik = input("Pilih Jumlah Soal (0-4): ")
        if jumlah_soal_klik in ("1","2","3","4"):
            return jumlah_soal_klik
        elif jumlah_soal_klik == "0":
            os.system('cls')
            return None
        else:
            os.system('cls')
            invalid_input()
            continue

# Cabang Permainan, Tingkat Kesulitan, dan Jumlah Soal
def cabang_soal(permainan,difficulty,banyak_soal):
    os.system('cls')
    print("""
    ╔══════════════════════════════════╗
    ║            📘 INFO KUIS          ║
    ╠══════════════════════════════════╣
    """)

    # Pilihan permainan
    if permainan == "1":
        print("    ║ Permainan        : Budaya 👺     ║")
    elif permainan == "2":
        print("    ║ Permainan        : Bentang Alam⛰️ ║")
    elif permainan == "3":
        print("    ║ Permainan        : Wilayah 🗺️     ║")
    elif permainan == "4":
        print("    ║ Permainan        : Makanan 🍗    ║")

    # Tingkat kesulitan
    if difficulty == "1":
        print("    ║ Kesulitan        : Mudah 😊      ║")
    elif difficulty == "2":
        print("    ║ Kesulitan        : Normal 😐     ║")
    elif difficulty == "3":
        print("    ║ Kesulitan        : Susah 😠      ║")

    # Jumlah soal
    if banyak_soal == "1":
        print("    ║ Jumlah Soal      : 10            ║")
    elif banyak_soal == "2":
        print("    ║ Jumlah Soal      : 15            ║")
    elif banyak_soal == "3":
        print("    ║ Jumlah Soal      : 20            ║")
    elif banyak_soal == "4":
        print("    ║ Jumlah Soal      : 30            ║")

    print("""
    ╚══════════════════════════════════╝
    """)
    countdown()
    tampil_soal(permainan, difficulty, banyak_soal)
    return

# Menjalankan permainan
from banksoal import bank_soal_quiz
def tampil_soal(permainan, difficulty, banyak_soal):
    os.system('cls')

    banyak = {"1": 10, "2": 15, "3": 20, "4": 30}[banyak_soal]
    jumlah_clue = {"1": 3, "2": 2, "3": 1}[difficulty]

    soal_list = bank_soal_quiz[permainan]["soal"]

    soal_kuis = random.sample(soal_list, banyak)

    skor = 0

    for i, item in enumerate(soal_kuis, start=1):
        os.system('cls')
        print(f"Soal {i}/{banyak}")
        print("=============================== SOAL ===============================")
        print(item["soal"])
        print("====================================================================")
        print("(Klik 0 untuk keluar dari kuis)")
        print("--------------------------------------------------------------------")

        for j in range(jumlah_clue):
            jawaban = input("\nJawaban: ").strip().lower()

            if jawaban == item["jawaban"].lower():
                print("Benar!")
                if j == 0:
                    skor += 10
                elif j == 1:
                    skor += 5
                elif j == 2:
                    skor += 2
                time.sleep(1)
                break
            elif jawaban == "0":
                os.system('cls')
                return
                
            else:
                if j < jumlah_clue - 1:
                    print(f"Salah! Clue {j+1}: {item['clue'][j]}")
                else:
                    print("Salah! Tidak ada clue lagi.")
                    print(f"Jawaban benar: {item['jawaban']}")
                time.sleep(1)

    os.system('cls')
    print("╔══════════════════════════════╗")
    print("║        🧮 SKOR KAMU          ║")
    print("╠══════════════════════════════╣")
    print(f"║      Hasil Akhir: {skor}     " + "║")
    print("╚══════════════════════════════╝")

    # Pasca permainan, cek dan simpan skor
    if skor > best_score[permainan][difficulty]:
        
        # 1. Simpan skor terbaik yang baru
        best_score[permainan][difficulty] = skor
        
        # 2. Tampilkan pesan rekor baru
        print("╔══════════════════════════════════════╗")
        print("║ ⭐ REKOR BARU! ⭐                    ║")
        print("╠══════════════════════════════════════╣")
        print("║ Skor terbaik yang pernah kamu raih!🔥║")
        print("║ Luar biasa! Kamu makin jago!         ║")
        print("╚══════════════════════════════════════╝")
        
    else:
        # Tampilkan pesan belum mengalahkan rekor
        print("╔══════════════════════════════════════╗")
        print("║ 😔 BELUM MENGALAHKAN REKOR NIH…      ║")
        print("╠══════════════════════════════════════╣")
        print("║ Tetap semangat! Coba lagi ya~ 💪     ║")
        print("╚══════════════════════════════════════╝")

    input("Tekan Enter untuk kembali...")

    os.system('cls')


# Lihat skor dan cabangnya

def lihat_skor():
    os.system('cls')
    while True:

        # Header kotak
        print("╔════════════════════════════════════════╗")
        print("║            🏆 SKOR ANDA 🏆             ║")
        print("╚════════════════════════════════════════╝")

        nama_kategori = {
            "1": "Budaya 👺",
            "2": "Bentang Alam ⛰️",
            "3": "Wilayah 🗺️",
            "4": "Makanan 🍗"
        }

        nama_diff = {
            "1": "Mudah 😊",
            "2": "Normal 😐",
            "3": "Susah 😠"
        }

        # Isi kotak
        for kategori in best_score:
            print(f" 📚 {nama_kategori[kategori]}")
            for diff in best_score[kategori]:
                skor = best_score[kategori][diff]
                print(f"    - {nama_diff[diff]} : {skor}")
            print("")  # garis kosong dalam kotak

        input("Tekan Enter untuk kembali...")
        os.system('cls')
        menu_quiz()

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