import requests
import json
from pystyle import Colors, Center, Colorate, Write

banner = Center.XCenter("""
██╗██████╗░      ░██████╗░███████╗░█████╗░██╗░░░░░░█████╗░░█████╗░░█████╗░████████╗███████╗
██║██╔══██╗      ██╔════╝░██╔════╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║██████╔╝      ██║░░██╗░█████╗░░██║░░██║██║░░░░░██║░░██║██║░░╚═╝███████║░░░██║░░░█████╗░░
██║██╔═══╝░      ██║░░╚██╗██╔══╝░░██║░░██║██║░░░░░██║░░██║██║░░██╗██╔══██║░░░██║░░░██╔══╝░░
██║██║░░░░░      ╚██████╔╝███████╗╚█████╔╝███████╗╚█████╔╝╚█████╔╝██║░░██║░░░██║░░░███████╗
╚═╝╚═╝░░░░░      ░╚═════╝░╚══════╝░╚════╝░╚══════╝░╚════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝
                     Made by * always#0001\n\n | Copied Banner from https://github.com/WebUwU/SigmaNuker
""")
print(Colorate.Vertical(Colors.blue_to_purple, banner, 2))

ip_address = input('Enter an IP address to geolocate: ')


url = f"https://ip-reputation-geoip-and-detect-vpn.p.rapidapi.com/?ip={ip_address}"

headers = {
    "X-RapidAPI-Key": "your-api-key-here",
    "X-RapidAPI-Host": "ip-reputation-geoip-and-detect-vpn.p.rapidapi.com"
}


try:
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    
    if not data:
        raise Exception(f"No data found for IP address {ip_address}")
    
    
    with open(f"{ip_address}.json", "w") as f:
        json.dump(data, f, indent=4)
    
    
    print(f"IP Address: {data['ip']}")
    print(f"City: {data['city']}")
    print(f"Country: {data['country']}")
    print(f"Continent: {data['continent']}")
    print(f"Latitude: {data['latitude']}")
    print(f"Longitude: {data['longitude']}")
    print(f"Timezone: {data['time_zone']}")
    print(f"Postal Code: {data['postal_code']}")

except Exception as e:
    
    with open("error.txt", "a") as f:
        f.write(str(e))
        f.write("\n")
    print(f"Error occurred while processing IP address {ip_address}: {str(e)}")
