# To run Spatial_Test, please click play in jupyter notebook.
# Ideally, please install voila 0.5.5 using pip. Afterwards, within terminal in this directory, run command "voila Spatial_Test_v2.0.0.ipynb"
# if working in a directory on your device. 
# if working in jupyterlab, please restart jupytter session completely (with logging off) after the installation. an icon should appear
# in the top ribbon, signalling that the file may be run with voila. alternatively, navigate to run>render notebook with voila.
# or consult voila documentation on running the file within jupyter notebook.

# The test works as a standalone application. User is first greeted by conscent and credentials submission panels which are important for statistical calculations. The user is then shown nine panels with 3D cube arrangements, and asked to determine, which 2D projection of the cubes does not fit any of the 3D-arranged cubes.
# At the end, the data is saved to google forms, and user is shown how well their did (as a score out of 9).

# The program is written completely using object-oriented programming. This choice was done specifically to allow abstraction of the used systems, and compartmentalisation of functions into distinct, separate parts. This was especially convenient as the code is quite extensive. Use of object-oriented programnming further aids readibility - classes Data_Saver, Widnow_Manager, Panels etc. are all self-explainatory, and their extent is highly separated from other parts of the code. 

# Additional features include the use of threading - a python library that allows two processes to co-exist simoultaneously. This is particularily convenient for the purposes of time managament - Without threading, it would be difficult to implement two subsequent timers - one that counts the time taken for each puzzle, and one that counts the overall time that passed since the beggining of the trial. 