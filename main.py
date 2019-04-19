import csv
from download import *


useless_entries = ('title','note','numD','sizeTxt','sizeKB','category','remarks','no. of data rows','no. of columns','narrow or wide(pivoted)')
'''with open('pune-data-listing.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	

	with open('new-listing.csv', 'w') as new_file:
		fieldnames = ['sr', 'download', 'extension']
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)
		csv_writer.writeheader()

		for line in csv_reader:
			for entry in useless_entries:
				del line[entry]
			csv_writer.writerow(line)
'''

with open('new-listing.csv', 'r') as new_clean_file:
	csv_reader = csv.DictReader(new_clean_file)

	for line in csv_reader:
		dlurl = line['download']
		srno = line['sr']
		extn = line['extension']

		downloadFile(dlurl, srno, extn)

print(sr_error_links)