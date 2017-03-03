import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.mlab import csv2rec
from matplotlib.cbook import get_sample_data
import datetime
from sys import platform as _platform
#
# Change the location of the files depending on mac or linux
#   
if _platform == "linux" or _platform == "linux2":
    fname = get_sample_data('/var/www/html/projects/Rainfall/2016-17/RainfallTracker/data/pastyears.csv')
    fnamecurrentyear = get_sample_data('/var/www/html/projects/Rainfall/2016-17/RainfallTracker/data/gaugeSAE')
elif _platform == "darwin":
    print 'Running on Mac'
    fname = get_sample_data('/Users/userdoug/documents/projects/Rainfall/2016-17/RainfallTracker/data/pastyears.csv')
    fnamecurrentyear = get_sample_data('/Users/userdoug/documents/projects/Rainfall/2016-17/RainfallTracker/data/gaugeSAE')
elif _platform == "win32":
    print 'not supported'
#
past_years_data = csv2rec(fname)
current_year_data = csv2rec(fnamecurrentyear)
#
# These are the colors that will be used in the plot
color_sequence = ['#000080', '#6495ed', '#006400', '#deb887', '#cd853f']

# You typically want your plot to be ~1.33x wider than tall. 
# Common sizes: (10, 7.5) and (12, 9)
fig, ax = plt.subplots(1, 1, figsize=(10, 8))

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
    print past_years_data.date
    print past_years_data[column_rec_name]
    line = plt.plot(past_years_data.date,past_years_data[column_rec_name],lw=2.5,color=color_sequence[rank])
    # The rank is 0, so could delete it, column is the number of items listed
    # Add a text label to the right end of every line. Most of the code below
    # is adding specific offsets y position because some labels overlapped.
    y_pos = past_years_data[column_rec_name][-1] - 0.5
#
    if column in y_offsets:
        y_pos += y_offsets[column]
#
    # Again, make sure that all labels are large enough to be easily read
    # by the viewer.
    plt.text(213, y_pos, column, fontsize=16, color=color_sequence[rank])
#
currentstorms = ['Rainfall']
for rank, column in enumerate(currentstorms):
    column_rec_name = column.replace('\n', '_').replace(' ', '_').lower()
    print column_rec_name
    print str(current_year_data.date[-1])[:10]
    print current_year_data.elapseddays
    print current_year_data[column_rec_name]
    line = plt.plot(current_year_data.elapseddays,current_year_data[column_rec_name],lw=4.5,color='black')
#    lastdatescraped='So far this year\nUpdated '+str(current_year_data.date[-1])[:10]
#    lastdatescraped='So far this year, Updated '+str(current_year_data.date[-1])[:10]
    lastdatescraped=str(current_year_data.date[-1])[:10]
    plt.text(240, 34,'El Nino Years',fontsize=16, color='blue', rotation=90)
    plt.text(240, 11,'Drought Years',fontsize=16, color='brown', rotation=90)
#    plt.annotate(lastdatescraped, xy=(current_year_data.elapseddays[-1]-2,current_year_data[column_rec_name][-1]+1), xytext=(current_year_data.elapseddays[-1]-12,current_year_data[column_rec_name][-1]+3), arrowprops=dict(facecolor='black', shrink=0.00, width=2.5, headwidth=9),horizontalalignment='right', fontsize=12, )
    plt.annotate(lastdatescraped, xy=(current_year_data.elapseddays[-1]-0,current_year_data[column_rec_name][-1]+0), xytext=(current_year_data.elapseddays[-1]-12,current_year_data[column_rec_name][-1]+3), arrowprops=dict(facecolor='black', shrink=0.10, width=2.5, headwidth=9, frac=.25),horizontalalignment='right', fontsize=12, )
#    plt.text(current_year_data.elapseddays[-1]+0,current_year_data[column_rec_name][-1]+1, lastdatescraped, fontsize=16, color='black', rotation=00, horizontalalignment='center', verticalalignment='bottom', backgroundcolor='white')
    plt.plot(current_year_data.elapseddays[-1],current_year_data[column_rec_name][-1], marker='o',markersize=10,markeredgewidth=2, fillstyle='none',color='black')
# Make the title big enough so it spans the entire plot, but don't make it
# so big that it requires two lines to show.
#
# Note that if the title is descriptive enough, it is unnecessary to include
# axis labels
plt.title('2016-2017 Wet Season\nRainfall Tracking\nIn Sacramento\nUpdated Daily', x=0.03, y=0.72, fontsize=24, ha='left')
ax.set_ylabel('Inches of Rainfall at Sacramento Executive Airport',fontsize=16)
ax.set_xlabel('Days After October 1',fontsize=16)
# Finally, save the figure as a PNG.
# You can also save it as a PDF, JPEG, etc.
# Just change the file extension in this call.
#
if _platform == "linux" or _platform == "linux2":
    plt.savefig('/var/www/html/projects/Rainfall/2016-17/RainfallTracker/outputcsv.png', bbox_inches='tight')
elif _platform == "darwin":
    plt.savefig('outputcsv.png', bbox_inches='tight')
elif _platform == "win32":
    print 'not supported'
