# code recipes  here: https://pyowm.readthedocs.io/en/latest/v3/code-recipes.html#onecall
# https://pyowm.readthedocs.io/_/downloads/en/develop/pdf/

from pyowm.owm import OWM  #importing the open weather map python library

myOwm = OWM('***API key goes here***')  #using your API key to tell OWM who you are

mgr = myOwm.weather_manager()   # command to access the weather using your API


# _________________________________________________________________
# |                           Task                                |
# |                   --------------------                        |
# | Given the locations below, find the optimal location in which |
# | to build a new offshore wind farm.                            |
# | Use data from the OWM API to determine this location          |
# | and justify your decision.                                    |
# |_______________________________________________________________|


locations = ['Killybegs, IE', 'Belmullet, IE', 'Clifden, IE', 'Doolin, IE', 'Kilkee, IE', 'Ventry, IE','Portmagee, IE','Bantry, IE','Baltimore, IE']








#answer = 
#print("the ideal location for a new windfarm is",answer)
