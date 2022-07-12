from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import argparse

parser = argparse.ArgumentParser(description='COT - Discord Automation Script')

required = parser.add_argument_group('required arguments')
required.add_argument('-i', '--input', help='The file path of the channel list', required=True)
required.add_argument('-u', '--username', help='Your Discord Username', required=True)
required.add_argument('-p', '--password', help='Your Discord Password', required=True)

args = parser.parse_args()

f = open(args.input, "r")
array_urls = []
for line in f:
    line = line.strip("\n")
    array_urls.append(line)
    

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://discord.com/login")

username = args.username
password = args.password
message = ":star::star:**EdgeGamers** :star::star:\n> A gaming community with almost **100,000** members! \nWe strive for a punk-free gaming environment where any and everyone can feel welcomed. Creating an atmosphere best suited for making new friends!\n\n**__What We Offer:__**\nActive community and friendly staff\nDaily Events from a selection of supported games\nA welcoming playerbase\nA fully nitro boosted server\nActive voice channels\nAbility to create new voice channels\nAnd much more!\n\n**__Our Community:__**\nDedicated servers such as Minecraft, CSGO, Rust, GTA, Overwatch, and more!\nSign up with our forums, get awards, and rank up to become an admin\nMeet tons of new people from all sorts of different walks of life \nEnjoy making new friends!\n─────────────────────\n**__Join us Today:__**\n:link: https://discord.gg/edgegamers\n:link: https://imgur.com/0RsQOvp"


username_input = driver.find_element(By.NAME, "email")
username_input.send_keys(username)

password_input = driver.find_element(By.NAME, "password")


password_input.send_keys(password)

# Initialize and login
password_input.send_keys(Keys.RETURN)
print(">>Login Complete! Go do the captcha >:(")
while(driver.current_url == "https://discord.com/login"):
    sleep(1)
    print(">>Waiting for captcha...")
    if(driver.current_url != "https://discord.com/login"):
        break
totalservers = len(array_urls)
serversdone = 0

for x in array_urls:
    driver.get(x)
    while True:
        try:
            sendmessage_input = driver.find_element(By.XPATH, "//div[@role = 'textbox']")
            break;
        except NoSuchElementException as e:
            sleep(1)
    for part in message.split('\n'):
        sendmessage_input.send_keys(part)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    sendmessage_input.send_keys(Keys.RETURN)
    serversdone = serversdone + 1
    print("Servers done: " + str(serversdone) + "       Servers left: " + str(totalservers-serversdone))
