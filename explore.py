import os
import sys
import time
import re
from banksoal import list_guardian
from banksoal import penjabaran_wilayah

# ---------------------------
# Cross-platform single key
# ---------------------------
if os.name == 'nt':
    import msvcrt

    def getch():
        ch = msvcrt.getch()
        # arrow keys come as two bytes; we ignore arrows
        if ch in b'\x00\xe0':
            msvcrt.getch()
            return ''
        try:
            return ch.decode('utf-8')
        except:
            return ''
else:
    import tty
    import termios

    def getch():
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
            return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

# ---------------------------
# Utilities
# ---------------------------
CSI = '\033['
RESET = '\033[0m'
GRAY = '\033[90m'
BOLD = '\033[1m'

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def enable_ansi_on_windows():
    # best-effort: modern Windows terminals support ANSI; on older ones no-op
    if os.name == 'nt':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            pass

# ---------------------------
# Original map (from upload)
# ---------------------------
MAP_TEXT = r"""
--------------------------------------------------------------------------------------------------------------------------------------------------------
|                                                                                                                                                      |
|         Tuban                                                                                                         Pamekasan                      |
|                                                         Gresik                                           Sampang                        Sumenep      |
|                                                                                            Bangkalan                                                 |
|     Bojonegoro                  Lamongan                                 Surabaya                                                                    |
|                                                                                                                                                      |
|                                                             Mojokerto                                                                                |
|                                                                                                                                                      |
|                                          Jombang                              Sidoarjo                                                               |    
| Ngawi                                                                                                                                                |
|                             Nganjuk                                                      Pasuruan                                                    |
|               Madiun                                                 Batu                                                                            |
|                                                                                                 Probolinggo                              Situbondo   |
|    Magetan                                   Kediri                                                                                                  |    
|                                                                                                                              Bondowoso               |
|          Ponorogo                                                                                                                                    |
|                                                                                                                                                      |
|                                     Tulunggagung                              Malang                             Jember                              | 
|   Pacitan         Trenggalek                                  Blitar                         Lumajang                              Banyuwangi        |
|                                                                                                                                                      |
--------------------------------------------------------------------------------------------------------------------------------------------------------
""".strip('\n')

# ---------------------------
# Parse map into grid
# ---------------------------
lines = MAP_TEXT.splitlines()
height = len(lines)
width = max(len(l) for l in lines)
grid = [list(line.ljust(width)) for line in lines]

# ---------------------------
# Find "names" on map: now each word individually using word boundaries
# ---------------------------
name_spans = []  # each: dict{name, y, x1, x2, text}
pattern = re.compile(r'\b[A-Za-z]+\b')  # individual words

for y, line in enumerate(lines):
    for m in pattern.finditer(line):
        word = m.group(0)
        x1, x2 = m.start(), m.end() - 1
        # store each word as a separate name
        name_spans.append({
            'text': word,
            'y': y,
            'x1': x1,
            'x2': x2,
            'visited': False
        })

# No need to merge since each is individual; but remove duplicates if any (same word at same pos)
unique_spans = []
seen = set()
for s in name_spans:
    key = (s['text'], s['y'], s['x1'], s['x2'])
    if key in seen:
        continue
    seen.add(key)
    unique_spans.append(s)
name_spans = unique_spans

# Sort by y then x for deterministic ordering
name_spans.sort(key=lambda s: (s['y'], s['x1']))

# For convenience, build map of coordinates -> name index
coord_to_name = {}
for idx, s in enumerate(name_spans):
    for x in range(s['x1'], s['x2'] + 1):
        coord_to_name[(s['y'], x)] = idx

# ---------------------------
# Player initial position: choose near center or a free space
# ---------------------------
# Find a space ' ' that's not boundary (not '|' or '-') and not letter
player_x = None
player_y = None
for y in range(height):
    for x in range(width):
        ch = grid[y][x]
        if ch == ' ':
            # ensure not border row/col
            if y > 0 and y < height-1 and x > 0 and x < width-1:
                player_x = x
                player_y = y
                break
    if player_x is not None:
        break

if player_x is None:
    # fallback
    player_y = height // 2
    player_x = width // 2

# ---------------------------
# Helper to render map
# ---------------------------
def render_map(player_x, player_y, highlight_names=True):
    # build copy
    out_lines = []
    for y in range(height):
        line_chars = []
        for x in range(width):
            ch = grid[y][x]
            # if this coordinate belongs to a name, and that name visited -> show gray
            if (y, x) in coord_to_name:
                idx = coord_to_name[(y, x)]
                s = name_spans[idx]
                if s['visited']:
                    # preserve character but in gray
                    line_chars.append(GRAY + ch + RESET)
                else:
                    line_chars.append(ch)
            else:
                line_chars.append(ch)
        out_lines.append(''.join(line_chars))
    # place player (overwrite)
    # convert line to list to replace char
    display = out_lines[:]
    # compute index if inside bounds
    if 0 <= player_y < height and 0 <= player_x < width:
        # Need to replace the raw character at that position, but display may contain ANSI sequences.
        # Simplify: reconstruct display from grid but when at player position print '8' (in bold)
        display = []
        for y in range(height):
            pieces = []
            for x in range(width):
                if x == player_x and y == player_y:
                    pieces.append(BOLD + '8' + RESET)
                else:
                    ch = grid[y][x]
                    if (y, x) in coord_to_name and name_spans[coord_to_name[(y,x)]]['visited']:
                        pieces.append(GRAY + ch + RESET)
                    else:
                        pieces.append(ch)
            display.append(''.join(pieces))
    # Print
    print('\n'.join(display))

# ---------------------------
# Interaction when visiting a name
# ---------------------------
def run_event_for_name(idx):
    s = name_spans[idx]
    # Ambil nama yang akan digunakan sebagai kunci dictionary
    name_key = s['text'].strip()
    
    guardian_data = list_guardian.get(name_key)
    name_key_clean = name_key.strip()
    event_data = penjabaran_wilayah.get(name_key, {
        "sejarah": f"Data sejarah {name_key} tidak tersedia. (Data default)",
        "budaya": f"Data budaya {name_key} tidak tersedia. (Data default)",
        "Makanan": f"Data makanan khas {name_key} tidak tersedia. (Data default)",
        "Adat": f"Data adat {name_key} tidak tersedia. (Data default)",
        "Tokoh_terkenal": f"Data tokoh terkenal {name_key} tidak tersedia. (Data default)",
        "bentang_alam": f"Data bentang alam {name_key} tidak tersedia. (Data default)"
    })

    if not guardian_data:
        clear()
        print(BOLD + f"~ Tidak ada Guardian untuk: {name_key} ~" + RESET)
        print("Anda diizinkan masuk tanpa pertanyaan.")
        s['visited'] = True
    else:
        # Tampilkan pembukaan dan pertanyaan
        clear()
        print(BOLD + f"~ Anda mendekati: {name_key} ~" + RESET)
        print("--------------------------------------------------")
        print(guardian_data.get('Pembukaan', f"Guardian {name_key}: Sampaikan tujuanmu!"))
        print("--------------------------------------------------")
        print()
        
        question = guardian_data.get('Pertanyaan', "Apa yang Anda cari?")
        correct_answer = guardian_data.get('Jawaban', "").strip()

        print(BOLD + ">>> PERTANYAAN DARI GUARDIAN <<<" + RESET)
        print(f"Soal: {question}")
        print()
        
        # Minta jawaban user (menggunakan input() untuk jawaban multi-karakter)
        # Note: Ini akan menggunakan input standar, bukan getch()
        user_answer = input("Jawab (ketik jawaban Anda, lalu Enter): ").strip()
        
        # Cek jawaban (case-insensitive)
        if user_answer.lower() == correct_answer.lower():
            # JAWABAN BENAR
            clear()
            print(BOLD + f"~ SELAMAT! Jawaban Benar! Anda berhasil melewati Guardian {name_key}! ~" + RESET)
            print("--------------------------------------------------")
            print(guardian_data.get('Penutupan', f"Guardian {name_key}: Selamat, Anda lulus."))
            print("--------------------------------------------------")
            print()
            
            # Tandai visited HANYA jika berhasil (sehingga daerah akan menjadi abu-abu)
            s['visited'] = True
            
        else:
            # JAWABAN SALAH
            clear()
            print(BOLD + "~ GAGAL! Jawaban Salah atau tidak dikenali! ~" + RESET)
            print()
            print(f"Anda tidak diizinkan masuk ke {name_key} dan dikembalikan ke peta. Coba lagi!")
            print()
            print("Tekan tombol apa saja untuk melanjutkan...")
            getch()
            return # Kembali ke loop peta tanpa menampilkan info
    
    # ---------------------------
    # TAHAP 2: TAMPILKAN INFORMASI (Hanya dijalankan jika s['visited'] = True)
    # ---------------------------
    
    if s['visited']:
        print(BOLD + f"~ INFORMASI DAERAH: {name_key_clean} ~" + RESET)
        print()
    
    # --- Tampilkan Informasi Baru ---
    
    # Sejarah Singkat
    print(BOLD + "Sejarah Singkat🌳" + RESET)
    print(event_data['sejarah'])
    print()
    
    # Budaya Terkenal
    print(BOLD + "Budaya Terkenal🎭" + RESET)
    print(f"- {event_data['budaya']}")
    print()
    
    # Makanan Khas
    print(BOLD + "Makanan Khas🍲" + RESET)
    print(f"- {event_data['Makanan']}")
    print()

    # Adat Istiadat
    print(BOLD + "Adat Istiadat🎎" + RESET)
    print(f"- {event_data['Adat']}")
    print()

    # Tokoh Terkenal
    print(BOLD + "Tokoh Terkenal👤" + RESET)
    print(f"- {event_data['Tokoh_terkenal']}")
    print()

    # Bentang Alam Terkenal
    print(BOLD + "Bentang Alam Terkenal🏞️" + RESET)
    print(f"- {event_data['bentang_alam']}")
    print()
    
    # --- Interaksi Sederhana (Hanya Enter) ---
    print()
    print("Tekan **Enter** untuk melanjutkan perjalanan...")
    getch()
    
    # wait for Enter
    while True:
        ch = getch()
        
        if not ch:
            continue
            
        if ch in ('\r', '\n'):
            break # Keluar dari loop dan kembali ke peta
        else:
            # Abaikan semua tombol lain yang bukan Enter
            pass
        
    # done, return to map
    clear()
# ---------------------------
# Movement loop
# ---------------------------
def can_move_to(x, y):
    if not (0 <= x < width and 0 <= y < height):
        return False
    target = grid[y][x]
    # can move into spaces OR into letters (to trigger) but not into border characters like '|' '-' or others
    if target == ' ' or re.match(r'[A-Za-z]', target):
        return True
    return False

def main_loop():
    enable_ansi_on_windows()
    clear()
    visited_count = 0
    total_names = len(name_spans)
    print("Peta interaktif Jawa Timur — kontrol W/A/S/D. Tekan g untuk keluar.")
    time.sleep(1.0)
    clear()

    while True:
        # 1. RENDER PETA DAN STATUS
        render_map(player_x, player_y)
        # show status
        visited_count = sum(1 for s in name_spans if s['visited'])
        print()
        print(f"Visited: {visited_count}/{total_names} (kunjungi semua nama untuk menyelesaikan)")
        print("W,A,S,D untuk bergerak.")
        print("Tekan g untuk keluar⬅️")

        # 2. TUNGGU INPUT
        ch = getch()
        if not ch:
            continue
        ch = ch.lower()

        # 3. PROSES INPUT 'g'
        if ch == 'g':
            import main
            os.system('cls')
            main.menu()
            return # Keluar dari loop

        dx = dy = 0
        if ch == 'w':
            dy = -1
        # ... (lanjutkan untuk s, a, d) ...
        elif ch == 's':
            dy = 1
        elif ch == 'a':
            dx = -1
        elif ch == 'd':
            dx = 1
        else:
            # Jika tombol bukan pergerakan, ulangi loop tanpa membersihkan layar
            continue
        
        # 4. HAPUS LAYAR SETELAH INPUT PERGERAKAN DITERIMA
        clear() 

        # 5. PERHITUNGAN DAN PEMBARUAN POSISI
        new_x = player_x + dx
        new_y = player_y + dy
        # ... (lanjutkan logika can_move_to) ...
        if not (0 <= new_x < width and 0 <= new_y < height):
            continue
        if not can_move_to(new_x, new_y):
            continue
            
        # Pindahkan pemain
        globals()['player_x'] = new_x
        globals()['player_y'] = new_y
        
        # 6. CEK EVENT
        key = (new_y, new_x)
        if key in coord_to_name:
            idx = coord_to_name[key]
            if not name_spans[idx]['visited']:
                run_event_for_name(idx)
                # ... (lanjutkan logika penyelesaian) ...
                if sum(1 for s in name_spans if s['visited']) >= total_names:
                    clear()
                    print("Selamat! Anda telah mengunjungi semua nama pada peta.")
                    break
        
        # JIKA BERHASIL BERGERAK, LOOP BERLANJUT
        # Dan karena kita sudah memanggil clear() di atas (di langkah 4), 
        # maka iterasi berikutnya akan mencetak peta baru di posisi paling atas.

# ---------------------------
# Run
# ---------------------------
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