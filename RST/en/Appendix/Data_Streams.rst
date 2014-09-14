Data Streams
============

Earthquake Library - test
------------------

.. external:: streams-earthquakes
    :url: https://github.com/RealTimeWeb/earthquakes
    
    Download the library below.

The United States Geological Service has a stream for all the earthquakes reported around the world. You can get all the earthquakes for the past hour, day, week, or even month. Notice that service reports the latest earthquakes, but does not remember between calls - it is up to the developer to determine if any of the quakes are new. Also, because of the way that earthquakes are reported, it is possible that over the course of the first hour more precise magnitudes could be found resulting in already reported quakes changing information between calls (however, this is something that can usually be ignored).

Example
^^^^^^^

>>> import earthquakes
# You can use either 'hour', 'day', 'week', or 'month'
>>> quakes = earthquakes.get_report('hour')
# The following code prints the latitude of the first earthquake
>>> quakes[0]['location']['latitude']
# If you have bad internet, put the following directly after your import
# and then you can work completely offline!
>>> earthquakes.disconnect()

Sample Data
^^^^^^^^^^^

The following demonstrates the sample data::

    report = [
        {
            # The location on a globe of the earthquake
            'location': {
                # The vertical part
                'latitude': 88,
                # The horizontal part
                'longitude': 74
            },
            # A human-readable name of the location
            'locationDescription': 'Santa Clara'
            # The strength of the earthquake on the Richter scale
            'magnitude': 3.1,
            # The time of the earthquake, measure in seconds since 1970
            'time': 128392739723,
        },
        ...
    ]


Geocode Library
---------------

.. external:: streams-geocode
    :url: https://github.com/RealTimeWeb/geocode
    
    Download the library below.

Google provides a service that accepts a given address, location, or landmark and returns available geographical information. The output data includes geographical coordinates, full address broken down into components, information about the type of address, and a few other fields.

Example
^^^^^^^
>>> import geocode


Sample Data
^^^^^^^^^^^

Lorem Ipsum



City Crimes Library
-------------------

.. external:: streams-citycrimes
    :url: http://google.com

    Download the library below.

Lorem Ipsum

Example
^^^^^^^

>>> import citycrime
# Get the crimes by state and population
>>> crimes = citycrime.get_crimes("State==VA and Population<200000")
# The following code prints the latitude of the first earthquake

Sample Data
^^^^^^^^^^^

Lorem Ipsum
