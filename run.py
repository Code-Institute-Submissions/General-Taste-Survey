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
music_data = music.get_all_values()

movies = SHEET.worksheet('movies')
movies_data = movies.get_all_values()

sports = SHEET.worksheet('sports')
sports_data = sports.get_all_values()


def get_music_data():
    i = 1
    while i < 6:
        print(music.col_values(i))
        i += 1


def get_movies_data():
    i = 1
    while i < 6:
        print(movies.col_values(i))
        i += 1


def get_sports_data():
    i = 1
    while i < 6:
        print(sports.col_values(i))
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
    if data_str == 'Music' or data_str == 'music':
        get_music_data()
    elif data_str == 'Movies' or data_str == 'movies':
        get_movies_data()
    elif data_str == 'Sports' or data_str == 'sports':
        get_sports_data()
    else:
        print('Invalid input, please try again')


get_input_data()
