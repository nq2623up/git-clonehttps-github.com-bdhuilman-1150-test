from openpyxl import Workbook
import requests, bs4
# The imports i needed to work on this assessments
# Beautiful soup is not a fan of i am not
minnstate = open('<tbody tabindex="0" class="yui-dt-data" style>//minneapolis.learn.minnstate.edu/d2l/le/content/4607101/viewContent/40774139/View')
Minnstate = bs4.BeautifulSoup()
Minnstate = Minnstate.select('td class=yui-dt0-col-couNbr')
type(Minnstate)
'<td headers="yui-dt0-th-ID " class="yui-dt0-col-ID yui-dt-col-ID yui-dt-sortable"><div class="yui-dt-liner'
# div are great to learn about
len(Minnstate)
'div class = yui-dt-liner'
type(Minnstate[0])
'tbody class= yui-dt-data'
res = requests.get('https://minneapolis.learn.minnstate.edu/d2l/le/content/4607101/viewContent/40774139/View')
# quickly its time request
res.raise_for_status()
# raise_for_status.res
Minnstate = bs4.BeautifulSoup(res.text)
# res is for requesting the url for these lines of code
type(Minnstate)
# time to type

# example this is for bs4 soup done not as well maybe
Minnstate.select('input[ID#]')
# i am selecting one line of code from this site
Minnstate.select('input[Subject]')
# i am taking all of this topics of code
Minnstate.select('input[Title]')
# Time to title this Minnstate.com
Minnstate.select('input[Days]')
# How many days you can do come here
Minnstate.select('input[Times]')
# how long your here per day
Minnstate.select('input[Cr/Hr]')
# A number verizon of times
Minnstate.select('input[instructor]')
# who's teaching you
# Soup selecting is not as bad
workbook = Workbook()
# yes workbook equals Workbook
sheet_names = workbook.sheetnames
# its time to name the sheet
print(sheet_names)
# its time revel the sheet name
worksheet = workbook.active
# Making a worksheet in a workbook
names_sheet = workbook.active
# naming a sheet
workbook = workbook.active
# the workbook coding
Workbook.save('ITEC.xlsx')
# This how to save a workbook



