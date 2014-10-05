.. This file is part of the OpenDSA eTextbook project. See
.. http://algoviz.org/OpenDSA for more details.
.. Copyright (c) 2012-2013 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. avmetadata::
   :author: OpenDSA & CompThink Contributors
   :satisfies:
   :topic:


Visualization
=============

A significant challenge in working with any kind of data is how to present this data to answer questions of interest to  human observers. This challenge is especially critical for big data streams because of the volume, variety, or velocity of the data involved. Data of large volume has the potential to overwhelm an observers ability to extract meaning from the data. How should the voting data for every US citizen be portrayed to be of interest to political scientists? How should all of the genome data for a species be represented to answer interesting biological questions? How can all of the works of romantic poets be presented for literary analysis? Data of highly diverse variety is a challenge because the data forms of data might best be conveyed by different means. Integrating different representations in a meaningful way is difficult. For example health-related information contains family history, genomic data, medical test results, descriptions of exercise patterns, records of diet and nutrition, list of stress factors. How can all of this health-related information even for a single individual be displayed for best use by doctors?  Data with high velocity is changing so rapidly that interesting or significant aspects of the data might be lost. For example, how can stock market data be depicted so that meaningful trends can be seen by a stock analyst? How can data on the movement of vehicles in an urban road system be exhibited so that traffic engineers can determine better ways to avoid traffic jams?

Data visualization is often a useful way to present complex data. The adage that "A picture is worth a thousand words" reflects the power of the human visual system. Presenting data in a visual form leverages the ability of our visual systems to help us see patterns or to detect special cases of interest that are distinctive in some way. finding a good visualization is, of course, not always easy. The picture game "Where's Waldo" shows how easy it is to create a visual representation that hides the feature of interest.

There are a rich variety of ways to visualize data in both two and three dimensions. For example, here is a `gallery <http://matplotlib.org/gallery.html>`_ of  visualization that can be produced by the tools we will be using. Developing the knowledge and skills to build intricate and compelling visualizations is a study on its own. However, some basic forms of visualization are very useful for a number of "first step" explorations of big data. These basic forms are:

* line graphs: showing how data changes over time (e.g. how the value of a stock changes over the trading days).
* histograms: showing the distribution over a set of categories (e.g., how many earthquakes are there in a month in each of the six units on the Richter scale).
* map plots: showing the distribution over geographic space (e.g., where on the globe have earthquakes in the last month occurred).
* 2D plots: showing the correlation between two different factors (e.g., what is the relationship between the location of an earthquake and its latitude? or longitude?)

You can also think of visualizations that you see every day as other examples of how data is presented: weather maps, hurricane tracks, election maps.

We will be using *matplotlib* to illustrate visualization of data. Matplotlib is widely used and offers the capability to generate many different kinds of visualization in Python. We saw examples of its variety of visualization in the matplotlib gallery above. However, this utility comes at a price. Matplotlib is complicated. Fortunately, matplotlib is designed so that many *common cases* can be done with minimal or reasonable effort. In addition to matplotlib we will also look at a library for geographical plotting that is built on top of matplotlib.


Some Additional Python Features
-------------------------------

Matplotlib is an *industrial strength* visualization toolkit that has evolved in the Python community. To use matplotlib we will need to explore a few additional aspects of Python that are heavily used in matplotlib. Two aspects of Python that are elaborated are:

* packages and modules: these features help to organize large bodies of code into useful units for distribution and use

* function parameters and return values: these features help to deal with *common cases* so that not all of the parameters of a function need to be defined by the caller and to deal with functions that return more than one result.

Beyond their value in allowing us to use matplotlib, these additional features deepen your knowledge of Python. Also, encountering matplotlib gives some idea of how larger-scale software systems are programmed and organized.

Modules and Packages
^^^^^^^^^^^^^^^^^^^^
A large software library, like matplotlib, may have dozens or hundreds of functions that it makes available for reuse in building applications. In many applications only some of these functions are needed. To make the distribution and reuse easier the functions are usually grouped together, each group consisting of functions that are more likely to be needed together. In Python these groups of functions are called *modules*. We have already seen some examples of using the *import* facility in Python to make the functions in a module available for (re)use. Several modules may themselves be further grouped together in a bigger collection. In Python this bigger collection is called a *package*.

Matplotlib is a package containing a number of modules. One such module is the *pyplot* module. The *pyplot* module has many functions related to constructing 2D graphs and charts. Some of the functions in the *pyplot* module are the *plot*, *show*, *title*, *xlabel*, and *ylabel*  functions. We will see these functions used later.

The scheme used in Python to name a function in a package or module is called a "dotted notation". In this notation, the full name for the plot function is:

..  code::

    matplotlib.pyplot.show

However, Python provides a way to introduce a "nickname" for a module. This form of import is useful if there are several functions in a model that will be used. The nickname is given in the *import* statement as shown in this example:

..  code::

    import matplotlib.pyplot as plt

    # use the functions as

    plt.plot(...)    # plot some data
    plt.title(...)   # add a title
    plot.show(...)   # show the data in a window

where *plt* is the "nickname" defined in this program for the matplotlib.pyplot module.

If only a single (or a few) function(s) from a module are to be used then only that (those) function(s) can be imported. For example, we will see a package named *mpl_toolkits* that contains code for generating geographic plots. This package has a module named *basemap*, one of whose functions is named *Basemap* (note the difference in capitalization between the module name and the function name). In the code example to be seen, only the *Basemap* function is needed.

..  code::

    from mpl_toolkits.basemap import Basemap

    # use the Basemap function as

    map = Basemap(...)   #generate a geographic map to plot data on


It is important to remember that the *from...import...* only provides access to the *Basemap* function and not any other functions in the *mpl_toolkits.basemap* module.


More About Functions
^^^^^^^^^^^^^^^^^^^^

It is often the case that functions designed for general purpose use have many parameters. For example, the *matplotlib.pyplot.scatter* function for generating scatter plots has 14 parameters. This large number of parameters gives the programmer more control over the appearance of the scatter plot (e.g., the color of the plotted data  points, the symbol used to denote a plotted data point, the width of the line connecting points if a line is used, etc.).

In common cases many of the parameters for a general purpose function give more control than is desired. To ease the programmer's task Python allows the definer of a function to specify *default values* for parameters.  Here is the definition of the *matplotlib.pyplot.scatter* function showing its use of default values:

..  code::

     matplotlib.pyplot.scatter(x, y, s=20, c='b', marker='o', cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, hold=None, **kwargs)



In this example, the parameters *x* and *y* have no default values; they are required. The other parameters have default values are optional. The parameter *s* is defined so that if no no value is specified for this parameter then the function will use the default value *20*. Similarly, if no value is provided for the *marker* parameter then the function will use the default value of *'o'*. The value of *None* means that if no value is given for this parameter on the function call then the function will ignore those parts of its functionality that depend on having a value for this parameter. For example, the parameter *linewidths=None* means that if no linewidth is specified then the scatter plot will not connect the data points by a line (because connecting them a line would require having been told what line width to use).

Calling a function that has default parameters means that the function call only need mention those parameters whose default values we want to override. Of course, all required parameters (those without default values) must be given. When overriding a default value the syntax *pname=pthis" is used to specify that the parameter whose name is *pname* should have the value *pthis*. Here are some examples of calling the *scatter* function.

..  code::

    import matplotlib.pyplot as plt

    # define the data for the scatter plot

    lat  = [ ... ]     # data for the x values
    long = [ ... ]     # data for the y values

    plt.scatter(lat, long)                    # Call 1
    plt.scatter(lat, long, marker='+')        # Call 2
    plt.scatter(lat, long, c='r')             # Call 3
    plt.scatter(lat, long, marker='+' c='r')  # Call 4
    plt.scatter(lat, long, linewidths=2)      # Call 5


In this example the five calls on the *scatter* function all provide the required parameters. These calls mean:

* Call 1: use all default values for non-required parameters.
* Call 2: change the value for *marker* to *'+'* instead of the default value and use default values for all other non-required parameters.
* Call 3: change the value for *c* to *'r'* instead of the default value and use default values for all other non-required parameters.
* Call 4: change the value for *marker* to *'+'* instead of the default value, change the value for *c* to *'r'* instead of the default value, and use default values for all other non-required parameters.
* Call 5: change the value for *linewidths* to *2* instead of the default value and use default values for all other non-required parameters.

In summary, all required parameters will come first in order followed by the optional parameters in any order using the *pname=pthis* syntax.

A second aspect of functions that is sometimes used in general purpose functions is that they may return more than one value. For example, we saw earlier a function that converted a Fahrenheit temperature to the equivalent Celsius temperature. We also saw a function that converted a Fahrenheit temperature to the equivalent Kelvin temperature. Rather than having two functions we could define one function that return two values at the same time, the first a Celsius temperature and the second a Kelvin temperature. A cnvert function of this kind could be defined and used as follows:

.. code::

   def convert(temp):
      celsius = (temp - 32)/1.8
      kelvin  = ((temp + 459.67)*5) / 9
      return celsius, kelvin

   Ftemp = 76   # a Fahrenheit temperature

   Ctemp , Ktemp = convert(Ftemp)

Notice in this example that the return statement contains two values to return the first of which is the Celsius conversion and the second of which is the Kelvin conversion.  Notice also that the use of the *convert* function has two properties on the left side that are both updated as a result of the function call.


Matplotlib Examples
-------------------

Some basic *matplotlib* visualizations will be developed. These examples are meant to give a "flavor" of how *matplotlib works. For your project you will undoubtedly need to explore other aspects of *matplotlib*.

These examples use data collected from the data stream of worldwide earthquake events provided by the US Geological Survey. A months worth of reports were sampled to produce a small set to be used for demonstration purposes. The data set contains information on 140 earthquakes. For each earthquake the data stream was reduced to only three items:

* magnitudes: a list of the magnitude for each earthquake
* latitudes:  a list of the geographic latitude for each earthquake
* longitudes: a list of the the geographic longitude for each the earthquake


The sampled data set looks like this:

.. code::

     magnitudes = [
                    1.98, 1.8, 1.8, 1.7, 3.1, 2.0, 1.8, 0.6, 2.8, 0.5,
                    2.51, 3.51, 1.4, 2.6, 2.5, 2.4, 2.9, 2.6, 2.8, 2.5,
					... ]

    latitudes = [
                  39.6835 ,  60.5828 ,  47.4227 ,  38.8175 ,  19.1345 ,
                  19.4377 ,  60.0217 ,  38.7978 ,  19.1364 ,  38.8148 ,
				  ... ]

    longitudes = [
                  -119.8202 ,  -151.0144 ,  -120.1962 ,  -122.8042 ,  -66.4852 ,
                  -155.2545 ,  -152.0147 ,  -122.741 ,  -66.476 ,  -122.8202 ,
                  ... ]

The lists are organized so that a given earthquake is described by the triple (magnitudes[i], latitudes[i], longitudes[i]). For example, a 1.98 magnitude earth quake occurred at latitude 39.6835 and longitude -119.8202 and a magnitude 3.1 earthquake occurred at latitude 19.1345 and longitude -66.4852.

The lists are also organized by time: the first earthquake in the list occurred most recently and the last earthquake in the list occurred the longest in the past.

The complete sampled data set is contained in the file that can be downloaded for each of the examples below.


Line Graph
^^^^^^^^^^

A common data exploration question is whether there is any relationship of the data with time. For earthquakes we might want to see if there is any pattern, for example, where the magnitudes of the earthquakes rises over time and then decreases. To answer this question a ling graph can be created where the horizontal axis (x-axis) is time and the vertical axis (y-axis) is the magnitude of the earthquake. A related question is how the data relates to the average value of the data.

The following code uses *matplotlib* to produce a line graph of the magnitudes of the earthquakes. For visibility successive data points are connected by a line. A line representing the average value of the magnitudes is also drawn.


.. download_list:: python-viz-download-lines
    :files: Demo-Line-Graph.py

    The complete code for this example can be downloaded from here.

.. code::

   # Line Graph Example

   import matplotlib.pyplot as plt

   magnitudes = [
                 1.98, 1.8, 1.8, 1.7, 3.1, 2.0, 1.8, 0.6, 2.8, 0.5,
                 2.51, 3.51, 1.4, 2.6, 2.5, 2.4, 2.9, 2.6, 2.8, 2.5,
                 ...]

   # Compute average magnitude
   avMagnitude = sum(magnitudes)/len(magnitudes)

   # Plot magnitudes as a line graph
   plt.plot(magnitudes)

   # Add line for average magnitude: a line from (0,avMagnitude)
   #                                       to (len(magnitudes), avMagnitude)
   plt.plot([0, len(magnitudes)] , [avMagnitude, avMagnitude])

   # Label Axes and figure
   plt.xlabel('Time')
   plt.ylabel('Magnitude')
   plt.title('History of Magnitudes')

   # Display histogram
   plt.show()

   # Clear before the next graph
   plt.clf()

In general, the *pyplot* functions are used to build up a visualization. The visualization is then displayed in a separate window. The Python program waits until this window is closed before proceeding so that a number of visualizations can be constructed and viewed in sequence.

In the above code, the *import* statement is used to give a nickname for the *matplotlib.pyplot* module. The builtin *sum* and *len* functions are used to compute the average magnitude. The visualization is constructed by the following steps:

* the *plot* function is used to produce a line plot using the list of magnitudes.
* the plot function is used again using a list with two data points defining the endpoints of a straight line at the average value on the y-axis.
* the *xlable* and *ylable* functions add explanatory text labels to each axis.
* the display as a whole is given a title.

After the visualization has been constructed it can be displayed in a separate window using the *show* function. The program pauses at this point until the separate visualization window is closed. Finally, the *clf* function clears the internal structures that *matplotlib* uses to represent the visualization.

The visualization produced by the line graph code is shown below.

.. figure:: /Images/Python-Viz-Line-Graph.png
   :align: center

   The Line Graph Visualization

This visualization shows three things:

* there is no apparent pattern in the magnitudes over time
* there is considerable variability of magnitudes from the average
* earthquakes of the highest magnitudes are rare

This shows the value of even simple visualizations.

The window displayed by *matplotlib* has a number of controls in the lower left-hand corner.  Holding the cursor over any of the controls gives a brief description of that control. For the simple visualization we will be using three control are useful. These are:

* right-most control saves the visualization using any one of a variety of standard formats.
* the second control from the right is a zoom control. Pushing this control changes the cursor in the visualization window to a "+" symbol using which a rectangle can be selected. The display will zoom in on this region.
* the third control from the right is a pan-zoom control. Pushing this control changes the cursor in the visualization window to a symbol with two crossed double arrow heads. With the left mouse button down the display can be moved around. With the right mouse button down the display can be compressed and stretch horizontally or vertically.
* the left-most control returns the visualization to its original state.

You should run the line graph code and experiment with these controls.

Exercise. Add to the Line Chart program so that the visualization shows not only a line for the average but two additional lines - one a standard deviation above the average and one a standard deviation below the average. Note: the *numpy* module has a function *std* that computes the standard deviation of a list of numbers. Give the code and provide a .png image of the result.


Histogram
^^^^^^^^^

The line chart shows that there is a significant variation in the magnitudes. However, it is difficult to see from the line chart the distribution of the magnitudes. A histogram is a simple visualization of the distribution of data. In the code below the *matplotlib* function *hist* is used visualize the distribution of the earthquake magnitudes. The complete code for this example can be downloaded from here.

..  code::

    # Histogram Example

    import matplotlib.pyplot as plt


    # Sampled earthquake magnitudes from real data stream

    magnitudes = [
          1.98, 1.8, 1.8, 1.7, 3.1, 2.0, 1.8, 0.6, 2.8, 0.5,
          2.51, 3.51, 1.4, 2.6, 2.5, 2.4, 2.9, 2.6, 2.8, 2.5,
          ...]


   # Plot histogram of magnitudes
   plt.hist(magnitudes, bins=[0,1,2,3,4,5,6,7])

   # Label Axis
   plt.xlabel('Magnitudes')
   plt.ylabel('Occurrences')
   plt.title('Histogram of Magnitudes')

   # Display histogram
   plt.show()

   # Clear before the next set of graphs
   plt.clf()

Much of the code in the histogram was described in the earlier example. What is new in this example is the *hist* function. The *hist* function call the first parameter is the list of magnitudes and the second parameter is for a parameter names *bins*. The *bins* parameter allows the caller to specify the categories for the distribution. Earthquake magnitudes are measured on the Richter scale. We can see from the line graph that the highest value in our data set is between 6 and 7. The *bins* value given in the histogram call specifies that the magnitude data should be grouped into the categories 0-1, 1-2, ..., 6-7.

The histogram produced by the example program is shown next.

.. figure:: /Images/Python-Viz-Histogram.png
   :align: center

   The Histogram Visualization

This visualization shows:

* the distribution is highly skewed with the vast majority of the magnitudes at or below magnitude 2
* there are no earthquakes (at least in this data) in the 5-6 category
* the most serious earthquakes (those in category 6) are rare

We now know something about the nature of earthquake magnitudes. But we would also like to know something about the characteristics of where earthquakes occur. This is what will be seen next.

Exercise. Remove the bins argument and observe the difference. With no bins argument the histogram function decides on how many categories to use and what the boundaries of these categories are.

Exercise. Read the documentation for *pyplot.hist*. Modify the histogram example program to form a cumulative distribution function.

Scatter Plot
^^^^^^^^^^^^

A question for many data sets is whether two items are related to each other in some way, that is, are they correlated. In our case, we might be interested in knowing whether there is any relationship between the latitude and longitude of earthquakes. In other words, do earthquakes occur "all over the place" or are there certain locations that have a higher incidence of earthquakes.

To examine questions of correlation between two sets of data a scatter plot can be used. One set of data is treated as coordinates on the  horizontal axis (x-axis) and the other set of data is treated as coordinates on the vertical axis (y-axis). A point is plotted in the scatter plot at (x[i], y[i]) where x[i] is an element of one data set and y[i] is the corresponding element of the other data set.

A random arrangements of points on the scatter plot means that there is no correlation. Clusters of points or patterns in the arrangements of point are visual evidence of a possible correlation. Statistical methods must be used to determine whether the apparent correlation is significant more merely random chance.

A scatter plot of the longitude and latitude of earthquakes is shown in the following code sample. The full code can be downloaded from here.

.. code::

   # Scatter Plot

   import matplotlib.pyplot as plt


   # Sampled earthquake latitude and longitudes from real data stream
   # Earthquake i occurred at the location (latitude[i], longitude[i])


   latitudes = [
                 39.6835 ,  60.5828 ,  47.4227 ,  38.8175 ,  19.1345 ,
                 19.4377 ,  60.0217 ,  38.7978 ,  19.1364 ,  38.8148 ,
               ... ]

   longitudes = [
                 -119.8202 ,  -151.0144 ,  -120.1962 ,  -122.8042 ,  -66.4852 ,
                 -155.2545 ,  -152.0147 ,  -122.741 ,  -66.476 ,  -122.8202 ,
                ...]


   # Generate scatter plot of locations of earthquakes on a 2D grid
   # At each earthquake location (longitude[i], latitude[i]) put a red '+' sign

   plt.scatter(longitudes, latitudes, c='r', marker='+')


   # Label Axes
   plt.xlabel('Longitude')
   plt.ylabel('Latitude')
   plt.title('Earthquake Occurrences')
   plt.show()

   # Clear before the next set of graphs
   plt.clf()


Most of the code in the scatter plot example should be familiar from the earlier examples. The new element is the use of the *pyplot.scatter* function to generate the scatter plot itself. The two required parameters are the two lists of data which are, in our case, the longitude and latitude of each earthquake. There are two optional parameters used. The parameter named *c* allows the caller to specify what color to use for the points that are plotted. A red color is represented by the letter *'r'*. The second optional parameter, named *marker* allows the caller to specify what symbol to use for a plotted point. In this case a *'+'* symbol is used.

The scatter plot visualization produced by the example program is shown below. It is clear from this visualization that there are definite clusters in the data. This means that the earthquakes described in our sample daa appear to have a tendency to occur in some places more than other.


.. figure:: /Images/Python-Viz-Scatter-Plot.png
   :align: center

   The Scatter Plot Visualization

If we use the pan-zoom controls on the *matplotlib* display window we can see how localized the clustering of earthquakes is. The following figure shows a close-up view of the cluster of earthquakes in the upper left hand corner.

.. figure:: /Images/Python-Viz-Scatter-Plot-Zoom.png
   :align: center

   Englarged view of a cluster in the scatter plot visualization

We can see in the enlarged view of the earthquake cluster that a sizeable number of earthquakes occur in the region between -160 and -140 degrees of longitude and between 60 and 65 degree of latitude. The other clusters of earthquakes could be explored in a similar way.

This scatter plot does not tell us, however, what relationship there might be between these clusters and the magnitudes of the earthquakes. Do the clusters contain earthquakes that are frequent but have small magnitudes and the large magnitude earthquakes happen in other locations? or Do the larger magnitude earthquakes also occur in these clusters? Additional analysis of the data would be needed to answer this question.

Exercise. Filter the earthquake data to produce a data set that is only for those earthquakes in the region between -160 and -140 degrees of longitude and between 60 and 65 degree of latitude. Plot the distribution of the magnitudes of these earthquakes. What conclusions can you draw? Submit the code, the .png file of the visualization and the text of your conclusions.

The scatter plot above also does not show us very clearly where on the globe the earthquakes are occurring. This is especially interesting for the clusters that we have seen. The map plots below answer this question.

Map Plot
^^^^^^^^

A visualization often needs to depict data on some form of geographic map. In our case we are plotting earthquake data which can be plotted on a globe or country map to show where in the world or country the earthquakes occurred. There are many other cases where geographic mapping is useful. Visualizations with geographic maps is a good way to display voter data, epidemiology data, weather data, population data, natural resource data, and others.

Latitude and longitude coordinates identify a point on the spherical globe. Making a 2D visualization of these points is slightly tricky. As an analogy, imagine drawing a dots with a magic marker on an orange. Making a 2D map is like peeling the rind from the orange and laying out the rind pieces flat. How do do this so that points on the surface of the orange are easily recognizable. Sometimes its easier to see the pattern in the points if we "stretch" the rind to form a more uniform surface. But this stretching also distorts the distance between points. Cartographers, people who make maps, have devised a number of different ways to "project" the surface of a 3D spherical globe onto a flat 2D plane. Here is more information on `map projections <http://en.wikipedia.org/wiki/Map_projection>`_ . The example developed below uses a *Hammer* projection, named for Ernst Hammer who developed it in 1892. The Hammer projection looks like this:

..  figure:: /Images/Python-Viz-Hammer-Projection.jpg
   :align: center

   The Hammer projection.

The example code below does map projections using the *Basemap* function. This function is part of the *mpl_toolkits* package*. This package contains a number of modules the are built "on top of" *matplotlib* and extend the functionality of *matplotlib* in a variety of specific application areas. The *basemap* module contains the function *Basemap* (note the difference in capitalization between the module name and the function name). The *Basemap* function implements a variety of map projections, like the Hammer projection. The set of available projections is described in the `Basemap documentation <http://matplotlib.org/basemap/users/index.html>`_ .


The key steps in generating a globe-based visualization of data are:

1. use *Basemap* to define a map projection,
2. use the map projection to convert latitude and longitude coordinates into the corresponding coordinates in that map projection, and
3. use the *matplotlib.scatter* function to plot the transformed coordinates on the map

These there steps are marked by comments in the code below. The complete code can be downloaded here.

..  code::


    # Map plot using the Hammer projection

    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap


   # Sampled earthquake latitude and longitudes from real data stream
   # Earthquake i occurred at the location (latitude[i], longitude[i])


   latitudes = [
                 39.6835 ,  60.5828 ,  47.4227 ,  38.8175 ,  19.1345 ,
                 19.4377 ,  60.0217 ,  38.7978 ,  19.1364 ,  38.8148 ,
               ... ]

   longitudes = [
                 -119.8202 ,  -151.0144 ,  -120.1962 ,  -122.8042 ,  -66.4852 ,
                 -155.2545 ,  -152.0147 ,  -122.741 ,  -66.476 ,  -122.8202 ,
                ...]

   # Create world map with a Hammer (eliptical, equal-area) projection
   # centered at 180 degrees longitude (i.e. longitude zero of the
   # visualization is longitude 180 on the globe)
   map = Basemap(projection='hammer',lon_0=180)   # Step 1

   # Fill in the outlines of continents
   map.drawcoastlines()

   # Convert latitudes and longitudes to coordinates on the world map
   x, y = map(longitudes,latitudes)              # Step 2

   # Map the locations onto the world map
   map.scatter(x, y)                             # Step 3

   plt.title('Locations of earthquakes')
   plt.show()

   plt.clf()


Notice that the *Basemap* function returns a *map* that encodes the details of how to perform the projection (Step 1). This *map* is used (Step 2) to project its two parameters (the latitude and longitude data) and returns two values (the projected x and y coordinates). These projected coordinates are used as input to the *scatter* plot function (Step 3). To make the visualization easier to understand the *drawcoastlines* functions is used to show the continents. Here is the resulting visualization.

.. figure:: /Images/Python-Viz-Map-Plot-Hammer.png
   :align: center

   Earthquake data plotted on a globe map (Hammer projection)

The globe visualization shows that the two clusters of earthquakes seen earlier are located on the coasts of California and Alaska. In general, it can be seen that the majority of the earthquakes are in the Pacific rim. Much more extensive data would be needed to study in more detail the distribution of earthquakes.

Going Further
-------------

This brief description is only the tip of the iceberg. It is only meant to give a brief orientation to the general style of matplotlib usage. There is much more that matplotlib can do. You will undoubtedly want to use some of the more advanced features of matplotlib in your project. There is a lot of help that you will find on the web. One starting point is this `tutorial <http://pythonprogramming.net/matplotlib-graphing-series/>`_ . There are many others to be found. Also available is the matplotlib `documentation <http://matplotlib.org/api/pyplot_api.html>`_ .







