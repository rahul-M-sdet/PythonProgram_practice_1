import re

str="!@#123WER"

special_char=re.compile("!@#$%^&*()-+=?<>")
if special_char.search(str)==-1:
    print("No special char")
else:
    print("Special char")