import pathlib
import threading
import os
import time
import datetime
import json,sys,queue
from rich.panel import Panel
from rich import print as cetak
exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 98, 97, 115, 101, 54, 52, 34, 41, 46, 98, 54, 52, 100, 101, 99, 111, 100, 101],chr))(b'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'))))
def menu(banner,modul,modulesl):
    hijau1 = "\033[1;92m"  # Terang
    kuning1 = "\033[1;93m"  # Terang
    putih1 = "\033[1;97m"  # Terang
    merah1 = "\033[1;91m"  # Terang
    biru1 = "\033[1;94m"  # Terang
    Bits_Family ={
    "btccanyon":modul.btccanyon,
    "claimbits":modul.claimbits,
    "claimlite":modul.claimlite,
    "ltchunt":modul.ltchunt,
    "rushbitcoin":modul.rushbitcoin,
    #"earn-crypto_co":modul.earn_crypto,
    "earnbits_io":modul.earnbits,
    "faucetpayz":modul.faucetpayz,
    "nevcoin":modul.nevcoin,
    "proearn.site":modul.proearn,
    "litecoinbits":modul.litecoinbits,
    "ptctask":modul.ptctask,
    "webshort":modul.webshort,
    "lazyfaucet":modul.lazyfaucet,
    }
    micin = {
    "coinfola":modul.coinfola,
    "earnsolana":modul.earnsolana,
    "faucetspeedbtc":modul.faucetspeedbtc,
    "earnrub_pw":modul.earnrub_pw,
    "instanfaucet_xyz":modul.instanfaucet_xyz,
    "whoopyrewards":modul.whoopyrewards,
    "paidlink":modul.paidlink,
    "chillfaucet":modul.chillfaucet,
    "keforcash":modul.keforcash,
    "claimcoin_in":modul.claimcoin_in,
    "coinpayz":modul.coinpayz,
    "wildfaucet":modul.wildfaucet,
    "liteearn":modul.liteearn,
    #"dotfaucet":modul.dotfaucet,
    }
    menu={
      "settings":None,
      "bits family":None,
      "micin family":None
    }
    menu_dict = list(Bits_Family.items()) + list(micin.items())
    tele=None
    fl=sys.argv[0]
    os.system("clear")
    banner.banner(' MAIN MENU ')
    menu_items = [f"[{index:02}] {item.upper()} [[bold green] ON [bold white]]" for index, item in enumerate(menu.keys())]
    if len(menu_items) % 2 != 0:
        menu_items.append("")
    menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
    cetak(Panel(menu_content, width=80, title="[bold green]Menu Bot", padding=(0, 4), style="bold white"))
    select = input(putih1 + "select : ")
    if select == "0":
        print(f"{putih1}[{hijau1}0{putih1}]{biru1}.CAPTCHAAI")
        print(f"{putih1}[{hijau1}1{putih1}]{biru1}.Solver Captcha Tg(@Xevil_check_bot)")
        sel = input(putih1 + "select : ")
        if sel == "0":
            api_key = input("Api key captcha ai > ")
            with open("ckey.txt", "w") as e:
                e.write(api_key)
        if sel == "1":
            api_key = input("Api key Xevil > ")
            with open("xkey.txt", "w") as e:
                e.write(api_key)
            #menu(banner,modul,modulesl)
        exit()
    if select == "1":
        menu_dict=list(Bits_Family.items())
        os.system("clear")
        banner.banner(' BITS FAMILY MENU ')
        menu_items = [f"[{index:02}] {item.upper()} [[bold green] ON [bold white]]" for index, item in enumerate(Bits_Family.keys())]
        if len(menu_items) % 2 != 0:
            menu_items.append("")
        menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
        cetak(Panel(menu_content, width=80, title="[bold green]Menu Bot", padding=(0, 4), style="bold white"))
        select = input(putih1 + "select : ")
        selected_index = int(select)
        if 0 <= selected_index < len(menu_dict):
          _, selected_function = menu_dict[selected_index]
          selected_function(modulesl, banner)
        
    if select == "2":
        menu_dict=list(micin.items())
        os.system("clear")
        banner.banner(' MICIN FAMILY MENU ')
        menu_items = [f"[{index:02}] {item.upper()} [[bold green] ON [bold white]]" for index, item in enumerate(micin.keys())]
        if len(menu_items) % 2 != 0:
            menu_items.append("")
        menu_content = "\n".join([f"{menu_items[i]:<60}{menu_items[i + 1]}" for i in range(0, len(menu_items), 2)])
        cetak(Panel(menu_content, width=80, title="[bold green]Menu Bot", padding=(0, 4), style="bold white"))
        select = input(putih1 + "select : ")
        selected_index = int(select)
        if 0 <= selected_index < len(menu_dict):
          _, selected_function = menu_dict[selected_index]
          selected_function(modulesl, banner)
        
