# meteo-client
A fast tool for downloading local numerical weather forecast from meteo.pl website with just one click. 

To set your location, first find a meteorogram that corresponds to it at meteo.pl website.
Then look at its address. It will look like the following one:

http://www.meteo.pl/um/php/meteorogram_list.php?ntype=0u&fdate=2017082012&row=406&col=250&lang=pl&cname=Warszawa

Copy numbers assigned to row and column (406 and 250 in this case) and paste them into the code, remembering about parentheses.

row = '406'
col = '250'  
