import json

# Fungsi untuk membaca data JSON
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Fungsi untuk mengambil daftar nama pengguna dari follower
def extract_follower_usernames(follower_data):
    follower_usernames = set()
    # Karena follower_data adalah list, kita iterasi setiap item
    for entry in follower_data:
        # Akses data dalam "string_list_data" di setiap item
        for user in entry['string_list_data']:
            follower_usernames.add(user['value'])
    return follower_usernames

# Fungsi untuk mengambil daftar nama pengguna dari following
def extract_following_usernames(following_data):
    following_usernames = {}
    # Periksa apakah following_data adalah list
    for entry in following_data['relationships_following']:
        username = entry['string_list_data'][0]['value']
        href = entry['string_list_data'][0]['href']
        following_usernames[username] = href
    return following_usernames

# Memuat data JSON
follower_data = load_json('follower.json')
following_data = load_json('following.json')

# Ekstraksi nama pengguna dari kedua file
follower_usernames = extract_follower_usernames(follower_data)
following_usernames = extract_following_usernames(following_data)

# Cari pengguna yang tidak follow back
not_following_back = {username: href for username, href in following_usernames.items() if username not in follower_usernames}

# Tampilkan hasil
print("Pengguna yang tidak follow back:")
for username, href in not_following_back.items():
    print(f"{username}: {href}")
