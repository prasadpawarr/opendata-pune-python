import ssl
import shutil
import tempfile
import urllib.request
context = ssl._create_unverified_context()

sr_error_links = []

def downloadFile(dlurl, srno, extn):
	try:
		with urllib.request.urlopen(dlurl, context=context) as response:
		    with open(f"C:\\Users\\poonam\\Desktop\\opendata-listing\\datasets\\{srno}.{extn}", 'wb') as tmp_file:
		        shutil.copyfileobj(response, tmp_file)
		        print(f"file : {srno} downloaded")
	except:
		sr_error_links.append(srno)
		print("Cannot download file : ", srno)
	

	
if __name__ == '__main__':
	main()