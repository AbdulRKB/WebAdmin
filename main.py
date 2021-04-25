import requests, sys
from rich.console import Console
from pages import pages

console = Console()


console.print('[bold][yellow]Contact: @CyberTitus')
console.print('[bold][red]NOTE: This Tool was made for educational purposes only.')
try:
	target = sys.argv[1]
except IndexError:
	console.print(f'[bold][yellow][+] Usage: python [green]{sys.argv[0]} [purple]<target>')
	sys.exit()




done_pages = []
done_status_codes = []
for track, page in enumerate(pages):
	if target[0:8] != "https://":
		target = "https://"+target
	else:
		pass
	if target[len(target)-1] == "/":
		pass
	else:
		target = target+"/"
	target = target+page
	try:
		res_code = requests.get(target).status_code
		if res_code == 200:
			console.print(f'[bold][yellow][+] FOUND! [green]{target}')
		else:
			pass
		done_pages.append(page)
		done_status_codes.append(res_code)
	except requests.exceptions.ConnectionError:
		console.print('[+] Error: Check Your Internet Connection  ', style="red bold")
		sys.exit()

for page, code in zip(done_pages, done_status_codes):
	print()