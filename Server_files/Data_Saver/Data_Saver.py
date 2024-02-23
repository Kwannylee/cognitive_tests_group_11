import gspread
from Login_Details import login_details_dictionary  # Import login_details_dictionary from Login_Details.py
from oauth2client.service_account import ServiceAccountCredentials

# Use creds to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('./bios0030-responses-87b07a1dcd4b.json', scope)
client = gspread.authorize(creds)


def save_login_details(login_details):  # login_details is a dictionary
    login_details_dictionary[login_details["username"]] = login_details["password"]  # Add login details to login_details_dictionary
    dict_content = repr(login_details_dictionary)  # Convert login_details_dictionary to a string
    with open('Login_Details.py', 'w') as file:  # Open Login_Details.py
        file.write('import ast\n\n')  # Write import ast
        file.write(f'login_details_dictionary = {dict_content}\n\n')  # Write login_details_dictionary
        file.write('def login_details_get(username):  # username is a string\n')  # Write login_details_get function
        file.write('    return login_details_dictionary.get(username)\n')  # Write login_details_get function
    return "Login details saved successfully!!"  # All updates done


def save_data(data):  # data is a dictionary
    login_details = data.get("login_details", {}) # Get login details
    username = login_details.get("username") # Get username
    password = login_details.get("password") # Get password

    if username in login_details_dictionary and login_details_dictionary[username] == password: # Check if username and password are correct
        if 'test' in data:  # Check if test key is present
            data_test = data['test']  # Get test name
            data.pop('test')  # Remove test name from data

            # Convert all values to strings and prepare data to be saved
            data_to_save = {f'{data_test}_{key}': str(value) for key, value in data.items() if key != "login_details"} # Convert all values except login_details to strings and prepare data to be saved
            data_to_save["login_details"] = username # Add username to data to be saved

            spreadsheet = client.open("BIOS0030_SERVER_ANWERS_FINAL") # Open spreadsheet
            sheet = spreadsheet.sheet1 # Open sheet


            all_values = sheet.get_all_values()  # Get all values
            if not all_values:  # If the sheet is empty
                sheet.update_cell(1, 1, "login_details")
                all_values = [['login_details']]  # Update all_values to reflect the change made to the sheet
            elif not "login_details" in all_values[0]:  # Check if login_details is not in the first row
                sheet.insert_row(["login_details"], 1)  # Insert login_details as first column header
                all_values = sheet.get_all_values()  # Update all_values to reflect the change made to the sheet
            for key, value in data_to_save.items(): # Loop through all column names
                if not key in all_values[0]: # Check if column name is not in the first row
                    sheet.update_cell(1, len(all_values[0])+1, key) # Add column name to the first row
                all_values = sheet.get_all_values() # Update all_values
                usernames = [row[0] for row in all_values] # Get all usernames
                if username in usernames: # Check if username is in the spreadsheet
                    user_row = usernames.index(username) + 1 # Get the row number of the username
                else:
                    user_row = len(all_values) + 1 # If the username is not in the spreadsheet, set the row number to the first empty row
                    sheet.update_cell(user_row, 1, username) # Add the username to the first empty row
                column_index = all_values[0].index(key) + 1 # Get the column index for the column name
                sheet.update_cell(user_row, column_index, value) # Update the cell with the value
            return "Data saved successfully!!"
        else:
            return "Error: Test name not provided"
    else:
        return "Error: Invalid username or password"