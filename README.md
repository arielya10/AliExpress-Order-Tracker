# AliExpress Order Tracker

This script automates the process of logging into a user's AliExpress account and retrieves information about their order history. It shows the total amount of money spent on AliExpress and the number of items bought in the "My orders" and "Deleted orders" sections.

## Requirements
- [Selenium](https://pypi.org/project/selenium/)
- [PyFiglet](https://pypi.org/project/pyfiglet/)
- [forex-python](https://pypi.org/project/forex-python/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

## Setup
 Install the required libraries using `pip install -r requirements.txt`


## Usage
1. Run the script using `python scan.py`
2. Choose your browser when prompted
3. Enter your AliExpress email and password when prompted
4. The script will retrieve and display information about your order history in the terminal

## Notes
- The script currently only supports Chrome and Firefox.
- The script will only retrieve information about orders with the status "Finished" or "Awaiting delivery". Orders with the status "Closed" or "Cancelled" will be ignored.
- The script converts all prices to USD.
- The script may take some time to retrieve and process all of the information about your order history. Please be patient.

## Screenshots
![2022-09-21 13-07-21_Trim](https://user-images.githubusercontent.com/68149162/191480383-00cb7454-f3c2-4b40-b73f-e1593f00f274.gif)

![Screenshot 2022-09-21 130919](https://user-images.githubusercontent.com/68149162/191479597-c966b002-f1f5-4531-9f36-95e0cfcc90ec.png)
