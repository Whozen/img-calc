from PIL import Image
from pytesseract import pytesseract
  
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Users\MyPC\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
image_path = r"job-source-count.png"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
  
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])

sum = 0
num = ''
i = 0
numsArr = []

while i < len(text):
    if text[i].isnumeric():
        while text[i].isnumeric():
            num += text[i]
            i += 1
        numsArr.append(num)
        sum += int(num)
        num = ''
    i += 1

print("The numbers are:")
for x in numsArr:
    print(x + " ")
print("Sum is {}".format(sum))