class  GuildMembers:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_gm(node):
    currentNode = node
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

def delete_gm(head, target_gm):
    if head.data == target_gm:
        return head.next
    
    currentNode = head
    while currentNode.next:
        if currentNode.next.data == target_gm:
            currentNode.next = currentNode.next.next
            break
        currentNode = currentNode.next
    return head

def insert_gm(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode.next == None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = GuildMembers("Angelica ven Ashera")
node2 = GuildMembers("Serafina de Lavilliant")
node3 = GuildMembers("Sylvie Leywin")

node1.next = node2
node2.next = node3

enemy_waves = ["Goblin", "Witch Cultist", "Orc", "Boss: Petelgeuse"]

def raid_simulation(waves: list, vanguard_head):
    for wave in waves:
        if wave == "Witch Cultist":
            vanguard_head = delete_gm(vanguard_head, "Serafina de Lavilliant")
        elif wave == "Boss: Petelgeuse":
            newNode = GuildMembers("Subaru")
            vanguard_head = insert_gm(vanguard_head, newNode, 1)
    return vanguard_head

# --- EKSEKUSI ---
print("Formasi Sebelum Raid:")
print_gm(node1)

# Jalankan simulasi
node1 = raid_simulation(enemy_waves, node1)

print("\nFormasi Setelah Raid Berakhir:")
print_gm(node1)