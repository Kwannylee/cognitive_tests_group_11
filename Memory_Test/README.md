import requests
from bs4 import BeautifulSoup
import json
import time

print("We are going to test your reaction time!")

print("Please enter your name:")
name = input("> ")

print("Please enter your age:")
age = input("> ")


results = []
for i in range(3):
    print("When the next message is shown press enter as quickly as possible!")
    time.sleep(3)
    
    # record time when message shown
    start_time = time.time() 
    input("Press enter now!")
    
    # record time when input box is closed
    end_time = time.time()
    
    # difference between time of message, 
    # and time user closed input by pressing enter
    # is the response time
    response_time =  end_time - start_time

    # store into results
    results.append(response_time)
    
    # To show the result we use an f-string
    # in the {} we add format code :.3f 
    # to specify we want to display the result to 3 decimal places
    print(f"Well done! your time was {response_time:.3f}")

data_dict = {name: name,
            age: age,
            time_1: result[0],
            time_2: result[1],
            time_3: result[2],

}


def send_to_google_form(data_dict, form_url):
    ''' Helper function to upload information to a corresponding google form 
        You are not expected to follow the code within this function!
    '''
    form_id = form_url[34:90]
    view_form_url = f'https://docs.google.com/forms/d/e/1FAIpQLScTeWhPLc9xkFxB3s4ot9U4hdor9yF9wJvR4XU3DF9W32meIg/viewform?usp=sf_link/viewform'
    post_form_url = f'https://docs.google.com/forms/d/e/1FAIpQLScTeWhPLc9xkFxB3s4ot9U4hdor9yF9wJvR4XU3DF9W32meIg/viewform?usp=sf_link/formResponse'

    page = requests.get(view_form_url)
    content = BeautifulSoup(page.content, "html.parser").find('script', type='text/javascript')
    content = content.text[27:-1]
    result = json.loads(content)[1][1]
    form_dict = {}
    
    loaded_all = True
    for item in result:
        if item[1] not in data_dict:
            print(f"Form item {item[1]} not found. Data not uploaded.")
            loaded_all = False
            return False
        form_dict[f'entry.{item[4][0][0]}'] = data_dict[item[1]]
    
    post_result = requests.post(post_form_url, data=form_dict)
    return post_result.ok
