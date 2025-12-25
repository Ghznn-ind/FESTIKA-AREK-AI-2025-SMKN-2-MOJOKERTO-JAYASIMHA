import time
import os
import sys
from fungsi import else_countdown as invalid_input

# Fungsi mengetik efek per karakter
def type_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def check_interrupt():
    global SKIP_DELAY
    
    # 1. Cek status: Jika sudah di-skip, langsung lanjut (return 'continue')
    if SKIP_DELAY > 0.001:
        
        # 2. Tampilkan prompt interupsi
        # Delay 0.0001 memastikan prompt ini muncul instan
        type_text("\n[Ketik Enter untuk lanjut atau 'm' (menu utama)],", delay=0.0001)
        
        # 3. Menerima input (input() adalah fungsi yang 'blocking')
        command = input("Perintah: ").lower()
        
        # 4. Logika Perintah
        if command == 'm':
            return 'menu' 
        
        else:
            # Mengaktifkan mode skip: mengubah kecepatan ketik global
            return 'skip'
        
    # 5. Lanjut (baik karena Enter, atau karena sudah dalam mode skip)
    return 'continue'

# Clear layar
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Input nama pemeran
def input_nama():
    global nama_laki, nama_perempuan
    clear()
    print("╔══════════════════════════════════════════════════╗")
    print("║     🧑 MASUKKAN NAMA PEMERAN LAKI-LAKI 🧑        ║")
    print("╠══════════════════════════════════════════════════╣")
    print("║  Nama pemeran laki-laki 👨 (default: Wawan)      ║")
    print("╚══════════════════════════════════════════════════╝")
    nama_laki = input("👉 Masukkan nama: ") or "Wawan"

    print("\n╔═════════════════════════════════════════════════╗")
    print("║     👩 MASUKKAN NAMA PEMERAN PEREMPUAN 👩       ║")
    print("╠═════════════════════════════════════════════════╣")
    print("║  Nama pemeran perempuan (default: Hani)         ║")
    print("╚═════════════════════════════════════════════════╝")
    nama_perempuan = input("👉 Masukkan nama: ") or "Hani"
    # Data wilayah
    global wilayahs
    wilayahs = [
     {
        # Kabupaten Ponorogo
        "nama": "Ponorogo",
        "story": [
            "\n"
            f"Kereta berhenti di Ponorogo pada sore hari. {nama_laki} dan {nama_perempuan} turun dari gerbong, merasakan udara yang sejuk dan wangi tanah basah setelah hujan ringan. "
            f"Suasana kota ramai dengan warga yang sibuk berjalan pulang atau mengantar anak-anak ke rumah. Tiba-tiba mata {nama_laki} tertuju pada sekelompok orang yang tengah menyiapkan sebuah pertunjukan. "
            f"Topeng besar berbentuk singa, dihiasi bulu-bulu warna-warni, siap dipentaskan.\n"
            "\n"
            f'"{nama_perempuan}, lihat itu! Topengnya besar banget, kok bisa ditahan sama orangnya?” tanya {nama_laki} sambil terkesima.\n'
            "\n"
            f'"Itu Reog Ponorogo, {nama_laki}. Tradisi ini sudah ada turun-temurun. Para penarinya bisa menahan topeng berat itu sambil menari. Mereka kuat banget, lincah, dan penuh semangat,” jawab {nama_perempuan} sambil tersenyum.\n'
            "\n"
            f'"{nama_laki} dan {nama_perempuan} duduk di sisi alun-alun, mengamati para penari yang berlatih. Anak-anak Ponorogo berlarian sambil menonton, tertawa, dan mencoba menirukan gerakan-gerakan para penari.\n'
            "\n"
            f'Musik gending yang mengiringi pertunjukan mengalun riang, dan setiap gerakan para penari menceritakan legenda kepahlawanan dan cerita rakyat yang penuh nilai moral.\n'
            "\n"
            f'"{nama_perempuan}, aku nggak nyangka tariannya seru banget dan penuh makna. Anak-anak pasti bisa belajar keberanian dan kekuatan dari sini,” kata {nama_laki} sambil memandang kagum.\n'
            "\n"
            f'"Iya {nama_laki}, budaya itu bukan cuma hiburan, tapi juga cara mengajarkan nilai-nilai penting kepada generasi muda. Anak-anak bisa belajar sambil bersenang-senang,” jawab {nama_perempuan}\n'
            "\n"
            f"Mereka berjalan mendekat, melihat pedagang yang menjual miniatur Reog, topeng, dan kostum kecil untuk anak-anak. {nama_laki} ikut membeli satu miniatur sebagai kenang-kenangan,"
            "dan mereka berdua pulang sambil tersenyum, merasa sudah belajar tentang salah satu warisan budaya terbesar di Jawa Timur.\n"
        ],

        "penjelasan":   "Reog Ponorogo adalah seni pertunjukan tradisional khas Ponorogo, Jawa Timur. "
                        "Pertunjukan ini menggabungkan tari, musik, dan drama yang menceritakan kisah legenda lokal. "
                        "Ciri khas Reog Ponorogo adalah penggunaan topeng besar berbentuk singa raksasa yang disebut Singa Barong, dihiasi bulu merak asli, serta topeng-topeng lain seperti Bujang Ganong dan Warok.\n" "\n"
                        "\n"
                        "Reog awalnya muncul pada abad ke-15-16 sebagai hiburan rakyat sekaligus sarana pendidikan moral, keberanian, dan kepahlawanan. Musik pengiringnya menggunakan gamelan tradisional, termasuk kendang, gong, dan kenong.\n" "\n",

        "fakta":    "1. Singa Barong bisa memiliki berat hingga 50-60 kg dan diangkat menggunakan gigi topeng oleh penari utama (Warok).\n"
                    "2. Bulu merak asli digunakan untuk hiasan topeng, yang membuat tampilannya sangat megah.\n"
                    "3. Bujang Ganong adalah karakter penari muda yang lincah, berperan sebagai penghibur dan pembawa humor.\n"
                    "4. Reog Ponorogo didaftarkan sebagai Warisan Budaya Takbenda oleh UNESCO melalui Indonesia.\n"
                    "5. Pertunjukan Reog biasanya disertai cerita kepahlawanan, legenda, dan ritual tradisional.\n"
                    "6. Reog juga menjadi simbol keberanian, kekuatan, dan kebersamaan masyarakat Ponorogo.\n",

        "soal": [
            {
                "pertanyaan": "Topeng besar berbentuk singa raksasa dalam Reog Ponorogo disebut…",
                "pilihan": ["A. Bujang Ganong", "B. Warok", "C. Singa Barong", "D. Kenong"],
                "jawaban": "C"
            },
            {
                "pertanyaan": "Musik pengiring Reog Ponorogo menggunakan alat musik tradisional, salah satunya…",
                "pilihan": ["A. Gitar", "B. Kendang", "C. Piano", "D. Biola"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Siapakah penari muda yang lincah dan humoris dalam pertunjukan Reog Ponorogo?",
                "pilihan": ["A. Singa Barong", "B. Bujang Ganong", "C. Warok", "D. Dalang"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Berat topeng Singa Barong yang diangkat oleh Warok bisa mencapai…",
                "pilihan": ["A. 10-15 kg", "B. 20-30 kg", "C. 50-60 kg", "D. 80-90 kg"],
                "jawaban": "C"
            },
            {
                "pertanyaan": "Fungsi awal Reog Ponorogo selain hiburan rakyat adalah…",
                "pilihan": ["A. Menjadi alat perdagangan", "B. Sarana pendidikan moral dan keberanian", "C. Upacara perkawinan", "D. Ritual pemakaman"],
                "jawaban": "B"
            },
        ],
    },
    {

        "nama": "Lumajang",
        "story": [
            "\n"
            f"Setelah menikmati keindahan budaya di Ponorogo, {nama_laki} dan {nama_perempuan} melanjutkan perjalanan mereka ke Lumajang. "
            f"Dari stasiun, mereka menaiki angkutan umum menuju kaki Gunung Semeru. Sepanjang perjalanan, pemandangan hijau pegunungan dan hutan pinus yang rimbun menyambut mereka. "
            f"Angin sejuk berhembus, membawa aroma tanah basah dan bunga liar yang tumbuh di pinggir jalan."
            "\n",
            f'"{nama_perempuan}, lihat gunung itu! Tingginya luar biasa, seolah menyentuh awan,” kata {nama_laki} sambil menunjuk ke puncak Semeru yang megah.\n'
            "\n"
            f'"Semeru memang gunung tertinggi di Pulau Jawa, {nama_laki}. Anak-anak bisa belajar banyak dari sini, tentang alam, keberanian, dan ekosistem gunung,” jawab {nama_perempuan}.\n'
            "\n"
            f"Setelah sampai di kaki gunung, mereka berjalan kaki menelusuri jalur pendakian ringan. Di sepanjang jalan, mereka melihat bunga liar yang mekar, burung-burung berkicau, dan monyet-monyet kecil bergelantungan di pohon. "
            f"Suasana tenang, tetapi penuh kehidupan. {nama_laki} dan {nama_perempuan} berhenti sejenak, mengambil napas dalam-dalam, dan menikmati udara segar.\n"
            "\n",
            f'"{nama_perempuan}, indah banget ya… alamnya luas, hijaunya menenangkan, dan udaranya segar,” kata {nama_laki}.\n'
            "\n"
            f'"Betul {nama_laki}, pengalaman seperti ini bisa membuat anak-anak belajar tentang alam secara langsung, bukan hanya dari buku,” jawab {nama_perempuan} sambil tersenyum.\n'
            "\n"
            f"Mereka duduk sebentar di tepi sungai kecil yang mengalir dari lereng Semeru, mendengarkan gemericik air dan suara alam. {nama_perempuan} menceritakan legenda rakyat tentang Semeru dan masyarakat yang tinggal di lereng gunung, sehingga {nama_laki} merasakan kombinasi keindahan alam dan budaya yang khas Lumajang.\n"
            "\n"
        ],
        "penjelasan":   "Gunung Semeru adalah gunung berapi tertinggi di Pulau Jawa, Indonesia, dengan ketinggian sekitar 3.676 meter di atas permukaan laut. "
                        "Gunung ini terletak di Kabupaten Malang dan Lumajang, Jawa Timur, dan termasuk dalam kawasan Taman Nasional Bromo Tengger Semeru.\n"
                        "\n"
                        "Gunung Semeru dikenal dengan puncaknya yang disebut Mahameru, yang selalu mengepulkan asap tipis karena aktivitas vulkaniknya."
                        "Semeru merupakan gunung berapi aktif, sehingga memiliki aktivitas erupsi yang harus selalu diwaspadai oleh pendaki. "
                        "Gunung ini menjadi tujuan populer bagi pendaki domestik maupun internasional karena keindahan alamnya, termasuk hutan tropis, savana, dan Danau Ranu Kumbolo yang terkenal di jalur pendakian.\n" "\n",

        "fakta":    "1.	Gunung tertinggi di Jawa dengan ketinggian 3.676 mdpl.\n"
                    "2.	Gunung berapi aktif yang sering mengalami erupsi ringan hingga sedang.\n"
                    "3.	Puncak tertingginya disebut Mahameru, yang dalam bahasa Sanskerta berarti 'Gunung Agung'.\n"
                    "4.	Semeru termasuk dalam Taman Nasional Bromo Tengger Semeru, yang juga melindungi flora dan fauna khas pegunungan tinggi.\n"
                    "5.	Jalur pendakian terkenal dimulai dari Ranu Pani menuju Ranu Kumbolo dan Kalimati sebelum mencapai puncak Mahameru.\n",

        "soal": [
            {
                "pertanyaan": "Gunung Semeru terletak di provinsi mana?",
                "pilihan": ["A. Bali", "B. Jawa Timur", "C. Jawa Tengah", "D. Sumatra Utara"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Apa nama puncak tertinggi Gunung Semeru?",
                "pilihan": ["A. Bromo", "B. Mahameru", "C. Penanggungan", "D. Arjuno"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Berapa ketinggian Gunung Semeru di atas permukaan laut?",
                "pilihan": ["A. 2.500 mdpl", "B. 3.676 mdpl", "C. 4.000 mdpl", "D. 3.000 mdpl"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Gunung Semeru termasuk jenis gunung apa?",
                "pilihan": ["A. Gunung api aktif", "B. Gunung api mati", "C. Gunung berapi tidak aktif", "D. Gunung karst"],
                "jawaban": "A"
            },
            {
                "pertanyaan": "Gunung Semeru berada dalam kawasan taman nasional yang juga melindungi Gunung Bromo. Apa nama taman nasional ini?",
                "pilihan": ["A. Taman Nasional Gunung Gede Pangrango", "B. Taman Nasional Bromo Tengger Semeru", "C. Taman Nasional Baluran", "D. Taman Nasional Alas Purwo"],
                "jawaban": "B"
            },
        ],
    },
    {
        
        "nama": "Magetan",
        "story": [
            "\n"
            f"Perjalanan berikutnya membawa mereka ke Telaga Sarangan di Magetan. Danau yang dikelilingi bukit hijau itu terlihat damai, dengan kabut tipis menutupi permukaan air. Mereka menyewa perahu kecil dan mendayung pelan di atas air yang tenang, sambil menikmati udara sejuk pegunungan.\n"
            "\n"
            f'"Wah, tenang banget airnya {nama_perempuan}… lihat ikan-ikan kecil berenang di bawah perahu,” kata {nama_laki} sambil tersenyum.\n'
            "\n"
            f'"Indah ya {nama_laki}… anak-anak bisa belajar ekosistem dan kehidupan di sekitar danau sambil melihat langsung,” jawab {nama_perempuan}.'
            f"Di tepi telaga, pedagang menawarkan jagung bakar, teh hangat, dan camilan tradisional. Aroma jagung dan teh membuat mereka merasa nyaman. Anak-anak yang bermain di tepi telaga berlarian, memberi makan ikan, dan berteriak riang. {nama_laki} dan {nama_perempuan} ikut menikmati suasana, sambil duduk dan menceritakan kepada anak-anak imajiner tentang sejarah dan legenda Telaga Sarangan.\n"
            "\n"
            f'"{nama_perempuan}, anak-anak pasti senang kalau bisa main air, belajar ekosistem dan sejarah di sini,” kata {nama_laki}.\n'
            "\n"
            f'"Iya {nama_laki}, belajar sambil bermain seperti ini lebih seru daripada cuma membaca di buku,” jawab {nama_perempuan}.\n'
            "\n"
        ],
        "penjelasan":   "Telaga Sarangan adalah danau alami yang terletak di kaki Gunung Lawu, di perbatasan Kabupaten Magetan dan Kabupaten Ngawi, Jawa Timur. "
                        "Danau ini berada pada ketinggian sekitar 1.200 meter di atas permukaan laut dan dikelilingi oleh hutan pinus yang sejuk. "
                        "Telaga Sarangan merupakan tujuan wisata populer untuk rekreasi, memancing, naik perahu, dan menikmati panorama alam pegunungan.\n"
                        "\n"
                        "Danau ini terbentuk secara alami dan memiliki legenda lokal yang terkenal. "
                        "Menurut cerita rakyat, danau ini terkait dengan kisah cinta antara Putri Sarangan dan Raja Majapahit, sehingga danau ini sering dikaitkan dengan keindahan alam sekaligus nilai budaya.\n" "\n",

        "fakta":    "1.	Terletak di kaki Gunung Lawu dengan ketinggian sekitar 1.200 mdpl."
                    "2.	Dikelilingi hutan pinus dan udara sejuk pegunungan."
                    "3.	Telaga Sarangan memiliki legenda lokal yang terkait dengan kisah cinta Putri Sarangan."
                    "4.	Menjadi tempat wisata populer untuk naik perahu, memancing, dan berkemah."
                    "5.	Akses ke danau cukup mudah dan sering dikunjungi wisatawan domestik maupun mancanegara.",

        "soal": [
            {
                "pertanyaan": "Telaga Sarangan berada di kaki gunung mana?",
                "pilihan": ["A. Gunung Semeru", "B. Gunung Lawu", "C. Gunung Bromo", "D. Gunung Arjuno"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Ketinggian Telaga Sarangan di atas permukaan laut kira-kira berapa?",
                "pilihan": ["A. 500 mdpl", "B. 1.200 mdpl", "C. 2.000 mdpl", "D. 800 mdpl"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Telaga Sarangan dikelilingi oleh jenis hutan apa?",
                "pilihan": ["A. Hutan hujan tropis", "B. Hutan pinus", "C. Hutan mangrove", "D. Hutan bambu"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Aktivitas wisata apa yang populer di Telaga Sarangan ?",
                "pilihan": ["A. Ski salju", "B. Naik perahu dan memancing", "C. Mendaki tebing es", "D. Paralayang"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Telaga Sarangan memiliki legenda yang berkaitan dengan siapa?",
                "pilihan": ["A. Raja Majapahit dan Putri Sarangan", "B. Pangeran Diponegoro", "C. Sultan Agung", "D. Ratu Kalinyamat"],
                "jawaban": "A"
            },
        ],          
    },
    {
        "nama": "Surabaya",
        "story": [
            f"Setelah meninggalkan Magetan, {nama_laki} dan {nama_perempuan} tiba di Surabaya. Kota besar ini ramai dengan kendaraan dan pejalan kaki, namun mereka segera menyeberang menuju Tugu Pahlawan, simbol perjuangan pahlawan Surabaya. Suara klakson dan riuh kota terasa jauh ketika mereka memasuki taman yang rindang di sekitar tugu."
            "\n",
            f'"{nama_perempuan}, lihat itu tugu! Tingginya luar biasa,” kata {nama_laki} sambil menatap ke atas.'
            f'"Iya {nama_laki}, itu Tugu Pahlawan, simbol perjuangan Arek-Arek Suroboyo. Anak-anak bisa belajar sejarah sambil melihat monumen ini langsung,” jawab {nama_perempuan} sambil menunjuk prasasti yang menceritakan pertempuran 10 November.',
            f"Mereka berjalan mengelilingi tugu, membaca prasasti dan patung di sekitarnya. {nama_laki} mencoba membayangkan bagaimana pahlawan Surabaya berjuang dengan keberanian luar biasa, sementara {nama_perempuan} menjelaskan makna tiap simbol di tugu tersebut. Anak-anak yang ikut berkunjung tampak antusias memegang miniatur tugu dan foto-foto pahlawan."
            "\n",
            f'"{nama_perempuan}, belajar sejarah jadi seru kalau bisa lihat langsung tempat dan simbolnya,” kata {nama_laki}.'
            f'"Betul {nama_laki}, anak-anak pasti mudah mengingat cerita pahlawan Surabaya dengan cara seperti ini,” jawab {nama_perempuan} sambil tersenyum.'
        ],

        "penjelasan":   "Tugu Pahlawan adalah monumen yang terletak di Kota Surabaya, Jawa Timur, sebagai simbol perjuangan rakyat Surabaya melawan penjajah pada peristiwa Pertempuran 10 November 1945."   
                        "Tugu ini dibangun untuk mengenang jasa para pahlawan yang gugur dalam mempertahankan kemerdekaan Indonesia. "
                        "\n"
                        "Monumen ini memiliki bentuk obelisk setinggi 41,15 meter dengan desain puncak berbentuk lingkaran terpotong, melambangkan semangat perjuangan yang tak pernah padam. "
                        "Di kompleks Tugu Pahlawan juga terdapat Museum 10 November, yang menyimpan berbagai diorama dan artefak sejarah perjuangan kemerdekaan Indonesia.",
        
        "fakta":    "1.	Terletak di Kota Surabaya, Jawa Timur."
                    "2.	Dibangun untuk mengenang peristiwa Pertempuran 10 November 1945."
                    "3.	Tinggi tugu sekitar 41,15 meter dengan puncak berbentuk lingkaran terpotong."
                    "4.	Di kompleks Tugu Pahlawan terdapat Museum 10 November." 
                    "5.	Menjadi ikon kota Surabaya dan simbol semangat perjuangan bangsa.",
        
        "soal": [
            {
                "pertanyaan": "Tugu Pahlawan terletak di kota mana?",
                "pilihan": ["A. Malang", "B. Surabaya", "C. Jombang", "D. Banyuwangi"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Tugu Pahlawan dibangun untuk mengenang peristiwa apa?",
                "pilihan": ["A. Proklamasi 17 Agustus 1945", "B. Pertempuran 10 November 1945", "C. Serangan Umum 1 Maret 1949", "D. Perang Diponegoro"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Berapa tinggi Tugu Pahlawan?",
                "pilihan": ["A. 30 meter", "B. 41,15 meter", "C. 50 meter", "D. 60 meter"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Apa yang ada di kompleks Tugu Pahlawan selain tugu itu sendiri?",
                "pilihan": ["A. Pasar tradisional", "B. Museum 10 November", "C. Stadion olahraga", "D. Perpustakaan kota"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Bentuk puncak Tugu Pahlawan melambangkan apa?",
                "pilihan": ["A. Keabadian dan semangat perjuangan", "B. Kedamaian dunia", "C. Kesejahteraan rakyat", "D. Keindahan alam"],
                "jawaban": "A"
            },
        ],
    },
    {
        "nama": "Kota Batu",
        "story": [
            "Perjalanan terakhir membawa mereka ke Kota Batu, sebuah kota kecil yang terkenal dengan udara sejuk dan pemandangan alam yang indah. Mereka mengunjungi Jatim Park, sebuah taman edukasi yang menggabungkan hiburan dan pembelajaran tentang alam, budaya, dan ilmu pengetahuan."
            "\n",
            f'"{nama_perempuan}, lihat wahana itu! Ada replika dinosaurus raksasa,” kata {nama_laki} sambil menunjuk ke arah taman yang penuh warna.'
            f'"Iya {nama_laki}, di sini anak-anak bisa belajar tentang sejarah bumi, hewan purba, dan berbagai fenomena alam dengan cara yang menyenangkan,” jawab {nama_perempuan}.',
            f"Mereka menjelajahi berbagai zona di Jatim Park, mulai dari zona dinosaurus, zona budaya Jawa Timur, hingga zona ilmu pengetahuan. {nama_laki} dan {nama_perempuan} ikut berpartisipasi dalam berbagai aktivitas interaktif, seperti simulasi gempa bumi, pertunjukan seni tradisional, dan eksperimen sains sederhana."
            "\n",
            f'"{nama_perempuan}, belajar jadi seru banget di tempat kayak gini,” kata {nama_laki} sambil tertawa.'
            f'"Betul {nama_laki}, anak-anak pasti suka belajar sambil bermain di sini,” jawab {nama_perempuan} sambil tersenyum.'    
        ],

        "penjelasan":   "Jatim Park adalah taman rekreasi dan edukasi yang terletak di Kota Batu, Jawa Timur. "
                        "Taman ini dirancang untuk memberikan pengalaman belajar yang menyenangkan bagi pengunjung, terutama anak-anak dan keluarga."
                        "\n"
                        "Jatim Park terdiri dari beberapa zona tematik, termasuk zona dinosaurus, zona budaya Jawa Timur, dan zona ilmu pengetahuan. "
                        "Setiap zona menawarkan berbagai wahana interaktif, pertunjukan seni, dan pameran edukatif yang menggabungkan hiburan dengan pembelajaran.",
        
        "fakta":    "1.	Terletak di Kota Batu, Jawa Timur." 
                    "2.	Dirancang sebagai taman rekreasi dan edukasi untuk keluarga."
                    "3.	Terdiri dari beberapa zona tematik seperti dinosaurus, budaya, dan ilmu pengetahuan."
                    "4.	Menawarkan wahana interaktif dan pertunjukan seni tradisional."
                    "5.	Sangat populer di kalangan wisatawan domestik, terutama keluarga dengan anak-anak.",

        "soal": [
            {
                "pertanyaan": "Di kota mana Jatim Park berada?",
                "pilihan": ["A. Malang", "B. Kota Batu", "C. Surabaya", "D. Kediri"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Apa tujuan utama dari Jatim Park?",
                "pilihan": ["A. Tempat belanja", "B. Taman rekreasi dan edukasi", "C. Pusat kuliner", "D. Tempat ibadah"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Salah satu zona tematik di Jatim Park adalah…",
                "pilihan": ["A. Zona olahraga", "B. Zona dinosaurus", "C. Zona musik", "D. Zona teknologi"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Jatim Park menawarkan wahana apa saja?",
                "pilihan": ["A. Wahana belanja", "B. Wahana interaktif dan pertunjukan seni", "C. Wahana olahraga ekstrem", "D. Wahana kuliner"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Siapa target utama pengunjung Jatim Park?",
                "pilihan": ["A. Remaja", "B. Keluarga dengan anak-anak", "C. Lansia", "D. Pelajar SMA"],
                "jawaban": "B"
            },
        ],           
    },
    {
        "nama": "Pasuruan",
        "story": [
            "Perjalanan mereka berakhir di Pasuruan, di mana mereka menyaksikan pertunjukan Bantengan, tarian rakyat yang menggunakan banteng tiruan berwarna-warni. Anak-anak dan orang dewasa berkumpul, bersorak menyemangati penari yang menari dengan penuh semangat."
            "\n",
            f'"Wah, seru banget {nama_perempuan}… tarian ini bikin semua orang semangat,” kata {nama_laki} sambil menepuk tangan.'
            f'"Iya {nama_laki}, itu Bantengan, budaya rakyat yang meriah. Anak-anak bisa belajar tentang keberanian, kerja sama, dan simbol-simbol yang ada di kostum,” jawab {nama_perempuan}.',
            f"Mereka berjalan di antara penonton, melihat anak-anak mencoba meniru gerakan tarian dengan ceria. Suasana semakin hidup dengan suara gendang dan teriakan riang penonton. {nama_laki} membeli miniatur banteng untuk kenang-kenangan, sementara {nama_perempuan} menjelaskan makna gerakan tarian."
            "\n",
            f'"Anak-anak pasti senang kalau bisa ikut menirukan tarian ini,” kata {nama_laki}.'
            f'"Betul {nama_laki}, belajar budaya sambil praktek langsung lebih menyenangkan,” jawab {nama_perempuan}.'
        ],

        "penjelasan":   "Bantengan adalah tarian rakyat tradisional yang berasal dari Pasuruan, Jawa Timur. "
                        "Tarian ini menampilkan penari yang mengenakan kostum banteng tiruan berwarna-warni, lengkap dengan hiasan dan atribut yang mencolok."
                        "\n"
                        "Bantengan biasanya dipentaskan dalam acara-acara budaya, festival, dan perayaan lokal. "
                        "Tarian ini melambangkan keberanian, semangat, dan kerja sama, serta mengandung nilai-nilai sosial yang penting bagi masyarakat setempat.",

        "fakta":    "1.	Berasal dari Pasuruan, Jawa Timur."
                    "2.	Menampilkan penari dengan kostum banteng tiruan berwarna-warni."
                    "3.	Dipentaskan dalam acara budaya dan festival lokal."
                    "4.	Melambangkan keberanian, semangat, dan kerja sama."
                    "5.	Mengandung nilai-nilai sosial penting bagi masyarakat setempat.",

        "soal": [
            {
                "pertanyaan": "Bantengan adalah tarian rakyat yang berasal dari…",
                "pilihan": ["A. Malang", "B. Pasuruan", "C. Surabaya", "D. Banyuwangi"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Apa yang dikenakan penari dalam tarian Bantengan?",
                "pilihan": ["A. Kostum singa", "B. Kostum banteng tiruan", "C. Kostum naga", "D. Kostum kuda"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Tarian Bantengan biasanya dipentaskan dalam acara apa?",
                "pilihan": ["A. Acara olahraga", "B. Acara budaya dan festival lokal", "C. Acara pernikahan", "D. Acara politik"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Apa makna utama dari tarian Bantengan?",
                "pilihan": ["A. Keberanian, semangat, dan kerja sama", "B. Kedamaian dan cinta", "C. Kesejahteraan dan kemakmuran", "D. Kebahagiaan dan kegembiraan"],
                "jawaban": "A"
            },
            {
                "pertanyaan": "Tarian Bantengan mengandung nilai-nilai apa bagi masyarakat setempat?",
                "pilihan": ["A. Nilai-nilai sosial penting", "B. Nilai-nilai ekonomi", "C. Nilai-nilai politik", "D. Nilai-nilai teknologi"],
                "jawaban": "A"
            },
        ],  
    },
    {
        "nama": "Probolinggo",
        "story": [
            f"Setelah meninggalkan Pasuruan, {nama_laki} dan {nama_perempuan} melanjutkan perjalanan mereka ke Probolinggo untuk menyaksikan keindahan Gunung Bromo. "
            "Mereka menaiki jeep menuju padang pasir Bromo, kabut tipis menutupi permukaan pasir, sementara matahari mulai muncul di ufuk timur."
            "\n",
            f'"{nama_perempuan}, indah banget… kabut dan matahari terbitnya luar biasa,” kata {nama_laki} sambil mengambil foto.'
            f'"Anak-anak pasti kagum kalau lihat langsung. Gunung Bromo nggak cuma indah, tapi juga sarat cerita dan legenda,” jawab {nama_perempuan}.',
            "Mereka berjalan menyusuri pasir hitam, melihat para wisatawan lain dan pedagang yang menjual camilan tradisional. "
            f"Angin dingin membawa aroma segar dari gunung, sementara suara alam menambah ketenangan suasana. {nama_laki} dan {nama_perempuan} menceritakan legenda Bromo, sekaligus menjelaskan proses terbentuknya gunung berapi dan pentingnya alam bagi masyarakat setempat."
            "\n",
            f'"{nama_perempuan}, anak-anak bisa belajar alam sekaligus budaya lokal dari sini,” kata {nama_laki}.'
            f'"Iya {nama_laki}, belajar sambil menikmati pemandangan lebih seru daripada cuma membaca buku,” jawab {nama_perempuan}.'
        ],

        "penjelasan":   "Gunung Bromo adalah gunung berapi yang terletak di Taman Nasional Bromo Tengger Semeru, Jawa Timur, Indonesia. "
                        "Gunung ini terkenal dengan pemandangan matahari terbit yang menakjubkan dan lautan pasir yang luas di sekitarnya."
                        "\n"
                        "Bromo merupakan bagian dari rangkaian pegunungan Tengger dan memiliki ketinggian sekitar 2.329 meter di atas permukaan laut. "
                        "Gunung ini masih aktif, sehingga sering terjadi erupsi kecil. Masyarakat Tengger yang tinggal di sekitar Bromo memiliki tradisi unik, yaitu upacara Yadnya Kasada, di mana mereka mempersembahkan sesaji kepada dewa gunung sebagai bentuk rasa syukur dan permohonan keselamatan.",
        "fakta":    "1.	Gunung Bromo terletak di Taman Nasional Bromo Tengger Semeru, Jawa Timur."
                    "2.	Ketinggian Gunung Bromo sekitar 2.329 meter di atas permukaan laut."
                    "3.	Gunung Bromo adalah gunung berapi aktif."
                    "4.	Gunung ini terkenal dengan pemandangan matahari terbit dan lautan pasir yang luas."
                    "5.	Masyarakat Tengger mengadakan upacara Yadnya Kasada setiap tahun sebagai bentuk persembahan kepada dewa gunung.",

        "soal": [
            {
                "pertanyaan": "Gunung Bromo terletak di provinsi mana?",
                "pilihan": ["A. Jawa Tengah", "B. Jawa Timur", "C. Bali", "D. Sumatra"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Ketinggian Gunung Bromo kira-kira berapa meter?",
                "pilihan": ["A. 1.500 mdpl", "B. 2.329 mdpl", "C. 3.676 mdpl", "D. 2.000 mdpl"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Apa nama upacara adat yang dilakukan masyarakat Tengger di Gunung Bromo?",
                "pilihan": ["A. Sekaten", "B. Yadnya Kasada", "C. Nyepi", "D. Grebeg Maulud"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Gunung Bromo terkenal dengan pemandangan alam apa?",
                "pilihan": ["A. Danau dan hutan hujan", "B. Lautan pasir dan matahari terbit", "C. Air terjun dan gua", "D. Sawah terasering"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Gunung Bromo termasuk jenis gunung apa?",
                "pilihan": ["A. Gunung api aktif", "B. Gunung karst", "C. Gunung mati", "D. Gunung berlapis"],
                "jawaban": "A"
            },
        ],      
    },
    {
        "nama": "Bojonegoro",
        "story": [
            "Di Bojonegoro, sore hari di alun-alun kota ramai dengan anak-anak dan keluarga yang menonton Wayang Thegul. Dalang menggerakkan wayang sambil menceritakan kisah klasik, diiringi musik tradisional yang mengalun riang."
            "\n",
            f'"{nama_perempuan}, gerakannya lincah banget… lucu juga ceritanya,” kata {nama_laki} sambil tersenyum.'
            f'"Itu Wayang Thegul, {nama_laki}… pertunjukan ini bisa menghibur dan mengajarkan nilai-nilai moral. Anak-anak pasti senang menonton langsung,” jawab {nama_perempuan}.',
            "Mereka ikut menebak tokoh-tokoh wayang, meniru gerakan sederhana, dan belajar simbolisme cerita. Anak-anak lokal tampak antusias, tertawa, dan mencoba mengikuti dalang."
            "\n",
            f'"Belajar budaya sambil terhibur itu seru banget ya {nama_perempuan},” kata {nama_laki}.'
            f'"Betul {nama_laki}, cara seperti ini bikin anak-anak mudah mengingat cerita dan karakter wayang,” jawab {nama_perempuan}.' 
        ],

        "penjelasan":   "Wayang Thegul Bojonegoro adalah seni pertunjukan tradisional yang berasal dari Kabupaten Bojonegoro, Jawa Timur. "
                        "Wayang ini menggunakan boneka kayu atau kulit yang digerakkan oleh seorang dalang untuk menceritakan kisah-kisah rakyat, legenda lokal, atau cerita kepahlawanan."
                        "\n"
                        "Pertunjukan Wayang Thegul biasanya diiringi oleh musik tradisional seperti gamelan dan lagu-lagu daerah setempat. "
                        "Wayang ini memiliki gerakan yang teatrikal dan ekspresif, serta sering dipertunjukkan dalam acara adat, perayaan, atau hiburan rakyat. "
                        "Selain sebagai hiburan, Wayang Thegul juga berfungsi sebagai sarana pendidikan moral dan pelestarian budaya bagi masyarakat setempat.",

        "fakta":    "1.	Berasal dari Kabupaten Bojonegoro, Jawa Timur."
                    "2.	Menggunakan boneka kayu atau kulit yang digerakkan oleh dalang."
                    "3.	Cerita yang dibawakan berasal dari legenda lokal, kisah rakyat, atau kepahlawanan."
                    "4.	Dipertunjukkan dengan iringan musik tradisional seperti gamelan."
                    "5.	Berfungsi sebagai hiburan sekaligus sarana pendidikan moral dan pelestarian budaya.",

        "soal": [
            {
                "pertanyaan": "Wayang Thegul berasal dari kabupaten mana?",
                "pilihan": ["A. Banyuwangi", "B. Bojonegoro", "C. Malang", "D. Kediri"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Alat utama yang digunakan dalam Wayang Thegul adalah?",
                "pilihan": ["A. Lukisan kain", "B. Boneka kayu atau kulit", "C. Patung tanah liat", "D. Boneka kertas"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Cerita dalam Wayang Thegul biasanya berasal dari?",
                "pilihan": ["A. Film modern", "B. Legenda lokal, kisah rakyat, atau kepahlawanan", "C. Novel asing", "D. Cerita televisi"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Musik apa yang mengiringi pertunjukan Wayang Thegul?",
                "pilihan": ["A. Musik pop", "B. Gamelan dan lagu tradisional", "C. Jazz", "D. Rock"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Wayang Thegul biasanya dipertunjukkan pada acara apa?",
                "pilihan": ["A. Festival internasional", "B. Acara adat, perayaan, atau hiburan rakyat", "C. Konser musik modern", "D. Pertandingan olahraga"],
                "jawaban": "B"
            },
        ],       
    },
    {
        "nama": "Tuban",
        "story": [
            f"Perjalanan mereka di Tuban berakhir dengan mengunjungi Pantai Boom. Ombak yang tenang dan pasir putih yang luas menciptakan suasana damai. {nama_laki} dan {nama_perempuan} berjalan di tepi pantai, menikmati angin laut yang segar sambil melihat kapal nelayan yang berlayar."
            "\n",
            f'"{nama_perempuan}, pantainya indah banget… tenang dan asri,” kata {nama_laki} sambil menghirup udara laut.'
            f'"Iya {nama_laki}, anak-anak bisa belajar tentang ekosistem laut dan kehidupan nelayan di sini,” jawab {nama_perempuan}.',
            "Mereka berbicara dengan nelayan lokal, mendengarkan cerita tentang kehidupan di laut, dan belajar tentang pentingnya menjaga kelestarian pantai. Anak-anak yang bermain di tepi pantai tampak riang, berlarian mengejar ombak kecil dan mengumpulkan kerang."
            "\n",
            f'"Belajar tentang laut sambil bermain di pantai itu asyik ya {nama_perempuan},” kata {nama_laki}.'
            f'"Betul {nama_laki}, pengalaman langsung seperti ini bikin anak-anak lebih paham tentang alam,” jawab {nama_perempuan}.'
        ],

        "penjelasan":   "Minuman Legen Tuban adalah minuman tradisional khas Tuban, Jawa Timur, yang terbuat dari getah pohon enau atau aren. "
                        "Cairan manis ini dikumpulkan dari batang pohon enau dan biasanya diminum segar atau diolah menjadi minuman tradisional seperti es legen."
                        "\n"
                        "Rasanya manis alami dan menyegarkan, sehingga populer di kalangan masyarakat lokal maupun wisatawan. "
                        "Selain diminum langsung, legen juga sering dijadikan bahan dasar untuk membuat gula aren atau dodol, serta memiliki nilai budaya karena berkaitan dengan tradisi pertanian dan kehidupan masyarakat desa di Tuban.",

        "fakta":    "1.	Minuman tradisional khas Tuban, Jawa Timur."
                    "2.	Terbuat dari getah pohon enau atau aren."
                    "3.	Rasanya manis alami dan menyegarkan."
                    "4.	Bisa diminum segar atau diolah menjadi es legen."
                    "5.	Sering digunakan sebagai bahan dasar gula aren atau dodol, serta terkait dengan tradisi pertanian lokal.",

        "soal": [
            {
                "pertanyaan": "Minuman Legen Tuban berasal dari daerah mana?",
                "pilihan": ["A. Malang", "B. Tuban", "C. Kediri", "D. Banyuwangi"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Bahan utama Minuman Legen Tuban adalah?",
                "pilihan": ["A. Kelapa parut", "B. Getah pohon enau atau aren", "C. Jahe dan gula", "D. Buah naga"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Rasanya Minuman Legen Tuban biasanya?",
                "pilihan": ["A. Pahit", "B. Asam", "C. Manis alami", "D. Pedas"],
                "jawaban": "C"
            },
            {
                "pertanyaan": "Minuman Legen Tuban bisa diolah menjadi apa?",
                "pilihan": ["A. Es legen", "B. Teh tarik", "C. Jus jeruk", "D. Kopi tubruk"],
                "jawaban": "A"
            },
            {
                "pertanyaan": "Selain diminum, Minuman Legen juga digunakan sebagai bahan dasar untuk apa?",
                "pilihan": ["A. Kue lapis", "B. Gula aren dan dodol", "C. Minyak kelapa", "D. Tahu dan tempe"],
                "jawaban": "B"
            },
        ],
    },
    {

        "nama": "Lamongan",
        "story": [
            "Perhentian terakhir mereka adalah Lamongan, di mana mereka mencicipi kuliner khas Wingko Babat. "
            "Di sebuah toko kue tradisional yang ramai, aroma kelapa dan ketan menyambut mereka hangat. "
            f"{nama_laki} dan {nama_perempuan} memilih beberapa potong Wingko Babat, kue kenyal dan manis yang terkenal di daerah itu."
            "\n",
            f'"{nama_perempuan}, wanginya enak banget! Aku lapar nih,” kata {nama_laki} sambil melihat kue-kue di etalase.'
            f'"Itu Wingko Babat, {nama_laki}… anak-anak pasti suka karena manis dan legit. Kue ini sering dibawa sebagai oleh-oleh,” jawab {nama_perempuan}.',
            "Mereka mencicipi beberapa potong Wingko Babat, sambil mengamati pedagang yang menyiapkan kue baru. "
            f"{nama_laki} belajar tentang tekstur dan rasa, sementara {nama_perempuan} menjelaskan asal-usul kue dan cara pembuatannya yang turun-temurun."
            "Anak-anak lokal tampak antusias mencicipi, sambil melihat proses pembuatan yang sederhana tapi menarik."
            "\n",
            f'"Anak-anak bisa belajar sejarah kuliner Lamongan sambil merasakan sendiri,” kata {nama_laki}.'
            f'"Betul {nama_laki}, cara seperti ini bikin mereka mudah mengingat dan menghargai budaya lokal,” jawab {nama_perempuan}.'
        ],

        "penjelasan":   "Wingko Babat adalah kue tradisional khas Jawa Timur, khususnya dari Kabupaten Lamongan. "
                        "Makanan ini terbuat dari kelapa parut, tepung ketan, dan gula, dibentuk bulat pipih atau persegi, lalu dipanggang hingga matang. "
                        "Wingko Babat memiliki rasa manis, gurih, dan aroma kelapa yang khas."
                        "\n"
                        "Kue ini biasanya dijadikan oleh-oleh khas Jawa Timur dan populer di kalangan wisatawan. "
                        "Wingko Babat bisa dimakan langsung sebagai camilan atau teman minum teh atau kopi.",

        "fakta":    "1.	Kue tradisional khas Kabupaten Lamongan, Jawa Timur."
                    "2.	Terbuat dari kelapa parut, tepung ketan, dan gula."
                    "3.	Bentuknya bulat pipih atau persegi."
                    "4.	Dipanggang hingga matang dan memiliki aroma kelapa yang khas."
                    "5.	Sering dijadikan oleh-oleh atau camilan pendamping minum teh/kopi.",

        "soal": [
            {
                "pertanyaan": "Wingko Babat berasal dari kabupaten mana?",
                "pilihan": ["A. Lamongan", "B. Malang", "C. Kediri", "D. Trenggalek"],
                "jawaban": "A"
            },
            {
                "pertanyaan": "Bahan utama Wingko Babat adalah?",
                "pilihan": ["A. Tepung terigu", "B. Kelapa parut, tepung ketan, dan gula", "C. Beras dan santan", "D. Jagung dan gula"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Bentuk Wingko Babat biasanya?",
                "pilihan": ["A. Bulat pipih atau persegi", "B. Segitiga", "C. Panjang tipis", "D. Lingkaran besar"],
                "jawaban": "A"
            },
            {
                "pertanyaan": "Wingko Babat biasanya dimasak dengan cara apa?",
                "pilihan": ["A. Digoreng", "B. Dipanggang", "C. Dikukus", "D. Direbus"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Wingko Babat sering dijadikan apa oleh wisatawan?",
                "pilihan": ["A. Oleh-oleh khas Jawa Timur", "B. Makanan utama", "C. Bahan baku kue lain", "D. Minuman"],
                "jawaban": "A"
            },
        ],
    },
    {
        "nama": "Gresik",
        "story": [
            "Perjalanan mereka di Gresik berakhir dengan mengunjungi Makam Sunan Giri, salah satu dari Wali Songo yang sangat dihormati. "
            "Mereka berjalan menyusuri kompleks makam yang tenang, dikelilingi oleh pepohonan rindang dan taman yang terawat."
            "\n",
            f'"{nama_perempuan}, suasananya damai banget di sini,” kata {nama_laki} sambil melihat sekeliling.'
            f'"Iya {nama_laki}, ini Makam Sunan Giri, tempat ziarah penting bagi umat Islam di Jawa Timur. Anak-anak bisa belajar tentang sejarah penyebaran Islam di Indonesia,” jawab {nama_perempuan}.',
            "Mereka membaca prasasti dan mendengarkan cerita tentang kehidupan Sunan Giri serta kontribusinya dalam menyebarkan ajaran Islam. "
            f"{nama_laki} dan {nama_perempuan} menjelaskan nilai-nilai toleransi, kebijaksanaan, dan pengabdian yang diajarkan oleh Sunan Giri kepada anak-anak."
            "\n",
            f'"Belajar sejarah agama sambil mengunjungi tempat bersejarah itu penting ya {nama_perempuan},” kata {nama_laki}.'
            f'"Betul {nama_laki}, pengalaman langsung seperti ini bikin anak-anak lebih menghargai nilai-nilai budaya dan agama,” jawab {nama_perempuan}.'
        ],

        "penjelasan":   "Wekasan Rebo di Gresik adalah tradisi keagamaan yang dilakukan setiap Rabu terakhir bulan Safar dalam kalender Hijriyah."
                        "Tradisi ini bertujuan untuk memohon keselamatan, kesehatan, dan perlindungan dari bencana bagi masyarakat setempat."
                        "\n"
                        "Di Gresik, Rebo Wekasan biasanya dilaksanakan di Makam Sunan Giri atau masjid-masjid setempat. "
                        "Acara ini melibatkan doa bersama, zikir, dan kenduri sebagai bentuk syukur dan permohonan kepada Allah SWT. "
                        "Selain nilai religius, Rebo Wekasan juga menjadi momen sosial bagi masyarakat untuk berkumpul, bersilaturahmi, dan memperkuat rasa kebersamaan.",

        "fakta":    "1.	Tradisi keagamaan yang dilakukan setiap Rabu terakhir bulan Safar."
                    "2.	Bertujuan memohon keselamatan, kesehatan, dan perlindungan dari bencana."
                    "3.	Dilaksanakan di Makam Sunan Giri atau masjid setempat."
                    "4.	Melibatkan doa bersama, zikir, dan kenduri."
                    "5.	Menjadi momen sosial untuk berkumpul, bersilaturahmi, dan memperkuat kebersamaan.",

        "soal": [
            {
                "pertanyaan": "Rebo Wekasan di Gresik dilakukan pada hari apa?",
                "pilihan": ["A. Senin terakhir bulan Safar", "B. Rabu terakhir bulan Safar", "C. Jumat pertama bulan Safar", "D. Sabtu terakhir bulan Safar"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Tujuan utama Rebo Wekasan di Gresik adalah?",
                "pilihan": ["A. Memperingati panen padi", "B. Memohon keselamatan, kesehatan, dan perlindungan dari bencana", "C. Menyambut tamu penting", "D. Memperingati hari kemerdekaan"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Di mana tradisi Rebo Wekasan biasanya dilaksanakan di Gresik?",
                "pilihan": ["A. Pasar tradisional", "B. Makam Sunan Giri atau masjid setempat", "C. Gunung dan bukit", "D. Pantai dan pelabuhan"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Kegiatan apa yang biasanya dilakukan dalam Rebo Wekasan Gresik?",
                "pilihan": ["A. Mendaki gunung", "B. Doa bersama, zikir, dan kenduri", "C. Karapan sapi", "D. Festival tari tradisional"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Selain religius, Rebo Wekasan Gresik juga memiliki fungsi apa?",
                "pilihan": ["A. Hiburan dan pertunjukan", "B. Momentum sosial untuk berkumpul dan memperkuat kebersamaan", "C. Kompetisi olahraga", "D. Festival kuliner"],
                "jawaban": "B"
            },
        ],
    },
    {

        "nama": "Pulau Madura",
        "story": [
            "Di Pulau Madura, mereka menyaksikan Karapan Sapi, lomba pacuan sapi yang terkenal. "
            "Sepasang sapi menarik kereta kayu kecil yang dikendalikan oleh seorang joki, diiringi sorak-sorai penonton.",
            f'"{nama_perempuan}, cepat banget sapinya! Seru ya {nama_laki},” kata {nama_laki} sambil terkagum.',
            f'"Itu Karapan Sapi, {nama_laki}. Anak-anak bisa belajar olahraga tradisional sekaligus budaya Madura. Kecepatan dan koordinasi sapi dan joki sangat penting,” jawab {nama_perempuan}.',
            "Mereka berjalan di sepanjang lintasan, memperhatikan cara joki mengendalikan sapi dan menirukan gerakan sederhana untuk anak-anak. "
            "Musik pengiring dan pakaian tradisional menambah semarak lomba.",
            f'"Belajar budaya sambil melihat langsung lebih seru ya {nama_perempuan},” kata {nama_laki}.',
            f'"Iya {nama_laki}, anak-anak bisa merasakan semangat dan tradisi Madura secara langsung,” jawab {nama_perempuan}.'
        ],
        "penjelasan":   "Karapan Sapi adalah tradisi lomba pacuan sapi khas Madura, Jawa Timur. Sapi ditarik oleh kereta kayu kecil yang dikendalikan joki. Lomba ini menjadi hiburan rakyat dan ritual budaya, biasanya diadakan saat panen atau festival adat. Selain olahraga, menampilkan musik pengiring, pakaian tradisional, dan festival masyarakat Madura.",
        "fakta":    "1. Tradisi lomba pacuan sapi khas Madura, Jawa Timur.\n"
                    "2. Dilakukan dengan sepasang sapi yang menarik kereta kayu kecil.\n"
                    "3. Diikuti seorang joki atau pengendara sapi.\n"
                    "4. Biasanya diadakan saat panen atau festival adat.\n"
                    "5. Menampilkan unsur budaya Madura, termasuk musik pengiring dan pakaian tradisional.",
        "soal": [
            {
                "pertanyaan": "Karapan Sapi berasal dari daerah mana?",
                "pilihan": ["A. Banyuwangi", "B. Madura", "C. Kediri", "D. Trenggalek"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Dalam Karapan Sapi, sapi biasanya menarik apa?",
                "pilihan": ["A. Becak", "B. Kereta kayu kecil", "C. Gerobak sapi", "D. Sepeda"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Siapa yang mengendalikan sapi dalam lomba Karapan Sapi?",
                "pilihan": ["A. Petani", "B. Joki atau pengendara sapi", "C. Anak-anak", "D. Guru adat"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Karapan Sapi biasanya diadakan saat apa?",
                "pilihan": ["A. Hari libur nasional", "B. Saat panen atau festival adat", "C. Perayaan ulang tahun kota", "D. Musim hujan"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Selain olahraga, Karapan Sapi juga menampilkan unsur apa?",
                "pilihan": ["A. Masakan tradisional", "B. Budaya Madura seperti musik pengiring dan pakaian tradisional", "C. Seni lukis", "D. Pertanian modern"],
                "jawaban": "B"
            },
        ],
    },
    {
        "nama": "Sidoarjo",
        "story": [
            "Di Sidoarjo, mereka menonton Ujung Ujungan, tarian rakyat yang enerjik. Penari menari dengan cepat dan berputar-putar, diiringi musik tradisional yang riang.",
            f'"{nama_perempuan}, gerakannya cepat banget! Seru banget,” kata {nama_laki}.',
            f'"Itu Ujung Ujungan, {nama_laki}. Anak-anak bisa belajar tari tradisional sekaligus simbol gerakan yang ada di budaya Sidoarjo,” jawab {nama_perempuan}.',
            f"{nama_laki} dan {nama_perempuan} ikut menirukan beberapa gerakan sederhana bersama anak-anak lokal, tertawa, dan bersenang-senang. Suasana meriah, musik dan tawa anak-anak menambah semarak pertunjukan.",
            f'"Belajar budaya sambil bergerak pasti menyenangkan bagi anak-anak,” kata {nama_laki}.',
            f'"Iya {nama_laki}, mereka jadi lebih mudah mengingat gerakan dan cerita tradisional,” jawab {nama_perempuan}.'
        ],

        "penjelasan":   "Ujung-Ujungan adalah tradisi budaya khas Sidoarjo, Jawa Timur, yang biasanya dilakukan oleh masyarakat pesisir. "
                "Tradisi ini melibatkan pawai perahu kecil atau perahu hias di sungai atau muara, diiringi nyanyian dan doa."
                "\n"
                "Ujung-Ujungan bertujuan untuk memohon keselamatan para nelayan, hasil laut yang melimpah, serta perlindungan dari bencana. "
                "Selain nilai religius dan keselamatan, tradisi ini juga menjadi media hiburan rakyat dan sarana pelestarian budaya lokal, sambil mempererat silaturahmi antarwarga.",

        "fakta":    "1. Tradisi budaya khas Sidoarjo, Jawa Timur."
                "2. Melibatkan pawai perahu kecil atau perahu hias di sungai atau muara."
                "3. Dihiasi dengan nyanyian dan doa untuk keselamatan nelayan dan hasil laut."
                "4. Bertujuan memohon perlindungan dari bencana dan keselamatan masyarakat pesisir."
                "5. Menjadi sarana hiburan rakyat dan pelestarian budaya lokal.",

        "soal": [
            {
                "pertanyaan": "Ujung-Ujungan berasal dari kabupaten mana?",
                "pilihan": ["A. Surabaya", "B. Sidoarjo", "C. Malang", "D. Gresik"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Tradisi Ujung-Ujungan melibatkan apa?",
                "pilihan": ["A. Pawai sapi", "B. Pawai perahu kecil atau perahu hias", "C. Pertunjukan wayang kulit", "D. Festival kuliner"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Tujuan utama Ujung-Ujungan adalah?",
                "pilihan": ["A. Memperingati hari kemerdekaan", "B. Memohon keselamatan nelayan dan hasil laut melimpah", "C. Kompetisi olahraga", "D. Pameran seni lukis"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Apa yang biasanya mengiringi pawai Ujung-Ujungan?",
                "pilihan": ["A. Musik pop modern", "B. Nyanyian dan doa", "C. Tarian kontemporer", "D. Pertunjukan sulap"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Selain religius, Ujung-Ujungan juga berfungsi sebagai?",
                "pilihan": ["A. Media hiburan rakyat dan pelestarian budaya lokal", "B. Festival internasional", "C. Kompetisi teknologi", "D. Lomba memasak modern"],
                "jawaban": "A"
            },
        ],
    },
    {

        "nama": "Nganjuk",

        "story": [

            "Di Nganjuk, mereka ikut menyaksikan Grebeg Sedudo, tradisi tahunan yang penuh warna dan semangat. Warga membawa sesaji, menari, bernyanyi sepanjang jalan desa."

            f'“Wah, ramai banget {nama_perempuan}… semua ikut serta,” kata {nama_laki}.'

            f'“Iya {nama_laki}, itu Grebeg Sedudo, anak-anak bisa belajar kebersamaan, gotong royong, dan tradisi lokal,” jawab {nama_perempuan}.'

            "\n"

            f"Mereka berjalan di antara peserta, melihat anak-anak membawa sesaji kecil dan ikut menari dengan riang. {nama_laki} dan {nama_perempuan} menjelaskan makna setiap gerakan dan simbol dalam tradisi ini. Anak-anak lokal tampak gembira, menari dan tersenyum sepanjang jalan."

            "\n"

            f'“Anak-anak pasti senang ikut merasakan tradisi ini,” kata {nama_laki}.'

            f'“Iya {nama_laki}, belajar budaya sambil merasakan langsung semangat tradisi lebih menyenangkan,” jawab {nama_perempuan}.'

        ],

        "penjelasan":    "Grebeg Sedudo adalah tradisi tahunan yang berlangsung di Nganjuk, Jawa Timur, sebagai bentuk syukuran dan ritual adat untuk keselamatan, kesuburan, dan kesejahteraan masyarakat. Acara ini biasanya diadakan setiap tanggal 7 Suro dalam kalender Jawa."
                        "\n"
                        "Kegiatan utama Grebeg Sedudo meliputi upacara penyiraman air dari sumber mata air Sedudo, prosesi budaya, dan pawai budaya. Air Sedudo dipercaya memiliki kekuatan magis dan berkah, sehingga masyarakat membawa pulang air tersebut untuk ritual di rumah masing-masing. Tradisi ini menjadi ikon budaya Nganjuk yang menggabungkan nilai religius, adat, dan seni pertunjukan.",

        "fakta":    "1. Tradisi tahunan yang berlangsung di Nganjuk, Jawa Timur."
                    "2. Diadakan setiap tanggal 7 Suro dalam kalender Jawa."
                    "3. Melibatkan upacara penyiraman air dari sumber mata air Sedudo."
                    "4. Air Sedudo dipercaya membawa berkah, keselamatan, dan kesuburan."
                    "5. Merupakan gabungan ritual adat, religius, dan pertunjukan budaya.",

        "soal": [
            {
                "pertanyaan": "Grebeg Sedudo berasal dari kabupaten mana?",
                "pilihan": ["A. Malang", "B. Nganjuk", "C. Kediri", "D. Banyuwangi"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Grebeg Sedudo diadakan setiap tanggal berapa dalam kalender Jawa?",
                "pilihan": ["A. 1 Suro", "B. 7 Suro", "C. 15 Suro", "D. 10 Suro"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Kegiatan utama dalam Grebeg Sedudo adalah?",
                "pilihan": ["A. Karapan sapi", "B. Upacara penyiraman air dari sumber mata air Sedudo", "C. Festival tari Gandrung", "D. Pameran kuliner"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Air Sedudo dipercaya memiliki apa?",
                "pilihan": ["A. Aroma harum", "B. Kekuatan magis dan berkah", "C. Warna biru", "D. Rasanya manis"],
                "jawaban": "B"
            },
            {
                "pertanyaan": "Grebeg Sedudo Nganjuk merupakan gabungan dari apa?",
                "pilihan": ["A. Musik modern dan tari kontemporer", "B. Ritual adat, religius, dan pertunjukan budaya", "C. Olahraga dan festival kuliner", "D. Seni lukis dan teater modern"],
                "jawaban": "B"
            },
        ],
    },
    {
        "nama": "Ngawi",
        "story": [
            "Di Ngawi, mereka mengunjungi Benteng Pendem, peninggalan kolonial Belanda. Bangunan batu tua menjulang, udara sejuk menyelimuti.",
            f'"{nama_perempuan}, bangunannya kokoh banget ya…,” kata {nama_laki} sambil mengagumi arsitektur benteng.',
            f'"Itu Benteng Pendem, {nama_laki}. Anak-anak bisa belajar sejarah lewat bangunan nyata, memahami fungsi dan cerita di baliknya,” jawab {nama_perempuan}.',
            f"Mereka berjalan menyusuri koridor benteng, membaca prasasti, dan membayangkan kehidupan zaman dulu. {nama_laki} menjelaskan kegunaan benteng untuk pertahanan, {nama_perempuan} menambahkan kisah sejarah lokal yang menarik bagi anak-anak.",
            f'"Belajar sejarah sambil melihat langsung bangunan asli itu seru ya {nama_perempuan},” kata {nama_laki}.',
            f'"Iya {nama_laki}, lebih hidup daripada cuma membaca buku,” jawab {nama_perempuan}.'
        ],
        "penjelasan": "Benteng Pendem adalah salah satu situs sejarah di Kabupaten Ngawi, Jawa Timur. Dibangun oleh pemerintah kolonial Belanda pada abad ke-19 sebagai markas pertahanan militer. Memiliki arsitektur kolonial dengan tembok tebal, parit, dan ruang bawah tanah. Kini menjadi objek wisata sejarah dan edukasi, serta lokasi fotografi."
        ,
        "fakta": "1. Terletak di Kabupaten Ngawi, Jawa Timur.\n"
            "2. Dibangun oleh Belanda pada abad ke-19 sebagai markas pertahanan militer.\n"
            "3. Memiliki arsitektur kolonial dengan tembok tebal dan parit.\n"
            "4. Terdapat lorong-lorong bawah tanah untuk penyimpanan senjata dan aktivitas militer.\n"
            "5. Kini menjadi objek wisata sejarah, edukasi, dan lokasi fotografi.",
        "soal": [
            {"pertanyaan": "Benteng Pendem terletak di kabupaten mana?",
             "pilihan": ["A. Malang", "B. Ngawi", "C. Kediri", "D. Trenggalek"],
             "jawaban": "B"},
            {"pertanyaan": "Benteng Pendem dibangun oleh siapa?",
             "pilihan": ["A. Kerajaan Mataram", "B. Belanda", "C. Jepang", "D. Portugis"],
             "jawaban": "B"},
            {"pertanyaan": "Pada abad berapa Benteng Pendem dibangun?",
             "pilihan": ["A. Abad ke-17", "B. Abad ke-18", "C. Abad ke-19", "D. Abad ke-20"],
             "jawaban": "C"},
            {"pertanyaan": "Fungsi utama Benteng Pendem pada masa kolonial adalah?",
             "pilihan": ["A. Tempat ibadah", "B. Markas pertahanan militer", "C. Pasar tradisional", "D. Sekolah"],
             "jawaban": "B"},
            {"pertanyaan": "Saat ini, Benteng Pendem digunakan sebagai?",
             "pilihan": ["A. Tempat tinggal", "B. Objek wisata sejarah dan edukasi", "C. Pabrik", "D. Perpustakaan"],
             "jawaban": "B"}
        ]
    },
    {
        "nama": "Bondowoso",
        "story": [
            "Di Bondowoso, mereka mendaki ke Kawah Ijen, kawah terkenal dengan api biru dan pemandangan menakjubkan. Kabut tipis menutupi permukaan air kawah, angin sejuk menambah sensasi petualangan.",
            f'"{nama_perempuan}, lihat itu api birunya! Cantik banget,” kata {nama_laki} sambil takjub.',
            f'"Anak-anak pasti kagum kalau melihat fenomena alam ini langsung. Ijen juga tempat tinggal masyarakat tradisional, jadi bisa belajar budaya sekaligus alam,” jawab {nama_perempuan}.',
            f"Mereka berhenti di titik aman, mengambil foto, dan mengamati kawah. {nama_perempuan} menceritakan tentang proses terbentuknya kawah dan api biru, sementara {nama_laki} menjelaskan ekosistem sekitar. Anak-anak lokal tampak antusias belajar sambil melihat fenomena unik ini.",
            f'"Belajar alam sekaligus budaya, pasti menyenangkan bagi anak-anak,” kata {nama_laki}.',
            f'"Iya {nama_laki}, pengalaman langsung seperti ini bikin mereka lebih mengingat dan menghargai alam,” jawab {nama_perempuan}.'
        ],
        "penjelasan": "Kawah Ijen adalah kawah gunung berapi di perbatasan Kabupaten Banyuwangi dan Bondowoso, Jawa Timur, terkenal dengan danau belerang berwarna biru kehijauan dan fenomena api biru pada malam hari. Kawah ini masih aktif dan digunakan untuk penambangan belerang tradisional."
        ,
        "fakta": "1. Terletak di perbatasan Banyuwangi dan Bondowoso, Jawa Timur.\n"
            "2. Memiliki danau belerang berwarna biru kehijauan.\n"
            "3. Fenomena api biru terlihat pada malam hari.\n"
            "4. Berada pada ketinggian 2.443 mdpl.\n"
            "5. Masih aktif dan menjadi tempat penambangan belerang tradisional.",
        "soal": [
            {"pertanyaan": "Kawah Ijen terletak di provinsi mana?",
             "pilihan": ["A. Bali", "B. Jawa Timur", "C. Jawa Tengah", "D. Sumatra"],
             "jawaban": "B"},
            {"pertanyaan": "Apa warna danau belerang di Kawah Ijen?",
             "pilihan": ["A. Merah", "B. Biru kehijauan", "C. Kuning", "D. Hitam"],
             "jawaban": "B"},
            {"pertanyaan": "Fenomena apa yang membuat Kawah Ijen terkenal pada malam hari?",
             "pilihan": ["A. Matahari terbit", "B. Blue fire atau api biru", "C. Aurora", "D. Kilatan petir"],
             "jawaban": "B"},
            {"pertanyaan": "Ketinggian Kawah Ijen kira-kira berapa meter di atas permukaan laut?",
             "pilihan": ["A. 1.200 mdpl", "B. 2.443 mdpl", "C. 3.000 mdpl", "D. 2.000 mdpl"],
             "jawaban": "B"},
            {"pertanyaan": "Selain untuk wisata, Kawah Ijen juga digunakan sebagai apa?",
             "pilihan": ["A. Lahan pertanian", "B. Penambangan belerang tradisional", "C. Kolam ikan", "D. Tempat olahraga ekstrem"],
             "jawaban": "B"}
        ]
    },
    {
        "nama": "Situbondo",
        "story": [
            "Di Situbondo, mereka berjalan di pasar tradisional dan mencoba Sego Tempong, nasi pedas khas daerah ini. Aroma sambal segar dan pedas menyebar ke udara, menarik perhatian pengunjung.",
            f'"Pedasnya mantap {nama_perempuan}, tapi enak banget,” kata {nama_laki} sambil tersenyum.',
            f'"Itu Sego Tempong, {nama_laki}. Anak-anak bisa belajar kuliner khas Situbondo sambil merasakan sensasi pedasnya,” jawab {nama_perempuan}.',
            f"Mereka duduk di bangku kayu, sambil mengamati pedagang lain menjajakan jajanan lokal. Anak-anak tampak penasaran mencicipi dan menanyakan bahan makanan. {nama_laki} dan {nama_perempuan} menjelaskan proses pembuatan Sego Tempong dan sejarah kuliner ini.",
            f'"Belajar kuliner sambil mencicipi, anak-anak pasti senang,” kata {nama_laki}.',
            f'"Iya {nama_laki}, sambil makan mereka juga belajar budaya,” jawab {nama_perempuan}.'
        ],
        "penjelasan": "Sego Tempong adalah kuliner khas Situbondo, Jawa Timur, terkenal dengan rasa pedas yang 'menampar lidah'. Berbahan dasar nasi putih dengan lalapan, sambal khas, dan lauk seperti ikan atau tempe goreng. Makanan ini menjadi ikon kuliner Situbondo dan populer di kalangan wisatawan.",
        "fakta": "1. Merupakan kuliner khas Situbondo, Jawa Timur.\n"
            "2. Nama 'tempong' berarti tamparan karena rasanya pedas.\n"
            "3. Berbahan dasar nasi putih, lalapan, sambal, dan lauk seperti ikan atau tempe goreng.\n"
            "4. Sambal terbuat dari cabai, tomat, dan bawang.\n"
            "5. Menjadi ikon kuliner Situbondo dan populer bagi wisatawan.",
        "soal": [
            {"pertanyaan": "Sego Tempong berasal dari kabupaten mana?",
             "pilihan": ["A. Situbondo", "B. Banyuwangi", "C. Malang", "D. Kediri"],
             "jawaban": "A"},
            {"pertanyaan": "Arti kata 'tempong' dalam Sego Tempong adalah?",
             "pilihan": ["A. Segar", "B. Tamparan", "C. Pedas", "D. Manis"],
             "jawaban": "B"},
            {"pertanyaan": "Bahan utama Sego Tempong adalah?",
             "pilihan": ["A. Nasi putih", "B. Jagung", "C. Kentang", "D. Tepung beras"],
             "jawaban": "A"},
            {"pertanyaan": "Sambal Sego Tempong biasanya terbuat dari?",
             "pilihan": ["A. Cabai, tomat, dan bawang", "B. Kacang tanah dan gula", "C. Jahe dan serai", "D. Kelapa dan santan"],
             "jawaban": "A"},
            {"pertanyaan": "Sego Tempong menjadi ikon kuliner dari mana?",
             "pilihan": ["A. Kabupaten Malang", "B. Kabupaten Situbondo", "C. Kabupaten Trenggalek", "D. Kota Surabaya"],
             "jawaban": "B"}
        ],
    },
    {
        "nama": "Banyuwangi",
        "story": [
            "Di Banyuwangi, mereka menonton Tari Gandrung di tepi pantai. Penari mengenakan kostum warna-warni, menari anggun diiringi musik gamelan.",
            f'"Cantik banget ya {nama_perempuan}… gerakannya anggun dan penuh semangat,” kata {nama_laki}.',
            f'"Anak-anak bisa belajar tari tradisional sekaligus sejarahnya. Gandrung awalnya untuk menyambut tamu dan merayakan panen,” jawab {nama_perempuan}.',
            f"{nama_laki} dan {nama_perempuan} mencoba menirukan gerakan sederhana, tertawa dan bersenang-senang bersama anak-anak lokal. Suasana meriah dan hangat.",
            f'"Belajar budaya sambil menari pasti menyenangkan bagi anak-anak,” kata {nama_laki}.',
            f'"Iya {nama_laki}, mereka bisa merasakan langsung semangat dan keindahan tradisi lokal,” jawab {nama_perempuan}.'
        ],
        "penjelasan": "Tari Gandrung adalah tarian tradisional dari Banyuwangi, Jawa Timur. Awalnya sebagai ungkapan syukur kepada Dewi Sri setelah panen. Dibawakan oleh penari perempuan dengan gerakan lemah gemulai, lincah, dan ekspresif, diiringi musik tradisional seperti gamelan dan kendang. Menjadi ikon budaya Banyuwangi dan sering tampil dalam festival atau upacara adat.",
        "fakta": "1. Tari Gandrung berasal dari Banyuwangi, Jawa Timur.\n"
                 "2. Awalnya sebagai ungkapan syukur setelah panen.\n"
                 "3. Dibawakan oleh penari perempuan dengan gerakan lemah gemulai dan lincah.\n"
                 "4. Diiringi musik tradisional seperti gamelan dan kendang.\n"
                 "5. Menjadi ikon budaya Banyuwangi dan sering tampil di festival dan upacara adat.",
        "soal": [
            {"pertanyaan": "Tari Gandrung berasal dari daerah mana?",
             "pilihan": ["A. Malang", "B. Banyuwangi", "C. Trenggalek", "D. Kediri"],
             "jawaban": "B"},
            {"pertanyaan": "Tari Gandrung awalnya berfungsi sebagai apa?",
             "pilihan": ["A. Hiburan raja", "B. Ungkapan rasa syukur setelah panen", "C. Pertunjukan perang", "D. Tari penyambutan tamu kerajaan"],
             "jawaban": "B"},
            {"pertanyaan": "Penari Tari Gandrung biasanya berjenis kelamin apa?",
             "pilihan": ["A. Laki-laki", "B. Perempuan", "C. Anak-anak", "D. Semua usia"],
             "jawaban": "B"},
            {"pertanyaan": "Musik tradisional apa yang biasanya mengiringi Tari Gandrung?",
             "pilihan": ["A. Angklung", "B. Gamelan dan kendang", "C. Seruling bambu", "D. Sasando"],
             "jawaban": "B"},
            {"pertanyaan": "Tari Gandrung menjadi ikon budaya dari mana?",
             "pilihan": ["A. Trenggalek", "B. Banyuwangi", "C. Malang", "D. Kediri"],
             "jawaban": "B"}
        ]
    },
    {
        "nama": "Jember",
        "story": [
            "Di Jember, mereka memasuki pasar rakyat yang penuh warna dan suara. Musik Daul, alat musik tradisional, terdengar riang mengiringi para penari.",
            f'"{nama_perempuan}, musiknya unik banget… bikin semangat,” kata {nama_laki}.',
            f'"Itu Musik Daul, {nama_laki}. Anak-anak bisa belajar ritme, alat musik, dan budaya lokal sambil bermain,” jawab {nama_perempuan}.',
            "Mereka ikut menirukan ritme sederhana, sambil melihat anak-anak lokal belajar alat musik dan menari mengikuti musik. Suasana penuh tawa, musik, dan kegembiraan.",
            f'"Belajar musik sambil bermain itu menyenangkan ya {nama_perempuan},” kata {nama_laki}.',
            f'"Iya {nama_laki}, anak-anak bisa mudah mengingat dan menikmati budaya tradisional,” jawab {nama_perempuan}.'
        ],
        "penjelasan": "Musik Daul adalah kesenian tradisional khas Jember, Jawa Timur, berupa permainan alat musik pukul yang mengiringi upacara adat, perayaan, atau hiburan rakyat. Biasanya dimainkan oleh sekelompok orang dengan gendang besar (daul) dan alat musik tambahan lainnya, menghasilkan ritme yang energik dan khas.",
        "fakta": "1. Kesenian tradisional khas Jember, Jawa Timur.\n"
                 "2. Menggunakan alat musik pukul, terutama gendang besar (daul).\n"
                 "3. Biasanya dimainkan dalam upacara adat, perayaan, atau hiburan rakyat.\n"
                 "4. Menghasilkan ritme energik yang mengiringi tari tradisional atau ritual.\n"
                 "5. Menjadi simbol kebersamaan dan pelestarian budaya lokal.",
        "soal": [
            {"pertanyaan": "Musik Daul berasal dari kabupaten mana?",
             "pilihan": ["A. Malang", "B. Jember", "C. Banyuwangi", "D. Kediri"],
             "jawaban": "B"},
            {"pertanyaan": "Alat musik utama dalam Musik Daul adalah?",
             "pilihan": ["A. Suling", "B. Gendang besar (daul)", "C. Rebab", "D. Angklung"],
             "jawaban": "B"},
            {"pertanyaan": "Musik Daul biasanya dimainkan dalam acara apa?",
             "pilihan": ["A. Festival film", "B. Upacara adat, perayaan, atau hiburan rakyat", "C. Konser musik pop", "D. Pertandingan olahraga"],
             "jawaban": "B"},
            {"pertanyaan": "Fungsi Musik Daul selain hiburan adalah?",
             "pilihan": ["A. Pengiring tari tradisional dan ritual", "B. Menjadi alat transportasi", "C. Media pendidikan formal", "D. Alat komunikasi modern"],
             "jawaban": "A"},
            {"pertanyaan": "Musik Daul juga menjadi simbol apa?",
             "pilihan": ["A. Kemewahan dan kekayaan", "B. Kebersamaan dan pelestarian budaya lokal", "C. Modernisasi dan teknologi", "D. Olahraga tradisional"],
             "jawaban": "B"}
        ]
    },
    {
        "nama": "Tulungagung",
        "story": [
            "Di Tulungagung, malam hari mereka menyaksikan Nyandran, tradisi warga yang membawa obor berkeliling rumah sambil bernyanyi.",
            f'"{nama_perempuan}, lihat itu… orang-orang bawa obor dari rumah ke rumah,” kata {nama_laki} terkejut.',
            f'"Ah itu Nyandran, {nama_laki}. Tradisi ini untuk menjaga kebersamaan dan mempererat hubungan tetangga. Anak-anak bisa belajar nilai gotong royong dan tradisi lokal,” jawab {nama_perempuan}.',
            "Mereka berjalan mengikuti warga sebentar, melihat anak-anak ikut membawa obor kecil. Suasana hangat dan riang membuat mereka betah berlama-lama.",
            f'"Anak-anak pasti senang bisa ikut merasakan langsung tradisi ini,” kata {nama_laki}.',
            f'"Iya {nama_laki}, belajar budaya sambil mengalami sendiri lebih seru,” jawab {nama_perempuan}.'
        ],
        "penjelasan": "Nyandran adalah tradisi unik masyarakat Tulungagung, Jawa Timur, dilakukan pada malam hari menjelang Ramadan atau acara adat lokal. Masyarakat berkeliling dari rumah ke rumah membawa lampu atau obor, sambil menyanyikan doa dan pantun tradisional. Tradisi ini mempererat silaturahmi dan menjaga keberlangsungan adat turun-temurun.",
        "fakta": "1. Tradisi khas Tulungagung, Jawa Timur.\n"
                 "2. Dilakukan pada malam hari menjelang Ramadan atau dalam acara adat lokal.\n"
                 "3. Bertujuan memohon keselamatan, keberkahan, dan menjaga kerukunan warga.\n"
                 "4. Kegiatan melibatkan berkeliling dari rumah ke rumah sambil membawa lampu atau obor.\n"
                 "5. Menjadi sarana mempererat silaturahmi dan menjaga keberlangsungan adat lokal.",
        "soal": [
            {"pertanyaan": "Nyandran berasal dari kabupaten mana?",
             "pilihan": ["A. Malang", "B. Tulungagung", "C. Kediri", "D. Jember"],
             "jawaban": "B"},
            {"pertanyaan": "Nyandran biasanya dilakukan pada waktu apa?",
             "pilihan": ["A. Siang hari saat panen", "B. Malam hari menjelang Ramadan atau acara adat", "C. Pagi hari setiap Senin", "D. Tengah malam pada musim hujan"],
             "jawaban": "B"},
            {"pertanyaan": "Tujuan Nyandran adalah untuk apa?",
             "pilihan": ["A. Memperingati ulang tahun kota", "B. Memohon keselamatan, keberkahan, dan menjaga kerukunan warga", "C. Menghibur tamu kerajaan", "D. Kompetisi antar desa"],
             "jawaban": "B"},
            {"pertanyaan": "Dalam Nyandran, masyarakat biasanya membawa apa?",
             "pilihan": ["A. Payung dan bendera", "B. Lampu atau obor", "C. Alat musik modern", "D. Sayuran dan buah"],
             "jawaban": "B"},
            {"pertanyaan": "Nyandran juga berfungsi sebagai sarana apa?",
             "pilihan": ["A. Kompetisi olahraga", "B. Mempererat silaturahmi dan menjaga adat lokal", "C. Festival kuliner", "D. Pertunjukan teater modern"],
             "jawaban": "B"}
        ]
    },
    {
        "nama": "Madiun",
        "story": [
            "Di Madiun, mereka melihat pertunjukan Pencak Silat di alun-alun kota. Para pesilat menunjukkan gerakan lincah dan kekuatan, sambil mempertahankan keseimbangan.",
            f'"{nama_perempuan}, keren banget gerakannya… kuat dan lincah,” kata {nama_laki}.',
            f'"Itu Pencak Silat, {nama_laki}. Anak-anak bisa belajar disiplin, kekuatan, dan budaya lokal lewat gerakan ini,” jawab {nama_perempuan}.',
            f"Mereka mencoba beberapa gerakan sederhana bersama anak-anak lokal. Suasana riang, anak-anak tertawa sambil menirukan gerakan, dan {nama_laki} serta {nama_perempuan} menjelaskan filosofi gerakan pencak silat.",
            f'"Belajar olahraga tradisional sambil bermain pasti menyenangkan,” kata {nama_laki}.',
            f'"Iya {nama_laki}, anak-anak belajar budaya dan fisik sekaligus,” jawab {nama_perempuan}.'
        ],
        "penjelasan": "Pencak Silat Madiun adalah salah satu aliran Pencak Silat yang berkembang di Kota dan Kabupaten Madiun, Jawa Timur. Menggabungkan teknik menyerang, bertahan, keseimbangan tubuh, serta filosofi hidup. Kadang diiringi musik tradisional seperti gamelan atau kendang. Sering diajarkan di sekolah atau perguruan silat sebagai olahraga, seni pertunjukan, dan pengembangan karakter.",
        "fakta": "1. Merupakan aliran Pencak Silat yang berkembang di Madiun, Jawa Timur.\n"
                 "2. Menggabungkan teknik menyerang, bertahan, keseimbangan, dan filosofi hidup.\n"
                 "3. Gerakannya lincah, fleksibel, dan kadang diiringi musik tradisional.\n"
                 "4. Sering dipelajari sebagai olahraga, seni pertunjukan, dan pengembangan karakter.\n"
                 "5. Menjadi salah satu ikon budaya tradisional Madiun yang dijaga kelestariannya.",
        "soal": [
            {"pertanyaan": "Pencak Silat Madiun berkembang di provinsi mana?",
             "pilihan": ["A. Jawa Tengah", "B. Jawa Timur", "C. Jawa Barat", "D. Bali"],
             "jawaban": "B"},
            {"pertanyaan": "Pencak Silat Madiun menggabungkan unsur apa saja?",
             "pilihan": ["A. Menyanyi dan menari", "B. Teknik menyerang, bertahan, keseimbangan, dan filosofi hidup", "C. Olahraga dan memasak", "D. Lukisan dan musik"],
             "jawaban": "B"},
            {"pertanyaan": "Gerakan Pencak Silat Madiun biasanya seperti apa?",
             "pilihan": ["A. Lambat dan statis", "B. Lincah dan fleksibel", "C. Terkadang kaku", "D. Tidak teratur"],
             "jawaban": "B"},
            {"pertanyaan": "Musik tradisional apa yang kadang mengiringi Pencak Silat Madiun?",
             "pilihan": ["A. Angklung", "B. Gamelan atau kendang", "C. Sasando", "D. Seruling bambu"],
             "jawaban": "B"},
            {"pertanyaan": "Selain sebagai olahraga, Pencak Silat Madiun juga berfungsi sebagai apa?",
             "pilihan": ["A. Sarana pengembangan karakter seperti disiplin dan keberanian", "B. Alat transportasi", "C. Hidangan tradisional", "D. Media komunikasi"],
             "jawaban": "A"}
        ]
    }
]
    start_perjalanan()

# Struktur gelar per daerah
gelar_daerah = {
    "Ponorogo": [
        (2, "Warok Cilik"),
        (3, "Warok Muda"),
        (5, "Sang Warok"),
    ],
    "Madiun": [
        (2, "Pesilat Pemula"),
        (3, "Pendekar Remaja"),
        (5, "Pendekar Silat Madiun"),
    ],
    "Lumajang": [
        (2, "Penjelajah Ranu"),
        (3, "Penerobos Savana"),
        (5, "Penakluk Mahameru"),
    ],
    "Surabaya": [
        (2, "Pejuang Cilik Suroboyo"),
        (3, "Pemimpin Arek Suroboyo"),
        (5, "Pahlawan Kota Pahlawan"),
    ],
    "Magetan": [
        (2, "Pelayar Telaga"),
        (3, "Pengabdi Lawu"),
        (5, "Duta Telaga Sarangan"),
    ],
    "Kota Batu": [
        (2, "Jago Wahana Jatim"),
        (3, "Spesialis Edukasi Alam"),
        (5, "Pakar Jatim Park"),
    ],
    "Pasuruan": [
        (2, "Penerus Banteng"),
        (3, "Pewaris Tradisi"),
        (5, "Penggerak Semangat Bantengan"),
    ],
    "Probolinggo": [
        (2, "Penikmat Lautan Pasir"),
        (3, "Pengawas Kaldera"),
        (5, "Penjaga Bromo Tengger"),
    ],
    "Bojonegoro": [
        (2, "Pencinta Thegul"),
        (3, "Pembaca Kisah Wayang"),
        (5, "Pelestari Wayang Thegul"),
    ],
    "Nganjuk": [
        (2, "Pencari Tirta"),
        (3, "Pengumpul Air Berkah"),
        (5, "Pengembara Air Suci Sedudo"),
    ],
    "Ngawi": [
        (2, "Peminat Arsitektur Kuno"),
        (3, "Penemu Lorong Benteng"),
        (5, "Pengamat Sejarah Kolonial"),
    ],
    "Banyuwangi": [
        (2, "Peminat Gandrung"),
        (3, "Penari Osing Cilik"),
        (5, "Penggiat Tari Gandrung"),
    ],
    "Situbondo": [
        (2, "Pencicip Sambal"),
        (3, "Penantang Pedas"),
        (5, "Jago Sego Tempong"),
    ],
    "Tulungagung": [
        (2, "Pembawa Cahaya"),
        (3, "Penyanyi Malam"),
        (5, "Penyebar Sinar Nyandran"),
    ],
}

# Gelar interaktif
gelar_interaktif = [
    (3, "Jawara 3 Daerah Berturut-turut"),
    (5, "Jawara 5 Daerah Berturut-turut"),
    (10, "Jawara 10 Daerah Berturut-turut")
    # Tambahkan gelar lain seperti menjawab cepat, dsb
]

# Tracking gelar yang didapat
gelar_didapat = []

# Tracking streak benar semua soal
streak = 0

# Tracking waktu untuk gelar kecepatan
start_time = None

def menu_utama():
    clear()
    print("╔════════════════════════════════════════╗")
    print("║         🦊 MENU STORY MODE 🦊          ║")
    print("╠════════════════════════════════════════╣")
    print("║ 1. Mulai 🏁       → Ayo bermain!       ║")
    print("║ 2. Lihat Gelar 🏆  → Cek gelarmu!      ║")
    print("║ 0. Kembali ⬅️      → Balik dulu yuk!    ║")
    print("╚════════════════════════════════════════╝")
    pilihan = input("Pilih (0-2): ")
    if pilihan == "1":
        input_nama()
    elif pilihan == "2":
        menu_gelar()
    elif pilihan == "0":
        import main
        os.system('cls')
        main.menu()
    else:
        invalid_input()
        menu_utama()

# Start perjalanan

# Start perjalanan
def start_perjalanan():
    global start_time, SKIP_DELAY
    
    # Reset state saat memulai perjalanan baru
    SKIP_DELAY = 0.03
    start_time = time.time()
    
    for wilayah in wilayahs:
        clear()
        type_text(f"══════════════════════════════ {wilayah['nama']} ══════════════════════════════", 0.025)
        
        # --- LOOP CERITA DENGAN INTERUPSI ---
        for kalimat in wilayah['story']:
            type_text(kalimat)
            
            # Cek interupsi (skip atau kembali ke menu)
            control_signal = check_interrupt()
            
            if control_signal == 'menu':
                menu_utama() # Langsung lompat ke menu utama
                return # Hentikan fungsi start_perjalanan
        # --- END LOOP CERITA ---

        while True:
            print("\n╔═════════════════════════════════════════╗")
            print("║               🌟 AKSI 🌟                ║")
            print("╠═════════════════════════════════════════╣")
            print("║ 1. Kuis Edukasi ✍️  → Uji ilmu!          ║")
            print("║ 2. Pelajari Lebih Lanjut ℹ️ → Baca info! ║")
            print("║ 3. Lanjut Perjalanan ➡️ → Terus maju!    ║")
            print("║ 0. Kembali ke Menu Utama ⬅️ → Balik dulu.║")
            print("╚═════════════════════════════════════════╝")
            pilihan = input("Pilih (0-3): ")

            if pilihan == '0':
                menu_utama()
                return
            elif pilihan == '3':
                break
            elif pilihan == '2':
                clear()
                type_text("══════════════════════════════ PENJELASAN ══════════════════════════════")
                type_text(wilayah['penjelasan'])
                type_text("══════════════════════════════ FAKTA MENARIK ══════════════════════════════")
                type_text(wilayah['fakta'])
                input("Tekan Enter untuk kembali ke menu aksi...")
            elif pilihan == '1':
                clear()
                type_text("══════════════════════════════ KUIS EDUKASI ══════════════════════════════")
                soal_wilayah = wilayah['soal']
                total_soal = len(soal_wilayah)
                benar = 0
                
                # --- LOGIKA GELAR DAERAH BERTINGKAT ---
                quiz_streak = 0
                gelar_diraih_di_daerah_ini = []
                
                for i, soal in enumerate(soal_wilayah):
                    type_text(f"\nSoal {i+1}: {soal['pertanyaan']}")
                    for j, pilihan_jawaban in enumerate(soal['pilihan']):
                        print(pilihan_jawaban)
                    print("Tekan 0 untuk kembali ke menu.")
                    jawaban_user = input("Jawaban Anda (A/B/C/D): ").upper()
                    
                    if jawaban_user == soal['jawaban']:
                        type_text("BENAR!👍")
                        benar += 1
                        quiz_streak += 1 # Tambah streak jika benar
                    elif jawaban_user == '0':
                        menu_utama()
                        return
                    else:
                        type_text(f"SALAH. Jawaban yang benar adalah {soal['jawaban']} ({soal['pilihan'][ord(soal['jawaban']) - ord('A')]})")
                        quiz_streak = 0 # Reset streak jika salah
                    
                    # Cek gelar daerah bertingkat setelah setiap jawaban
                    nama_daerah = wilayah['nama']
                    if nama_daerah in gelar_daerah:
                        # Iterasi dari streak tertinggi ke terendah
                        for min_streak, nama_gelar in sorted(gelar_daerah[nama_daerah], reverse=True):
                            if quiz_streak >= min_streak:
                                if nama_gelar not in gelar_didapat:
                                    gelar_didapat.append(nama_gelar)
                                    gelar_diraih_di_daerah_ini.append(nama_gelar)
                                    type_text(f"\n SELAMAT! ANDA MENDAPAT GELAR DAERAH: {nama_gelar}! \n", 0.05)
                                break # Ambil gelar tertinggi yang memenuhi kriteria streak

                type_text(f"\nHasil Kuis: Benar {benar} dari {total_soal} soal.")
                if gelar_diraih_di_daerah_ini:
                    type_text(f"Gelar baru yang didapat di {nama_daerah}: {', '.join(gelar_diraih_di_daerah_ini)}")

                input("Klik Enter untuk melanjutkan perjalanan Anda...")
                # Reset SKIP_DELAY kembali normal setelah kuis (jika sebelumnya di-skip)
                SKIP_DELAY = 0.03 
                break
            else:
                invalid_input()
                continue
    # Cek gelar kecepatan (Jika Anda ingin mempertahankan ini)
    waktu_total = time.time() - start_time
    if waktu_total < 180: # misal < 3 menit
        if "Penjelajah Super Cepat" not in gelar_didapat:
            gelar_didapat.append("Penjelajah Super Cepat")
    
    # Menampilkan semua gelar setelah perjalanan selesai
    menu_gelar()


# Menu gelar

def menu_gelar():
    clear()
    print("╔════════════════════════════════════════╗")
    print("║            🏆 GELAR ANDA 🏆            ║")
    print("╚════════════════════════════════════════╝")
    if gelar_didapat:
        for i, gelar in enumerate(gelar_didapat, 1):
            print(f"{i}. {gelar}")

    else:
        print("Belum ada gelar yang didapatkan.")
        
    input("Tekan Enter untuk kembali ke menu utama...")
    menu_utama()

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