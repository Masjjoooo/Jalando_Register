import os
import sys
import json
import time
import random
import requests

# ==================== WARNA ANSI ====================
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"

if os.name == "nt":
    os.system("")

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def loading(text="Memproses", duration=1.0):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        sys.stdout.write(f"\r{C.CYAN}{frames[i % len(frames)]} {text}...{C.RESET}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\r" + " " * (len(text) + 20) + "\r")

def banner():
    clear()
    print(C.CYAN + C.BOLD + r"""
   ███████╗ █████╗ ██╗      █████╗ ███╗   ██╗██████╗  ██████╗ 
   ╚══███╔╝██╔══██╗██║     ██╔══██╗████╗  ██║██╔══██╗██╔═══██╗
     ███╔╝ ███████║██║     ███████║██╔██╗ ██║██║  ██║██║   ██║
    ███╔╝  ██╔══██║██║     ██╔══██║██║╚██╗██║██║  ██║██║   ██║
   ███████╗██║  ██║███████╗██║  ██║██║ ╚████║██████╔╝╚██████╔╝
   ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ 
    """ + C.RESET)
    print(C.YELLOW + C.BOLD + "        ╔══════════════════════════════════════════╗")
    print(C.YELLOW + C.BOLD + "        ║   AUTO REGISTER ACCOUNT  •  © masjjoooo       ║")
    print(C.YELLOW + C.BOLD + "        ╚══════════════════════════════════════════╝" + C.RESET)
    print()

# ==================== SESSION DATA (HARDCODE dari snipeet kamu) ====================
CSRF       = "c12a14a5-20c2-4ee5-b4ef-891d0c3fd0be"
FLOW_ID    = "rendering-engine-48775e04-3e54-4b09-96a5-720630f0a2ba"
REQUEST_ID = "jlp0vovSDvlrGaHp:201e694d-00f3-4837-9a59-8e61efde80e5:klp0vovSDvlrGaHp"

REFERER = ("https://accounts.zalando.com/authenticate?redirect_uri=https%3A%2F%2Fwww.zalando.es%2Fsso%2Fcallback"
           "&client_id=fashion-store-web&response_type=code"
           "&request_id=klp0vovSDvlrGaHp%3A201e694d-00f3-4837-9a59-8e61efde80e5%3Aklp0vovSDvlrGaHp"
           "&nonce=19e97e35-87c0-48dd-adeb-4ede9dacbb4e"
           "&state=eyJvcmlnaW5hbF9yZXF1ZXN0X3VyaSI6Ii9teWFjY291bnQvPyIsInRzIjoiMjAyNi0wOS0xOFQwMjoxMjoyNFoifQ%3D%3D"
           "&premise=unified_sso_ui&scope=openid&ui_locales=es-ES"
           "&zalando_client_id=201e694d-00f3-4837-9a59-8e61efde80e5"
           "&tc=zcid%3A201e694d-00f3-4837-9a59-8e61efde80e5%2Cpf%3Aweb"
           "&appearance=system&sales_channel=1e161d6e-0427-4cfc-a357-e2b501188a15"
           "&client_country=ES&client_category=fs")

COOKIE = ("X-Zalando-Client-Id=201e694d-00f3-4837-9a59-8e61efde80e5; "
          "bm_so=0E87C08E0830B93ED73A3574240B77AD8F8D122A09ECFFB216D878A43B86D32C~YAAQEtkRAq+bCqegAQAAPlRJsglmwyhYKqej/8D3BoteUFBy3w/MxZtmwkVn1tYP0Ijdc3G1yY+6HO3ifo8GuByxxJIelRB7U7+TSKEGEwlkBedtTq3oLkyqSqxf5SxknRgtjB3ws7y2bUtzj/NPe8URTdChexW7a9jRmPf2AXOxrUclSrdofCKZQglkfoZ3bchEqwpQuectlHvZfWas06w7cNGIWjJim3FHevqaJO5FHnHYjkREYGYX+Qu+ejLt7JgshOYoQmw1r8tkEZr6VGWY+r3oma/dJ5RRiph/VxKY/1QNcho9+HP6/m/mvDMWOu21Ym8jEpQNK7UhzDTplnUrN+4AwYPX3ys8O0MIxeXB+8ERpeRbGaKl97Z2FTSgNlGxpOyW5d8fhfOLNhtWD7WGyo5NYAoyLZ+q2NVTyjMCycVh10IaGjRrEsX3CUVfqiQYkyNCSdIisdPXYxdTflcXf6ILCvpdr/dsbg==~8; "
          "csrf-token=c12a14a5-20c2-4ee5-b4ef-891d0c3fd0be; "
          "bm_lso=0E87C08E0830B93ED73A3574240B77AD8F8D122A09ECFFB216D878A43B86D32C~YAAQEtkRAq+bCqegAQAAPlRJsglmwyhYKqej/8D3BoteUFBy3w/MxZtmwkVn1tYP0Ijdc3G1yY+6HO3ifo8GuByxxJIelRB7U7+TSKEGEwlkBedtTq3oLkyqSqxf5SxknRgtjB3ws7y2bUtzj/NPe8URTdChexW7a9jRmPf2AXOxrUclSrdofCKZQglkfoZ3bchEqwpQuectlHvZfWas06w7cNGIWjJim3FHevqaJO5FHnHYjkREYGYX+Qu+ejLt7JgshOYoQmw1r8tkEZr6VGWY+r3oma/dJ5RRiph/VxKY/1QNcho9+HP6/m/mvDMWOu21Ym8jEpQNK7UhzDTplnUrN+4AwYPX3ys8O0MIxeXB+8ERpeRbGaKl97Z2FTSgNlGxpOyW5d8fhfOLNhtWD7WGyo5NYAoyLZ+q2NVTyjMCycVh10IaGjRrEsX3CUVfqiQYkyNCSdIisdPXYxdTflcXf6ILCvpdr/dsbg==~8~1789697545954; "
          "g_state={\"i_l\":0,\"i_ll\":1789697546272,\"i_b\":\"aYSu4NC9mQN4qrNJWweHlWEl8EiWvORi7j/CIdO/QWU\",\"i_e\":{\"enable_itp_optimization\":24},\"i_et\":1789697546272}; "
          "ak_bmsc=477A31CD1C7BF4831CB3207F3A8D84A0~000000000000000000000000000000~YAAQEtkRAgucCqegAQAANmFJsgHo2MI//JrP8qd/KplYy/7y8O87u8kzF0GnlikhN3qTkjmU8s7yOeguMc0mUElPik1TSXgb9I/PuL1F2x+dMxrTqHMgZJb4B7xD15ahD2Mtm4tEiaaKGTWRtA+OoyJnAU4Cftf8f82LIpzkXPzD7nFSvr07z9xMqi+c2nkfYrIJUjJHxOwJx5imxWa1elz/TGdBQbzlUAsivQ3DC5fgGeryDpXzlgc7/iTvT78HI36SRnrfsi6uUiHcTrW2jB10Yk7v/ReBDazXzGBE7bov/17L2Ir0OIeln4j0pLsy7N9aDEFqGYZnkHeEm5ZYnP4JhuOy5MXwo8OS7Jkq06XsKOL7ruWkC3Wu168BwWuYNq949xj7TdbvaFoGFlBb1OIzchWhSn+lvk0ouB76CmvYVVlYx48s3tSsc9tiBYbKJ7ZxWv96QonICl/H7BK1; "
          "bm_s=YAAQEtkRAsycCqegAQAAFIJJsgbdMNu0t6fduzU5+c5I8OFkdwogoFGqK1cbel0MqvhCd8mCqUlFR/v3UvVbrCGkS6kExBdDC4VP8l0fHNZPp9kWaddFQCON+tq/MwaxBTmenTnUyKcIRRpxGgPzkZgHvcH68avzq7W3V1HYbZpp/hRh+Ee3mzUvlgRKzmH07eL5VkKQd9v2P2vH/ThSkdgdALB+Q6TrqtLPZxwigx9WrxPMt/xgHeG54x+hYTjyMagK6At7ZgN5qY4WamJnG8mvAsJSEm+omEGJBgd/53S150gHVERrB3o/nwYAoa1FG3FuAJ3m6/s4UMq1XZamrLtL9KrA+sLQ1jdkzEVqTBgYsh9iPJFBNsf5ERex1wr7CfgrhqvJjxHnssNwX7Vg4oYnKOWaMIKLwP89uD/CTFIGKPbkk8agu1A3Vq0TF4r0QHsKLd5cZBm9m2Hv8aQ0smXI3A79seHHEyMg9UfHwC3fsBtUjtEQnbmo1caPu/I0SdsmekzdcwGfUtdat+qmGb+8QYVQ20fL4W2M3ud9PWPdFcRLDVrqE5sm249WaVO1ObdZeR7Hlg9oDW91UF0j1QYNBxQcVQztC8k7tMA8dEC39PI3oMid7ahQhuApyIi50GTlnf4yzGhnfmlkJeCs2bVcqVLzIUuYaeHbRZ0T6Z7jesO4UbR6/bdoh7PBytp1KepfmCuxzIFEw+LiNVgQ4Eu/IITZWNJ/4+X81/dzK3iEL0XcIN5SoEcgzEzNRjXW/7Ir2wQDLPARJ7RhV1eJTod2iKZb8MC91PG0VRyNl0gUNVkZFq3nM/+VgBM0ubfnNFPYFr4qCLRV7Qbl1H/j/bTaC1wpxDcCVd3QwxzkWtvB6PsPO3fvIbdGnmqzlnf+djr6Vz97tNtQEAGmXiv6vpLyjZuDXZ/qLtPIkGMeTk71gWOri9O01ZLAxDRDy2EE1my4yzwvaHQ0Kif1vo0gEAyJsiYVmjVSzBdedQH4LUKPn4ZiaNCd+ce56nbRZ3HfeKrSSYPC+OLuZWv0OG+wYaslN2vz94G/ISgksGlBldrAsMPoF2wqJjGQcWS0W5uMAK41kmBmiB70K15xy4NemCGD+7BUPslAViSdqTKWMOgDdoLZ4LZa3l2vSxUnP7IEsXyP/iiUVRcl3jNRUCBlrg==; "
          "bm_sz=9922C61D5A70392F0C1835EE3BD6010F~YAAQEtkRAs6cCqegAQAAFIJJsgFjRd0BmZGeClkhgn7Bpbmz1L20C4rjw03vtNxA8cR9euN3uYybH2o3Fao8KVO9JCv0SW+LiNYfngVMjovh4t+IZk/KOH2xfFPixDRBRpOK1IP6rFN2B548lJVlv8F3TPlJjubBWRpLi5fS1aNFPEq6Ye0ZYTUgAX8xMbhgLkHYje5IPYQUx0F/biOAnWHf7UKHmkkTcCrdC2zzB5MRZ2LGZsU6qFz8tVOKPZnkqrwqhwOJb9QMAXuXJMkHr/SWHvaWFncJKDF6areiBpfhH9qR4fJg59W1u+5zG+i3VzpX91RMGJRu+X57f7XUAu3+Vy9QKtpIrixCZQY9zB3odZr8LsU/i880gNR4LY42F+ptRv2/vZ+bzzW4fTsOTkH/Jm9OxZ7NsUijPLLctI6US+vqe1WM+Qq4K/dLpZPtrg==~4405560~3294007; "
          "_abck=E9A40E74F6EF5ACF73A06DABF72CD471~0~YAAQEtkRAlOeCqegAQAANtJJshAHQlockfCENzw++v95UXUoy3ZlL+NfSJMYdWnma/OSs/Bvzf9XIoYj0lmToaib1rN/zMhIePk2Mve5n0ne82FSUKhU1k5L8V/XQY7AoYKvRuNtITaiqITKC+TCY36B1iT6X1ne8K6uZEfGRH1BD0cfx3eoQvndNjRnxYPVvN1DNuC77mJaiAK/qquQIAJqvd6Ylwb6QJiQEvXD26kQQmrgGfWnxfeOlD5D4HzcDQKRNGNKIKaMCiUxJ/k2EDw1N/MG1OGT+JMbYMpsIABGWrBH6bkk9/Tbhmyjf8RvzlBVYNLlT4MqJwWqeFhMRXF2MC1y9w4JGCjtq7fsqrl3YFqGZsVsSwO+TBTJ2J99X9aE0Y6I1G4/FwZNdLW1mdBbD32dBhvTsw1QvPaoIBiaxS9evYy5uSHH9nZlRH7UUrfjuNtmqeNmW8xJsgUeNNFk+zfDDnc+p6pv/EGiZL26umuBsxjsupIzSHkYHNx8xDKKHzpxDLP2peLhBADu/mpPE59N9uTL25GdZXKTQaxCCY7QiOEz10GaOHzAhAKdjozdHP9U5k7vqzxLMiY9A/DPokH/40TdI0PTPU0rwgN+SLyX9seyRbl8myhc7ncnk3r0r/rB4bh3RSL6C800lV5WayysOrgwOtV8OFgJg551dV9tk6P2NwsRm5tWw9vqiiPuzZIv/OeLaDAupMr7cSPXDdq48JdoOXx+YoMPq71tFZf6V7VT4X7ARYysOjH36Abbbvx9e/67iTFPBOvUhuUxlDrgyfL413mMpVtf78F+94cOhtlU59QfUcfgLAghoFkLXcn79naOoa3+I4kFHzZh8yoRgyLYz+uYSjGQ7G7MQRtE8p8WzVIgxgXQxPfkPev14DJdF7wtPYRHAd/Q8Wt9lr2EWPbbepRbwU9zlo7XFYUjvoLnJCcuOQQRGpgIs4ofSd+nh8sbEppJ4Cnt4sE=~-1~-1~1789701177~AAQAAAAG%2f%2f%2f%2f%2f9frc7hvGfRc2EFukMQ+T5jzcsPgowgs4YK9ogGI4i6+2kODsqKBaj8MMjTYBEosjT9M7%2fCSCO3ExjPr%2fe1MEXbG+7iUTKH2NNAK~-1; "
          "bm_sv=5CE4200106E75A71C0B6FB71D34FAE21~YAAQEtkRAlWeCqegAQAAANNJsgFrsxUcuJ1Ookc1VuxsR8onqzgO5FCac2+PgW0dcsWWuRd7X+q9YrYssPlZ3D5GS2VmVfEzOc5N3GYla9PFuHbgzd3EBAQJiWTBl9NKVgNtLKCebJIt4Ns2NVQy7Ie3Pc9/o9CDCRYm3B+x+CVggZel0x7VHriD8iQfsvCtoRPUCHEKU/Fl6pfN3dQvwAS0AHM3V8QqEJXXKW8VRbgCOUna1nQ4HEL1gKmtxfFlEL8=~1")

# ==================== FUNGSI ====================
def random_name():
    first_names = [
        "Andi","Budi","Citra","Dewi","Eko","Fajar","Gita","Hadi","Indra","Joko",
        "Kartika","Lina","Maya","Nanda","Oki","Putri","Rizky","Sari","Tono","Umar",
        "Vina","Wahyu","Yudi","Zahra","Adit","Bayu","Cinta","Dian","Erwin","Fitri"
    ]
    last_names = [
        "Santoso","Wijaya","Pratama","Saputra","Nugroho","Kurniawan","Hidayat",
        "Setiawan","Ramadhan","Maulana","Permana","Firmansyah","Halim","Gunawan",
        "Susanto","Hartono","Iskandar","Lestari","Anggraini","Puspita"
    ]
    return random.choice(first_names), random.choice(last_names)

def register(email, secret, first_name, last_name):
    url = "https://accounts.zalando.com/api/sso/registrations"

    payload = {
        "email": email,
        "secret": secret,
        "first_name": first_name,
        "last_name": last_name,
        "accepts_terms_and_conditions": True,
        "authentication_request": {
            "client_id": "fashion-store-web",
            "request_id": REQUEST_ID,
            "redirect_uri": "https://www.zalando.es/sso/callback",
            "ui_locales": "es-ES",
            "tc": "zcid:201e694d-00f3-4837-9a59-8e61efde80e5,pf:web"
        }
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 15; TECNO KM4 Build/AP3A.240905.015.A2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.7922.202 Mobile Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'Content-Type': "application/json",
        'ot-tracer-spanid': "e9608e1ad85b228b",
        'sec-ch-ua-platform': "\"Android\"",
        'x-csrf-token': CSRF,
        'x-flow-id': FLOW_ID,
        'x-xsrf-token': "",
        'sec-ch-ua': "\"Not=A?Brand\";v=\"99\", \"Android WebView\";v=\"151\", \"Chromium\";v=\"151\"",
        'sec-ch-ua-mobile': "?1",
        'ot-tracer-sampled': "true",
        'ot-tracer-traceid': "82f333547ee3f575",
        'viewport-width': "411",
        'dpr': "1.75",
        'origin': "https://accounts.zalando.com",
        'x-requested-with': "mark.via.gp",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': REFERER,
        'accept-language': "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        'priority': "u=1, i",
        'Cookie': COOKIE,
    }

    try:
        r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=30)
        return r.status_code, r.text
    except Exception as e:
        return None, str(e)

def save_account(email, secret, first_name, last_name, status):
    with open("akun.txt", "a", encoding="utf-8") as f:
        f.write(f"{email}|{secret}|{first_name} {last_name}|{status}\n")

# ==================== MAIN ====================
def main():
    banner()

    print(C.BOLD + C.CYAN + "  ┌─[ INPUT DATA ]─────────────────────────────┐" + C.RESET)
    email  = input(C.GREEN + "  │ " + C.WHITE + "Email  : " + C.RESET).strip()
    secret = input(C.GREEN + "  │ " + C.WHITE + "Secret : " + C.RESET).strip()
    while True:
        try:
            jumlah = int(input(C.GREEN + "  │ " + C.WHITE + "Jumlah akun : " + C.RESET).strip())
            if jumlah > 0:
                break
        except ValueError:
            pass
        print(C.RED + "  │ [!] Masukkan angka > 0" + C.RESET)
    print(C.BOLD + C.CYAN + "  └────────────────────────────────────────────┘" + C.RESET)
    print()

    print(C.YELLOW + f"  [i] Akan membuat {jumlah} akun dari base: {email}" + C.RESET)
    print(C.YELLOW + f"  [i] Nama depan & belakang akan diacak otomatis" + C.RESET)
    print(C.YELLOW + f"  [i] Hasil disimpan ke: akun.txt" + C.RESET)
    print()

    if input(C.BOLD + C.WHITE + "  Lanjutkan? (y/n) : " + C.RESET).strip().lower() != "y":
        print(C.RED + "\n  [!] Dibatalkan." + C.RESET)
        return

    print()
    sukses, gagal = 0, 0

    if "@" in email:
        local, domain = email.split("@", 1)
    else:
        local, domain = email, "mail.com"

    for i in range(1, jumlah + 1):
        current_email = email if jumlah == 1 else f"{local}+{i}@{domain}"
        first, last = random_name()

        print(C.BOLD + C.CYAN + f"  ┌─[ AKUN {i}/{jumlah} ]─────────────────────────" + C.RESET)
        print(C.GREEN + f"  │ Email  : " + C.WHITE + current_email + C.RESET)
        print(C.GREEN + f"  │ Nama   : " + C.WHITE + f"{first} {last}" + C.RESET)

        loading(f"Mengirim request akun {i}", 1.0)
        status_code, resp = register(current_email, secret, first, last)

        if status_code and 200 <= status_code < 300:
            print(C.GREEN + f"  │ Status : ✔ SUKSES ({status_code})" + C.RESET)
            save_account(current_email, secret, first, last, "SUCCESS")
            sukses += 1
        else:
            print(C.RED + f"  │ Status : ✘ GAGAL ({status_code})" + C.RESET)
            msg = resp[:200].replace("\n", " ") if isinstance(resp, str) else "-"
            print(C.DIM + C.RED + f"  │ Resp   : {msg}" + C.RESET)
            save_account(current_email, secret, first, last, f"FAILED-{status_code}")
            gagal += 1

        print(C.BOLD + C.CYAN + "  └──────────────────────────────────────────" + C.RESET)
        print()
        time.sleep(0.4)

    print(C.BOLD + C.YELLOW + "  ╔══════════════════════════════════════════╗")
    print(C.BOLD + C.YELLOW + "  ║              RINGKASAN HASIL             ║")
    print(C.BOLD + C.YELLOW + "  ╚══════════════════════════════════════════╝" + C.RESET)
    print(C.GREEN + f"  ✔ Sukses : {sukses}" + C.RESET)
    print(C.RED   + f"  ✘ Gagal  : {gagal}"  + C.RESET)
    print(C.CYAN  + f"  📁 File   : akun.txt"    + C.RESET)
    print()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(C.RED + "\n\n  [!] Dihentikan user." + C.RESET)
