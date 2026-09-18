🚀 Zalando Auto Register Bot

<div align="center">

https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white
https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20Termux-green?style=for-the-badge&logo=linux&logoColor=white
https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge
https://img.shields.io/badge/Status-Active-success?style=for-the-badge

Automated Zalando Account Registration Tool
Fast • Clean • Professional CLI Interface

Features • Installation • Usage • Screenshots • Disclaimer

</div>

---

📖 Description

Zalando Auto Register Bot adalah script Python otomatis untuk melakukan registrasi akun Zalando secara massal menggunakan teknik email aliasing (+1, +2, +3, dst). Script ini dilengkapi dengan antarmuka CLI berwarna, loading animation, dan auto-save hasil ke file akun.txt.

Cocok untuk keperluan testing, automation research, dan pembelajaran HTTP request handling.

---

✨ Features

Feature Description
🎨 Beautiful CLI Tampilan berwarna dengan ANSI Color + banner ASCII
⚡ Auto Email Alias Generate email otomatis pakai +1, +2, dst
👤 Random Name Generator Nama depan & belakang Indonesia diacak otomatis
💾 Auto Save Hasil disimpan ke akun.txt dengan format rapi
📊 Live Progress Status sukses/gagal per akun secara real-time
🔄 Bulk Register Support registrasi multiple akun sekaligus
🎯 Clean Summary Ringkasan hasil akhir yang jelas

---

🖼️ Screenshots

```
   ███████╗ █████╗ ██╗      █████╗ ███╗   ██╗██████╗  ██████╗ 
   ╚══███╔╝██╔══██╗██║     ██╔══██╗████╗  ██║██╔══██╗██╔═══██╗
     ███╔╝ ███████║██║     ███████║██╔██╗ ██║██║  ██║██║   ██║
    ███╔╝  ██╔══██║██║     ██╔══██║██║╚██╗██║██║  ██║██║   ██║
   ███████╗██║  ██║███████╗██║  ██║██║ ╚████║██████╔╝╚██████╔╝
   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ 
        ╔══════════════════════════════════════════╗
        ║   AUTO REGISTER ACCOUNT  •  © masjjoooo  ║
        ╚══════════════════════════════════════════╝
```

---

⚙️ Installation

1️⃣ Clone Repository

```bash
git clone [https://github.com/Masjjoooo/Jalando_Register.git]
cd Jalando-Register
```

2️⃣ Install Dependencies

```bash
pip install requests
```

3️⃣ Run Script

```bash
python mantap.py
```

---

🚀 Usage

1. Jalankan script dengan perintah python mantap.py
2. Masukkan data yang diminta:
   · Email → Base email (contoh: user@gmail.com)
   · Secret → Password akun
   · Jumlah akun → Berapa banyak akun yang ingin dibuat
3. Konfirmasi dengan y untuk mulai
4. Tunggu proses selesai
5. Hasil tersimpan di akun.txt

📄 Format Output (akun.txt)

```
email+1@gmail.com|password123|Andi Santoso|SUCCESS
email+2@gmail.com|password123|Citra Wijaya|SUCCESS
email+3@gmail.com|password123|Budi Pratama|FAILED-429
```

---

📁 Project Structure

```
zalando-auto-register/
│
├── mantap.py         # Main script
├── akun.txt          # Output hasil registrasi (auto-generated)
├── README.md         # Documentation
└── requirements.txt  # Python dependencies
```

---

🧩 Requirements

· Python >= 3.8
· requests library
· OS: Windows / Linux / macOS / Termux (Android)

Install manually:

```bash
pip install requests
```

---

⚠️ Important Notes

⚠️ Session Data Required
Script ini membutuhkan CSRF token, Flow ID, Request ID, dan Cookie yang valid dari session Zalando. Data ini bisa berubah sewaktu-waktu dan harus di-update jika request mulai gagal.

⏱️ Rate Limiting
Zalando memiliki sistem rate-limit. Jangan register terlalu banyak sekaligus atau akun akan terkena 429 Too Many Requests.

📧 Email Alias
Gunakan email yang mendukung alias (+), seperti Gmail, Outlook, atau Yahoo.

---

🛠️ Troubleshooting

Problem Solution
ModuleNotFoundError: requests Jalankan pip install requests
Semua akun gagal (403/401) Update COOKIE, CSRF, FLOW_ID di script
Error 429 Tunggu beberapa menit sebelum retry
Warna tidak muncul di Windows Sudah otomatis fix via os.system("")

---

🤝 Contributing

Pull requests are welcome! Untuk perubahan besar, silakan buka issue terlebih dahulu untuk mendiskusikan apa yang ingin diubah.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

---

📜 License

Distributed under the MIT License. See LICENSE for more information.

---

⚠️ Disclaimer

This tool is for EDUCATIONAL PURPOSES ONLY.

· ❌ Tidak untuk spam atau penyalahgunaan
· ❌ Penulis tidak bertanggung jawab atas penyalahgunaan script ini
· ✅ Gunakan dengan bijak dan sesuai Terms of Service platform
· ✅ Segala risiko ditanggung pengguna

---

<div align="center">

💖 Made with Passion by @masjjoooo

⭐ Jangan lupa kasih bintang kalau bermanfaat! ⭐

</div>

