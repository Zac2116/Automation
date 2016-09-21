import urllib
import re 


newsymbolslist = ["googl","aapl","srpt"]

i = 0
while i < len(newsymbolslist):
	url = "https://www.google.com/finance?authuser=0&q="+newsymbolslist[i] + "&ei=qxjiV5CkDsaFmAHBqZq4Bg"
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span [^.] id="ref_[0-9]_cp">(.+?)</span>'
	print regex
	pattern = re.compile(regex)
	change = re.findall(pattern,htmltext)
	print change
	i+=1




