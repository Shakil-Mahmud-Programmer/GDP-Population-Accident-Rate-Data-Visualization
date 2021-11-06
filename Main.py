import matplotlib.pyplot as plt, pandas as pd,numpy as np
gdp=pd.read_csv("file/data-gdp.csv")
population=pd.read_csv("file/data-population.csv")
accident=pd.read_csv("file/data-accident.csv")

plt.style.use('seaborn')
fig,ax=plt.subplots(3,1)
fig.suptitle('GDP, Population & Accident Rate\nby Shakil Mahmud',color='royalblue',size=14)
fig.tight_layout(pad=2)

ax[0].set_title('GDP Growth Rate',color='limegreen',size=10)
ax[0].bar(gdp['Year'],gdp['GDP Growth Rate'],color='limegreen',width=0.2,label='GDP')
ax[0].set_xlabel('Year',color='limegreen',size=9)
ax[0].set_ylabel('Rate',color='limegreen',size=9)
ax[0].legend()


ax[1].set_title('Population Growth Rate',color='fuchsia',size='10')
x_lab = population['Year']
x_pos=np.arange(len(population))
ax[1].set_xticks(x_pos)
ax[1].set_xticklabels(x_lab)
ax[1].bar(x_pos-0.2,population['Male'],color='deepskyblue',width=0.2,label='Male')
ax[1].bar(x_pos,population['Female'],color='fuchsia',width=0.2,label='Female')
ax[1].bar(x_pos+0.2,population['Population'],color='lime',width=0.2,label='Population')
ax[1].set_xlabel('Year',color='fuchsia',size=9)
ax[1].set_ylabel('Rate',color='fuchsia',size=9)
ax[1].legend()


x_lab2 = accident['Year']
x_pos2=np.arange(len(accident))
ax[2].set_xticks(x_pos2)
ax[2].set_xticklabels(x_lab2)
ax[2].set_title('Accident Rate',color='royalblue',size='10')
ax[2].bar(x_pos2-0.1,accident['Number of Accidents'],color='royalblue',width=0.1,label='Accidents')
ax[2].bar(x_pos2,accident['Injury'],color='darkorchid',width=0.1,label='Injury')
ax[2].bar(x_pos2+0.1,accident['Death'],color='crimson',width=0.1,label='Death')
ax[2].set_xlabel('Year',color='royalblue',size=9)
ax[2].set_ylabel('Accidents',color='royalblue',size=9)
ax[2].legend()


plt.show()