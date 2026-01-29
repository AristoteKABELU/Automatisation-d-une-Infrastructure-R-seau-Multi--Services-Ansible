from netmiko import ConnectHandler

# Définition du routeur
cisco1 = {
    "device_type": "cisco_ios",
    "host": "192.168.122.18",  # IP du routeur c7200 sur VMnet1
    "username": "cisco",
    "password": "cisco",
}

# Connexion au routeur
net_connect = ConnectHandler(**cisco1)

# Afficher le running-config
print("=== Running Config ===")
running_config = net_connect.send_command("show running-config")
print(running_config)

# Afficher les interfaces Up
print("\n=== Interfaces Up ===")
interfaces_up = net_connect.send_command("show ip interface brief | include up")
print(interfaces_up)

# Afficher les interfaces Down
print("\n=== Interfaces Down ===")
interfaces_down = net_connect.send_command("show ip interface brief | include administratively down")
print(interfaces_down)

# Compter FastEthernet et GigabitEthernet
print("\n=== Count Interfaces ===")
interfaces = net_connect.send_command("show ip interface brief")
fast_count = interfaces.count("FastEthernet")
gig_count = interfaces.count("GigabitEthernet")
print(f"FastEthernet: {fast_count}, GigabitEthernet: {gig_count}")

# Liste des réseaux accessibles
print("\n=== Routes ===")
routes = net_connect.send_command("show ip route")
print(routes)

# Déconnexion
net_connect.disconnect()
