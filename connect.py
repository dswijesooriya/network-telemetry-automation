from netmiko import ConnectHandler

# Define the connection details for your router
device = {
    "device_type": "nokia_srl",
    "host": "172.20.20.2",
    "username": "admin",
    "password": "NokiaSrl1!",
}

print("Connecting to the router...")

# Connect to the device
net_connect = ConnectHandler(**device)

print("Successfully connected!")

# Send a command and save the output
output = net_connect.send_command("show version")

print("--- ROUTER OUTPUT ---")
print(output)

# Disconnect
net_connect.disconnect()
print("Disconnected.")
