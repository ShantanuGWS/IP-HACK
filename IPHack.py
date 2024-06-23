
import time
import colorama
import os
import sys

logo = """     
                ██████╗ ██╗    ██╗███████╗     ██╗  ██╗
               ██╔════╝ ██║    ██║██╔════╝     ╚██╗██╔╝ 
               ██║  ███╗██║ █╗ ██║███████╗█████╗╚███╔╝ 
               ██║   ██║██║███╗██║╚════██║╚════╝██╔██╗ 
               ╚██████╔╝╚███╔███╔╝███████║     ██╔╝ ██╗ 
                ╚═════╝  ╚══╝╚══╝ ╚══════╝     ╚═╝  ╚═╝ 

"""

red = "\033[91;1m"
reset = "\033[0m"
green = "\033[92;1m"
cyan = "\033[96;1m"
yellow = "\033[93;1m"
magenta = "\033[95;1m"
blue = "\033[94;1m"
white = "\033[97;1m"
blink = "\033[5m"

os.system("clear")

def anime(text):
  for txt in text:
    sys.stdout.write(txt)
    sys.stdout.flush()
    time.sleep(0.03)

golo = colorama.Fore.YELLOW + logo
anime(golo)

sp = ">> Script By Shantanu <<"
name = f"\t\t       {colorama.Back.RED + colorama.Fore.WHITE}{sp}"
anime(name)
print(colorama.Back.RESET)
print(colorama.Fore.RESET)

ghub = colorama.Back.BLACK +  ">> \033[97;1mOur More Tools On GitHub : \033[94;1mShantanuGWS\033[97;1m << "
anime(f"\t      {ghub}")
print(colorama.Back.RESET)

import ipinfo

def get_user_info_by_ip(ip_address, token):
    time.sleep(2)
    # Initialize the ipinfo handler with the token
    handler = ipinfo.getHandler(token)
    
    # Get details for the provided IP address
    details = handler.getDetails(ip_address)
    
    # Print the details
    user_info = {
        "IP": details.ip,
        "City": details.city,
        "Region": details.region,
        "Country": details.country,
        "Location": details.loc,
        "Postal": details.postal,
        "Timezone": details.timezone,
        "Organization": details.org,
    }
    
    return user_info

if __name__ == "__main__":
    # Replace 'YOUR_ACCESS_TOKEN' with your actual token
    access_token = 'a58e4d78308c99'

    print("\n\n\n\033[96;1m[00]\033[5m exit\033[0m\n")

    # Replace '8.8.8.8' with the IP address you want to query
    try:   
       ip_to_query = input("\033[92;1m[+]\033[93;1m Enter IP Address:\033[0m")


       if ip_to_query == "00":
          endmsg =colorama.Fore.GREEN +  "\nThanks For Using Our Tool\nDon't Forget To Subscribe Our YT Channel 'DCs Radio YT' "
          anime(endmsg)
          print(colorama.Fore.RESET)
          time.sleep(1)
          exit()
    
       info = get_user_info_by_ip(ip_to_query, access_token)
    
       for key, value in info.items():
           print(f"\n\033[92;1m{key}\033[0m: {value}")

    except:
         print(colorama.Fore.RED + "\nSome Error Occured")
         print("Please Restart This Tool")
         print(colorama.Fore.RESET) 
