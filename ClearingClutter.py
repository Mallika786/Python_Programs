import os
import random
import string

# # if os.path.exists("png1_file"):
# os.mkdir("png1_file")
# # if os.path.exists("pdf1_file"):
# os.mkdir("pdf1_file")
# # if os.path.exists("webp1_file"):
# os.mkdir("webp1_file")

# for i in range (1,11):
#     r1=random.choice(string.ascii_lowercase)
#     r2=random.choice(string.ascii_lowercase)
#     r3=random.choice(string.ascii_lowercase)
#     r4=random.choice(string.ascii_lowercase)
#     os.mkdir(f"png1_file/{r1}{r2}{r3}{r4}.png")

# for i in range (1,11):
#     r1=random.choice(string.ascii_lowercase)
#     r2=random.choice(string.ascii_lowercase)
#     r3=random.choice(string.ascii_lowercase)
#     r4=random.choice(string.ascii_lowercase)
#     os.mkdir(f"pdf1_file/{r1}{r2}{r3}{r4}.pdf")

# for i in range (1,11):
#     r1=random.choice(string.ascii_lowercase)
#     r2=random.choice(string.ascii_lowercase)
#     r3=random.choice(string.ascii_lowercase)
#     r4=random.choice(string.ascii_lowercase)
#     os.mkdir(f"webp1_file/{r1}{r2}{r3}{r4}.webp")




# clearing clutter
fl=os.listdir("png1_file")
a=1
for i in fl:
    if(i.endswith(".png")):
        os.rename(f"png1_file/{i}",f"png1_file/{a}.png")
        a=a+1

fl=os.listdir("pdf1_file")
a=1
for i in fl:
    if(i.endswith(".pdf")):
        os.rename(f"pdf1_file/{i}",f"pdf1_file/{a}.pdf")
        a=a+1

fl=os.listdir("webp1_file")
a=1
for i in fl:
    if(i.endswith(".webp")):
        os.rename(f"webp1_file/{i}",f"webp1_file/{a}.pdf")
        a=a+1

