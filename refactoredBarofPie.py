import matplotlib.pyplot as plt
import fixedData


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
fig.tight_layout(h_pad=None, w_pad=None, rect=None)
fig.subplots_adjust(left=0.03, right=0.94, top=0.92, bottom=0.05,wspace=0)

overall_ratios = [fixedData.plasticPercent, fixedData.clothPercent, fixedData.paperPercent, 
                  fixedData.metalPercent,fixedData.otherPercent]
labels = ['Plastic', 'Cloth', 'Paper', 'Metal','Other']
explode = [0.1, 0, 0, 0, 0]
# rotate so that first wedge is split by the x-axis
angle = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, explode=explode, colors=["#8093f1","#72ddf7", "#b388eb", "#f7aef8","#fdc5f5"])

# bar chart parameters
type_percent = fixedData.plasticBreakdownPercent
type_labels = fixedData.plasticItems
bottom = 1
width = .1

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(type_percent, type_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, label=label, color = ['#506BB6'],alpha=0.1 + 0.1 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

ax1.set_title('Wardie Bay - Rubbish Collected')
ax2.set_title('Plastic Breakdown')
ax2.legend(loc='upper right', fontsize=8,bbox_to_anchor=(1.1, 1))
ax2.axis('off')
ax2.set_xlim(- 2.5 * width, 2.5 * width)

# use ConnectionPatch to draw lines between the two plots
theta1, theta2 = wedges[0].theta1, wedges[0].theta2
center, r = wedges[0].center, wedges[0].r
bar_height = sum(type_percent)

plt.show()