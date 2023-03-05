import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import random

areas={
	"Training Forest":[1,45,'good'],
	"Wakare Camp":[10, 65, 'moderate'],
	"Kakuzetsu Swamp":[40,95, 'bad'],
	"Hitokuro Whole":[35,135,'moderate'],
	"Wolf Cave (Hito)":[30,90,'moderate'],
	"Burnt Mansion":[1,55,'bad'],
	"Hitokurou North":[35,65,'good'],
	"Hitokurou South":[60,135,'good'],
	"Yamayuki":[150,210, 'good'],
	"Atsusugi Desert \n(Desert)":[70,130,'moderate'],
	"Atsusugi Desert \n(Ruins)":[90,150,'good'],
	"Atsusugi Temple":[195,255, 'good'],
	"Riyoku Facility":[245,300, 'good']
	}
area_names = [name for name in areas.keys()]
area_lows = [range[0] for range in areas.values()]
area_highs = [range[1] for range in areas.values()]
area_quality = [values[2] for values in areas.values()]

fig = plt.gcf()
ax = plt.gcf().subplots()
#ax.xaxis.grid(True,color="black")
ax.set_axisbelow(True)
ax.xaxis.grid(color="black")

#index = np.arange(len(areas))
wide = 0.25
color_select = {"good":"green","moderate":"yellow","bad":"red","no-data":"gray"}

for index in range(len(areas.keys())):
	rand_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
	area_range = area_highs[index] - area_lows[index]
	color_choice = color_select[area_quality[index]]
	plt.barh(area_names[index], area_range, color=color_choice, left=area_lows[index], label=area_names[index])
plt.title("Area Level Ranges")
plt.xlabel("Level range")
plt.ylabel("Area")
plt.xlim(0,300)
plt.xticks(range(0,301,25))



legend_handles = [mpatches.Patch(color=value,label=key) for key,value in color_select.items()]
#legend_handles = [color for color in color_select.values()]
#legend_labels = [quality for quality in color_select.keys()]
plt.legend(handles=legend_handles, loc=4)



#plt.legend(handles=legend_handles, labels=legend_labels, loc=4)
#test_lege = mpatches.Patch(color="green",label = "good")
#plt.legend(handles=[test_lege])
plt.show()