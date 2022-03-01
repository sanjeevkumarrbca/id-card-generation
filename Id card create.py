#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install qrcode')


# In[3]:


from PIL import Image, ImageDraw, ImageFont
import random
import os
import datetime
import qrcode


# In[4]:


image = Image.new('RGB', (1000,900), (255, 255, 255))
draw = ImageDraw.Draw(image)


# In[5]:


font = ImageFont.truetype('arial.ttf', size=45)
os.system("ID CARD Generator")


# In[6]:


d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%Y\t ID CARD Generator\t  %I:%M:%S %p")
print (reg_format_date)


# In[7]:


print('\n\nAll Fields are Mandatory') 
print('Avoid any kind of Spelling Mistakes')
print('Write Everything in uppercase letters')
(x, y) = (50, 50)
message = input('\nEnter Your Company Name: ')
company=message
color = 'rgb(0, 0, 0)'
font = ImageFont.truetype('arial.ttf', size=50)
draw.text((x, y), message, fill=color, font=font)


# In[8]:


# adding an unique id number. You can manually take it from user
(x, y) = (600, 75)
idno=random.randint(10000000,90000000)
message = str('ID '+str(idno))
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=60)
draw.text((x, y), message, fill=color, font=font)


# In[9]:


(x, y) = (50, 250)
message = input('Enter Your Full Name: ')
name=message
color = 'rgb(0, 0, 0)' # black color
font = ImageFont.truetype('arial.ttf', size=45)
draw.text((x, y), message, fill=color, font=font)


# In[10]:


(x, y) = (50, 350)
message = input('Enter Your Gender: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)
(x, y) = (250, 350)
message = input('Enter Your Age: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)


# In[11]:


(x, y) = (50, 450)
message = input('Enter Your Date Of Birth: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)


# In[12]:


(x, y) = (50, 550)
message = input('Enter Your Blood Group: ')
color = 'rgb(255, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)


# In[ ]:


(x, y) = (50, 650)
message = input('Enter Your Mobile Number: ')
temp=message
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)



# In[ ]:



(x, y) = (50, 750)
message = input('Enter Your Address: ')
color = 'rgb(0, 0, 0)' # black color 
draw.text((x, y), message, fill=color, font=font)


# In[ ]:


image.save(str(name)+'.png')


# In[ ]:


img = qrcode.make(str(company)+str(idno))   # this info. is added in QR code, also add other things
img.save(str(idno)+'.bmp')


# In[ ]:


til = Image.open(name+'.png')
im = Image.open(str(idno)+'.bmp') #25x25
til.paste(im,(600,350))
til.save(name+'.png')


# In[ ]:


print(('\n\n\nYour ID Card Successfully created in a PNG file '+name+'.png'))
eval(input('\n\nPress any key to Close program...'))



# In[ ]:




