# SpendSense API Client

![Лого SpendSense](src/img/logo.png)

A simple console-based API client for interacting with the SpendSense API, designed to manage financial transactions, accounts, and categories.

This client allows users to:
- Check API token validity
- List transactions, accounts, and categories
- Create new transactions, accounts, and categories
- Retrieve profile data
- View example configuration parameters for API calls

The client interacts with the SpendSense API and requires a valid API token and configuration file to function properly.

## Related Repository

This API client is built to work with the [SpendSense](https://github.com/HappyMaxxx/SpendSense) project. Visit the main repository for more details about the SpendSense application.

## Prerequisites

- **Python 3.6+**: Ensure Python is installed on your system.
- **Dependencies**: The client uses the `requests` library for HTTP requests.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/HappyMaxxx/SpendSense-API-Client.git
   cd SpendSense-API-Client
   ```

2. **Install Dependencies**

   Install the required Python package using pip:

   ```bash
   pip install requests
   ```

3. **Set Up Configuration**

   - The client requires a `config.json` file in the same directory as `main.py`.
   - If the `config.json` file does not exist, the client will create one with default values:

     ```json
     {
         "base_url": "http://127.0.0.1:8000/",
         "api_token": "your-api-token-here"
     }
     ```

   - Update the `api_token` field in `config.json` with your valid SpendSense API token.
   - Ensure the `base_url` points to the correct SpendSense API endpoint (e.g., `http://127.0.0.1:8000/` for local development or the production URL).

## Usage

1. **Run the Client**

   Start the client by running the following command:

   ```bash
   python main.py
   ```

2. **Interact with the Client**

   Upon running, the client displays a menu with available commands:

   ```
   🔧 Available commands:
     1: Check token validity
     2: List transactions
     3: List accounts
     4: List categories
     5: Get profile data
     6: Create transaction
     7: Create category
     8: Create account
     i: Show info about config parameters
     q: Quit the program
   ```

   - Enter a number (1-8), `i` for parameter info, or `q` to quit.
   - Follow the prompts to execute API calls or view configuration examples.
   - For commands that create resources (e.g., transactions, categories, accounts), ensure the relevant parameters are defined in the `config.json` file under the appropriate keys (e.g., `create_transaction`, `create_category`, `create_acc`).

3. **Configuration Parameters**

   - Use the `i` command to view example payloads for API calls.
   - Update the `config.json` file with the required parameters for specific API calls. For example:

     ```json
     {
         "base_url": "http://127.0.0.1:8000/",
         "api_token": "your-api-token-here",
         "create_transaction": {
             "account": "Cash",
             "category": "Food",
             "amount": 100.0,
             "type": "spent"
         },
         "create_category": {
             "name": "Food",
             "icon": "🍽️",
             "type": "spent"
         },
         "create_acc": {
             "account": "Cash",
             "amount": 100.0
         },
         "transactions": {
             "from": "2025-01-01T00:00:00",
             "to": "2025-07-31T23:59:59"
         },
         "categories": {
             "type": "spent",
             "user": "true"
         }
     }
     ```

## Features

- **Token Validation**: Verify the validity of your API token.
- **List Resources**: Retrieve lists of transactions, accounts, and categories.
- **Create Resources**: Add new transactions, accounts, or categories via the API.
- **Parameter Info**: View example JSON payloads for API calls to help configure `config.json`.
- **Error Handling**: Clear error messages for invalid JSON, missing configuration keys, or API request failures.

## Troubleshooting

- **Missing `config.json`**: If the file is missing, the client will create one. Update it with your API token and restart.
- **Invalid JSON**: Ensure `config.json` is properly formatted. Use the example payloads provided by the `i` command.
- **API Token Issues**: Verify your API token is valid and correctly entered in `config.json`.
- **Connection Errors**: Ensure the `base_url` in `config.json` is correct and the SpendSense API is running.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m "Add your feature"`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

Please ensure your code follows the existing style and includes appropriate comments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.