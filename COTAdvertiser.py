from utils.functions import post_to_servers, ask_for_creds_window_gui, create_alert_popup

# User interface imports
import PySimpleGUI as sg
import os, json

if os.path.isfile(os.getcwd() + '/' + "COTAdvertiser.json"):
    print("[+] Config file found, using credentials from file")
    with open(os.getcwd() + '/' + "COTAdvertiser.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    username = data['username']
    password = data['password']
    input_file = data['input_file']
    post_to_servers(input_file, username, password, sg)
    create_alert_popup(sg, "Success", "Successfully posted to servers")
else:
    ask_for_creds_window_gui(sg)
    with open(os.getcwd() + '/' + "COTAdvertiser.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    username = data['username']
    password = data['password']
    input_file = data['input_file']
    post_to_servers(input_file, username, password, sg)
