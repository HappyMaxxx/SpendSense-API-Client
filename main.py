import requests
import os
import json

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_config():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = "config.json"
    config_path = os.path.join(base_dir, file_name)
    
    if not os.path.exists(config_path):
        default_config = {
            "base_url": "http://127.0.0.1:8000/",
            "api_token": "your-api-token-here"
        }
        with open(config_path, "w") as f:
            json.dump(default_config, f, indent=4)
        clear()
        print(f"Your '{file_name}' file was not found, so a new one was created.")
        input("Please insert your API token into it and press Enter...")
        exit(1)
    
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        if not all(key in config for key in ["base_url", "api_token"]):
            print(f"❌ Missing required keys in {file_name}.")
            input("Press Enter to exit...")
            exit(1)
        return config
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON in {file_name}.")
        input("Press Enter to exit...")
        exit(1)

def show_param_info():
    while True:
        clear()
        param_examples = {
            "6": {
                "title": "Create Transaction (create_transaction)",
                "key": "create_transaction",
                "example": {
                    "amount": 100.0,
                    "account_id": 1,
                    "category_id": 2,
                    "type": "expense",  # or "income"
                    "description": "Lunch"
                }
            },
            "7": {
                "title": "Create Category (create_category)",
                "key": "create_category",
                "example": {
                    "name": "Food",
                    "type": "expense"  # or "income"
                }
            },
            "8": {
                "title": "Create Account (create_acc)",
                "key": "create_acc",
                "example": {
                    "name": "Cash",
                    "currency": "USD"
                }
            },
            "2": {
                "title": "List Transactions (transactions)",
                "key": "transactions",
                "example": {
                    "date_from": "2024-01-01",
                    "date_to": "2024-12-31"
                }
            },
            "4": {
                "title": "List Categories (categories)",
                "key": "categories",
                "example": {
                    "type": "expense"  # or "income"
                }
            }
        }

        print("📘 Parameter Info Menu:\n")
        for key, info in param_examples.items():
            print(f"  {key}: {info['title']}")
        print("  q: Back to main menu")

        choice = input("\n> Choose a function: ").strip().lower()
        clear()

        if choice in param_examples:
            info = param_examples[choice]
            print(f"🔹 {info['title']}")
            print(f"Config key: \"{info['key']}\"\n")
            print("Example value:")
            print(json.dumps({info["key"]: info["example"]}, indent=4))
        elif choice == 'q':
            break
            return
        else:
            print("❓ Unknown selection.")
        
        input("\n> Press Enter to continue...")

def make_api_call(endpoint, method="GET", config_key=None, extract_key=None):
    config = load_config()
    if config['api_token'] == "your-api-token-here":
        print("⚠️ Please update your API token in config.json")
        input()
        return
    
    url = f"{config['base_url']}{endpoint}"
    headers = {"Authorization": f"Bearer {config['api_token']}"}
    payload = config.get(config_key) if config_key else None
    
    try:
        if method.upper() == "POST":
            response = requests.post(url, headers=headers, json=payload)
        else:
            response = requests.request(method, url, headers=headers, params=payload)
        response.raise_for_status()
        data = response.json()
        if extract_key:
            items = data.get(extract_key, [])
            for item in items:
                print(item)
        else:
            print(data)
    except requests.exceptions.RequestException as e:
        print(f"❌ Помилка ({response.status_code if 'response' in locals() else 'N/A'}): {e}")
    except ValueError as e:
        print(f"❌ Помилка розбору JSON: {e}")

def token_check():
    make_api_call("api/v1/token/check")

def transactions():
    make_api_call("api/v1/transactions/", config_key="transactions", extract_key="transactions")

def accounts_api():
    make_api_call("api/v1/accounts/")

def get_cats():
    make_api_call("api/v1/categories/get/", config_key="categories", extract_key="categories")

def get_profile_data():
    make_api_call("api/v1/profile-data/")

def trans_create():
    make_api_call("api/v1/transactions/create/", config_key="create_transaction")

def cat_create():
    make_api_call("api/v1/categories/create/", config_key="create_category")

def account_create():
    make_api_call("api/v1/accounts/create/", config_key="create_acc")

funcs = {
    '1': token_check,
    '2': transactions,
    '3': accounts_api,
    '4': get_cats,
    '5': get_profile_data,
    '6': trans_create,
    '7': cat_create,
    '8': account_create,
    'i': show_param_info,
}
descriptions = {
    '1': 'Check token validity',
    '2': 'List transactions',
    '3': 'List accounts',
    '4': 'List categories',
    '5': 'Get profile data',
    '6': 'Create transaction',
    '7': 'Create category',
    '8': 'Create account',
    'i': 'Show info about config parameters',
    'q': 'Quit the program'
}
anable_vals = list(funcs.keys())
anable_vals.append('q')

if __name__ == '__main__':
    try:
        while True:
            clear()
            print("🔧 Available commands:")
            for key in anable_vals:
                desc = descriptions.get(key, funcs[key].__name__ if key in funcs else "No description")
                print(f"  {key}: {desc}")
            
            a = input("\n> Enter a command: ").strip().lower()
            clear()

            if a in funcs:
                print()
                try:
                    funcs[a]()
                except Exception as e:
                    print(f"⚠️ An error occurred while executing the command: {e}")
            elif a == 'q':
                print("👋 Goodbye!")
                break
            else:
                print(f"❓ Unknown command: '{a}'.")

            if a != 'i':
                input("\n> Press Enter to continue...")
    except KeyboardInterrupt:
        clear()
        print("👋 Goodbye!")