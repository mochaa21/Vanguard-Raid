# Fungsi class, print, insert, dan delete lu taruh di atas ini...

# 1. Inisialisasi Formasi Awal (Linked List)
node1 = GuildMembers("Angelica ven Ashera")
node2 = GuildMembers("Serafina de Lavilliant")
node3 = GuildMembers("Sylvie Leywin")

node1.next = node2
node2.next = node3

# 2. Radar Musuh (Array/List Biasa)
enemy_waves = ["Goblin", "Witch Cultist", "Orc", "Boss: Petelgeuse"]

# 3. Fungsi Simulasi
def raid_simulation(waves: list, vanguard_head):
    # Lakukan looping pada array 'waves'
    # Tangkap kondisi "Witch Cultist" dan "Boss: Petelgeuse"
    # Eksekusi insert_gm atau delete_gm pada vanguard_head
    # Return vanguard_head yang sudah dimodifikasi
    pass

# --- EKSEKUSI ---
print("Formasi Sebelum Raid:")
print_gm(node1)

# Jalankan simulasi
node1 = raid_simulation(enemy_waves, node1)

print("\nFormasi Setelah Raid Berakhir:")
print_gm(node1)