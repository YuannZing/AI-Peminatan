import streamlit as st

# Menambahkan CSS kustom agar tampilan lebih menarik
st.markdown("""
    <style>
    .title {
        font-size: 36px;
        font-weight: bold;
        color: black;
        text-align: center;
        margin-bottom: 20px;
    }
    .question {
        font-size: 18px;
        font-weight: bold;
        margin-top: 20px;
        color: #333;
    }
    .radio-group label {
        font-size: 16px;
        color: #555;
    }
    .stRadio {
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Judul
st.markdown('<div class="title">Asesmen Minat Siswa: Front End, Back End, Full Stack atau Game Development</div>', unsafe_allow_html=True)

# Pertanyaan 1
st.markdown('<div class="question">1. Saat memulai proyek pengembangan aplikasi, apa yang paling menarik bagi Anda?</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 1
display_options_1 = [
    '1. Mendesain tampilan dan interaksi pengguna (UI/UX)',
    '2. Mengelola data dan logika di balik aplikasi',
    '3. Menggabungkan keduanya, saya suka melihat keseluruhan proses dari awal sampai akhir',
    '4. Membuat dunia interaktif dan gameplay yang menarik'
]

real_options_1 = [
    'Mendesain tampilan dan interaksi pengguna (UI/UX)',
    'Mengelola data dan logika di balik aplikasi',
    'Menggabungkan keduanya, saya suka melihat keseluruhan proses dari awal sampai akhir',
    'Membuat dunia interaktif dan gameplay yang menarik'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 1
selected_display_option_1 = st.radio("Pilih salah satu opsi:", display_options_1, key=1)
selected_option_1 = real_options_1[display_options_1.index(selected_display_option_1)]

# Menampilkan hasil pilihan 1
st.write(f'Kamu memilih: {selected_option_1}')



# Pertanyaan 2
st.markdown('<div class="question">2. Apakah Anda lebih tertarik dengan:</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 2
display_options_2 = [
    '1. Menciptakan tampilan website atau aplikasi yang menarik secara visual?',
    '2. Menulis logika dan kode untuk memproses data dan fungsionalitas aplikasi?',
    '3. Memiliki kemampuan di kedua bidang dan memahami bagaimana keduanya bekerja bersama?',
    '4. Membangun karakter, level, dan mekanisme dalam game?'
]

real_options_2 = [
    'Menciptakan tampilan website atau aplikasi yang menarik secara visual?',
    'Menulis logika dan kode untuk memproses data dan fungsionalitas aplikasi?',
    'Memiliki kemampuan di kedua bidang dan memahami bagaimana keduanya bekerja bersama?',
    'Membangun karakter, level, dan mekanisme dalam game?'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 2
selected_display_option_2 = st.radio("Pilih salah satu opsi:", display_options_2, key=2)
selected_option_2 = real_options_2[display_options_2.index(selected_display_option_2)]

# Menampilkan hasil pilihan 2
st.write(f'Kamu memilih: {selected_option_2}')



# Pertanyaan 3
st.markdown('<div class="question">3. Ketika bekerja dalam sebuah tim, peran apa yang paling Anda sukai?</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 3
display_options_3 = [
    '1. Mendesain dan mengimplementasikan tampilan yang dilihat pengguna.',
    '2. Mengurus server, database, dan bagaimana aplikasi bekerja di belakang layar.',
    '3. Mengintegrasikan tampilan dan fungsionalitas secara keseluruhan.',
    '4. Mengembangkan animasi, efek suara, atau mekanisme game.'
]

real_options_3 = [
    'Mendesain dan mengimplementasikan tampilan yang dilihat pengguna.',
    'Mengurus server, database, dan bagaimana aplikasi bekerja di belakang layar.',
    'Mengintegrasikan tampilan dan fungsionalitas secara keseluruhan.',
    'Mengembangkan animasi, efek suara, atau mekanisme game.'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 3
selected_display_option_3 = st.radio("Pilih salah satu opsi:", display_options_3, key=3)
selected_option_3 = real_options_3[display_options_3.index(selected_display_option_3)]

# Menampilkan hasil pilihan 3
st.write(f'Kamu memilih: {selected_option_3}')



# Pertanyaan 4
st.markdown('<div class="question">4. Mana yang lebih Anda nikmati?</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 4
display_options_4 = [
    '1. Menggunakan HTML, CSS, dan JavaScript untuk membuat tampilan yang interaktif.',
    '2. Menggunakan bahasa pemrograman server-side seperti PHP, Python, atau Node.js untuk logika backend.',
    '3. Membuat aplikasi lengkap dari frontend hingga backend, mengintegrasikan keduanya.',
    '4. Menggunakan Unity, Unreal Engine, atau framework lain untuk membuat game.'
]

real_options_4 = [
    'Menggunakan HTML, CSS, dan JavaScript untuk membuat tampilan yang interaktif.',
    'Menggunakan bahasa pemrograman server-side seperti PHP, Python, atau Node.js untuk logika backend.',
    'Membuat aplikasi lengkap dari frontend hingga backend, mengintegrasikan keduanya.',
    'Menggunakan Unity, Unreal Engine, atau framework lain untuk membuat game.'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 4
selected_display_option_4 = st.radio("Pilih salah satu opsi:", display_options_4, key=4)
selected_option_4 = real_options_4[display_options_4.index(selected_display_option_4)]

# Menampilkan hasil pilihan 2
st.write(f'Kamu memilih: {selected_option_4}')



# Pertanyaan 5
st.markdown('<div class="question">5. Apakah Anda tertarik untuk belajar lebih dalam tentang:</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 5
display_options_5 = [
    '1. Desain antarmuka, animasi, dan bagaimana membuat aplikasi mudah digunakan.',
    '2. Mengelola basis data, API, dan keamanan aplikasi.',
    '3. Mengembangkan solusi end-to-end, mulai dari desain hingga fungsionalitas backend.',
    '4. Desain game, pengkodean fisika, dan interaksi dalam game.'
]

real_options_5 = [
    'Desain antarmuka, animasi, dan bagaimana membuat aplikasi mudah digunakan.',
    'Mengelola basis data, API, dan keamanan aplikasi.',
    'Mengembangkan solusi end-to-end, mulai dari desain hingga fungsionalitas backend.',
    'Desain game, pengkodean fisika, dan interaksi dalam game.'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 5
selected_display_option_5 = st.radio("Pilih salah satu opsi:", display_options_5, key=5)
selected_option_5 = real_options_5[display_options_5.index(selected_display_option_5)]

# Menampilkan hasil pilihan 5
st.write(f'Kamu memilih: {selected_option_5}')



# Pertanyaan 6
st.markdown('<div class="question">6. Proyek ideal bagi Anda adalah:</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 6
display_options_6 = [
    '1. Membuat website atau aplikasi yang indah dengan animasi yang menarik.',
    '2. Mengembangkan aplikasi dengan struktur data yang kompleks dan keamanan yang ketat.',
    '3. Membangun aplikasi web yang berfungsi penuh dari frontend hingga backend.',
    '4. Membuat game interaktif dengan grafik yang menarik dan gameplay yang menyenangkan.'
]

real_options_6 = [
    'Membuat website atau aplikasi yang indah dengan animasi yang menarik.',
    'Mengembangkan aplikasi dengan struktur data yang kompleks dan keamanan yang ketat.',
    'Membangun aplikasi web yang berfungsi penuh dari frontend hingga backend.',
    'Membuat game interaktif dengan grafik yang menarik dan gameplay yang menyenangkan.'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 6
selected_display_option_6 = st.radio("Pilih salah satu opsi:", display_options_6, key=6)
selected_option_6 = real_options_6[display_options_6.index(selected_display_option_6)]

# Menampilkan hasil pilihan 6
st.write(f'Kamu memilih: {selected_option_6}')



# Pertanyaan 7
st.markdown('<div class="question">Ketika menghadapi bug atau masalah dalam kode, mana yang lebih menarik untuk diselesaikan?</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 7
display_options_7 = [
    '1. Menemukan dan memperbaiki masalah dalam tampilan atau interaksi pengguna.',
    '2. Menemukan dan memperbaiki masalah pada logika backend atau pemrosesan data.',
    '3. Menemukan solusi untuk masalah yang melibatkan keduanya.',
    '4. Menemukan bug dalam gameplay atau mekanisme game.'
]

real_options_7 = [
    'Menemukan dan memperbaiki masalah dalam tampilan atau interaksi pengguna.',
    'Menemukan dan memperbaiki masalah pada logika backend atau pemrosesan data.',
    'Menemukan solusi untuk masalah yang melibatkan keduanya.',
    'Menemukan bug dalam gameplay atau mekanisme game.'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 7
selected_display_option_7 = st.radio("Pilih salah satu opsi:", display_options_7, key=7)
selected_option_7 = real_options_7[display_options_7.index(selected_display_option_7)]

# Menampilkan hasil pilihan 7
st.write(f'Kamu memilih: {selected_option_7}')



# Pertanyaan 8
st.markdown('<div class="question">8. Teknologi atau alat mana yang paling ingin Anda pelajari lebih lanjut?</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 8
display_options_8 = [
    '1. Framework frontend seperti React, Vue, atau Angular.',
    '2. Teknologi backend seperti Node.js, Django, atau Ruby on Rails.',
    '3. Full stack development dengan tools seperti MERN (MongoDB, Express, React, Node).',
    '4. Game engines seperti Unity atau Unreal Engine.'
]

real_options_8 = [
    'Framework frontend seperti React, Vue, atau Angular.',
    'Teknologi backend seperti Node.js, Django, atau Ruby on Rails.',
    'Full stack development dengan tools seperti MERN (MongoDB, Express, React, Node).',
    'Game engines seperti Unity atau Unreal Engine.'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 8
selected_display_option_8 = st.radio("Pilih salah satu opsi:", display_options_8, key=8)
selected_option_8 = real_options_8[display_options_8.index(selected_display_option_8)]

# Menampilkan hasil pilihan 8
st.write(f'Kamu memilih: {selected_option_8}')



# Pertanyaan 9
st.markdown('<div class="question">Anda lebih suka bekerja pada:</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 9
display_options_9 = [
    '1. Proyek yang menuntut kreativitas dan perhatian pada detail visual.',
    '2. Proyek yang menuntut logika dan pemecahan masalah di tingkat server.',
    '3. Proyek yang memungkinkan saya menangani kedua aspek, frontend dan backend.',
    '4. Proyek yang memungkinkan saya membuat pengalaman bermain yang unik.'
]

real_options_9 = [
    'Proyek yang menuntut kreativitas dan perhatian pada detail visual.',
    'Proyek yang menuntut logika dan pemecahan masalah di tingkat server.',
    'Proyek yang memungkinkan saya menangani kedua aspek, frontend dan backend.',
    'Proyek yang memungkinkan saya membuat pengalaman bermain yang unik.'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 9
selected_display_option_9 = st.radio("Pilih salah satu opsi:", display_options_9, key=9)
selected_option_9 = real_options_9[display_options_9.index(selected_display_option_9)]

# Menampilkan hasil pilihan 9
st.write(f'Kamu memilih: {selected_option_9}')



# Pertanyaan 10
st.markdown('<div class="question">10. Saat menyelesaikan sebuah proyek, Anda merasa puas jika:</div>', unsafe_allow_html=True)

# Opsi jawaban untuk pertanyaan 10
display_options_10 = [
    '1. Tampilan dan antarmuka terlihat rapi, interaktif, dan mudah digunakan oleh pengguna.',
    '2. Sistem backend berjalan lancar dan data diproses dengan efisien.',
    '3. Aplikasi berjalan sempurna dari tampilan hingga fungsionalitas backend.',
    '4. Game yang saya buat dapat dimainkan dengan lancar, dan mekanisme gameplay-nya menyenangkan.'
]

real_options_10 = [
    'Tampilan dan antarmuka terlihat rapi, interaktif, dan mudah digunakan oleh pengguna.',
    'Sistem backend berjalan lancar dan data diproses dengan efisien.',
    'Aplikasi berjalan sempurna dari tampilan hingga fungsionalitas backend.',
    'Game yang saya buat dapat dimainkan dengan lancar, dan mekanisme gameplay-nya menyenangkan.'
]

# Membuat pilihan ganda menggunakan radio button untuk pertanyaan 10
selected_display_option_10 = st.radio("Pilih salah satu opsi:", display_options_10, key=10)
selected_option_10 = real_options_10[display_options_10.index(selected_display_option_10)]

# Menampilkan hasil pilihan 10
st.write(f'Kamu memilih: {selected_option_10}')
