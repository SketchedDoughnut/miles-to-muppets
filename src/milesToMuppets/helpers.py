'''
This file contains helper functions, that print data for the user.
'''

# HELPERS
# all were originally "info_(func)"

# gets help info
def get_help() -> None:
    '''
    A function to print help info
    '''

    print('For help, go to the documentation: https://pypi.org/project/MilesToMuppets/')
    print('Alternatively, go to the github page: https://github.com/SketchedDoughnut/miles-to-muppets')

# gets the name of the current license
def get_license() -> None:
    '''
    A function to print license name, also refers you to the Github page to read license in-depth
    '''

    print('This code is licensed under "Apache License". Check the license on Github for more information (refer to get_help())')

# gets credits for this project
def get_credits() -> None:
    '''
    A function to print the credits of who made this
    '''

    print('This project is created and maintained by Sketched Doughnut.')