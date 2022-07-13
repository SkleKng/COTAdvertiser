from time import sleep
import json, os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

def create_config_file(value: dict) -> None:
    with open(os.getcwd() + '/' + "COTAdvertiser.json", 'w', encoding='utf-8') as f:
        json.dump(value, f, ensure_ascii=False, indent=4)
    print("[+] Created config file")

def ask_for_creds_window_gui(sg) -> None:
    value = {}
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Please enter your Discord username'), sg.InputText()],
                [sg.Text('Please enter your Discord password'), sg.InputText()],
                [sg.Text('Please find the path to the servers.txt file'), sg.FileBrowse()],
                [sg.Button('Ok'), sg.Button('Cancel')] 
            ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == 'Cancel': # if user closes window or clicks cancel
            break

        if event == 'Ok':
            value = values
            break

    window.close()

    data = {'username': value[0], 'password': value[1], 'input_file': value["Browse"]}
    create_config_file(data)

def create_alert_popup(sg, title: str, message: str) -> None:
    sg.theme('DarkAmber')   # Add a touch of color
    return sg.popup_ok(title, message)

def post_to_servers(input_file: str, username: str, password: str, sg) -> None:
    f = open(input_file, "r")
    array_urls = []
    for line in f:
        line = line.strip("\n")
        array_urls.append(line)
        

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://discord.com/login")

    message = ":star::star:**EdgeGamers** :star::star:\n> A gaming community with almost **100,000** members! \nWe strive for a punk-free gaming environment where any and everyone can feel welcomed. Creating an atmosphere best suited for making new friends!\n\n**__What We Offer:__**\nActive community and friendly staff\nDaily Events from a selection of supported games\nA welcoming playerbase\nA fully nitro boosted server\nActive voice channels\nAbility to create new voice channels\nAnd much more!\n\n**__Our Community:__**\nDedicated servers such as Minecraft, CSGO, Rust, GTA, Overwatch, and more!\nSign up with our forums, get awards, and rank up to become an admin\nMeet tons of new people from all sorts of different walks of life \nEnjoy making new friends!\n─────────────────────\n**__Join us Today:__**\n:link: https://discord.gg/edgegamers\n:link: https://imgur.com/0RsQOvp"


    username_input = driver.find_element(By.NAME, "email")
    sleep(3)
    username_input.send_keys(username)

    password_input = driver.find_element(By.NAME, "password")
    sleep(3)
    password_input.send_keys(password)

    # Initialize and login
    password_input.send_keys(Keys.RETURN)
    print("[+] Login Complete! Go do the captcha >:(")
    while(driver.current_url == "https://discord.com/login"):
        sleep(1)
        print("[/] Waiting for captcha...")
        if(driver.current_url != "https://discord.com/login"):
            break
    total_servers = len(array_urls)
    servers_done = 0

    for x in array_urls:
        driver.get(x)
        while True:
            try:
                sendmessage_input = driver.find_element(By.XPATH, "//div[@role = 'textbox']")
                break
            except NoSuchElementException:
                sleep(1)
        for part in message.split('\n'):
            sendmessage_input.send_keys(part)
            sendmessage_input.send_keys(Keys.SHIFT, Keys.RETURN)
        sendmessage_input.send_keys(Keys.RETURN)

        servers_done += 1
        print("[+] Sent message to " + x + " (" + str(servers_done) + "/" + str(total_servers) + ")")
        sleep(1)
