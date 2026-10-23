from netmiko import ConnectHandler

device = {
    "device_type": "nokia_srl",
    "host": "172.20.20.2",
    "username": "admin",
    "password": "NokiaSrl1!",
}

print("Connecting to router to back up configuration...")

net_connect = ConnectHandler(**device)

# Get the configuration
output = net_connect.send_command("info")

# Save to a file
filename = "router1_backup.txt"
with open(filename, "w") as file:
    file.write(output)

print("Backup saved to:", filename)

net_connect.disconnect()
