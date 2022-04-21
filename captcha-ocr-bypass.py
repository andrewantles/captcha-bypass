from PIL import Image
import requests
import easyocr

DEBUG = True

def solve_captcha():
	# Retrieve CAPTCHA image and cookies:
	r = requests.get('https://url.that.responds/with/captcha/challenges', stream=True)

	with open('tmp-img_' + str(counter) + '.jpg', 'wb') as fd:
	    for chunk in r.iter_content(chunk_size=128):
	        fd.write(chunk)

	img = Image.open('tmp-img_' + str(counter) + '.jpg')

	# Use EasyOCR on the image to retrieve text.
	reader = easyocr.Reader(['en'])
	text = reader.readtext('tmp-img_' + str(counter) + '.jpg', detail=0)

	if DEBUG: print("[-] Capthca processing: {}".format(str(text)))

	# Process the EasyOCR output and format for submission:
	output = ""
	for x in text:
		output += x

	post = output.replace(" ", "").replace("0", "O").replace("|", "I")

	if DEBUG: print("[-] Captcha solution is: {}".format(post))

	return post, r.cookies


counter = 10

while counter >= 0:
	bundle = solve_captcha()
	captcha = bundle[0]
	cookies = bundle[1]

	# Build URL parameter string: -adjust if using POST request: 
	# https://2.python-requests.org/projects/3/user/quickstart/
	payload = {'userid':'<username_to_check>' + str(counter) + 'test', 'captchastring':captcha}

	# Submit the username lookup request:
	s = requests.get(
			'https://url.that.accepts/usernames/and/captcha/solutions', 
			params=payload, 
			cookies=cookies
			) 

	if DEBUG: print("[-] Sending URL: {}".format(s.url))

	print("[*] Application response: {}".format(s.text))
	counter -= 1
