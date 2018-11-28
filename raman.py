
import matplotlib.pyplot as plt
import urllib.request
import sys
import os
url = input("rruff URL ( .txt or .rruff)\n@")
file_title = url.split('/')[-1]
urllib.request.urlretrieve(url,"{0}".format(file_title))
f = open(file_title).readlines()
RamanShift,Intensity,title_name = [],[],str()
for i in f:
    if not i[0]=="#" and len(i) >= 2:
        RamanShift.append(int((i.split(',')[0]).split('.')[0].rstrip()))
        Intensity.append(float((i.split(',')[1]).rstrip()))
    elif i.split('=')[0] == "##NAMES":
        title_name = i.split('=')[1].rstrip() + " "
    elif i.split('=')[0] == "##RRUFFID":
        title_name += i.split('=')[1].rstrip()

#plot
plt.figure()
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 10
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.width'] = 1.0
plt.rcParams['ytick.major.width'] = 1.0
plt.rcParams['lines.linewidth'] = 0.8
plt.title(str(title_name))
plt.plot(RamanShift,Intensity,color="red")
plt.xlabel(r"Raman Shift (cm$^{-1}$)")
plt.ylabel(r"Intensity")
plt.xlim(min(RamanShift),max(RamanShift))
plt.grid(which='major',color='lightgray',linestyle='-')
plt.grid(which='minor',color='lightgray',linestyle='-')
save_name = title_name.replace(" ","_")+'.png'
plt.savefig(save_name)
sel = input('open '+save_name+' ? (y/n) ')
if sel == 'y':os.system("open "+save_name)
