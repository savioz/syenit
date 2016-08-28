from Bio import Entrez
import sys
Entrez.email = "stephane@savioz.ch"
#handle = Entrez.einfo() # or esearch, efetch, ...
#record = Entrez.read(handle)
#handle.close()


#handle = Entrez.efetch("pubmed", id="19304878,14630660", retmode="xml")
#records = Entrez.parse(handle)
#for record in records:
	# each record is a Python dictionary or list.
	#print(record['MedlineCitation']['Article']['ArticleTitle'])
#handle.close()

termToSearchFor = "Anhydrous milk fat"
#termToSearchFor = "milk Anhydrous"
handle = Entrez.esearch("pubmed", term=termToSearchFor)
records = Entrez.read(handle)
handle.close()

print("Searchin for {} \n\n".format(termToSearchFor))
print records["Count"]
print records["IdList"]


'''
pmid = records["IdList"][0]
handle = Entrez.elink(dbfrom="pubmed", id=pmid, linkname="pubmed_pubmed")
record = Entrez.read(handle)
print(record)
sys.exit()

print(record['MedlineCitation']['Article']['Abstract']['AbstractText'])
handle.close()
print(record[0]["LinkSetDb"][0]["LinkName"])
'''

#sys.exit()

ct = 1
for id in records["IdList"]:
	print "\n************************"
	handle = Entrez.efetch("pubmed", id=id, retmode="xml")
	records = Entrez.parse(handle)

	for record in records:
	# each record is a Python dictionary or list.
		article = record['MedlineCitation']['Article']
		#print(type(article))
		#print(article.keys())
		abstractText = article['Abstract']['AbstractText']
		print(type(abstractText))
		print(len(abstractText))
		print(abstractText)
		#print(record['MedlineCitation']['Article'])
		#print(record['MedlineCitation']['Article']['ArticleTitle'])
	handle.close()
	ct = ct + 1
	if ct == 12:
		break



print("ct : {}".format(ct))




