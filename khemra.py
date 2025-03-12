import os
import subprocess
import requests
import pyfiglet
from colorama import Fore, Style, init

# Initialize colorama for colored output
init()

# Display ASCII Art Title
def display_banner():
    ascii_banner = pyfiglet.figlet_format("VEASNA TOOL")
    print(Fore.GREEN + ascii_banner + Style.RESET_ALL)
    print(Fore.CYAN + "--------------------------------------------------")
    print("        VEASNA's LINUX INFORMATION TOOL")
    print("--------------------------------------------------" + Style.RESET_ALL)

# Function to check system information
def check_system_info():
    print(Fore.YELLOW + "\n======= SYSTEM INFORMATION =======\n" + Style.RESET_ALL)
    os.system("uname -a")  # Kernel and OS info
    os.system("lsb_release -a")  # Distro info

# Function to check IP addresses
def check_ip():
    print(Fore.YELLOW + "\n======= NETWORK INFORMATION =======\n" + Style.RESET_ALL)
    
    # Get local IP
    print(Fore.CYAN + "Local IP Addresses:" + Style.RESET_ALL)
    os.system("ip a | grep 'inet ' | awk '{print $2}'")

    # Get external IP
    try:
        external_ip = requests.get("https://api64.ipify.org?format=text").text
        print(Fore.GREEN + f"External IP: {external_ip}\n" + Style.RESET_ALL)
    except:
        print(Fore.RED + "Failed to retrieve external IP\n" + Style.RESET_ALL)

# Function to check MAC address
def check_mac():
    print(Fore.YELLOW + "\n======= MAC ADDRESS =======\n" + Style.RESET_ALL)
    os.system("ip link show | grep 'link/ether'")

# Function to check saved WiFi networks
def check_wifi():
    print(Fore.YELLOW + "\n======= SAVED WIFI NETWORKS =======\n" + Style.RESET_ALL)
    os.system("nmcli connection show")

    wifi_name = input(Fore.CYAN + "Enter WiFi name to view password: " + Style.RESET_ALL)
    os.system(f"nmcli connection show '{wifi_name}' | grep 'wifi-sec.psk'")

# Function to check another IP address (Geolocation)
def check_other_ip():
    ip = input(Fore.CYAN + "Enter IP address to check: " + Style.RESET_ALL)
    print(Fore.YELLOW + f"\n======= INFORMATION FOR IP: {ip} =======\n" + Style.RESET_ALL)
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        
        if data['status'] == 'fail':
            print(Fore.RED + f"Failed to retrieve data for IP: {ip}\n" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + f"IP: {data['query']}")
            print(f"Location: {data['city']}, {data['country']}")
            print(f"Latitude/Longitude: {data['lat']}, {data['lon']}")
            print(f"ISP: {data['isp']}")
            print(f"Organization: {data['org']}\n" + Style.RESET_ALL)
    except:
        print(Fore.RED + "Failed to retrieve geolocation information.\n" + Style.RESET_ALL)

# Function to check disk usage
def check_disk_usage():
    print(Fore.YELLOW + "\n======= DISK USAGE =======\n" + Style.RESET_ALL)
    os.system("df -h")

# Function to check running processes
def check_running_processes():
    print(Fore.YELLOW + "\n======= RUNNING PROCESSES =======\n" + Style.RESET_ALL)
    os.system("ps aux")

# Function to check listening ports
def check_listening_ports():
    print(Fore.YELLOW + "\n======= LISTENING PORTS =======\n" + Style.RESET_ALL)
    os.system("ss -tuln")

# Function to check memory usage
def check_memory_usage():
    print(Fore.YELLOW + "\n======= MEMORY USAGE =======\n" + Style.RESET_ALL)
    os.system("free -h")

# Function to check system uptime
def check_uptime():
    print(Fore.YELLOW + "\n======= SYSTEM UPTIME =======\n" + Style.RESET_ALL)
    os.system("uptime")

# Function to run Wifite
def run_wifite():
    print(Fore.YELLOW + "\n======= RUNNING WIFITE =======\n" + Style.RESET_ALL)
    os.system("sudo wifite")

# Function to run Aircrack-ng
def run_aircrack_ng():
    print(Fore.YELLOW + "\n======= RUNNING AIRCRACK-NG =======\n" + Style.RESET_ALL)
    interface = input(Fore.CYAN + "Enter wireless interface (e.g., wlan0): " + Style.RESET_ALL)
    capture_file = input(Fore.CYAN + "Enter the capture file (e.g., capture.cap): " + Style.RESET_ALL)
    os.system(f"sudo aircrack-ng -w /usr/share/wordlists/rockyou.txt {capture_file} -b <target MAC>")

# Function to run MDK3 for Deauthentication
def run_mdk3():
    print(Fore.YELLOW + "\n======= RUNNING MDK3 DEAUTH ATTACK =======\n" + Style.RESET_ALL)
    interface = input(Fore.CYAN + "Enter wireless interface (e.g., wlan0): " + Style.RESET_ALL)
    target_mac = input(Fore.CYAN + "Enter target MAC address (e.g., 00:11:22:33:44:55): " + Style.RESET_ALL)
    os.system(f"sudo mdk3 {interface} d -a {target_mac}")

# Main Menu
def main():
    while True:
        os.system("clear")  # Clear screen for Linux
        display_banner()
        print(Fore.CYAN + "[1] Check System Information")
        print("[2] Check IP Addresses (Local & External)")
        print("[3] Check MAC Address")
        print("[4] Check Saved WiFi Networks & Passwords")
        print("[5] Check Information for Another IP")
        print("[6] Check Disk Usage")
        print("[7] Check Running Processes")
        print("[8] Check Listening Ports")
        print("[9] Check Memory Usage")
        print("[10] Check System Uptime")
        print("[11] Run Wifite (WiFi Cracking)")
        print("[12] Run Aircrack-ng (WiFi Cracking)")
        print("[13] Run MDK3 (Deauth Attack)")
        print("[14] Exit" + Style.RESET_ALL)
        
        choice = input(Fore.YELLOW + "Enter your choice: " + Style.RESET_ALL)

        if choice == '1':
            check_system_info()
        elif choice == '2':
            check_ip()
        elif choice == '3':
            check_mac()
        elif choice == '4':
            check_wifi()
        elif choice == '5':
            check_other_ip()
        elif choice == '6':
            check_disk_usage()
        elif choice == '7':
            check_running_processes()
        elif choice == '8':
            check_listening_ports()
        elif choice == '9':
            check_memory_usage()
        elif choice == '10':
            check_uptime()
        elif choice == '11':
            run_wifite()
        elif choice == '12':
            run_aircrack_ng()
        elif choice == '13':
            run_mdk3()
        elif choice == '14':
            print(Fore.RED + "\nExiting the tool...\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "\nInvalid choice! Please enter a number from 1 to 14.\n" + Style.RESET_ALL)

        input(Fore.CYAN + "\nPress Enter to continue..." + Style.RESET_ALL)

# Run the program
if __name__ == "__main__":
    main()
