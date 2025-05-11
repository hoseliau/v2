import re

# File paths
canonical_file = "/home/zhunl/welcome/v1/golang/canonical.txt"  # File yang berisi domain baru
go_file = "golang/main.go"  # File Go yang akan dimodifikasi

# Step 1: Baca file canonical.txt dan ekstrak domain baru
try:
    with open(canonical_file, "r") as file:
        canonical_content = file.readlines()
except FileNotFoundError:
    print(f"File {canonical_file} tidak ditemukan.")
    exit()

# Bersihkan data dan simpan sebagai list
new_domains = [line.strip() for line in canonical_content if line.strip()]

if not new_domains:
    print("Tidak ada domain baru yang ditemukan di canonical.txt.")
    exit()

# Step 2: Baca file main.go
try:
    with open(go_file, "r") as file:
        go_content = file.read()
except FileNotFoundError:
    print(f"File {go_file} tidak ditemukan.")
    exit()

# Step 3: Ganti placeholder "##########" dengan domain baru
placeholder = "##########"
replaced_count = 0  # Hitung jumlah domain yang berhasil diganti

for new_domain in new_domains:
    # Ganti hanya jika placeholder masih ada
    if placeholder in go_content:
        go_content = go_content.replace(placeholder, new_domain, 1)
        replaced_count += 1
    else:
        print("Tidak ada lagi placeholder yang tersisa untuk diganti.")
        break

# Step 4: Tulis ulang file main.go
with open(go_file, "w") as file:
    file.write(go_content)

print(f"CONGRATULATION! {replaced_count} URL berhasil diganti di {go_file}.")