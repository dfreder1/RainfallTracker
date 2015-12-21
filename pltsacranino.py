import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
from matplotlib.cbook import get_sample_data
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import datetime

fname = get_sample_data('/Users/userdoug/documents/projects/sacranino/data/OutputCSV2.csv')
gender_degree_data = csv2rec(fname)
#
fnamecurrentyear = get_sample_data('/Users/userdoug/documents/projects/sacranino/data/gaugeSAE')
current_year_data = csv2rec(fnamecurrentyear)

# These are the colors that will be used in the plot
color_sequence = ['#000080', '#6495ed', '#006400', '#deb887', '#cd853f']

# You typically want your plot to be ~1.33x wider than tall. 
# Common sizes: (10, 7.5) and (12, 9)
fig, ax = plt.subplots(1, 1, figsize=(12, 9))

# Remove the plot frame lines. They are unnecessary here.
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

# Ensure that the axis ticks only show up on the bottom and left of the plot.
# Ticks on the right and top of the plot are generally unnecessary.
ax.get_xaxis().tick_bottom()
ax.get_yaxis().tick_left()

# Limit the range of the plot to only where the data is.
# Avoid unnecessary whitespace.
plt.xlim(0,249)
plt.ylim(-0.25, 37)

# Make sure your axis ticks are large enough to be easily read.
# You don't want your viewers squinting to read your plot.
#plt.xticks(range(1970, 1971, 10), fontsize=14)
#plt.yticks(range(0, 91, 10), ['{0}%'.format(x)
                               # for x in range(0, 91, 10)], fontsize=14)

# Provide tick lines across the plot to help your viewers trace along
# the axis ticks. Make sure that the lines are light and small so they
# don't obscure the primary data lines.
#for y in range(5, 36, 5):
#    plt.plot(range(10, 221), [y] * len(range(10,221)), '--',lw=0.5, color='black', alpha=0.3)
# Remove the tick marks; they are unnecessary with the tick lines we just
# plotted.
plt.tick_params(axis='both', which='both', bottom='off', top='off',
                labelbottom='on', left='off', right='off', labelleft='on')

# Now that the plot is prepared, it's time to actually plot the data!
paststorms= ['1982', '1997', 'Average Year','2014', '1976']

y_offsets = {'1982': 0.5, '1997': 0.5,
             'Average Year': 0.5, '2014': 0.5,
             '1976': 0.5}

for rank, column in enumerate(paststorms):
    # Plot each line separately with its own color.
    column_rec_name = column.replace('\n', '_').replace(' ', '_').lower()
    print column_rec_name
    print gender_degree_data.date
    print gender_degree_data[column_rec_name]
    line = plt.plot(gender_degree_data.date,gender_degree_data[column_rec_name],lw=2.5,color=color_sequence[rank])
    # The rank is 0, so could delete it, column is the number of items listed

    # Add a text label to the right end of every line. Most of the code below
    # is adding specific offsets y position because some labels overlapped.
    y_pos = gender_degree_data[column_rec_name][-1] - 0.5

    if column in y_offsets:
        y_pos += y_offsets[column]

    # Again, make sure that all labels are large enough to be easily read
    # by the viewer.
    plt.text(213, y_pos, column, fontsize=16, color=color_sequence[rank])

currentstorms = ['Rainfall']
for rank, column in enumerate(currentstorms):
    column_rec_name = column.replace('\n', '_').replace(' ', '_').lower()
    print column_rec_name
    print str(current_year_data.date[-1])[:10]
    #print str(current_year_data.date)[:10]
    #print a.strftime('Timestamp %d %b, %Y')
#    print a
    print current_year_data.elapseddays
    print current_year_data[column_rec_name]
    line = plt.plot(current_year_data.elapseddays,current_year_data[column_rec_name],lw=4.5,color='black')
    #plt.text(current_year_data.elapseddays[-1]+4,current_year_data[column_rec_name][-1]-1, 'So Far\nThis Season',fontsize=16, color='black')
    lastdatescraped='So far this year\nUpdated '+str(current_year_data.date[-1])[:10]
    plt.text(240, 34,'El Nino Years',fontsize=16, color='blue', rotation=90)
    plt.text(240, 11,'Drought Years',fontsize=16, color='brown', rotation=90)
    plt.text(current_year_data.elapseddays[-1]+4,current_year_data[column_rec_name][-1], lastdatescraped,fontsize=10, color='black')
    plt.plot(current_year_data.elapseddays[-1],current_year_data[column_rec_name][-1], marker='x',markersize=10,markeredgewidth=5 ,color='black')
# Make the title big enough so it spans the entire plot, but don't make it
# so big that it requires two lines to show.

# Note that if the title is descriptive enough, it is unnecessary to include
# axis labels
plt.title('2015-2016 Wet Season\nEl Nino Tracking\nIn Sacramento', x=0.12, y=0.70, fontsize=24, ha='left')
ax.set_ylabel('Inches of Rainfall at Sacramento Executive Airport',fontsize=16)
ax.set_xlabel('Days After October 1',fontsize=16)
# Finally, save the figure as a PNG.
# You can also save it as a PDF, JPEG, etc.
# Just change the file extension in this call.
plt.savefig('outputcsv.png', bbox_inches='tight')
