"""Method 1: The one which I did"""
""" Write code using find() and string slicing (see section 6.10) to extract the number at the end of 
the line below. Convert the extracted value to a floating point number and print it out."""

text = "X-DSPAM-Confidence:    0.8475"
ftext= text.find('0'), text.find('5')
stext = text[23:29]

num = float(stext)
print(num)

"""Method 2:
text = "X-DSPAM-Confidence:    0.8475"
ipos =  text.find(':')
print(ipos)
piece=str[ipos+2:]
print(piece)
"""
