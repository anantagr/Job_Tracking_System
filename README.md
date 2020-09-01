# Job_Tracking_System
This application can be used to find jobs on linkedin based on job tittle/location and store them in an excel file for reference. 

 ![](https://github.com/anantagr/Job_Tracking_System/blob/master/README_imgs/img.png) 

[Link to article]()

## Step 1
- Download the application and unzip it.

## Step 2
- Find the Google Chrome version you are using.
  [Chrome version](https://www.howtogeek.com/299243/which-version-of-chrome-do-i-have/)
  
 - Download Chromedriver.exe and save it in the same folder with the application.
 [Download Chromedriver](https://chromedriver.chromium.org/downloads)
 
 **It is important that you have the correct version of Chromedriver for this application to run successfully**
 
 ## Step 3
 - Open command prompt by typing cmd in your windows search bar (win + cmd) 
 - Navigate to application folder in command prompt
 [Using Command prompt in Windows](https://youtu.be/8-mYKkNzjU4)
 
 ## Step 4
 - Intall a virtual environment by typing ``` pip install pipenv ``` in the command promptcls
 - **Note: This application can run without virtual environment as well but I recommend using a it. Jump to step 5 if you are skipping it**
 - To create the vitual environment use ```pipenv install``` in the command prompt
 - To activate the vitual environment use ```pipenv shell``` in the command prompt
 - [Learn about using virual environment in Python](https://youtu.be/Ns4t5NkmFoQ)
 
 ## Step 5
 - To install all the packages and dependencies required to the application are in requirments.txt file in the folder
 - ```pip install -r requirements.txt``` in the command prompt will install everything in your virtual environment
 
 ## The difficult part is over !!!
 ## Step 6
 - ```python app.py``` in the command prompt will run the python file for the application
 ![](https://github.com/anantagr/Job_Tracking_System/blob/master/README_imgs/img2.png) 
 
 - **http://127.0.0.1:5000/** is link to the webpage running the application
 
 
# Using Job Tracking System
- Enter the *Job tittle*
- Enter the *Job location* (E.g. Calgary, Newyork, India, Australia)
- **Chromedriver folder path** is the folder path where chromedriver is stored along with the application files
- ```Ctrl+L``` is the shortcut to find folder path
- Click **Submit** and see the magic


# Error handling
Some of the error you might come across while running the application

- **Folder path** is not provided correctly
 ![](https://github.com/anantagr/Job_Tracking_System/blob/master/README_imgs/img4.png) 

- Incorrect version of **Chromedriver** was downloaded
 ![](https://github.com/anantagr/Job_Tracking_System/blob/master/README_imgs/img5.png) 

- Excel file for storing job details is open
 ![](https://github.com/anantagr/Job_Tracking_System/blob/master/README_imgs/img6.png) 
