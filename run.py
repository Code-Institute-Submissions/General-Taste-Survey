import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('general_taste_survey')

music = SHEET.worksheet('music')
data = music.get_all_values()


def get_category_data():
    i = 1
    while i < 6:
        print(music.col_values(i))
        i += 1


def get_input_data():
    '''
    Get input data from user
    '''
    print('Welcome to the General Taste Survey!')
    print('------------------------------------\n')
    print('This survey contains answers from 150 people')
    print('The categories are: Music, Movies and Sports\n')
    data_str = input('Please enter a category here: ')
    if data_str == 'Music' or 'music':
        get_category_data()


get_input_data()
