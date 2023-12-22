#####################################################
Server_files are the files necessary for launching our project as a website application. 
the website may be visited at: 

https://bios30cognitivetest.ddns.net/

#####################################################

The files include:
a) All_tests_launcher which consists of a jupyter notebook file that functions as a main menu on the website. Users select the test they want to run,
are interrupted with a consent and credentials submission screens, and are are re-directed to an appropriate notebook of chocie. The file was developed by Szymon Lic with support of Jan Uher, who designed the consent and credentials screens.

b) Data_Saver which includes python scripts that replace data saving within google forms with google sheets API. The scripts enable saving of data from multiple
notebooks within ONE google sheet. This is made possible by a simple data association mechanism - every test running on the website (every webpage)
has a panel where user needs to provide a login and password. This gets saved in a file Login_Details.py and is used by Data_Saver.py in associating
data to be saved with the user. Data_Saver.py works in a way analogous to google forms, however prevents multiple entries of data by the same user, and also
saves the data in a slightly different manner. 

Please find the google sheet here: https://docs.google.com/spreadsheets/d/1mpx0-GbZgS44p7bzB5uYPTzHb2OoCIHOPqoxy4_duAU/edit?usp=sharing
You may track the changes that are happening on this google sheet live.

c) Spatial_Test_server_adopted consists of the Spatial_test.ipynb code which runs on the website. It is adopted to work with the Data_Saver.py script, and thus includes a few adjustments over the final standalone version of this code (version 2.0.0) 

d) nginx_configuration_file This file is a script that's used by the server, a rented DigitalOcean VPS running Ubuntu 22.04. This file connects the server domain 
bios30cognitivetest.ddns.net with localhost:8866, where Voila application is running. It also determines routing to a specific voila-run jupyter notebook
file - the "main menu" - All_tests_launcher.ipynb.

Overall, the website runs in the following way: 
            a) all notebooks are run through server's terminal, using the command 
                "nohup voila --no-browser --port=8866 -show_tracebacks=true --VoilaConfiguration.file_allowlist="['.*']" /root/BIOS0030_server2/ &"
            b) nginx routes all http traffic from domain bios30cognitivetest.ddns.net to localhost:8866 where voila is running, and into the specific file
                in "/voila/render/All_tests_launcher/All_tests_launcher.ipynb" which is the main menu. Thus anyone visiting the website sees this as the front                    page of the website.
            c) User selects a test they want to run. They give their login detials which are saved in Login_Details.py, give their consents and credentials,                     which are saved in a
                google sheet, using Data_Saver.py, and are re-directed to their desired test.
            d) User logs in again, associating the data about to be saved with the already exisitng ones in the google sheets. Once they complete the test, their                data is associated with the existing one in the google sheet, again using Data_Saver.py, and the user is re-directed to the main menu again.

Please note, the server currently running at the domain https://bios30cognitivetest.ddns.net/
is NOT running directly from the files submitted here. The files that are submitted are indicative of what the setup looks like as of 
22.12.2023, however it is impossible for the actual server files to be shared, as it requires access to the remote DigitalOcean VPS Ubuntu server.
Nevertheless, you may track the changes happening in the google sheet live, as you are using the website.

All files except for All_tests_launcher were created by Szymon Lic. 