import requests
import discord_webhook

# ANSI escape codes for purple text
PURPLE = '\033[95m'
ENDC = '\033[0m'

def delete_webhook(webhook_url):
    response = requests.delete(webhook_url)
    if response.status_code == 204:
        print(f"{PURPLE}Webhook deleted successfully{ENDC}")
    else:
        print(f"{PURPLE}Error deleting webhook. Status code: {response.status_code}{ENDC}")

def say_in_webhook(webhook_url, message):
    payload = {"content": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print(f"{PURPLE}Message sent successfully{ENDC}")
    else:
        print(f"{PURPLE}Error sending message. Status code: {response.status_code}{ENDC}")

def get_webhook_info(webhook_url):
    response = requests.get(webhook_url)
    if response.status_code == 200:
        data = response.json()
        print(f"{PURPLE}Webhook Information:{ENDC}")
        print(f"{PURPLE}ID: {data['id']}{ENDC}")
        print(f"{PURPLE}Name: {data['name']}{ENDC}")
        print(f"{PURPLE}Token: {data['token']}{ENDC}")
        print(f"{PURPLE}Type: {data['type']}{ENDC}")
        print(f"{PURPLE}Channel ID: {data['channel_id']}{ENDC}")
    else:
        print(f"{PURPLE}Error getting webhook information. Status code: {response.status_code}{ENDC}")

# Main function
def main():
    print(f"{PURPLE}Discord Webhook Multi Tool{ENDC}")
    print(f"{PURPLE}[1] Delete Webhook{ENDC}")
    print(f"{PURPLE}[2] Say Stuff In Webhook{ENDC}")
    print(f"{PURPLE}[3] Get Webhook Info{ENDC}")

    choice = input(f"{PURPLE}Enter your choice (1, 2, or 3): {ENDC}")

    if choice == '1':
        webhook_url = input(f"{PURPLE}Enter the webhook URL to delete: {ENDC}")
        delete_webhook(webhook_url)
    elif choice == '2':
        webhook_url = input(f"{PURPLE}Enter the webhook URL to send a message: {ENDC}")
        message = input(f"{PURPLE}Enter the message to send: {ENDC}")
        say_in_webhook(webhook_url, message)
    elif choice == '3':
        webhook_url = input(f"{PURPLE}Enter the webhook URL to get information: {ENDC}")
        get_webhook_info(webhook_url)
    else:
        print(f"{PURPLE}Invalid choice. Please enter 1, 2, or 3.{ENDC}")

if __name__ == "__main__":
    main()
