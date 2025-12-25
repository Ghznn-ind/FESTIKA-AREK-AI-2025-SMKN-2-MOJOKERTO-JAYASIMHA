import os

bank_soal_quiz = {
    "1": {  # Budaya
        "soal": [
            {
                "soal": "Tari tradisional dari Surabaya yang sering dipentaskan untuk penyambutan tamu kehormatan.",
                "jawaban": "Tari Remo",
                "clue": ["Penarinya memakai gelang kaki berbunyi.", 
                         "Penarinya memakai gelang kaki berbunyi.", 
                         "Sering menjadi bagian pertunjukan Ludruk."
                         ]
            },
            {
                "soal": "Tari khas Banyuwangi yang dibawakan penari perempuan dengan selendang.",
                "jawaban": "Tari Gandrung",
                "clue": ["Berasal dari budaya Using.", 
                         "Identik dengan Festival Banyuwangi.", 
                         "Sering dibawakan oleh seorang 'Paju'."
                         ]
            },
            {
                "soal": "Senjata tradisional masyarakat Madura yang berbentuk melengkung.",
                "jawaban": "Celurit",
                "clue": ["Dipakai dalam tradisi karapan.",
                         "Melambangkan keberanian.",
                         "Merupakan simbol khas Madura."
                         ]
            },
            {
                "soal": "Rumah adat khas Madura yang dihuni keluarga besar dalam satu kompleks memanjang.",
                "jawaban": "Tanean Lanjeng",
                "clue": ["Rumah-rumahnya tertata memanjang.",
                         "Digunakan untuk berkumpul keluarga besar.",
                         "Merupakan ciri permukiman tradisional Madura."
                         ]
            },
            {
                "soal": "Kesenian yang menggunakan kuda-kudaan dari bambu dan kadang melibatkan trance.",
                "jawaban": "Jaranan",
                "clue": ["Memakai kuda kepang.",
                         "Musiknya didominasi kendang.",
                         "Sering disebut kuda lumping."
                         ]
            },
            {
                "soal": "Pertunjukan drama tradisional yang menggunakan bahasa khas Jawa Timur.",
                "jawaban": "Ludruk",
                "clue": ["Mengangkat kisah rakyat.",
                         "Menampilkan tokoh Cak dan Ning.",
                         "Berasal dari Surabaya."
                         ]
            },
            {
                "soal": "Tari tradisional Madura yang memiliki fungsi tolak bala.",
                "jawaban": "Tari Muang Sangkal",
                "clue": ["Menggunakan busana khas Madura.",
                         "Dibawakan saat acara adat.",
                         "Melambangkan penolak kesialan."
                         ]
            },
            {
                "soal": "Kesenian tradisional Ponorogo yang terkenal dengan topeng besar.",
                "jawaban": "Reog Ponorogo",
                "clue": ["Ada penari Warok.",
                         "Diiringi tarian Jathil.",
                         "Topeng utamanya Singo Barong."
                         ]
            },
            {
                "soal": "Upacara adat suku Tengger yang dilakukan di Gunung Bromo.",
                "jawaban": "Kasada",
                "clue": ["Dilakukan di kawah gunung.",
                         "Warga membawa hasil bumi.",
                         "Tradisi umat Hindu Tengger."
                         ]
            },
            {
                "soal": "Seni yang menampilkan atraksi berjalan di atas bambu panjang.",
                "jawaban": "Egrang",
                "clue": ["Menggunakan bambu tinggi.",
                         "Permainan tradisional.",
                         "Sering hadir di festival budaya."
                         ]
            },
            {
                "soal": "Seni musik Jawa Timur yang menggunakan rebana besar.",
                "jawaban": "Hadrah",
                "clue": ["Mengandung syair Islami.",
                         "Diiringi rebana.",
                         "Ditampilkan pada acara keagamaan."
                         ]
            },
            {
                "soal": "Kesenian khas Jombang yang berupa humor rakyat.",
                "jawaban": "Jepenan",
                "clue": ["Menggunakan dialog lucu.",
                         "Mengandung kritik sosial.",
                         "Asal Jombang."
                         ]
            },
            {
                "soal": "Seni bela diri tradisional Jawa Timur.",
                "jawaban": "Pencak Silat",
                "clue": ["Diakui sebagai seni bela diri nasional",
                         "Mengandung filosofi luhur.",
                         "Masuk dalam budaya Nusantara."
                         ]
            },
            {
                "soal": "Pertunjukan tradisional yang memakai boneka kulit.",
                "jawaban": "Wayang",
                "clue": ["Boneka terbuat dari kulit.",
                         "Dibawakan umat Hindu.",
                         "Masuk dalam budaya Nusantara."
                         ]
            },
            {
                "soal": "Seni pertunjukan yang menampilkan cerita Panji dengan topeng.",
                "jawaban": "Tari Topeng",
                "clue": ["Menggunakan topeng kayu.",
                         "Pemain tidak berbicara.",
                         "Populer di Malang."
                         ]
            },
            {
                "soal": "Topeng kayu khas Malang yang digunakan dalam tarian tradisional.",
                "jawaban": "Topeng Malangan",
                "clue": ["Berwarna cerah.",
                         "Tokohnya berasal dari kisah Panji.",
                         "Berasal dari Malang."
                         ]
            },
            {
                "soal": "Musik tradisional dari Madura yang menggunakan alat tiup khas.",
                "jawaban": "Saronen",
                "clue": ["Suara alatnya nyaring.",
                         "Sering untuk upacara adat.",
                         "Menjadi identitas musik Madura."
                         ]
            },
            {
                "soal": "Tradisi masyarakat Using yang dilakukan sebagai ritual bersih desa.",
                "jawaban": "Kebo-keboan",
                "clue": ["Peserta berdandan seperti kerbau.",
                         "Dilakukan untuk menolak bala.",
                         "Berasal dari Banyuwangi."
                         ]
            },
            {
                "soal": "Pakaian adat khas Madura yang dikenakan oleh pria.",
                "jawaban": "Baju Pesaan",
                "clue": ["Didominasi warna hitam.",
                         "Dipadukan dengan sarung.",
                         "Identik dengan Madura."
                         ]
            },
            {
                "soal": "Tari hiburan rakyat yang banyak ditemukan di wilayah Kediri.",
                "jawaban": "Tari Tayub",
                "clue": ["Diiringi musik tradisional.",
                         "Penari mengajak tamu menari.",
                         "Termasuk hiburan tradisional."
                         ]
            },
            {
                "soal": "Kesenian yang menampilkan dua pria bermain peran jenaka.",
                "jawaban": "Dagelan Mataraman",
                "clue": ["Mengandung unsur komedi.",
                         "Menggunakan logat Jawa Timuran.",
                         "Termasuk hiburan rakyat."
                         ]
            },
            {
                "soal": "Tari dari Trenggalek yang menggambarkan kegagahan prajurit.",
                "jawaban": "Tari Turonggo Yakso",
                "clue": ["Gerakannya tegas.",
                         "Menggunakan kostum prajurit.",
                         "Berasal dari Trenggalek."
                         ]
            },
            {
                "soal": "Tari khas Madura yang menggambarkan kegesitan gadis muda.",
                "jawaban": "Tari Galundung",
                "clue": ["Gerakannya lincah.",
                         "Penari memakai selendang.",
                         "Berasal dari Madura."
                         ]
            },
            { 
                "soal": "Ritual adat untuk meminta hujan yang dilakukan di Jawa Timur.",
                "jawaban": "Upacara Manten Air",
                "clue": ["Menggunakan air sebagai simbol.",
                         "Dipimpin sesepuh desa.",
                         "Dilakukan saat musim kemarau."
                         ]
            },
            {
                "soal": "Seni musik khas Banyuwangi yang menggunakan kendang sebagai alat utama.",
                "jawaban": "Kendang Kempul",
                "clue": ["Berirama cepat.",
                         "Sering mengiringi gandrung.",
                         "Ciri khas Banyuwangi."
                         ]
            },
            {
                "soal": "Tari yang menggambarkan kehidupan nelayan di pesisir Jawa Timur.",
                "jawaban": "Tari Nelayan",
                "clue": ["Gerakannya meniru menarik jala.",
                         "Diiringi musik ceria.",
                         "Sering ditampilkan di daerah pesisir."
                         ]
            },
            {
                "soal": "Seni permainan tradisional yang melibatkan atraksi debus.",
                "jawaban": "Debus Jawa Timur",
                "clue": ["Menampilkan ketahanan tubuh.",
                         "Menggunakan senjata tajam.",
                         "Ada unsur magisnya."
                         ]
            },
            {
                "soal": "Tari khas Malang yang menggambarkan kelincahan kera.",
                "jawaban": "Tari Topeng Kera",
                "clue": ["Penarinya memakai topeng hewan.",
                         "Gerakannya lincah dan cepat.",
                         "Berasal dari Malang."
                         ]
            },
            {
                "soal": "Tari tradisional yang menggambarkan kegigihan petani.",
                "jawaban": "Tari Petik Laut",
                "clue": ["Berasal dari pesisir.",
                         "Mengandung unsur syukur.",
                         "Ditampilkan saat ritual adat."
                         ]
            },
            {
                "soal": "Seni sulap tradisional yang dilakukan dalam pertunjukan rakyat.",
                "jawaban": "Sulap Kampung",
                "clue": ["Menghibur masyarakat desa.",
                         "Tanpa teknologi modern.",
                         "Sering hadir di pasar malam."]
            }
        ]
    },
    "2": { # Bentang Alam
        "soal": [
            {
                "soal": "Gunung api tertinggi di Pulau Jawa yang puncaknya disebut Mahameru dan terletak di perbatasan Kabupaten Lumajang dan Malang.",
                "jawaban": "Gunung Semeru",
                "clue": [" Berada di kawasan Taman Nasional Bromo Tengger Semeru.",
                         "Statusnya saat ini aktif normal.",
                         "Sering menjadi tujuan pendakian yang menantang di Jawa."
                         ]
            },
            {
                "soal": "Fenomena alam unik berupa 'api biru' (blue fire) yang hanya terlihat pada dini hari di salah satu kompleks pegunungan di ujung timur Jawa.",
                "jawaban": "Kawah Ijen",
                "clue": [
                    "Merupakan danau kawah vulkanik yang sangat asam.",
                    "Terletak di perbatasan Kabupaten Banyuwangi dan Bondowoso.",
                    "Tempat penambangan belerang tradisional."
                ]
            },
            {
                "soal": "Sungai terpanjang kedua di Pulau Jawa setelah Bengawan Solo yang hulunya berada di sekitar Gunung Arjuno dan menjadi sumber air vital bagi banyak wilayah di Jawa Timur.",
                "jawaban": "Sungai Brantas",
                "clue": [
                    "Bermuara di sekitar Selat Madura (Gresik/Surabaya).",
                    "Melewati kota-kota besar seperti Malang, Kediri, dan Mojokerto.",
                    "Memiliki anak sungai penting, yaitu Kali Mas dan Kali Porong."
                ]
            },
            {
                "soal": "Selat yang memisahkan Pulau Jawa dengan Pulau Madura, di mana di atasnya membentang jembatan terpanjang di Indonesia.",
                "jawaban": "Selat Madura",
                "clue": [
                    "Menghubungkan Laut Jawa dengan Samudra Hindia.",
                    "Terdapat Pelabuhan Tanjung Perak.",
                    "Memiliki nama yang sama dengan pulau yang dipisahkannya."
                ]
            },
            {
                "soal": "Kawasan konservasi yang terkenal dengan lautan pasir (sand sea) yang luas dan kaldera purba, serta dihuni oleh Suku Tengger.",
                "jawaban": "Taman Nasional Bromo Tengger Semeru",
                "clue": [
                    "Terbentang di empat wilayah kabupaten (Pasuruan, Probolinggo, Malang, Lumajang).",
                    "Di dalamnya terdapat gunung yang masih aktif.",
                    "Merupakan destinasi wisata ikonik untuk melihat matahari terbit."
                ]
            },
            {
                "soal": "Gunung api di dekat Kediri yang kawahnya pernah membentuk danau sebelum meletus hebat pada tahun 2014, menghasilkan hujan abu vulkanik yang meluas.",
                "jawaban": "Gunung Kelud",
                "clue": [
                    "Terletak di perbatasan tiga kabupaten (Kediri, Blitar, dan Malang).",
                    "Namanya sering dikaitkan dengan legenda tentang Joko Lelono.",
                    "Jalur pendakiannya telah diperbaiki dan mudah diakses."
                ]
            },
            {
                "soal": "Dataran tinggi yang terkenal dengan iklim sejuk dan menjadi pusat penghasil apel serta pariwisata modern di Jawa Timur.",
                "jawaban": "Kota Batu",
                "clue": [
                    "Secara administratif berstatus sebagai Kota Otonom.",
                    "Dulunya merupakan bagian dari Kabupaten Malang.",
                    "Dijuluki De Kleine Zwitserland (Swiss Kecil)."
                ]
            },
            {
                "soal": "Pantai yang terletak di pesisir selatan Kabupaten Banyuwangi dan sangat terkenal di kalangan peselancar internasional karena ombak besarnya yang dijuluki Seven Giant Waves.",
                "jawaban": "Pantai Plengkung",
                "clue": [
                    "Merupakan bagian dari Taman Nasional Alas Purwo.",
                    "Sering disingkat menjadi G-Land.",
                    "Termasuk dalam The Triangle Diamond Banyuwangi."
                ]
            },
            {
                "soal": "Pegunungan yang membentang di wilayah selatan Jawa Timur, mulai dari Pacitan hingga Trenggalek, yang didominasi oleh batuan kapur (karst).",
                "jawaban": "Pegunungan Sewu",
                "clue": [
                    "Kawasan ini kaya akan gua-gua alam.",
                    "Termasuk dalam rangkaian Pegunungan Seribu.",
                    "Pesisirnya terkenal dengan tebing-tebing curam dan pantai pasir putih."
                ]
            },
            {
                "soal": "Danau vulkanik di lereng Gunung Lawu yang terkenal sebagai tempat wisata di Kabupaten Magetan, sering disebut telaga yang berada di ketinggian.",
                "jawaban": "Telaga Sarangan",
                "clue": [
                    "Dikelilingi oleh hutan pinus dan memiliki suhu yang dingin.",
                    "Terdapat mitos naga di dalamnya.",
                    "Pengunjung dapat menyewa perahu motor untuk berkeliling."
                ]
            },
            {
                "soal": "Selat yang memisahkan daratan Pulau Jawa di Banyuwangi dengan Pulau Bali, menjadi jalur penyeberangan utama kapal feri.",
                "jawaban": "Selat Bali",
                "clue": [
                    "Kedalamannya relatif dangkal dan arusnya kuat.",
                    "Terdapat Pelabuhan Ketapang di sisi Jawa.",
                    "Merupakan batas alami paling timur dari Pulau Jawa."
                ]
            },
            {
                "soal": "Salah satu pulau besar di Jawa Timur yang terpisah dari daratan utama, dikenal dengan hasil garam dan memiliki budaya yang khas.",
                "jawaban": "Pulau Madura",
                "clue": [
                    "Terbagi menjadi empat kabupaten administratif.",
                    "Terhubung dengan Surabaya melalui jembatan.",
                    "Memiliki julukan Pulau Garam."
                ]
            },
            {
                "soal": "Pantai di Kabupaten Pacitan yang terkenal dengan fenomena 'Seruling Laut' karena suara unik yang dihasilkan oleh air laut yang masuk ke celah batu karang.",
                "jawaban": "Pantai Klayar",
                "clue": [
                    "Terletak di pesisir selatan yang menghadap Samudra Hindia.",
                    "Kawasan ini didominasi oleh perbukitan karst.",
                    "Merupakan salah satu pantai terpopuler di daerah tersebut."
                ]
            },
            {
                "soal": "Gunung api yang terletak di antara Malang, Blitar, dan Kediri, dikenal memiliki kaldera besar dan merupakan gunung api purba yang masih aktif.",
                "jawaban": "Gunung Arjuno",
                "clue": [
                    "Berada di kawasan yang relatif subur untuk pertanian.",
                    "Berdekatan dengan Gunung Kelud.",
                    "Puncaknya sering dikaitkan dengan kisah Dewi Anjasmoro dan Joko Tole."
                ]
            },
            {
                "soal": "Wilayah di pesisir utara Jawa Timur yang merupakan daerah paling datar dan menjadi tempat muara banyak sungai, termasuk Sungai Brantas, serta terkenal dengan rawa-rawanya.",
                "jawaban": "Dataran Rendah Pantura (Pesisir Utara)",
                "clue": [
                    "Termasuk wilayah Kabupaten Gresik dan Sidoarjo.",
                    "Berdekatan dengan pusat Kota Surabaya.",
                    "Ketinggiannya sangat rendah, rentan terhadap banjir rob."
                ]
            },
            {
                "soal": "Gunung api di perbatasan Kabupaten Probolinggo dan Lumajang yang dikenal dengan letusannya yang sering dan menghasilkan lautan pasir luas di sekitarnya.",
                "jawaban": "Gunung Bromo",
                "clue": [
                    "Termasuk bagian dari kaldera Tengger.",
                    "Memiliki kawah yang aktif dan mudah dicapai wisatawan.",
                    "Sering digunakan untuk upacara adat Yadnya Kasada."
                ]
            },
            {
                "soal": "Pulau kecil di Selat Madura yang terkenal dengan tambak garam dan rumah-rumah bercat putih, serta menjadi bagian Kabupaten Sumenep.",
                "jawaban": "Pulau Gili Iyang",
                "clue": [
                    "Dikenal memiliki kualitas udara terbaik di Indonesia.",
                    "Menjadi destinasi wisata kesehatan.",
                    "Berada di wilayah paling timur Pulau Madura."
                ]
            },
            {
                "soal": "Air terjun tinggi di Kabupaten Lumajang yang mengalir melalui tebing vertikal dan kerap disalahpahami sebagai tirai air karena bentuknya.",
                "jawaban": "Air Terjun Tumpak Sewu",
                "clue": [
                    "Berada di perbatasan Lumajang-Malang.",
                    "Dijuluki Niagara-nya Indonesia.",
                    "Sumber airnya berasal dari aliran Gunung Semeru."
                ]
            },
            {
                "soal": "Sungai besar yang menjadi batas alami antara Surabaya dan Gresik serta menjadi jalur pelayaran sejak zaman kolonial.",
                "jawaban": "Kali Mas",
                "clue": [
                    "Merupakan salah satu anak sungai Brantas.",
                    "Berperan penting sebagai jalur perdagangan masa lalu.",
                    "Melintas di kawasan Kota Tua Surabaya."
                ]
            },
            {
                "soal": "Gunung tertinggi kedua di Jawa Timur setelah Semeru dan terkenal dengan puncaknya yang disebut 'Ongko-Ombo'.",
                "jawaban": "Gunung Raung",
                "clue": [
                    "Memiliki kaldera berbentuk cincin besar.",
                    "Termasuk gunung berapi yang masih aktif.",
                    "Berada di wilayah Banyuwangi dan Bondowoso."
                ]
            },
            {
                "soal": "Bentuk bentang alam berupa tanjung yang menjorok ke laut, berada di Banyuwangi, dan terkenal sebagai titik awal sunrise of Java.",
                "jawaban": "Pantai Boom Banyuwangi",
                "clue": [
                    "Berada dekat pusat kota Banyuwangi.",
                    "Sering dipakai untuk festival internasional.",
                    "Memiliki dermaga modern dengan latar Selat Bali."
                ]
            },
            {
                "soal": "Gunung dengan ketinggian sedang di Pasuruan yang terkenal sebagai spot melihat sunrise serta pemandangan hamparan rumput savana.",
                "jawaban": "Gunung Penanjakan",
                "clue": [
                    "Masih satu kawasan dengan TNBTS.",
                    "Sering menjadi lokasi foto ikon Bromo Sunrise.",
                    "Dapat dicapai menggunakan jeep wisata."
                ]
            },
            {
                "soal": "Pantai berpasir putih di Tulungagung yang memiliki bentuk teluk dan tebing karang tinggi, sehingga ombaknya relatif tenang.",
                "jawaban": "Pantai Popoh",
                "clue": [
                    "Terletak di pesisir selatan Jawa Timur.",
                    "Dekat dengan Pantai Sidem dan Pantai Coro.",
                    "Menjadi tujuan wisata keluarga sejak lama."
                ]
            },
            {
                "soal": "Danau alami di Banyuwangi yang terbentuk dari aktivitas vulkanik dan berada di dataran tinggi, dekat kawasan Raung.",
                "jawaban": "Danau Blawu",
                "clue": [
                    "Sering diselimuti kabut tebal.",
                    "Menjadi habitat burung liar.",
                    "Akses jalannya melewati hutan pinus."
                ]
            },
            {
                "soal": "Gunung yang membentuk gugusan pegunungan kapur di area Tuban dan Lamongan serta memiliki sistem gua bawah tanah yang luas.",
                "jawaban": "Pegunungan Kapur Utara",
                "clue": [
                    "Merupakan rangkaian bentang karst yang luas.",
                    "Memiliki banyak sumber air bawah tanah.",
                    "Menjadi lokasi Gua Maharani dan Gua Akbar."
                ]
            },
            {
                "soal": "Pantai yang berada di Pacitan dengan hamparan batu karang besar di tengah laut yang menjadi ikon foto wisatawan.",
                "jawaban": "Pantai Banyu Tibo",
                "clue": [
                    "Memiliki air terjun yang langsung jatuh ke laut.",
                    "Berhadapan langsung dengan Samudra Hindia.",
                    "Termasuk pantai tersembunyi yang aksesnya menurun terjal."
                ]
            },
            {
                "soal": "Gunung di Kabupaten Jember yang memiliki hutan tropis lebat serta menjadi habitat satwa liar seperti macan tutul.",
                "jawaban": "Gunung Argopuro",
                "clue": [
                    "Jalur pendakiannya dikenal sangat panjang.",
                    "Memiliki danau kecil bernama Danau Taman Hidup.",
                    "Termasuk salah satu gunung dengan legenda Dewi Rengganis."
                ]
            },
            {
                "soal": "Pulau kecil di selatan Banyuwangi yang dipisahkan oleh selat sempit dan dikenal dengan ekosistem mangrove yang luas.",
                "jawaban": "Pulau Sembulungan",
                "clue": [
                    "Dekat dengan pantai selancar internasional.",
                    "Terdapat menara mercusuar tua.",
                    "Dikelilingi hutan lindung Alas Purwo."
                ]
            },
            {
                "soal": "Padang rumput luas di Situbondo yang menjadi habitat banteng Jawa dan bagian penting dari kawasan konservasi di ujung timur Jawa.",
                "jawaban": "Savana Bekol",
                "clue": [
                    "Berada dalam Taman Nasional Baluran.",
                    "Sering disebut 'Little Africa of Java'.",
                    "Memiliki latar Gunung Baluran yang ikonik."
                ]
            },
            {
                "soal": "Pulau kecil di perairan Sumenep yang terkenal dengan air laut yang sangat jernih serta pasir putih halusnya.",
                "jawaban": "Gili Labak",
                "clue": [
                    "Akses utamanya dari Pelabuhan Kalianget.",
                    "Terkenal sebagai spot snorkeling.",
                    "Di sekitarnya terdapat terumbu karang yang masih alami."
                ]
            }
        ] 
    },
    "3": { # Wilayah
        "soal": [
            {
                "soal": "Kota metropolitan terbesar dan sekaligus menjadi ibu kota Provinsi Jawa Timur.",
                "jawaban": "Surabaya",
                "clue": [
                    "Dikenal dengan julukan Kota Pahlawan.",
                    "Memiliki Pelabuhan Tanjung Perak.",
                    "Pusat perdagangan dan bisnis terbesar kedua di Indonesia."
                ]
            },
            {
                "soal": "Kabupaten paling timur di Pulau Jawa yang berbatasan langsung dengan Selat Bali dan sering disebut The Sunrise of Java.",
                "jawaban": "Banyuwangi",
                "clue": [
                    "Memiliki pelabuhan penyeberangan Ketapang.",
                    "Terdapat kawasan wisata Kawah Ijen.",
                    "Ternyata memiliki tradisi adat Suku Osing."
                ]
            },
            {
                "soal": "Kabupaten yang terletak paling barat di Pulau Jawa Timur, berbatasan dengan Jawa Tengah, dan dikenal dengan julukan Kota 1001 Gua.",
                "jawaban": "Pacitan",
                "clue": [
                    "Pesisir selatannya menghadap Samudra Hindia.",
                    "Tempat kelahiran salah satu Presiden Republik Indonesia.",
                    "Salah satu guanya yang terkenal adalah Goa Gong."
                ]
            },
            {
                "soal": "Nama akronim kawasan metropolitan yang mencakup Kota Surabaya dan lima wilayah penyangganya.",
                "jawaban": "Gerbangkertosusila",
                "clue": [
                    "Merupakan pusat pertumbuhan ekonomi utama Jawa Timur.",
                    "Singkatannya merujuk pada nama daerah-daerah tersebut.",
                    "Terhubung oleh infrastruktur jalan tol."
                ]
            },
            {
                "soal": "Kabupaten di Pulau Madura yang merupakan gerbang utama pulau tersebut dan menjadi lokasi ujung Jembatan Suramadu.",
                "jawaban": "Bangkalan",
                "clue": [
                    "Berbatasan langsung dengan Surabaya.",
                    "Terkenal dengan sentra batiknya.",
                    "Wilayahnya berada di bagian paling barat Madura."
                ]
            },
            {
                "soal": "Kabupaten yang berbatasan dengan Surabaya dan dikenal sebagai pusat industri semen, pupuk, dan pelabuhan logistik.",
                "jawaban": "Gresik",
                "clue": [
                    "Termasuk dalam kawasan Gerbangkertosusila.",
                    "Terdapat makam salah satu Wali Songo.",
                    "Dikenal dengan julukan Kota Pudak."
                ]
            },
            {
                "soal": "Kabupaten di tengah Jawa Timur yang terkenal sebagai sentra tembakau.",
                "jawaban": "Jember",
                "clue": [
                    "Wilayahnya berada di selatan Pegunungan Ijen.",
                    "Berbatasan langsung dengan Samudra Hindia.",
                    "Penghasil kopi Robusta dan Arabika."
                ]
            },
            {
                "soal": "Kota di kaki Gunung Lawu yang terkenal dengan industri tekstil, kerajinan kulit, dan Telaga Sarangan.",
                "jawaban": "Magetan",
                "clue": [
                    "Secara kultural termasuk wilayah Mataraman.",
                    "Memiliki Pangkalan Udara Iswahjudi.",
                    "Terdapat Monumen Gubernur Suryo."
                ]
            },
            {
                "soal": "Kabupaten di wilayah selatan Mataraman yang memiliki julukan Kota Marmer.",
                "jawaban": "Tulungagung",
                "clue": [
                    "Berbatasan dengan Trenggalek dan Kediri.",
                    "Memiliki garis pantai Samudra Hindia.",
                    "Terdapat Goa Selomangleng dan Goa Pasir."
                ]
            },
            {
                "soal": "Kabupaten yang menjadi pintu masuk utama ke Bromo dari sisi utara dan terkenal dengan buah anggurnya.",
                "jawaban": "Probolinggo",
                "clue": [
                    "Berada di jalur pantura.",
                    "Terletak di sebelah timur Pasuruan.",
                    "Memiliki Pelabuhan Perikanan Tanjung Tembaga."
                ]
            },
            {
                "soal": "Kota di Jawa Timur yang dianggap pusat kebudayaan Mataraman dan tempat dimakamkannya Soekarno.",
                "jawaban": "Blitar",
                "clue": [
                    "Berada di kaki Gunung Kelud.",
                    "Terkenal dengan Candi Penataran.",
                    "Dikenal sebagai Kota Patria."
                ]
            },
            {
                "soal": "Kabupaten di Pulau Madura yang terletak paling timur dan memiliki banyak pulau kecil.",
                "jawaban": "Sumenep",
                "clue": [
                    "Terdapat Keraton Sumenep.",
                    "Berbatasan dengan Selat Madura dan Laut Jawa.",
                    "Namanya berasal dari bahasa Sansekerta."
                ]
            },
            {
                "soal": "Kabupaten pesisir utara yang terkenal dengan wisata bahari WBL.",
                "jawaban": "Lamongan",
                "clue": [
                    "Berbatasan dengan Laut Jawa.",
                    "Terletak di barat Kabupaten Gresik.",
                    "Terkenal dengan makanan Nasi Boran."
                ]
            },
            {
                "soal": "Kabupaten di bawah Gunung Wilis yang terkenal sebagai pusat industri rokok dan perkebunan.",
                "jawaban": "Kediri",
                "clue": [
                    "Namanya berasal dari Kerajaan Kuno.",
                    "Memiliki Gunung Klotok.",
                    "Dilewati Sungai Brantas."
                ]
            },
            {
                "soal": "Kota di Jawa Timur bagian barat yang terkenal dengan kerajinan kulit dan Monumen Kresek.",
                "jawaban": "Madiun",
                "clue": [
                    "Dikenal dengan julukan Kota Gadis.",
                    "Berbatasan dengan Ngawi dan Magetan.",
                    "Dilalui jalur utama Jatim-Jateng."
                ]
            },
            {
                "soal": "Kabupaten di Jawa Timur yang terkenal dengan kawasan Semenanjung Blambangan dan Taman Nasional Alas Purwo.",
                "jawaban": "Banyuwangi",
                "clue": [
                    "Dikenal sebagai wilayah paling tua dalam sejarah Blambangan.",
                    "Banyak desa adat masih bertahan di sini.",
                    "Dekat dengan Pantai Plengkung (G-Land)."
                ]
            },
            {
                "soal": "Kabupaten di barat daya Jawa Timur yang terkenal dengan kuliner pecelnya dan wilayah pegunungan Wilis.",
                "jawaban": "Nganjuk",
                "clue": [
                    "Dijuluki Kota Angin.",
                    "Memiliki bendungan besar bernama Gondang.",
                    "Terletak di jalur utama Surabaya-Madiun."
                ]
            },
            {
                "soal": "Kabupaten yang menjadi pusat industri perkapalan dan memiliki pelabuhan internasional di utara Jawa Timur.",
                "jawaban": "Sidoarjo",
                "clue": [
                    "Wilayahnya masuk Gerbangkertosusila.",
                    "Dekat dengan Bandara Juanda.",
                    "Terkenal dengan lumpur Lapindo."
                ]
            },
            {
                "soal": "Kabupaten yang terkenal sebagai pusat seni Reyog dan terletak di selatan Pegunungan Wilis.",
                "jawaban": "Ponorogo",
                "clue": [
                    "Budayanya berpengaruh pada wilayah Mataraman.",
                    "Sering mengadakan Festival Reyog Nasional.",
                    "Berbatasan dengan Jawa Tengah."
                ]
            },
            {
                "soal": "Kota di Jawa Timur yang terkenal sebagai pusat pendidikan militer karena berdirinya Akademi Angkatan Laut.",
                "jawaban": "Surabaya",
                "clue": [
                    "Dekat kawasan Kenjeran.",
                    "Memiliki patung Buddha raksasa Four Faces.",
                    "Dilewati tol ke arah Madura."
                ]
            },
            {
                "soal": "Wilayah pesisir yang terkenal dengan pantai Papuma dan Watu Ulo.",
                "jawaban": "Jember",
                "clue": [
                    "Menghadap Samudra Hindia.",
                    "Terkenal dengan batu karang raksasa.",
                    "Dekat kawasan wisata Tanjung Papuma."
                ]
            },
            {
                "soal": "Kabupaten yang merupakan pintu gerbang jalur selatan Jawa Timur menuju Malang dan Blitar.",
                "jawaban": "Trenggalek",
                "clue": [
                    "Memiliki pantai Prigi yang terkenal.",
                    "Dikelilingi pegunungan kapur.",
                    "Kuliner khasnya adalah alen-alen."
                ]
            },
            {
                "soal": "Kabupaten yang memiliki gunung Butak dan terkenal dengan pegunungan Kawi lainnya.",
                "jawaban": "Malang",
                "clue": [
                    "Dekat dengan Kota Batu.",
                    "Wilayahnya memiliki banyak air terjun.",
                    "Penduduknya banyak bermata pencaharian petani."
                ]
            },
            {
                "soal": "Kabupaten yang dialiri Sungai Solo kecil dan terkenal dengan budaya Samin.",
                "jawaban": "Bojonegoro",
                "clue": [
                    "Terletak di perbatasan Jateng.",
                    "Terkenal sebagai daerah pengeboran minyak tua.",
                    "Memiliki Waduk Pacal."
                ]
            },
            {
                "soal": "Kabupaten di jalur selatan Jatim yang terkenal dengan pusat kuliner pecel pincuk dan hasil pertanian organik.",
                "jawaban": "Blitar",
                "clue": [
                    "Menghadap Samudra Hindia.",
                    "Banyak desa penghasil kopi.",
                    "Dekat dengan Wisata Pantai Tambakrejo."
                ]
            },
            {
                "soal": "Wilayah di ujung barat Madura yang dikenal dengan peternakan sapi dan tradisi karapan sapi.",
                "jawaban": "Bangkalan",
                "clue": [
                    "Dekat Pelabuhan Kamal.",
                    "Memiliki desa-desa dengan kultur Madura kuat.",
                    "Daerahnya datar dan banyak padang rumput."
                ]
            },
            {
                "soal": "Kabupaten di jalur lintas selatan yang terkenal dengan pemandangan perbukitan karst dan pantai Srau.",
                "jawaban": "Pacitan",
                "clue": [
                    "Menghadap langsung Samudra Hindia.",
                    "Banyak ditemukan gua batu kapur.",
                    "Termasuk daerah rawan abrasi."
                ]
            },
            {
                "soal": "Kota di Jawa Timur yang dikenal dengan alun-alun bulatnya dan industri kerajinan tenun.",
                "jawaban": "Kota Kediri",
                "clue": [
                    "Dilintasi Sungai Brantas.",
                    "Memiliki Monumen Simpang Lima Gumul.",
                    "Dekat dengan kawasan wisata Gunung Maskumambang."
                ]
            },
            {
                "soal": "Kabupaten di kawasan tapal kuda yang terkenal dengan kuda Bromo dan pertanian sayur mayurnya.",
                "jawaban": "Pasuruan",
                "clue": [
                    "Berbatasan dengan Malang.",
                    "Dekat jalur utama Surabaya-Banyuwangi.",
                    "Terkenal dengan daerah Nongkojajar."
                ]
            },
            {
                "soal": "Kabupaten yang terkenal dengan Kampung Inggris di Pare dan berada di dataran rendah subur.",
                "jawaban": "Kediri",
                "clue": [
                    "Menjadi pusat pendidikan bahasa.",
                    "Dekat jalur Kediri-Nganjuk.",
                    "Banyak pondok pesantren besar berdiri di sini."
                ]
            }
        ] 
    },
    "4": { # Makanan
        "soal": [
            {
                "soal": "Makanan khas Surabaya berupa soto dengan kuah kuning dan irisan daging ayam serta telur.",
                "jawaban": "Soto Ambengan",
                "clue": ["Berkuah kuning kental.",
                         "Sering disajikan dengan koya.",
                         "Berasal dari Surabaya."
                         ]
            },
            {
                "soal": "Makanan pedas khas Surabaya berisi daging ayam dan kuah merah pekat.",
                "jawaban": "Ayam Penyet",
                "clue": ["Dihidangkan dengan sambal pedas.",
                         "Dagingnya dipenyet agar empuk.",
                         "Populer di Jawa Timur."
                         ]
            },
            {
                "soal": "Nasi khas Surabaya yang berisi daging sapi, sambal petis, dan kuah kental.",
                "jawaban": "Nasi Krawu",
                "clue": ["Berasal dari Gresik.",
                         "Disajikan dengan serundeng.",
                         "Cita rasa gurih dan pedas."
                         ]
            },
            {
                "soal": "Makanan khas Madura berupa sate dengan bumbu kacang kental dan petis.",
                "jawaban": "Sate Madura",
                "clue": ["Tusukan daging ayam atau kambing.",
                         "Bumbu kacang gurih.",
                         "Daerah asalnya pulau Madura."
                         ]
            },
            {
                "soal": "Makanan khas Lamongan berupa kuah kuning dengan daging ayam suwir.",
                "jawaban": "Soto Lamongan",
                "clue": ["Ada koya sebagai pelengkap.",
                         "Kuahnya kekuningan.",
                         "Berasal dari Lamongan."
                         ]
            },
            {
                "soal": "Nasi campur khas Lamongan dengan lauk ayam, empal, dan sambal terasi.",
                "jawaban": "Nasi Boranan",
                "clue": ["Dijual dalam wadah bernama boran.",
                         "Ciri khasnya sambal terasi.",
                         "Asal Lamongan."
                         ]
            },
            {
                "soal": "Makanan khas Probolinggo berupa bakso kuah dengan rasa pedas dan gurih.",
                "jawaban": "Bakso Probolinggo",
                "clue": ["Cita rasa pedas khas.",
                         "Dari Probolinggo.",
                         "Sering disajikan dengan sambal banyak."
                         ]
            },
            {
                "soal": "Makanan khas Surabaya berwarna hitam karena petis dan sering dijual sebagai rujak.",
                "jawaban": "Rujak Cingur",
                "clue": ["Memakai cingur sapi.",
                         "Ada buah dan sayur.",
                         "Warnanya hitam pekat."
                         ]
            },
            {
                "soal": "Kue basah manis khas Jawa Timur berlapis dan warna-warni.",
                "jawaban": "Kue Lapis",
                "clue": ["Berbentuk lapisan.",
                         "Terbuat dari tepung beras.",
                         "Manis dan kenyal."
                         ]
            },
            {
                "soal": "Makanan khas Bojonegoro berupa nasi dengan daun jati dan lauk sederhana.",
                "jawaban": "Sego Buwuhan",
                "clue": ["Dibungkus daun jati.",
                         "Nasi khas acara besar.",
                         "Asal Bojonegoro."
                         ]
            },
            {
                "soal": "Camilan khas Trenggalek yang terbuat dari singkong dan berbentuk pipih panjang.",
                "jawaban": "Kripik Tempe",
                "clue": ["Biasanya renyah.",
                         "Sering jadi oleh-oleh.",
                         "Trenggalek sebagai pusatnya."
                         ]
            },
            {
                "soal": "Makanan khas Madiun berupa soto dengan kuah bening dan daging sapi.",
                "jawaban": "Soto Madiun",
                "clue": ["Berkuah bening.",
                         "Ditambah taoge.",
                         "Asal Madiun."
                         ]
            },
            {
                "soal": "Makanan khas Ponorogo berupa sate dengan bumbu kacang dan lontong.",
                "jawaban": "Sate Ponorogo",
                "clue": ["Tusukan panjang.",
                         "Ada irisan ayam panjang.",
                         "Asalnya dari Ponorogo."
                         ]
            },
            {
                "soal": "Makanan khas Banyuwangi berupa pecel dengan sambal kacang khas.",
                "jawaban": "Pecel Banyuwangi",
                "clue": ["Menggunakan sayur rebus.",
                         "Sambal kacangnya khas.",
                         "Berasal dari Banyuwangi."
                         ]
            },
            {
                "soal": "Makanan khas Kediri berupa tahu goreng yang renyah dan gurih.",
                "jawaban": "Tahu Takwa",
                "clue": ["Kuning warnanya.",
                         "Cirinya padat dan gurih.",
                         "Dari Kediri."
                         ]
            },
            {
                "soal": "Makanan khas Jombang berupa bubur dengan kuah santan manis.",
                "jawaban": "Jenang",
                "clue": ["Manis dan kenyal.",
                         "Biasanya untuk oleh-oleh.",
                         "Berwarna putih kekuningan atau coklat."
                         ]
            },
            {
                "soal": "Makanan khas Sidoarjo berupa olahan bandeng tanpa duri.",
                "jawaban": "Bandeng Presto",
                "clue": ["Dimasak bertekanan tinggi.",
                         "Tulangnya lunak.",
                         "Sidoarjo terkenal dengan ini."
                         ]
            },
            {
                "soal": "Makanan khas Situbondo berupa nasi dengan lauk ikan asin dan sambal.",
                "jawaban": "Nasi Karak",
                "clue": ["Menggunakan nasi kering.",
                         "Sering dipadukan dengan kacang.",
                         "Khas Situbondo."
                         ]
            },
            {
                "soal": "Makanan khas Malang berupa bakso dengan berbagai jenis isian.",
                "jawaban": "Bakso Malang",
                "clue": ["Pangsit adalah pelengkapnya.",
                         "Populer se-Indonesia.",
                         "Berasal dari Malang."
                         ]
            },
            {
                "soal": "Makanan khas Mojokerto berisi kacang hijau yang manis.",
                "jawaban": "Onde-onde",
                "clue": ["Berbahan tepung ketan.",
                         "Wijen yang banyak",
                         "Berbentuk bulat"
                         ]
            },
            {
                "soal": "Makanan khas Sumenep berupa soto dengan kuah santan kuning.",
                "jawaban": "Soto Sumenep",
                "clue": ["Ada aroma rempah kuat.",
                         "Mengandung santan.",
                         "Asal Madura bagian timur."
                         ]
            },
            {
                "soal": "Camilan khas Pacitan berbahan dasar ketela pohon.",
                "jawaban": "Kerupuk Rambak",
                "clue": ["Gurih renyah.",
                         "Warna putih keruh.",
                         "Biasanya dibuat cemilan"
                         ]
            },
            {
                "soal": "Makanan khas Gresik berupa nasi yang disajikan dengan empal, krengsengan, dan sambal.",
                "jawaban": "Nasi Krawu",
                "clue": ["Daun pisang sebagai alas.",
                         "Serundeng menjadi pelengkap.",
                         "Asal Gresik."
                         ]
            },
            {
                "soal": "Makanan khas Tulungagung berupa sate daging dengan bumbu kacang encer.",
                "jawaban": "Sate Tulungagung",
                "clue": ["Daging dipotong kecil.",
                         "Rasanya gurih manis.",
                         "Khas Tulungagung."
                         ]
            },
            {
                "soal": "Kue kering khas Jawa Timur berbahan kacang tanah.",
                "jawaban": "Kue Kacang",
                "clue": ["Rasanya manis gurih.",
                         "Sering ditemui saat lebaran.",
                         "Camilan tradisional."
                         ]
            },
            {
                "soal": "Makanan khas Lamongan berupa nasi dengan lauk iwak peyek.",
                "jawaban": "Nasi Iwak Peyek",
                "clue": ["Disajikan dengan sambal.",
                         "Peyek ikan sebagai ciri khas.",
                         "Khas Lamongan."
                         ]
            },
            {
                "soal": "Bakwan khas Malang dengan kuah gurih dan tambahan bakwan serta tahu.",
                "jawaban": "Bakwan Malang",
                "clue": ["Nama lain dari Bakso Malang.",
                         "Ada bakwan kering.",
                         "Dari Malang."
                         ]
            },
            {
                "soal": "Makanan khas Jember berupa tape singkong yang manis.",
                "jawaban": "Tape Jember",
                "clue": ["Warnanya putih kekuningan.",
                         "Manis asam.",
                         "Oleh-oleh khas Jember."
                         ]
            },
            {
                "soal": "Makanan khas Kediri berupa nasi dengan kulupan sayur dan tempe.",
                "jawaban": "Sego Tumpang",
                "clue": ["Menggunakan bumbu sambal tumpang.",
                         "Bahan utama tempe bosok.",
                         "Dari Kediri."
                         ]
            },
            {
                "soal": "Makanan terbuat dari ketan berisi remahan daging ayam",
                "jawaban": "Lemper",
                "clue": ["Terbuat dari ketan",
                         "Dibungkus daun pisang",
                         "Biasanya ada di setiap acara hajatan"
                         ]
            }
        ] 
    }
}

list_guardian = {
    "Batu": {
        "Pembukaan": "Mbah Wastu : Selamat datang di Kota Wisata dingin kami. Aku adalah jiwa dari keindahan alam dan hasil bumi apel yang subur di Kota Batu. Apa yang mendorongmu untuk mencari tahu tentang destinasi wisata unggulan dan ikon buah dari wilayah pegunungan ini?",
        "Jawaban": "Apel",
        "Pertanyaan": "Buah khas apakah yang menjadi ikon agrowisata dari Kota Batu, yang memiliki rasa manis-asam dan banyak diolah menjadi keripik atau sari buah?",
        "Penutupan": "Mbah Wastu : Tepat sekali! Apel adalah kebanggaan petani kami. Masuklah, nikmati sejuknya udara dan jelajahi berbagai wahana wisata modern di Kota Batu."
    },
    "Bangkalan": {
        "Pembukaan": "Ratu Sekar Kedaton : Salam dari ujung barat Madura, tempat di mana angin membawa aroma garam dan semangat adu cepat yang membara. Aku, Ratu Sekar Kedaton, adalah roh penguasa dari tanah Arosbaya. Sebelum melangkah lebih jauh, apa maksud kedatanganmu ke gerbang Madura ini?",
        "Jawaban": "Karapan Sapi",
        "Pertanyaan": "Ada festival balapan hewan yang sangat terkenal di Madura, di mana sepasang sapi berlari kencang. Apa nama festival balapan sapi ini?",
        "Penutupan": "Ratu Sekar Kedaton : Jawabanmu benar! Karapan Sapi memang kebanggaan Madura. Silakan, nak, pelajari lebih dalam semangat balap dan budaya di Bangkalan!"
    },
    "Banyuwangi": {
        "Pembukaan": "Naga Kemiren : Aku bangkit dari perbatasan timur. Namaku Naga Kemiren, perwakilan Bumi Blambangan yang penuh tarian mistis. Aku merasakan getaran asing; sampaikan tujuanmu menginjakkan kaki di tanah para penari leluhur ini.",
        "Jawaban": "Tari Gandrung",
        "Pertanyaan": "Tarian khas Banyuwangi yang selalu dipertunjukkan oleh gadis-gadis untuk menyambut tamu, bahkan menjadi simbol daerah. Apa nama tarian ini?",
        "Penutupan": "Naga Kemiren : Tepat sekali, Tari Gandrung! Engkau telah melunasi rasa ingin tahuku. Kami persilakan kamu mengulik tradisi dan seluruh cerita di Bumi Blambangan."
    },
    "Blitar": {
        "Pembukaan": "Bhre Wengker : Aku berdiri tegak di atas makam pahlawan, nafas dari raja-raja. Aku adalah Bhre Wengker, yang menjamin kejayaan seni rakyat. Katakan padaku, apa yang kau cari di kota yang diselimuti kisah heroik dan kesenian tari topeng ini?",
        "Jawaban": "Tari Topeng Barong",
        "Pertanyaan": "Ada tarian khas Blitar yang menggunakan topeng dan menceritakan kisah dari epos Ramayana, yang sering ditampilkan dekat Candi Penataran. Apa nama tarian topeng ini?",
        "Penutupan": "Bhre Wengker : Hebat! Tari Topeng Barong memang kunci pentingnya. Masuklah, dan telusuri kisah kejayaan Wengker serta warisan seni topeng di kota ini."
    },
    "Bojonegoro": {
        "Pembukaan": "Danyang Bengawan : Dengarkan gemericik alat musik bambu di sepanjang Bengawan Solo. Aku, Danyang Bengawan, adalah semangat dari seni pertunjukan rakyat. Aku ingin tahu, apa alasanmu mendatangi kota yang hidup berdampingan dengan sungai purba dan kesenian Thengul ini?",
        "Jawaban": "Thengul",
        "Pertanyaan": "Apa nama kesenian pertunjukan khas Bojonegoro yang menggunakan alat musik perkusi dari bambu, sering ditampilkan saat musim panen?",
        "Penutupan": "Danyang Bengawan : Kamu benar! Thengul adalah kesenian kami. Sekarang, kamu boleh menelusuri aliran Bengawan Solo dan kekayaan budaya Bojonegoro."
    },
    "Bondowoso": {
        "Pembukaan": "Kyai Singo Ulung : Raungan Singo Ulung adalah panggilan! Namaku Kyai Singo Ulung, roh dari tradisi topeng singa yang agung. Jelaskan padaku, mengapa kau tertarik pada rahasia yang tersembunyi di balik tarian Bondowoso?",
        "Jawaban": "Singo Ulung",
        "Pertanyaan": "Apa nama kesenian ikonik Bondowoso yang memiliki topeng menyerupai kepala singa berbulu putih?",
        "Penutupan": "Kyai Singo Ulung : Raungan gembira! Jawabanmu tentang Singo Ulung benar. Kunci menuju situs dan keindahan budaya Bondowoso kini ada di tanganmu."
    },
    "Gresik": {
        "Pembukaan": "Panji Jayengrana : Lihatlah menara dan kubah masjid yang menjulang! Aku, Panji Jayengrana, adalah simbol dari perdagangan dan dakwah para Wali. Sebutkan tujuanmu mengunjungi kota yang menjadi pintu gerbang Islam di Jawa ini.",
        "Jawaban": "Sunan Giri",
        "Pertanyaan": "Siapakah salah satu Wali Songo yang makamnya menjadi pusat ziarah di Gresik dan dikenal dengan julukan Sunan Giri?",
        "Penutupan": "Panji Jayengrana : Tepat sekali, Sunan Giri! Kota wali ini terbuka untukmu. Silakan selami semangat dakwah dan jejak perdagangan kuno di Gresik."
    },
    "Jember": {
        "Pembukaan": "Gandrung Sewu : Sambut aku dengan irama yang meriah, dari ladang-ladang kebun hingga tarian anggun. Aku adalah Gandrung Sewu, personifikasi budaya yang dinamis. Ceritakan padaku, mengapa kau mencari tahu tentang kota yang dikelilingi kebun tembakau dan tarian Lahbako?",
        "Jawaban": "Tari Lahbako",
        "Pertanyaan": "Ada tarian yang menggambarkan kegiatan petani saat memanen dan mengolah tembakau, yang menjadi hasil bumi andalan Jember. Apa nama tarian ini?",
        "Penutupan": "Gandrung Sewu : Indah! Tari Lahbako adalah budaya kami. Masuk dan nikmati ritme budaya Jember, dari tembakau hingga tarian anggun kami."
    },
    "Jombang": {
        "Pembukaan": "Pangeran Sudirman : Aku, Pangeran Sudirman, mewakili semangat ilmu dan kearifan di Kota Santri. Sebelum kuberi kunci sejarah, jelaskan niatmu datang ke persimpangan spiritual Jawa ini.",
        "Jawaban": "Tebuireng",
        "Pertanyaan": "Jombang dikenal sebagai Kota Santri. Sebutkan nama salah satu pesantren tua dan besar yang ada di Jombang?",
        "Penutupan": "Pangeran Sudirman : Jawaban yang cerdas. Tebuireng adalah pusat kearifan kami. Aku persilakan kamu menelusuri lebih jauh persimpangan spiritual Jombang."
    },
    "Kediri": {
        "Pembukaan": "Lembu Suro : Deburan kawah Kelud adalah sumpahku, aku adalah Lembu Suro, yang menyaksikan lahirnya karya-karya sastra dan tarian Jaranan. Katakan, apa yang kau harapkan dari kota Panjalu, tempat lahirnya seni tari yang termasyhur?",
        "Jawaban": "Jaranan",
        "Pertanyaan": "Kesenian tari khas Kediri yang dimainkan oleh penari yang menunggangi kuda tiruan dari anyaman bambu adalah...?",
        "Penutupan": "Lembu Suro : Kamu berhasil! Jaranan adalah seni tarian kami. Kediri dan pertunjukan rakyatnya terbuka untuk kamu pelajari."
    },
    "Lamongan": {
        "Pembukaan": "Joko Tingkir : Aku adalah pelindung makam wali dan nelayan. Joko Tingkir adalah namaku. Apa yang membuatmu tertarik dengan Lamongan, daerah yang kaya akan kuliner dan nilai-nilai kesenian Boran?",
        "Jawaban": "Tari Boran",
        "Pertanyaan": "Tarian apa yang menceritakan kisah seorang putri dan raja, di mana penarinya membawa wadah tempat nasi (bakul)?",
        "Penutupan": "Joko Tingkir : Benar, Tari Boran! Kini, pintu menuju kisah tarian dan kekayaan kuliner Lamongan telah terbuka untukmu."
    },
    "Lumajang": {
        "Pembukaan": "Dewa Semeru : Aku mengawasi puncak tertinggi Jawa, Semeru. Aku, Dewa Semeru, adalah roh dari tanah yang kaya seni tari topeng. Ungkapkan padaku, mengapa kau ingin mengungkap kisah dari reruntuhan kerajaan kuno dan tarian kami?",
        "Jawaban": "Tari Topeng Kaliwungu",
        "Pertanyaan": "Kesenian tari apa yang menjadi ciri khas Lumajang, di mana penarinya mengenakan topeng dan menggambarkan tokoh-tokoh dari cerita Panji?",
        "Penutupan": "Dewa Semeru : Luar biasa! Tari Topeng Kaliwungu adalah keindahan kami. Aku izinkan kamu menjejakkan kaki di lereng Semeru dan mengungkap warisan Lumajang."
    },
    "Madiun": {
        "Pembukaan": "Pendekar Silat : Salam persaudaraan! Aku adalah Pendekar Silat, simbol kekuatan fisik dan batin Kota Gadis. Sebelum kita bertukar cerita, apa yang memandumu datang ke Madiun, jantungnya budaya Pencak Silat?",
        "Jawaban": "Pencak Silat",
        "Pertanyaan": "Madiun dikenal sebagai pusatnya bela diri. Apa nama seni bela diri tradisional Indonesia yang sangat terkenal di Madiun?",
        "Penutupan": "Pendekar Silat : Salam hormat! Pencak Silat memang identitas Madiun. Silakan selami semangat persaudaraan dan kekayaan bela diri di Kota Gadis."
    },
    "Magetan": {
        "Pembukaan": "Naga Lawu : Aku bersemayam di lereng Lawu. Aku adalah Naga Lawu, penjaga kesenian Tiban yang unik. Aku menanti jawabanmu: Apa motifmu mengunjungi danau yang diselimuti kisah mitologis dan cambuk sakti ini?",
        "Jawaban": "Kesenian Tiban",
        "Pertanyaan": "Kesenian rakyat apa dari Magetan yang melibatkan dua orang saling mencambuk untuk meminta turunnya hujan?",
        "Penutupan": "Naga Lawu : Tepat, Kesenian Tiban! Kamu boleh masuk dan menikmati keindahan telaga sambil memahami budaya minta hujan Magetan."
    },
    "Malang": {
        "Pembukaan": "Singasari Kencana : Aku adalah Singasari Kencana, pewaris dan penjaga kejayaan teater topeng. Sebutkan alasanmu menelusuri kisah di balik kerajaan besar dan kesenian topeng Malangan ini.",
        "Jawaban": "Wayang Topeng Malangan",
        "Pertanyaan": "Kesenian teater tradisional Malang yang terkenal, di mana para pemainnya mengenakan topeng kayu saat berdialog, adalah...?",
        "Penutupan": "Singasari Kencana : Aku akui jawabanmu! Wayang Topeng Malangan adalah kuncinya. Jelajahi sejarah Tumapel dan agungnya warisan seni Malang."
    },
    "Mojokerto": {
        "Pembukaan": "Gajah Mada : Aku bersuara dari Trowulan. Aku, Gajah Mada, menguji setiap jiwa yang berani mendekati pusat peradaban Nusantara. Apa yang kau cari di ibukota Majapahit, di mana ada ritual Manten Kucing?",
        "Jawaban": "Manten Kucing",
        "Pertanyaan": "Apa nama kesenian khas Trowulan yang berupa boneka dari jerami dan dipakai untuk menari saat musim kemarau agar turun hujan?",
        "Penutupan": "Gajah Mada : Sempurna! Manten Kucing adalah ritual unik kami. Engkau layak mengulik lebih dalam tentang tradisi Trowulan."
    },
    "Nganjuk": {
        "Pembukaan": "Anjuk Ladang : Aku adalah Anjuk Ladang, roh dari tanah kemenangan. Angin adalah nafasku, dan tarian anggun adalah budayaku. Katakan, apa yang ingin kau ketahui dari 'Kota Angin' yang memiliki sejarah panjang dan Tari Tayub ini?",
        "Jawaban": "Tari Tayub",
        "Pertanyaan": "Apa nama tarian khas Nganjuk yang dibawakan oleh banyak penari dengan gerakan yang anggun dan menggunakan selendang?",
        "Penutupan": "Anjuk Ladang : Benar! Tari Tayub adalah ikon kami. Silakan selami kisah kemenangan dan keindahan tarian anggun 'Kota Angin' ini."
    },
    "Ngawi": {
        "Pembukaan": "Untung Suropati : Aku mewakili perlawanan dan keberanian. Untung Suropati adalah namaku, yang berdiri teguh di antara benteng kuno. Aku ingin mendengar tujuanmu datang ke Ngawi, tempat lahirnya seni panggung Ludruk?",
        "Jawaban": "Kesenian Ludruk",
        "Pertanyaan": "Kesenian pertunjukan rakyat yang populer di Ngawi dan sering menceritakan kisah-kisah lucu dan kehidupan sehari-hari adalah...?",
        "Penutupan": "Untung Suropati : Tepat! Kesenian Ludruk adalah hiburan rakyat kami. Ngawi terbuka, telusuri sejarah dan seni pertunjukan kami."
    },
    "Pacitan": {
        "Pembukaan": "Samudro Emas : Aku adalah Samudro Emas, penjaga keindahan laut dan keajaiban wayang kulit. Sebelum kau masuk ke dalam goa, jelaskan mengapa kau datang ke tanah yang kaya akan budaya Jawa ini.",
        "Jawaban": "Wayang Kulit",
        "Pertanyaan": "Apa nama pertunjukan wayang yang dimainkan oleh dalang dengan menggunakan boneka dari kulit kerbau?",
        "Penutupan": "Samudro Emas : Menakjubkan! Wayang Kulit adalah budaya kami. Engkau dipersilakan menguak keajaiban seni dan alam di Pacitan."
    },
    "Pamekasan": {
        "Pembukaan": "Api Abadi Wiroguno : Api abadi di Larangan Tokol adalah semangatku. Aku adalah Api Abadi Wiroguno, roh dari kota yang menghargai seni Sandur. Apa yang membuatmu ingin mengungkap kisah dari Madura bagian tengah ini?",
        "Jawaban": "Ludruk Sandur",
        "Pertanyaan": "Kesenian drama tradisional khas Madura yang populer di Pamekasan dan melibatkan musik gamelan adalah...?",
        "Penutupan": "Api Abadi Wiroguno : Jawabanmu benar, Ludruk Sandur! Api kebudayaan di Pamekasan kini menyala untukmu. Silakan pelajari lebih lanjut."
    },
    "Pasuruan": {
        "Pembukaan": "Sayid Arif : Aku menyaksikan sejarah bupati dan tarian Kuda Lumping. Aku, Sayid Arif, adalah saksi bisu transisi kekuasaan dan tradisi. Aku menanti, apa yang membawamu ke kota dengan peninggalan VOC dan kesenian rakyat ini?",
        "Jawaban": "Kuda Lumping",
        "Pertanyaan": "Apa nama kesenian rakyat yang sering ditampilkan di Pasuruan, di mana penari menirukan gerakan kuda tiruan?",
        "Penutupan": "Sayid Arif : Tepat, Kuda Lumping! Aku persilakan kamu menelusuri keindahan alam dan seni rakyat di Pasuruan."
    },
    "Ponorogo": {
        "Pembukaan": "Singo Barong : Raunganku memanggil! Aku adalah Singo Barong, ruh dari kesenian Reyog yang mendunia. Ceritakan padaku, mengapa kau mencari tahu tentang Ponorogo, kota yang melahirkan pendekar dan raja singa?",
        "Jawaban": "Reog Ponorogo",
        "Pertanyaan": "Kesenian apa yang menjadi ikon Ponorogo, di mana topeng utamanya adalah kepala singa yang dihiasi bulu merak?",
        "Penutupan": "Singo Barong : Raungan bangga! Reog Ponorogo adalah kebanggaan kami. Selami semangat seni dan Pesantren modern di Ponorogo."
    },
    "Probolinggo": {
        "Pembukaan": "Kyai Bromo : Aku adalah Kyai Bromo, roh yang bersemayam di lautan pasir, dihormati oleh Suku Tengger. Sampaikan tujuanmu; hanya yang menghormati tradisi yang boleh bertanya tentang upacara suci kami.",
        "Jawaban": "Upacara Yadnya Kasada",
        "Pertanyaan": "Apa nama upacara adat Suku Tengger yang diadakan setiap tahun di Gunung Bromo untuk memberikan persembahan hasil bumi kepada dewa?",
        "Penutupan": "Kyai Bromo : Luar biasa! Upacara Yadnya Kasada adalah kuncinya. Kamu boleh mendekati Bromo dan memahami kearifan Suku Tengger."
    },
    "Sampang": {
        "Pembukaan": "Trunojoyo : Aku adalah darah Madura yang berani. Trunojoyo adalah jiwaku, simbol perlawanan dan seni Topeng. Mengapa kau datang ke Sampang, kota yang penuh dengan kisah heroik dan tarian tradisional?",
        "Jawaban": "Topeng Dalang",
        "Pertanyaan": "Kesenian apa yang menjadi simbol kegembiraan rakyat Madura, di mana tokoh utamanya menari dengan wajah yang lucu dan diiringi musik gamelan?",
        "Penutupan": "Trunojoyo : Semangat perjuanganmu terbukti. Topeng Dalang adalah budaya kami. Sampang terbuka untukmu, pelajari kisah heroiknya."
    },
    "Sidoarjo": {
        "Pembukaan": "Joko Tarub : Aku bangkit dari delta. Aku adalah Joko Tarub, penjaga warisan Kerajaan Janggala dan Tari Remo. Aku ingin tahu, apa alasanmu mengunjungi kota yang menjadi pusat industri dan seni tari lincah ini?",
        "Jawaban": "Tari Remo",
        "Pertanyaan": "Apa nama tarian khas Sidoarjo yang menggambarkan kepahlawanan dengan gerakan kaki yang lincah dan sering ditarikan oleh laki-laki?",
        "Penutupan": "Joko Tarub : Tepat sekali! Tari Remo adalah seni kami. Engkau dipersilakan menguak sejarah dan tarian Sidoarjo."
    },
    "Situbondo": {
        "Pembukaan": "Pangeran Sokaraja : Aku menjaga Taman Nasional Baluran dan tarian nelayan. Aku adalah Pangeran Sokaraja. Jelaskan, mengapa kau menjelajah ke Situbondo, tanah di mana keindahan alam bertemu tarian Petik Laut?",
        "Jawaban": "Tari Petik Laut",
        "Pertanyaan": "Ada tarian khas Situbondo yang terinspirasi dari gerakan nelayan saat menangkap ikan di laut. Apa nama tarian ini?",
        "Penutupan": "Pangeran Sokaraja : Benar! Tari Petik Laut adalah tarian unik kami. Situbondo menyambutmu. Jelajahi keindahan Baluran dan pesisir kami."
    },
    "Sumenep": {
        "Pembukaan": "Arya Wiraraja : Aku adalah arsitek dari keraton. Aku, Arya Wiraraja, mengawasi kejayaan Adipati terakhir dan alat musik Sape'. Apa yang mendorongmu untuk mengungkap garis keturunan para penguasa dan musik tradisional Sumenep ini?",
        "Jawaban": "Sape' (Sapek)",
        "Pertanyaan": "Apa nama alat musik khas Madura, mirip dengan gitar, yang terbuat dari kayu dan menghasilkan bunyi yang merdu?",
        "Penutupan": "Arya Wiraraja : Hebat! Sape' adalah alat musik kami. Masuklah, pelajari sejarah Keraton dan budaya musik tradisional Madura."
    },
    "Surabaya": {
        "Pembukaan": "Suro : Aku adalah spirit perjuangan arek Suroboyo. Aku, bersama Bung Tomo, menyaksikan heroiknya pertempuran 10 November dan gagahnya Tugu Pahlawan. Apa yang membuatmu penasaran dengan sejarah kepahlawanan dan ciri khas kota kami, Kota Pahlawan?",
        "Jawaban": "Tugu Pahlawan",
        "Pertanyaan": "Monumen peringatan apakah yang menjadi ikon Kota Surabaya dan didirikan untuk memperingati peristiwa Pertempuran 10 November 1945?",
        "Penutupan": "Suro : Betul sekali! Tugu Pahlawan adalah simbol keberanian kami. Mari, telusuri lebih dalam kisah perjuangan dan semangat pantang menyerah dari Kota Surabaya."
    },
    "Trenggalek": {
        "Pembukaan": "Dewi Amis : Aku terlahir dari legenda air dan goa. Aku, Dewi Amis, melindungi keajaiban geologis dan alat musik khas. Aku penasaran, apa yang kau cari di Trenggalek, yang menyimpan goa terpanjang dan bunyi Gumbeng?",
        "Jawaban": "Gong Gumbeng",
        "Pertanyaan": "Apa nama alat musik perkusi khas dari Trenggalek yang dimainkan dengan cara dipukul, biasanya untuk mengiringi tarian atau upacara adat?",
        "Penutupan": "Dewi Amis : Jawaban yang luar biasa, Gong Gumbeng! Kesenian Trenggalek terbuka. Silakan telusuri goa terpanjang kami."
    },
    "Tuban": {
        "Pembukaan": "Ronggolawe : Aku adalah Ronggolawe, penentang Raden Wijaya. Tuban, Kota Seribu Goa dan makam Wali. Mengapa kau memilih kota di jalur perdagangan kuno dan tarian Batik yang anggun ini?",
        "Jawaban": "Tari Batik",
        "Pertanyaan": "Apa nama tarian khas Tuban yang menggambarkan kegembiraan para gadis saat membatik kain tenun tradisional Tuban?",
        "Penutupan": "Ronggolawe : Tepat sekali, Tari Batik! Kota Seribu Goa dan tarian anggun menyambutmu. Silakan pelajari sejarah pesisir Tuban."
    },
    "Tulungagung": {
        "Pembukaan": "Lembu Peteng : Aku berdiri di atas bumi marmer, saksi peninggalan Wayang Kulit. Aku adalah Lembu Peteng. Sampaikan niatmu, apa yang kau harapkan dari kota yang kaya akan seni Wayang ini?",
        "Jawaban": "Wayang Kulit",
        "Pertanyaan": "Kesenian tradisional di Tulungagung yang berupa boneka kulit yang dimainkan oleh dalang dengan iringan gamelan adalah...?",
        "Penutupan": "Lembu Peteng : Kamu berhasil. Wayang Kulit adalah warisan budaya kami. Silakan pelajari seni dalang dan kekayaan alam di atas bumi ini."
    }
}

penjabaran_wilayah = {
    "Nganjuk": {
        "sejarah": "Hari jadi Nganjuk ditetapkan pada 10 April 937 M, didasarkan pada penemuan Prasasti Anjuk Ladang (kini Candi Lor). Prasasti ini menceritakan penetapan wilayah Anjuk Ladang (Nganjuk) sebagai tanah perdikan oleh Raja Mpu Sendok dari Kerajaan Medang (Mataram Kuno) sebagai penghargaan atas jasa rakyat dalam menumpas musuh. Nama 'Anjuk Ladang' berarti 'Tanah Kemenangan', menjadikannya salah satu kabupaten tertua di Jawa Timur.",
        "budaya": "Budaya Nganjuk kental dengan Mataraman dan dikenal dengan kesenian tradisional seperti **Tari Remo Jombangan** dan **Jaranan Pegon**. Wilayah ini juga dikenal sebagai 'Kota Angin' karena topografinya.",
        "Makanan": "Makanan khasnya adalah **Nasi Becek** (mirip gulai pedas berisikan daging, jeroan, dan tauge), **Dumbeg Nganjuk** (jajanan dari tepung beras dan gula merah, dibungkus daun lontar berbentuk kerucut), dan **Onde-onde Ketawa**.",
        "Adat": "Tradisi yang menonjol adalah **Kirab Pusaka dan Tumpeng Sembilan**, yang diadakan saat Hari Jadi Kabupaten, melambangkan sembilan pintu air bendungan yang menjadi simbol kemakmuran Nganjuk.",
        "Tokoh_terkenal": "Tokoh bersejarah: **Mpu Sendok** (Raja yang menetapkan Prasasti Anjuk Ladang) dan sejumlah tokoh ulama dari masa awal penyebaran Islam.",
        "bentang_alam": "Topografi Nganjuk adalah dataran rendah yang diapit oleh Gunung Wilis di sebelah selatan dan Pegunungan Kendeng di utara, menjadikannya daerah irigasi yang subur."
    },
    "Kediri": {
        "sejarah": "Kabupaten Kediri merupakan pusat dari **Kerajaan Kediri** (abad ke-11 hingga ke-13 M) yang mencapai puncak kejayaan di masa Raja Jayabaya, yang ramalannya masih dipercaya hingga kini. Hari jadi ditetapkan pada 25 Maret 804 M, merujuk pada Prasasti Harinjing. Setelah keruntuhan Kediri, wilayah ini menjadi penting di masa Majapahit dan Mataram. Pada masa kolonial, Kediri menjadi Karesidenan penting.",
        "budaya": "Budaya Kediri sangat kental dengan tradisi Mataraman. Kesenian yang menonjol adalah **Jaranan Dor** (mirip kuda lumping) dan berbagai ritual yang berkaitan dengan peninggalan purbakala, seperti Candi Penataran.",
        "Makanan": "**Tahu Takwa** dan **Getuk Pisang** (makanan khas kota, namun diproduksi dan dikenal luas hingga kabupaten), **Nasi Goreng Arang**, dan **Gudeg Blitar** (mirip gudeg Yogya tapi lebih pedas).",
        "Adat": "Tradisi keagamaan dan budaya Jawa seperti **Nyadran** (pembersihan makam leluhur) dan ritual di Goa Selomangleng (dikenal sebagai tempat bertapa Putri Dewi Kilisuci).",
        "Tokoh_terkenal": "**Raja Jayabaya** (Kerajaan Kediri), **Kyai Mojo** (pemimpin Perang Jawa), dan berbagai tokoh ulama terkemuka.",
        "bentang_alam": "Terletak di lembah Sungai Brantas, dengan Gunung Kelud di timur (sumber tanah subur) dan Gunung Wilis di barat. Topografinya subur dan cocok untuk pertanian."
    },
    "Blitar": {
        "sejarah": "Hari jadi Kabupaten Blitar ditetapkan pada 5 Agustus 1333 M, dikaitkan dengan penugasan Arya Blitar oleh Gajah Mada (Majapahit) untuk menaklukkan Bali. Blitar dikenal sebagai 'Bumi Proklamator' karena merupakan tempat kelahiran dan peristirahatan terakhir Presiden Pertama RI, Soekarno. Secara historis, Blitar juga merupakan lokasi perlawanan terhadap Jepang yang dipimpin oleh Supriyadi.",
        "budaya": "Budaya Blitar adalah perpaduan Jawa Mataraman. Kesenian utama adalah **Jaranan Senterewe** dan **Tayuban**. Blitar juga merupakan lokasi dari **Candi Penataran**, kompleks candi terluas di Jawa Timur.",
        "Makanan": "**Pecel Blitar** (mirip pecel Madiun namun dengan bumbu yang lebih manis), **Nasi Ampok** (nasi jagung), dan **Wajik Kletik** (wajik dari beras ketan dengan tekstur renyah).",
        "Adat": "Tradisi yang paling terkenal adalah **Upacara Adat di Candi Penataran** dan ritual di sekitar makam Bung Karno, yang sering dikunjungi peziarah dari seluruh Indonesia.",
        "Tokoh_terkenal": "**Ir. Soekarno** (Presiden RI pertama) dan **Supriyadi** (pemimpin PETA).",
        "bentang_alam": "Terletak di kaki Gunung Kelud, wilayah utara bergunung-gunung dan subur, sedangkan wilayah selatan (Pesisir Selatan) memiliki potensi pariwisata bahari yang besar."
    },
    "Tulungagung": {
        "sejarah": "Hari jadi Tulungagung ditetapkan pada 18 November 1205 M, merujuk pada penetapan status daerah di masa Kerajaan Singasari. Tulungagung dikenal sebagai pusat peradaban dan perdagangan maritim di pesisir selatan sejak era Majapahit, dan kemudian menjadi wilayah penting di Karesidenan Kediri di masa kolonial.",
        "budaya": "Tulungagung kaya akan kerajinan marmer, menjadikannya 'Kota Marmer'. Keseniannya mencakup **Reog Kendang** (tarian dengan properti kendang/gendang) dan tradisi **Manten Kucing** (ritual meminta hujan).",
        "Makanan": "**Soto Ayam Lodho** (ayam utuh dimasak dengan kuah santan kental yang dimakan dengan nasi), **Kopi Ijo** (kopi khas yang diolah dengan biji hijau), dan **Gethuk Lindri**.",
        "Adat": "Adat yang unik adalah **Upacara Adat Ulur-Ulur** di Telaga Buret (ritual tolak bala dan meminta berkah air) serta **Manten Kucing** di beberapa desa saat kemarau panjang.",
        "Tokoh_terkenal": "**Pangeran Antasena** (tokoh pewayangan yang dikaitkan dengan wilayah ini) dan sejumlah tokoh ulama besar.",
        "bentang_alam": "Terdiri dari dataran rendah subur yang dialiri Sungai Brantas dan wilayah Pegunungan Kendeng serta Pesisir Selatan yang dikenal sebagai penghasil marmer."
    },
    "Trenggalek": {
        "sejarah": "Hari jadi Trenggalek ditetapkan pada 31 Agustus 1194 M, merujuk pada masa Kerajaan Kediri. Nama Trenggalek diduga berasal dari kata *Terang Golek* (Terang Mencari), dikaitkan dengan peristiwa penangkapan perampok oleh tentara Kerajaan Kediri. Wilayah ini dikenal sebagai daerah pegunungan yang sulit ditembus di masa Mataram dan Belanda.",
        "budaya": "Budaya Trenggalek sangat dipengaruhi oleh lingkungan pegunungan. Kesenian khasnya adalah **Jaranan Turonggo Yakso** (tarian kuda lumping yang menggunakan topeng raksasa menyerupai buto/raksasa) dan **Longan** (musik gamelan khas).",
        "Makanan": "**Nasi Gegok** (nasi yang dikukus dengan lauk pedas, dibungkus daun pisang), **Ayam Lodho** (sama seperti Tulungagung), dan **Tempe Keripik Domas** (keripik tempe tipis).",
        "Adat": "Tradisi **Upacara Longan** (upacara adat tahunan) dan ritual di sekitar **Goa Lowo** (Goa Kelelawar), yang merupakan salah satu goa terbesar di Asia Tenggara.",
        "Tokoh_terkenal": "**Menak Sopal** (tokoh legenda yang diyakini sebagai penemu mata air di Trenggalek).",
        "bentang_alam": "Hampir seluruh wilayah Trenggalek adalah pegunungan dan perbukitan (Pegunungan Kendeng Selatan), menjadikannya daerah yang kaya akan goa dan memiliki garis pantai selatan yang ekstrem."
    },
    "Mojokerto": {
        "sejarah": "Mojokerto merupakan pusat dari **Kerajaan Majapahit** (berdiri 1293 M), salah satu kerajaan maritim terbesar di Nusantara. Hari jadi Kabupaten Mojokerto ditetapkan pada 9 Mei 1293 M, tanggal penobatan Raden Wijaya sebagai Raja Majapahit. Peninggalan utama adalah Trowulan, yang diyakini sebagai ibu kota Majapahit.",
        "budaya": "Budaya Majapahitan sangat kental, tercermin dalam seni ukir dan arsitektur peninggalan. Kesenian yang populer adalah **Wayang Kulit Mojokertoan** dan berbagai pertunjukan yang mengangkat kisah-kisah Majapahit.",
        "Makanan": "**Sate Keong** (sate dari siput sawah), **Sambal Wader** (ikan wader kecil digoreng garing dan disajikan dengan sambal), dan **Onde-onde Mojokerto**.",
        "Adat": "Tradisi **Kirab Pusaka** pada Hari Jadi Kabupaten, serta ritual di situs-situs purbakala Trowulan yang menjadi tempat ziarah dan penelitian.",
        "Tokoh_terkenal": "**Raden Wijaya** (pendiri Majapahit), **Gajah Mada** (Patih Amangkubhumi Majapahit), dan **Hayam Wuruk** (Raja terbesar Majapahit).",
        "bentang_alam": "Terletak di lembah Sungai Brantas dengan Gunung Penanggungan di bagian tenggara, menjadikannya wilayah pertanian yang subur dan kaya situs arkeologi."
    },
    "Jombang": {
        "sejarah": "Jombang awalnya merupakan bagian dari Kabupaten Mojokerto, namun ditingkatkan statusnya menjadi kabupaten sendiri pada 21 Oktober 1910 M oleh Pemerintah Kolonial Belanda. Jombang mendapat julukan 'Kota Santri' karena memiliki banyak pondok pesantren besar dan bersejarah, yang menjadi pusat pendidikan dan pergerakan nasional.",
        "budaya": "Budaya Jombang kental dengan perpaduan nilai Islam (Pesantren) dan Jawa. Kesenian khasnya adalah **Wayang Topeng Jombang** dan **Ludruk**. Jombang juga dikenal sebagai tempat berdirinya organisasi Islam terbesar di Indonesia, Nahdlatul Ulama (NU).",
        "Makanan": "**Pecel Semanggi** (sayur semanggi dengan bumbu pecel encer yang khas), **Sate Galunggung** (sate daging yang dimasak dengan bumbu khusus), dan **Es Legen**.",
        "Adat": "Tradisi **Haul Massal** para pendiri pesantren (terutama Tebuireng) yang menjadi acara keagamaan besar, serta berbagai acara tradisi Pesantren.",
        "Tokoh_terkenal": "**KH. Hasyim Asy'ari** (pendiri NU), **KH. Abdurrahman Wahid (Gus Dur)** (Presiden RI ke-4), dan **KH. Wahid Hasyim** (Pahlawan Nasional).",
        "bentang_alam": "Berada di antara dua sungai besar, Sungai Brantas dan Sungai Bengawan Solo, yang menjadikannya dataran rendah yang sangat subur, cocok untuk pertanian tebu dan padi."
    },
    "Gresik": {
        "sejarah": "Gresik adalah kota pelabuhan kuno yang sangat penting sejak era Majapahit dan menjadi pintu gerbang masuknya Islam di Jawa. Hari jadi Gresik ditetapkan pada 9 Maret 1341 M. Julukannya adalah 'Kota Wali' karena merupakan lokasi makam Syekh Maulana Malik Ibrahim (Sunan Gresik), salah satu Walisongo yang paling awal. Di masa kolonial, Gresik berkembang menjadi pusat industri dan perdagangan penting.",
        "budaya": "Budaya pesisir yang kental dengan nilai-nilai Islam. Kesenian khasnya adalah **Pudak Kopyor** (tarian rakyat yang menirukan pembuatan kue pudak), dan tradisi **Makam Panjang** (haul atau ziarah ke makam leluhur).",
        "Makanan": "Makanan khas Gresik yang paling terkenal adalah **Nasi Krawu** (nasi pulen dengan serundeng tiga warna dan daging suwir), **Bebek Goreng Harissa**, dan kue tradisional **Pudak** (terbuat dari tepung beras, gula, dan santan, dibungkus pelepah pinang).",
        "Adat": "Tradisi keagamaan seperti **Ziarah ke Makam Walisongo** dan acara **Makam Panjang** (ritual tahunan). Gresik juga memiliki tradisi **Pasar Bandeng** yang merayakan hasil tangkapan bandeng.",
        "Tokoh_terkenal": "**Syekh Maulana Malik Ibrahim (Sunan Gresik)** (Walisongo), dan tokoh-tokoh lokal yang berperan dalam perlawanan kolonial.",
        "bentang_alam": "Gresik didominasi oleh dataran rendah dan pesisir. Wilayahnya mencakup Pulau Bawean, yang memiliki bentang alam kepulauan unik dengan taman laut."
    },
    "Lamongan": {
        "sejarah": "Lamongan memiliki akar sejarah yang kuat sejak zaman Majapahit, dan kemudian berkembang pesat sebagai salah satu pusat penyebaran Islam di Pantura. Hari jadi Lamongan ditetapkan pada 26 Mei 1569 M, merujuk pada pengangkatan Tumenggung Surajaya sebagai Adipati. Wilayah ini juga erat kaitannya dengan Sunan Drajat dan tokoh legenda Joko Tingkir.",
        "budaya": "Budaya pesisir dan Mataraman berpadu. Kesenian khasnya adalah **Tari Boran** (tari yang menggambarkan kehidupan penjual nasi boran) dan pertunjukan **Jula-Juli** (puisi rakyat).",
        "Makanan": "**Nasi Boran** (nasi dengan berbagai lauk khas, seperti udang, bandeng, dan jeroan), **Soto Lamongan** (dengan taburan koya khas), **Tahu Campur Lamongan**, dan **Jeroan Bandeng Sate**.",
        "Adat": "Tradisi **Malam Selawe** (ziarah pada malam ke-25 Ramadan), **Haul Sunan Drajat**, dan upacara **Sedekah Laut** bagi masyarakat pesisir.",
        "Tokoh_terkenal": "**Sunan Drajat** (Walisongo), dan **Joko Tingkir** (tokoh legenda dan pendiri Kesultanan Pajang).",
        "bentang_alam": "Terbentang dari dataran rendah pesisir di utara hingga perbukitan kapur di selatan. Memiliki garis pantai yang panjang dan dikenal sebagai penghasil ikan laut, air tawar (bandeng), dan pertanian padi."
    },
    "Sumenep": {
        "sejarah": "Sumenep, yang terletak di ujung timur Pulau Madura, merupakan kerajaan tertua di Madura. Hari jadi Sumenep ditetapkan pada 31 Oktober 1269 M, tanggal pengangkatan Arya Wiraraja sebagai Adipati pertama oleh Raja Kertanegara (Singasari). Wilayahnya meliputi daratan Madura dan ratusan pulau kecil (kepulauan Kangean).",
        "budaya": "Budaya Madura murni dengan dialek yang khas. Kesenian utamanya adalah **Tari Topeng Gethak** (tari topeng khas Keraton Sumenep), **Kerapan Sapi** (pacuan sapi), dan arsitektur keraton yang indah.",
        "Makanan": "**Sate Lalat** (sate dari daging sapi/kambing yang dipotong sangat kecil, bukan lalat), **Kaldu Kokot** (kaldu sapi dengan bumbu rempah dan kacang hijau), dan **Rujak Selingkuh** (rujak dengan toping cingur).",
        "Adat": "Tradisi **Kerapan Sapi** (khas Madura), ritual **Petik Laut**, dan berbagai upacara kebesaran yang masih dilestarikan di sekitar Keraton Sumenep.",
        "Tokoh_terkenal": "**Arya Wiraraja** (Adipati Pertama Sumenep dan tokoh penting dalam pendirian Majapahit) dan para Raja dari Dinasti Sumenep.",
        "bentang_alam": "Terdiri dari wilayah daratan dan ratusan pulau kecil (pulau-pulau Sumenep). Bentang alamnya didominasi oleh dataran rendah dan perbukitan, dengan kekayaan laut yang luar biasa."
    },
    "Pamekasan": {
        "sejarah": "Pamekasan adalah salah satu wilayah inti di Pulau Madura yang sejarahnya terkait erat dengan perjuangan melawan pengaruh Jawa (Mataram) dan VOC. Hari jadi Pamekasan ditetapkan pada 3 November 1530 M, dikaitkan dengan penetapan Adipati Ronggosukowati sebagai penguasa lokal oleh Mataram. Wilayah ini dikenal sebagai pusat batik Madura.",
        "budaya": "Budaya Madura yang kental dengan nuansa Islam dan ksatria. Dikenal sebagai pusat **Batik Pamekasan** yang memiliki motif cerah dan berani. Kesenian lainnya adalah **Hadrah** dan **Wayang Topeng Madura**.",
        "Makanan": "**Sate Laler** (Sate lalat, potongan sangat kecil), **Tajin Sobih** (bubur dengan kuah manis santan), dan **Kacang Santan**.",
        "Adat": "Tradisi **Kerapan Sapi**, **Upacara Nyadran** (sedekah bumi), dan prosesi ritual yang berkaitan dengan makam leluhur di kompleks pemakaman Asta Tinggi.",
        "Tokoh_terkenal": "**Adipati Ronggosukowati** dan para tokoh ulama dari pondok pesantren Pamekasan.",
        "bentang_alam": "Didominasi oleh dataran rendah dengan lahan pertanian tembakau yang luas. Pesisirnya menghasilkan garam dan ikan."
    },
    "Sampang": {
        "sejarah": "Sampang merupakan bagian tengah dari Pulau Madura, yang sejarahnya terikat dengan pembagian wilayah oleh Mataram dan kemudian menjadi lokasi penting di masa kolonial. Hari jadi Sampang ditetapkan pada 23 Desember 1624 M, pada masa kepemimpinan Pangeran Cakraningrat I dari Mataram yang menata administrasi Madura.",
        "budaya": "Budaya Madura dengan karakter yang keras dan terbuka. Kesenian yang populer adalah **Karapan Sapi** dan berbagai jenis musik tradisional Madura seperti **Saronen** (alat musik tiup).",
        "Makanan": "**Nasi Kobel** (nasi dicampur lauk-pauk dan bumbu), **Kue Lopis** (beras ketan disajikan dengan kuah gula merah kental), dan **Sate Ayam Sampang**.",
        "Adat": "Tradisi **Karapan Sapi**, ritual **Tanduk Tani** (syukuran panen), dan upacara keagamaan di sekitar makam leluhur.",
        "Tokoh_terkenal": "**Pangeran Trunojoyo** (pahlawan yang melawan Mataram dan VOC) diyakini memiliki hubungan erat dengan wilayah ini.",
        "bentang_alam": "Terletak di dataran rendah tengah Madura yang memiliki potensi pertanian (terutama tembakau dan garam) dan garis pantai utara-selatan."
    },
    "Bangkalan": {
        "sejarah": "Bangkalan adalah gerbang Madura, terletak di ujung barat pulau dan terhubung dengan Surabaya via Jembatan Suramadu. Hari jadi Bangkalan ditetapkan pada 24 Oktober 1624 M, pada masa kepemimpinan Pangeran Cakraningrat I. Bangkalan menjadi pusat dinasti Cakraningrat yang menguasai Madura dan memiliki pengaruh besar terhadap politik Jawa.",
        "budaya": "Budaya Madura yang paling dekat dengan Jawa, namun tetap mempertahankan identitas khas. Kesenian andalan adalah **Karapan Sapi** dan **Tari Topeng Bangkalan**.",
        "Makanan": "**Nasi Serpang** (nasi dengan lauk-pauk khas Bangkalan), **Bebek Sinjay** (bebek goreng dengan sambal pencit/mangga muda), dan **Tajin Pedas** (bubur pedas/asin).",
        "Adat": "Tradisi **Karapan Sapi** (paling terkenal), ritual **Rokat Tase'** (sedekah laut), dan upacara **Petik Laut**.",
        "Tokoh_terkenal": "**Pangeran Cakraningrat** (dinasti penguasa Madura), dan tokoh-tokoh ulama dari pesantren setempat.",
        "bentang_alam": "Dataran rendah di bagian selatan dan perbukitan kapur di utara. Berada di ujung barat Madura, yang menjadikannya lokasi strategis untuk perdagangan dan perhubungan."
    },
    "Pacitan": {
        "sejarah": "Pacitan adalah kabupaten paling barat daya Jawa Timur, berbatasan dengan Jawa Tengah. Hari jadi ditetapkan pada 7 November 1745 M, merujuk pada pengangkatan Tumenggung Setroketipo oleh Pakubuwana II (Mataram) sebagai Adipati. Pacitan dikenal sebagai daerah perbatasan yang sulit ditembus, menjadikannya 'Tanah Ksatria' di selatan Jawa. Ia juga dikenal sebagai tempat kelahiran Presiden ke-6 RI.",
        "budaya": "Budaya Jawa Mataraman dengan pengaruh Priangan Timur. Kesenian khasnya adalah **Reog Ponorogo** (walaupun Ponorogo adalah pusat utama, reog populer di sini) dan **Jaranan Thek**.",
        "Makanan": "**Nasi Tiwul** (nasi dari singkong/gaplek), **Sayur Cabuk** (sayur dengan bumbu kelapa sangrai), **Tahu Tuna** (olahan tahu dengan isian daging tuna khas pesisir selatan).",
        "Adat": "Tradisi **Gerebek Suro** (perayaan tahun baru Jawa), upacara **Larung Sesaji** (sedekah laut) di pesisir selatan, dan ritual di Goa Gong.",
        "Tokoh_terkenal": "**Susilo Bambang Yudhoyono** (Presiden RI ke-6) dan **Ki Ageng Buwono Keling** (tokoh penyebar Islam).",
        "bentang_alam": "Dominasi pegunungan kapur (Pegunungan Sewu), menjadikannya daerah yang kaya akan goa-goa eksotis (Goa Gong) dan pantai-pantai tersembunyi di pesisir selatan."
    },
    "Ponorogo": {
        "sejarah": "Ponorogo didirikan oleh Adipati Bathara Katong, putra Raja Brawijaya V (Majapahit), dan ditetapkan hari jadinya pada 11 Agustus 1496 M. Ponorogo dikenal sebagai 'Bumi Reog' karena merupakan pusat seni tari **Reog Ponorogo** yang legendaris. Pada masa Mataram dan kolonial, Ponorogo menjadi wilayah Karesidenan Madiun yang penting secara budaya dan politik.",
        "budaya": "Budaya kental dengan Jawa Mataraman dan memiliki identitas seni yang sangat kuat. Kesenian utama adalah **Reog Ponorogo** (tari topeng singa raksasa, Singo Barong), **Gamelan Reyog**, dan **Jathil** (tari berkuda wanita).",
        "Makanan": "**Sate Ponorogo** (sate ayam dengan irisan daging tebal dan bumbu kacang manis kental), **Nasi Pecel Pincuk**, dan **Dawet Jabung** (minuman dawet khas).",
        "Adat": "Tradisi utama adalah **Grebeg Suro** yang meliputi **Larungan Risalah Doa** di Telaga Ngebel dan festival Reog Nasional yang diselenggarakan setiap tahun baru Hijriah.",
        "Tokoh_terkenal": "**Adipati Bathara Katong** (pendiri Ponorogo), dan tokoh-tokoh spiritual seperti **Kyai Ageng Hasan Besari** (pendiri Pesantren Tegalsari).",
        "bentang_alam": "Wilayah dataran tinggi dan pegunungan (Gunung Wilis dan Gunung Lawu) yang memiliki potensi wisata alam seperti Telaga Ngebel dan hawa yang sejuk."
    },
    "Magetan": {
        "sejarah": "Kabupaten Magetan didirikan pada 12 Oktober 1676 M oleh Yosonegoro (Ki Mageti) atas perintah Raja Mataram. Magetan terletak di lereng timur Gunung Lawu, menjadikannya daerah pegunungan yang strategis. Wilayah ini dikenal sebagai penghasil kerajinan kulit dan memiliki potensi pertanian hortikultura yang subur.",
        "budaya": "Budaya Jawa Mataraman yang dipengaruhi oleh lingkungan pegunungan. Kesenian khasnya adalah **Tari Jalak Lawu** dan kerajinan **Anyaman Bambu** serta **Kulit**.",
        "Makanan": "**Tepo Tahu** (tahu goreng disajikan dengan bumbu kecap pedas dan kerupuk), **Sate Kelinci** (khas daerah lereng Lawu), dan **Jeruk Pamelo** (jeruk besar khas Magetan).",
        "Adat": "Tradisi **Labuhan** di Telaga Sarangan (upacara sesaji untuk meminta keselamatan dan kemakmuran) dan upacara tradisional yang berhubungan dengan Gunung Lawu.",
        "Tokoh_terkenal": "**Yosonegoro (Ki Mageti)** (Bupati Pertama Magetan) dan sejumlah tokoh ulama dari pesantren setempat.",
        "bentang_alam": "Terletak di lereng Gunung Lawu (sebelah timur), sehingga memiliki udara yang sangat dingin dan bentang alam pegunungan yang indah, termasuk Telaga Sarangan."
    },
    "Ngawi": {
        "sejarah": "Ngawi secara administratif dibentuk pada 7 November 1830 M, tidak lama setelah berakhirnya Perang Diponegoro, oleh Pemerintah Kolonial Belanda. Lokasinya yang strategis di pertemuan Sungai Bengawan Solo dan Sungai Madiun menjadikannya penting sebagai pusat pertahanan, dibuktikan dengan keberadaan **Benteng Van Den Bosch**.",
        "budaya": "Budaya Jawa Mataraman. Kesenian yang menonjol adalah **Tari Jaranan** dan **Ludruk Ngawi**. Ngawi juga dikenal sebagai daerah yang sangat menjunjung tinggi tradisi pertanian.",
        "Makanan": "**Tahu Campur Ngawi**, **Ledre Telo** (Ledre dari ubi), dan **Botok Mercon** (botok dengan rasa sangat pedas).",
        "Adat": "Tradisi **Sedekah Bumi** (perayaan panen raya) dan upacara adat di sekitar Benteng Van Den Bosch yang kini menjadi situs bersejarah.",
        "Tokoh_terkenal": "**KH. Abdul Fatah** (ulama pendiri pondok pesantren), dan tokoh-tokoh lokal yang terlibat dalam pergerakan kemerdekaan.",
        "bentang_alam": "Terletak di dataran rendah yang dialiri dua sungai besar (Bengawan Solo dan Madiun). Wilayahnya sangat subur, menjadikannya lumbung pangan utama Jawa Timur."
    },
    "Lumajang": {
        "sejarah": "Lumajang ditetapkan hari jadinya pada 15 Desember 1276 M, merujuk pada penetapan **Arya Wiraraja** sebagai Adipati Lumajang. Lumajang diyakini sebagai pusat dari **Kerajaan Lamajang Tigang Juru** (kerajaan vasal Majapahit). Wilayah ini menjadi benteng pertahanan terakhir Majapahit setelah runtuh.",
        "budaya": "Budaya perpaduan Jawa Mataraman, Madura, dan Tengger. Kesenian khasnya adalah **Kuda Kencak** (kuda menari dengan iringan musik) dan **Tari Godril**.",
        "Makanan": "**Pisang Agung** (pisang khas Lumajang yang berukuran besar), **Jajan Geti** (kue wijen dan gula merah), dan **Pecel Lele/Mujaer**.",
        "Adat": "Tradisi **Tari Kuda Kencak** (sebagai hiburan rakyat dan upacara), ritual di Gunung Semeru, dan tradisi lokal yang terkait dengan pertanian.",
        "Tokoh_terkenal": "**Arya Wiraraja** (Adipati Lumajang dan tokoh penting Majapahit) serta para tokoh yang terlibat dalam perlawanan kolonial.",
        "bentang_alam": "Didominasi oleh Gunung Semeru (gunung tertinggi di Jawa), menjadikannya daerah yang kaya akan potensi pasir, air terjun, dan memiliki garis pantai selatan."
    },
    "Jember": {
        "sejarah": "Jember adalah kabupaten yang relatif modern, dibentuk pada 1 Januari 1929 M oleh Pemerintah Hindia Belanda. Perkembangannya sangat pesat berkat industri perkebunan, terutama tembakau (cerutu) dan kopi di masa kolonial. Jember kini dikenal sebagai pusat pendidikan dan fashion dunia (Jember Fashion Carnival).",
        "budaya": "Budaya 'Pandhalungan', perpaduan antara Jawa, Madura, dan Osing (Banyuwangi). Kesenian modern seperti **Jember Fashion Carnival (JFC)** menjadi ikon utama. Kesenian tradisional mencakup **Musik Patrol** dan **Tari Lahbako** (tari tembakau).",
        "Makanan": "**Soto Daging Jember** (soto dengan bumbu yang kaya), **Suwar-Suwir** (manisan tape), dan berbagai olahan dari tape (Tapai Manis).",
        "Adat": "Tradisi yang menonjol adalah **Upacara Petik Tembakau** dan perayaan budaya tahunan JFC yang menarik perhatian internasional.",
        "Tokoh_terkenal": "**Dynand Fariz** (pendiri Jember Fashion Carnival) dan tokoh-tokoh ulama dari pesantren terkemuka.",
        "bentang_alam": "Terbentang dari dataran rendah subur (pusat perkebunan) hingga Pegunungan Hyang di utara dan Pesisir Selatan yang ekstrem."
    },
    "Bondowoso": {
        "sejarah": "Bondowoso dibentuk pada 17 Agustus 1819 M oleh Pangeran Bondowoso (anak dari Adipati Wiroguno) atas perintah Daendels (Gubernur Jenderal Belanda). Awalnya merupakan bagian dari Karesidenan Besuki. Wilayah ini dikenal sebagai penghasil kopi dan tempat bersejarah perlawanan heroik rakyat Bondowoso terhadap Belanda.",
        "budaya": "Budaya 'Pendhalungan' yang dipengaruhi Madura dan Jawa. Kesenian khasnya adalah **Singo Ulung** (tarian topeng singa yang melambangkan keberanian). Bondowoso juga dikenal sebagai **Republik Kopi** karena kualitas kopinya.",
        "Makanan": "**Tape Manis Bondowoso** (tape singkong yang sangat manis), **Rujak Panggul**, dan **Nasi Kotok/Gudeg Nangka**.",
        "Adat": "Tradisi **Kesenian Singo Ulung** (digelar saat upacara adat atau penyambutan), dan ritual yang berhubungan dengan perkebunan kopi.",
        "Tokoh_terkenal": "**Pangeran Bondowoso** (pendiri kabupaten) dan tokoh-tokoh pergerakan nasional seperti **KH. Ali Wafa**.",
        "bentang_alam": "Wilayah pegunungan (Pegunungan Hyang) yang menjadikannya daerah penghasil kopi terbaik dan memiliki lanskap Kawah Ijen yang sebagian besar masuk wilayah ini."
    },
    "Situbondo": {
        "sejarah": "Situbondo awalnya merupakan bagian dari Karesidenan Besuki. Situbondo resmi menjadi kabupaten mandiri pada 15 Oktober 1950 M, setelah penataan ulang administrasi di masa kemerdekaan. Situbondo dikenal dengan julukan 'Kota Santri' karena banyaknya pesantren, dan 'Bumi Sholawat Nariyah'.",
        "budaya": "Budaya Pendhalungan yang kuat dipengaruhi oleh suku Madura dan Osing. Keseniannya adalah **Tari Landung** (tari rakyat) dan berbagai tradisi islami yang berpusat di pondok pesantren.",
        "Makanan": "**Nasi Sodu** (nasi dengan lauk-pauk khas Situbondo), **Sate Kelapa** (sate dengan parutan kelapa), dan **Tajin Palappa** (bubur dengan kuah rempah).",
        "Adat": "Tradisi **Tumpeng Sewu** (acara syukuran besar) dan ritual keagamaan yang berpusat di masjid dan pesantren.",
        "Tokoh_terkenal": "**Kiai Haji As'ad Syamsul Arifin** (ulama besar dan Pahlawan Nasional dari Pondok Pesantren Salafiyah Syafi'iyah Sukorejo).",
        "bentang_alam": "Terletak di pantai utara Jawa, didominasi oleh dataran rendah dan perbukitan. Memiliki potensi wisata bahari yang besar di kawasan Taman Nasional Baluran."
    },
    "Probolinggo": {
        "sejarah": "Probolinggo didirikan pada 24 Januari 1746 M di masa VOC. Awalnya bernama **Banger** sebelum diubah menjadi Probolinggo. Wilayah ini dikenal sebagai pusat perkebunan anggur, mangga, dan tebu sejak zaman kolonial. Sejarahnya erat dengan perkembangan pelabuhan dagang di Pantai Utara Jawa Timur.",
        "budaya": "Budaya pesisir dan Tengger. Kesenian khasnya adalah **Tari Glipang** (tari heroik yang bernuansa Islam) dan berbagai tradisi yang berkaitan dengan suku Tengger di kawasan Bromo.",
        "Makanan": "**Nasi Jagung** (sajian nasi dari jagung), **Anggur Probolinggo**, **Mangga Manalagi**, dan **Soto Kerbau**.",
        "Adat": "Tradisi **Upacara Kasada** (ritual tahunan suku Tengger di Gunung Bromo) dan **Petik Laut** (syukuran nelayan).",
        "Tokoh_terkenal": "**Ki Ronggo** (tokoh lokal yang berperan dalam pemerintahan awal Probolinggo) dan para pemimpin pergerakan di masa kolonial.",
        "bentang_alam": "Terbentang dari pantai utara yang subur hingga Pegunungan Bromo-Tengger-Semeru di selatan. Memiliki keindahan alam yang sangat beragam."
    },
    "Pasuruan": {
        "sejarah": "Pasuruan adalah kota pelabuhan penting di Pantai Utara Jawa sejak era Mataram hingga kolonial. Hari jadi Kabupaten Pasuruan ditetapkan pada 18 Oktober 1929 M. Pasuruan menjadi pusat Karesidenan penting bagi Belanda karena produksi gula dan kopi yang besar, menjadikannya daerah yang kaya secara ekonomi historis.",
        "budaya": "Budaya pesisir dan percampuran Jawa-Madura. Kesenian khasnya adalah **Tari Srandul** (tari rakyat yang berisi kritik sosial) dan musik tradisional **Hadrah**.",
        "Makanan": "**Nasi Punel** (nasi pulen dengan berbagai lauk dan parutan kelapa), **Rawon Nguling** (rawon dengan daging sapi khas), dan **Bipang Jipang** (snack manis dari beras ketan).",
        "Adat": "Tradisi **Petik Laut** (ritual syukuran nelayan) dan tradisi keagamaan yang kuat di lingkungan pesantren.",
        "Tokoh_terkenal": "**Untung Suropati** (pahlawan perlawanan terhadap VOC), dan tokoh-tokoh ulama dari pesantren Gadingrejo.",
        "bentang_alam": "Didominasi oleh Gunung Arjuno dan Welirang di selatan (pusat penghasil sayur dan apel) dan dataran rendah pesisir di utara (pusat industri dan pelabuhan)."
    },
    "Banyuwangi": {
        "sejarah": "Hari jadi Banyuwangi ditetapkan pada 18 Desember 1771 M, merujuk pada peristiwa heroik **Perang Puputan Bayu** melawan VOC. Banyuwangi adalah pusat dari **Kerajaan Blambangan** yang merupakan benteng pertahanan terakhir Hindu-Jawa di timur. Wilayah ini kental dengan budaya Suku Osing.",
        "budaya": "Budaya **Osing** (suku asli Banyuwangi) yang unik dan berbeda dari Jawa Mataraman. Kesenian utamanya adalah **Tari Gandrung** (tari selamat datang), **Kuntulan** (tari bernuansa islami), dan **Janger**.",
        "Makanan": "**Rujak Soto** (perpaduan rujak sayur dengan kuah soto), **Pecel Pitik** (ayam panggang dengan bumbu kelapa sangrai), dan **Sego Tempong** (nasi dengan lauk pedas).",
        "Adat": "Tradisi **Gandrung Sewu** (festival tari massal), **Grebeg Tumpeng Sewu** (ritual syukuran Osing), dan ritual **Adat Kebo-keboan** (meminta hujan) di desa adat.",
        "Tokoh_terkenal": "**Rempeg Jaga Raga** (pemimpin Perang Puputan Bayu) dan tokoh-tokoh lokal dari Kerajaan Blambangan.",
        "bentang_alam": "Bentang alam yang lengkap, dari Gunung Ijen (kawah api biru), hutan, hingga Pesisir Selatan (Alas Purwo) dan Pesisir Utara (Selat Bali)."
    },
    "Bojonegoro": {
        "sejarah": "Hari jadi Bojonegoro ditetapkan pada 20 Oktober 1677 M, merujuk pada pemindahan pusat pemerintahan dari Jipang ke Rajekwesi (Bojonegoro) oleh Amangkurat II (Mataram). Dikenal sebagai 'Tanah Begawan' karena dilalui Sungai Bengawan Solo dan kaya akan sumber daya hutan jati dan migas (minyak dan gas).",
        "budaya": "Perpaduan Jawa Mataraman dan Pesisir. Kesenian khasnya adalah **Tari Thengul** (tari boneka kayu), **Tari Tayub**, dan komunitas adat **Samin**.",
        "Makanan": "**Ledre** (kue pisang tipis renyah), **Nasi Pecel** khas Bojonegoro, dan berbagai olahan dari singkong.",
        "Adat": "Tradisi **Tayuban** dan ritual di **Kayangan Api** (sumber api abadi), yang dianggap sakral oleh masyarakat setempat.",
        "Tokoh_terkenal": "**Adipati Rajekwesi** (Bupati pertama) dan tokoh-tokoh dari Komunitas Samin.",
        "bentang_alam": "Dibelah oleh Sungai Bengawan Solo. Memiliki perbukitan kapur di utara dan selatan, serta hutan jati yang luas."
    },
    "Tuban": {
        "sejarah": "Tuban adalah pelabuhan dagang utama Majapahit dan pusat penyebaran Islam. Hari jadi ditetapkan pada 12 November 1293 M, tanggal pengangkatan **Ronggolawe** sebagai Adipati pertama. Dikenal sebagai 'Bumi Wali' karena terdapat makam Sunan Bonang dan Maulana Malik Ibrahim.",
        "budaya": "Budaya Jawa Pesisir dan Islam yang kuat. Kesenian khasnya adalah **Sandur** (pertunjukan rakyat) dan kerajinan **Batik Gedog** (batik kapas khas Tuban).",
        "Makanan": "**Garang Asem**, **Becek Menthok** (masakan itik kental), dan kue tradisional **Dumbek**.",
        "Adat": "Tradisi **Haul Sunan Bonang** (ziarah besar), **Sedekah Laut**, dan upacara tahunan di makam leluhur.",
        "Tokoh_terkenal": "**Raden Haryo Ronggolawe** (Adipati Pertama) dan **Sunan Bonang** (Walisongo).",
        "bentang_alam": "Dataran rendah pesisir di utara dan perbukitan kapur (Pegunungan Kendeng Utara) di selatan, menjadikannya 'Kota Seribu Goa'."
    },
    "Malang": {
        "sejarah": "Kabupaten Malang adalah salah satu yang tertua, ditetapkan hari jadinya pada 28 November 760 M, berdasarkan **Prasasti Dinoyo** (berdirinya Kerajaan Kanjuruhan). Malang kemudian menjadi pusat **Kerajaan Singasari**. Di masa kolonial, Malang adalah Karesidenan penting dan dikenal sebagai daerah perkebunan yang subur.",
        "budaya": "Budaya Jawa Mataraman yang kuat. Kesenian khasnya adalah **Tari Topeng Malangan** dan berbagai kesenian yang terkait dengan gunung (Bromo/Semeru).",
        "Makanan": "**Bakso Malang** (populer secara nasional), **Cwie Mie Malang** (mie ayam khas), dan **Apel Malang** (buah khas dataran tinggi).",
        "Adat": "Tradisi ritual di Candi Singosari, **Kirab Pusaka** pada Hari Jadi, dan upacara adat di kawasan lereng gunung.",
        "Tokoh_terkenal": "**Raja Gajayana** (Kanjuruhan), **Ken Arok** (Singasari), dan para tokoh ulama dari pesantren setempat.",
        "bentang_alam": "Dikelilingi gunung (Semeru, Arjuno, Kawi) dengan dataran tinggi yang dingin dan subur. Memiliki garis pantai selatan yang berpotensi wisata bahari."
    },
    "Sidoarjo": {
        "sejarah": "Sidoarjo awalnya bernama Afdeeling **Sidokare** di bawah Karesidenan Surabaya. Nama Sidokare diubah menjadi **Sidoarjo** ('Sido' = Jadi, 'Harjo/Jo' = Makmur) pada 31 Januari 1859 M oleh Pemerintah Kolonial Belanda. Kini dikenal sebagai penyangga utama Kota Surabaya dan pusat industri.",
        "budaya": "Budaya 'Arek' (Surabaya) dan Pesisir. Kesenian khasnya adalah **Tari Remo** dan **Ujung-ujungan** (tari adu betis sebagai ritual memohon hujan).",
        "Makanan": "**Bandeng Asap/Presto**, **Kupang Lontong** (kupang kecil dengan kuah petis dan lontong), dan **Kerupuk Udang**.",
        "Adat": "Tradisi **Nyadran** (bersih desa) dan ritual **Ujung-ujungan** di beberapa daerah sebagai tradisi kuno meminta hujan.",
        "Tokoh_terkenal": "**KH. Ali Mas'ud** (ulama kharismatik), dan tokoh-tokoh pergerakan nasional di sekitar Surabaya.",
        "bentang_alam": "Dataran rendah aluvial, merupakan delta Sungai Brantas. Topografi rata dan padat penduduk, menjadikannya pusat industri dan perikanan tambak (bandeng/udang)."
    },
    "Surabaya": {
        "sejarah": "Didirikan pada **31 Mei 1293 M** dan dikenal sebagai **Kota Pahlawan** karena pertempuran 10 November 1945. Nama Surabaya berasal dari legenda pertarungan antara Ikan **Sura** (hiu) dan **Baya** (buaya). Dahulu merupakan pusat niaga utama Hindia Belanda.",
        "budaya": "Budaya **'Arek'** yang blak-blakan dan egaliter, dipengaruhi akulturasi Jawa Pesisir, Tionghoa, dan Arab. Kesenian khasnya adalah **Tari Remo** dan tradisi **Cangkruk**.",
        "Makanan": "**Rujak Cingur** (sayur, buah, dan cingur/hidung sapi dengan bumbu petis), **Lontong Balap** (lontong, tauge, tahu, dan lentho dengan kuah petis), **Rawon** (sup daging kuah hitam dari kluwek), dan **Sate Klopo**.",
        "Adat": "Tradisi **Kenduri** atau **Sedekah Bumi/Laut** (Nyadar) di beberapa kawasan pesisir. Semangat kepahlawanan dan nasionalisme yang kental.",
        "Tokoh_terkenal": "**Dr. Soetomo** (pendiri Boedi Oetomo), **Bung Tomo** (pemimpin pertempuran 10 November), dan **Sunan Ampel** (Wali Sanga).",
        "bentang_alam": "Dataran rendah aluvial yang sangat datar. Dilalui oleh **Kali Mas** (anak Sungai Brantas). Berfungsi sebagai pusat pemerintahan, industri, dan pelabuhan (Tanjung Perak)."
    },
    "Batu": {
        "sejarah": "Menjadi kota otonom pada **17 Oktober 2001**. Sejak abad ke-10 dikenal sebagai tempat peristirahatan (peristirahatan keluarga Kerajaan Medang). Dijuluki **'De Kleine Zwitserland'** (Swiss Kecil di Pulau Jawa) oleh Belanda karena udaranya yang sejuk.",
        "budaya": "Budaya yang dipengaruhi oleh kultur Malang Raya (Malangan) dengan basis agraris dan pariwisata. Kesenian lokal yang masih berkembang meliputi **Kuda Lumping** dan **Campursari**.",
        "Makanan": "**Apel Batu** (buah ikonik), **Ketela/Ubi Madu**, berbagai **Olahan Apel** (sari apel, keripik apel), dan **Pos Ketan Legenda**.",
        "Adat": "Tradisi yang berkaitan dengan kesuburan tanah dan hasil panen seperti **Sedekah Bumi** (bertepatan dengan panen).",
        "Tokoh_terkenal": "Tokoh-tokoh lokal yang menjadi pionir pembangunan pariwisata dan pertanian di kawasan ini.",
        "bentang_alam": "Wilayah pegunungan dan dataran tinggi, terletak di kaki dan lereng **Gunung Panderman, Gunung Arjuno,** dan **Gunung Welirang**. Ketinggian rata-rata 700-1.800 mdpl. Dikenal dengan udara yang sejuk dan tanah subur untuk perkebunan."
    }
}
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