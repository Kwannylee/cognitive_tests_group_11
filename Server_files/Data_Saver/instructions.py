#before you begin, make sure that your code is running in Voila. The edits below will make your code 
#unusable outside of the server, unless you download Data_Saver folder and put it OUTSIDE of the a folder where you are running your code.
#Directory has to look like this:
#  -Data_Saver
#    --login_details.py 
#    --Data_Saver.py
#  -Your_folder
#    --Your_notebook.ipynb
#You can also skip this step but then you will never actually know if your whole code is working properly.
#Until I upload it to the server.
##############################--STEP-1--####################################################
#These imports are necessary for the code to work. Please paste this whole block into your notebook at the beginning of your code.
import sys
import os
from IPython.display import display, Javascript
original_sys_path = sys.path.copy()
module_path = os.path.abspath(os.path.join('..', 'Data_Saver'))
if module_path not in sys.path:
    sys.path.append(module_path)
import Data_Saver as dsf
sys.path = original_sys_path
##############################--STEP-2-#####################################################
#collect a login and password from the user. the user must know that you are collecting a login and a password
#from them and that they need to remember them. That is because the same login and password will be used for them 
#to access other notebooks.
login = "kwan"
password = "password1234"
##############################--STEP-3-#####################################################
#create a dictionary with the login and password. The keys must be "username" and "password" as shown below, wit the values being the actual login and password.
login_info_dictionary = {"username":login, "password":password} #
##############################--STEP-4-#####################################################
#Save the login details using the function below. This will save the login details in a file called "login_details.py" which is present on the server. 
dsf.save_login_details(the_actual_details_you_wanna_save) 
##############################--STEP-5-#####################################################
#Once your test has collected all the data, you prepare it for sending to a spreadsheet.
#The data that is being saved to the spreadsheet must be in the form of a dictionary.
#It can take in as many keys as you want, but the keys must be strings and the values can be any data type.
data_to_save = {"login_details": {"username":login, "password":password},
                "test": "Spatial_Test", #These two are mandatory! Make sure the "test" key is not capitalized!
                
                "saving total_correct": 12
                }
##############################--STEP-6-#####################################################
#Once you are done preparing the data, you can send it to the spreadsheet using the function below.
#I strongly recommend doing this at the very end of your script, as the sending takes a bit of time. 
dsf.save_data(data_to_save)
##############################--STEP-7-#####################################################
#Because your notebook will be on the server, after this step, we want your notebook to redirect to the main menu.
#This is done using the function below:
def link_redirection(self):
        display(Javascript(f"""window.location.href = 'http://bios30cognitivetest.ddns.net/voila/render/All_tests_launcher/All_tests_launcher.ipynb';"""))

