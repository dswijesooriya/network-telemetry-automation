from netmiko import ConnectHandler
import time

# A list of routers to back up
routers = ["172.20.20.2", "172.20.20.99"] # .99 is fake, to test the error handling

for ip in routers:
    print(f"\n--- Starting backup for {ip} ---")
    
    device = {
        "device_type": "nokia_srl",
        "host": ip,
        "username": "admin",
        "password": "NokiaSrl1!",
        "timeout": 5,  # Only wait 5 seconds before giving up
    }
    
    try:
        # Try to connect
        net_connect = ConnectHandler(**device)
        
        # Run the command
        output = net_connect.send_command("info / system name")
        
        # Save to a file named after the IP
        filename = f"backup_{ip}.txt"
        with open(filename, "w") as file:
            file.write(output)
            
        print(f"✅ Success: Saved {filename}")
        
        net_connect.disconnect()
        
    except Exception as e:
        # If anything fails, print the error but KEEP GOING to the next router
        print(f"❌ Failed to connect to {ip}.")
        print(f"Error message: {e}")

print("\n--- Automation Complete ---")
