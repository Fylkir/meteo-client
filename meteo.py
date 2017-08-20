import urllib as url
from PIL import Image as im
import datetime as dt



tod = dt.date.today()
hr = dt.datetime.now().hour
tstr = str(tod.year) + str(tod.month).zfill(2) + str(tod.day).zfill(2)

if hr > 0 and hr <12:
    hstr = '00'
elif hr>12 and hr < 18:
    hstr = '06'
else:
    hstr = '12'
    
row = '406'
col = '250'    

saveimg = url.urlretrieve('http://www.meteo.pl/um/metco/mgram_pict.php?ntype=0u&fdate=' + tstr + hstr + '&row='+ row + '&col=' + col + '&lang=pl', 'image.png')
imag = im.open('image.png')
imag.show()

