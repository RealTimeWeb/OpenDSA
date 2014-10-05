.. This file is part of the OpenDSA eTextbook project. See
.. http://algoviz.org/OpenDSA for more details.
.. Copyright (c) 2012-2013 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. avmetadata::
   :author: OpenDSA & CompThink Contributors
   :satisfies:
   :topic:


Blockly and Big Data
====================

Blockly is useful not only for the simple examples we have seen so far (e..g, the Maze problems) but also for constructing algorithms and programs that manipulate realistic data. We are now going to start learning how to use Blockly to access and manipulate "big data" streams. The streams we will start with are small versions of the actual big data. These small versions are used so that it is possible to view all of the data we are working with as an aid in learning. However, the programs we are building will work not only for these small stream but for the actual big data streams themselves.


Exploring the Big Data Blocks
-----------------------------

The Blockly environment we will be working with is shown below. This is a "live" workspace in which you can develop and run Blockly programs interactively. The palette of blocks on the left is organized into six categories. The work space for building the Blockly program is on the right. Two blocks have been loaded into the work space and linked together. In the bottom right corner is a trash can icon. Blocks in the workspace that are not needed can be dragged into the trash can to clear them from the workspace. At the top are two controls. The "Run" control executes the program in the work space. The "Python" control displays a window containing the complete Python code that corresponds to the Blockly program in the workspace. Any results printed by the program when is it is executed by the "Run" control is shown in the output area at the bottom.

We will not look now at the Python code now but you can look at this code whenever you are curious. You should be able to recognize at least some parts of the correspondence between the Blockly representation of the program and the Python equivalent. Seeing the Python code for a Blockly program is further evidence that Blockly itself is a "real" programming language. Eventually we will make the transition from building programs in Blockly to building them directly and exclusively in Python. While Blockly is a good learning aid we will eventually be able to write larger programs more quickly by using Python directly.


The palette of blocks is organized into six categories.  The categories can the following kinds of blocks:

* Controls: blocks for decision and iteration
* Logic: blocks for complex conditions used in decisions
* Math: blocks for calculating
* Text: blocks for printing (to the output area) and prompting for input
* Variables: for setting the value of a property
* Big Data: blocks for accessing a big data stream

You can explore the blocks in each category by clicking on the category name. There are more blocks in this palette than we will need immediately. Many of the other blocks will be needed as we advance to more interesting problems.

A word about terminology is needed here. In Blockly (and many other programming languages) what we have been referring to as a "variable property" (or sometimes just "property") is referred to as a "variable".

Explore the workspace below but leave the two original blocks in the workspace. Look at the set of available blocks in each category so that you know what blocks you have available to solve the problems we will be working with in this section. Drag some blocks into the workspace, assemble them together, and clear the workspace by moving all of the blocks to the trash can.


.. blockly:: blockly-bigdata1
   :submission:

   preload::
   <xml xmlns="http://www.w3.org/1999/xhtml">
       <block type="text_print" inline="false" x="53" y="213">
	      <value name="TEXT">
	         <block type="weather_get_temperature">
		         <title name="CITY">BLACKSBURG</title>
		     </block>
		   </value>
	   </block>
   </xml>


You will notice that there are four blocks in the Big Data category. Two of the blocks give access to weather data and two of the blocks give access to stock market data.  These blocks are:

* get temperature for: returns a single number that is the temperature in Fahrenheit for the selected city
* get forecasts for: returns a list of numbers with the temperature forecast over the next nine days for the selected city
* get current stock for: returns a single number that is the current *change* in the value of the selected stock
* get past stocks for: returns a list of numbers with the nine most recently reported changes in the value of the selected stock

Two of the blocks return single numbers and two of the blocks return a list of numbers. We will see in the following examples how to construct small Blockly programs that use calculation, sequence, decision, and iteration to process the data returned by these blocks.

The example workspace above had two blocks connected together: a "print" block (from the Text category) and a "get temperature for" block (from the Bid Data category) where "Blacksburg,VA" is the selected city. Click the Run button and observe what is printed in the output area (just below the work space). You should see the number "60" in the output area.

Using the output produced in the work space answer these questions using the "print" block in combination with the "get temperature for" and "get current stock for" blocks.

.. mchoicemf:: blockly-1-1
   :submission: cohort
   :answer_a: 75
   :answer_b: 88
   :answer_c: 47
   :answer_d: 54
   :correct: c
   :feedback_a: No, this is for Miami, FL. Change the city option in the "get temperature for" block.
   :feedback_b: No, this is for San Jose, CA. Change the city option in the "get temperature for" block.
   :feedback_c: Yes! This is it.
   :feedback_d: No, this is for New York, NY. Change the city option in the "get temperature for" block.

   What is the temperature in Seattle, WA?

.. mchoicemf:: blockly-1-2
   :submission: cohort
   :answer_a: higher
   :answer_b: lower
   :correct: a
   :feedback_a: That is right!
   :feedback_b: No, a positive number means that it is trading higher. Be sure that you have the stock option set for "Microsoft".

   Is the Microsoft stock currently trading higher or lower?



Sequence and Calculation
------------------------

The temperature returned by the "get temperature for" block is measured on the Fahrenheit scale. An alternative scale is the Celsius (or Centigrade) scale. The conversion between these two scales is:

.. code::

   Celsius = (Fahrenheit - 32)/1.8

The work space that follows shows the program needed to convert the temperature from Fahrenheit to Celsius. In this program this conversion calculation is performed using some of the blocks in the Math category. The "set to" and variable blocks are both in the Variable category. The print block is in the Text category.


.. blockly:: blockly-bigdata2
   :submission:

   preload::


The code in the work space makes use of a sequence of operations:

* setting the property "ftemp" to the current temperature in Fahrenheit,
* setting the property "ctemp" to the result of calculating the conversion of the temperature to Celsius,
* printing the converted temperature.

The assembly of the blocks often involves multiple steps. Here is a diagram that shows the way in which the blocks for the Fahrenheit to Celsius conversion can be assembled. The arrows shows how the blocks are snapped together. There is no strict ordering of which blocks are assembled first.

.. figure:: /Images/Blockly-Fahrenheit-Celsius-Conversion.png
   :align:  center

   Assembling the Blocks for the Temperature Conversion Example


Creating the blocks with the property names "ftemp" and "ctemp" involves renaming one of the standard blocks. For example, to create the "set ftemp to" block:

* drag a "set item to" block from the Variable category to the work space
* click on the name "item" and select the option "Rename variable..."
* in the window that appears replace the name "item" with the name "ftemp" and click the OK button

A similar renaming is done for the variable blocks.

Another temperature scale is the Kelvin scale. Temperatures in Fahrenheit can be converted to Kelvin as follows:

.. code::

   Kelvin = 273.15 + ((Fahrenheit - 32) *5)/9


Using the above work space build a Blockly program that does the conversion from Fahrenheit to Kelvin. Use this program to answer these questions.

.. mchoicemf:: blockly-1-3
   :submission: cohort
   :answer_a: 24
   :answer_b: 297
   :answer_c: 315
   :answer_d: 0
   :correct: b
   :feedback_a: No. Check to be sure you have the right city and the correct conversion.
   :feedback_b: Yes! This is it.
   :feedback_c: No. Check to be sure you have the right city and the correct conversion.
   :feedback_d: No. Check to be sure you have the right city and the correct conversion.

   What is the temperature (rounded to the nearest degree) in Miami, FL expressed in Kelvin?


.. mchoicemf:: blockly-1-4
   :submission: cohort
   :answer_a: 15
   :answer_b: 297
   :answer_c: 212
   :answer_d: 8
   :correct: d
   :feedback_a: No. Check to be sure you have the right calculations.
   :feedback_b: No. Check to be sure you have the right calculations.
   :feedback_c: No. Check to be sure you have the right calculations.
   :feedback_d: Yes! Congratulations.

   What is the approximate temperature difference in Kelvin between Blacksburg,VA and Miami, FL?


Decision
--------

In addition to working with specific temperatures we often want to know if the temperature is above or below some threshold. Temperatures that are too high may be uncomfortably hot and temperatures that are too low may be uncomfortably cold. For this example we will take any Fahrenheit temperature below 60 degrees to be "cool", from 60 to 75 to be "mild", from 75 to 85 to be "warm" and 85 and above to be "hot".  The work space below uses decision blocks (from the Controls category) to output the current temperature and whether the current temperature is "cool" or "warm".


.. blockly:: blockly-bigdata3
   :submission:

   preload::
   <xml xmlns="http://www.w3.org/1999/xhtml"> <block type="variables_set" inline="false" x="5" y="36"> <title name="VAR">temp</title> <value name="VALUE"> <block type="weather_get_temperature"> <title name="CITY">BLACKSBURG</title> </block> </value> <next> <block type="text_print" inline="false"> <value name="TEXT"> <block type="variables_get"> <title name="VAR">temp</title> </block> </value> <next> <block type="controls_if" inline="false"> <mutation elseif="1"></mutation> <value name="IF0"> <block type="logic_compare" inline="true"> <title name="OP">LT</title> <value name="A"> <block type="variables_get"> <title name="VAR">temp</title> </block> </value> <value name="B"> <block type="math_number"> <title name="NUM">60</title> </block> </value> </block> </value> <statement name="DO0"> <block type="text_print" inline="false"> <value name="TEXT"> <block type="text"> <title name="TEXT">Cool</title> </block> </value> </block> </statement> <value name="IF1"> <block type="logic_operation" inline="true"> <title name="OP">AND</title> <value name="A"> <block type="logic_compare" inline="true"> <title name="OP">GTE</title> <value name="A"> <block type="variables_get"> <title name="VAR">temp</title> </block> </value> <value name="B"> <block type="math_number"> <title name="NUM">75</title> </block> </value> </block> </value> <value name="B"> <block type="logic_compare" inline="true"> <title name="OP">LT</title> <value name="A"> <block type="variables_get"> <title name="VAR">temp</title> </block> </value> <value name="B"> <block type="math_number"> <title name="NUM">85</title> </block> </value> </block> </value> </block> </value> <statement name="DO1"> <block type="text_print" inline="false"> <value name="TEXT"> <block type="text"> <title name="TEXT">Warm</title> </block> </value> </block> </statement> </block> </next> </block> </next> </block> </xml>

There are two important things to notice about the code in the above work space. The first is the block used for the decision. This block has two slots each of which holds the condition for an "if" test. The second condition is only tested if the first condition is false. This logic is used because a temperature less than 60 degrees then it cannot also be between 75 and 85 degrees. Thus, if the temperature is less than 60 degrees the decision block causes "Cool" to be printed and does not evaluate the second condition. However, the temperature is not less than 60 degrees then it is necessary to evaluate the second condition to decide whether or not to print "Warm".

It is slightly tricky in Blocky to create an "if..do..else if..do" decision block like the one used above. Here is how it is done:

 * In the Controls category select an "if..do" block. Notice that the block as a star in a blue box the left of the word "if".

 * Click the star in the blue box. In the popup window there is an "if" form on the right and, on the left, an "else if" form and an "else" form. Drag the "else if" form from the left into the slot of "if" form on the right. When it snaps into place you will see the original "if..do" block change to the desired block.

 * Click on the star in the blue box to close the popup window.

The second thing to notice about the code in the above workspace is the second condition. To test if the temperature is within a range there are two separate but related conditions:

 * is the temperature at or above the lower limit of the range,
 * is the temperature less than the upper limit of the range.


To combine these two separate conditions into one compound conditions an "and" Boolean operator is used. A compound condition with an "and" operator in Boolean logic is true only if both of its two conditions are true (and false otherwise). A related Boolean operator, the "or" operator, is true if either of its two conditions is true (and false otherwise). The block for building compound and/or conditions is in the Logic category. The category also contains a third Boolean operator, "not". This block has a single slot into which a condition can be plugged. The combination of the "not" and a condition form a compound condition which is true if the condition is false and false if the condition is true. For example, the compound condition

 .. code::

     not (temp > 50)

is

* true if the value of the variable temp is 50 or less
* false if the value of the variable temp is greater than 50

Such negated conditions are sometimes used when the statement of a negative condition is easier to understand.

.. mchoicemf:: blockly-1-5
   :submission: cohort
   :answer_a: true
   :answer_b: false
   :correct: a
   :feedback_a: Both conditions are true so the compound "and" condition is true.
   :feedback_b: Since both conditions are true, the compound "and" conditions is true.

   If the value of temp is 65 is the compound condition (temp > 40) and (temp < 70) true or false?


.. mchoicemf:: blockly-1-6
   :submission: cohort
   :answer_a: true
   :answer_b: false
   :correct: b
   :feedback_a: The second condition (temp < 65) is false so the compound condition is false.
   :feedback_b: Since the second condition (temp < 65) is false the compound condition is false.

   If the value of temp is 65 is the compound condition (temp > 40) and (temp < 65) true or false?


.. mchoicemf:: blockly-1-7
   :submission: cohort
   :answer_a: true
   :answer_b: false
   :correct: a
   :feedback_a: Both conditions are true so the compound "or" condition is true since at least one of the conditions is true.
   :feedback_b: Since both conditions are true, the compound "or" conditions is true since at least one of the conditions is true.

   If the value of temp is 65 is the compound condition (temp > 40) or (temp < 70) true or false?


.. mchoicemf:: blockly-1-8
   :submission: cohort
   :answer_a: true
   :answer_b: false
   :correct: a
   :feedback_a: The first condition (temp > 40) is true so the compound condition is true since only one of the conditions needs to be true.
   :feedback_b: Since the first condition (temp > 40) is true the compound condition is true even though the second condition is false since only one of the two conditions needs to be true.

   If the value of temp is 65 is the compound condition (temp > 40) or (temp < 65) true or false?


.. mchoicemf:: blockly-1-9
   :submission: cohort
   :answer_a: true
   :answer_b: false
   :correct: b
   :feedback_a: The negated condition is false because the condition itself is true.
   :feedback_b: The negated condition is false because the condition itself is true.

   If the value of temp is 65 is the compound condition not (temp > 40) true or false?


Exercise. Write a Blockly program that will classify a temperature as cool, mild, warm and hot according to the above rule.


Iteration
---------

So far we have only been dealing with single values that were retrieved from a data stream - the current temperature or the current stock price. The next step is to begin developing the tools to work with a true stream of data. That is, work with a sequence of values that comprise the stream. Even though we will be working with small example streams to start with the algorithms that work for a small stream will also work for a longer stream of the same kind - it will just take longer to run.

To work effectively with big data two concepts need to be brought together:

* list: a data structure that represents the data stream, and
* iteration: applying an algorithm for each item of the list, one item at a time.

A list, like a data stream, is simply a sequence of individual items arranged one after the other. The list of the digits 1 through 9 is written like this:

..  code::

     [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]


where the square brackets surround the list and each item in the list is separated from the next item by a comma. The list is read left-to-right, so the leftmost item is the first item in the list and the rightmost item is the last item in the list. In the example above, the number 1 is the first item and the number 9 is the last item.

There is a  general pattern for processing a list that represents a data stream. The three steps in the pattern are:

1. set the value of a variable to the stream data.

2. perform the iteration using the "for each" where the variable denotes the  item in the data stream used for each step in the iteration.

3. apply some processing to the current item.

The general structure can be adapted to individual problems by specializing the kind of processing that is done on each item. The processing step is often one of four kinds:

1. uniform: apply the same processing to each item in the stream

2. filter: select certain items in the stream to process and ignore the others

3. accumulate: compute a global property for the stream where the global property is updated by each item

4. transform: produce a new data stream from the original stream by transforming the individual items in some way.

We will look at examples of each of these four patterns.


Iteration: Uniform
------------------

The Blockly work space below shows an example of combining lists and iteration to process each item in a data stream in a uniform way. This code simply prints each item of the data stream, one item per line. Run the code and see what values are in the data streams for different cities. Note: you may need to use the scroll bar on the right to be able to see all of the output.

.. blockly:: blockly-bigdata4
   :submission:

   preload::
   <xml xmlns="http://www.w3.org/1999/xhtml"><block type="variables_set" inline="false" x="0" y="0"><title name="VAR">temp-stream</title><value name="VALUE"><block type="weather_get_forecasts"><title name="CITY">BLACKSBURG</title></block></value><next><block type="controls_forEach" inline="false"><title name="VAR">temp</title><value name="LIST"><block type="variables_get"><title name="VAR">temp-stream</title></block></value><statement name="DO"><block type="text_print" inline="false"><value name="TEXT"><block type="variables_get"><title name="VAR">temp</title></block></value></block></statement></block></next></block></xml>



The example above was one of uniform processing - each item in the data stream was printed. No items were excluded.

Iteration: Filter
-----------------

In other cases there are certain items in a data stream of particular interest. We can "filter" the data stream by iterating through the stream looking for the items of interest and ignoring those not of interest.  Only those items of interest are processed. For example, for our forecast temperature data stream we might want to print only the cool temperatures in the forecast. According to our earlier definition, a cool temperature is one that is below 60 degrees. The Blockly work space below illustrates this pattern of filtering a data stream.

.. blockly:: blockly-bigdata5
   :submission:

   preload::
   <xml xmlns="http://www.w3.org/1999/xhtml"> <block type="variables_set" inline="false" x="-6" y="16"> <title name="VAR">temp-stream</title> <value name="VALUE"> <block type="weather_get_forecasts"> <title name="CITY">BLACKSBURG</title> </block> </value> <next> <block type="controls_forEach" inline="false"> <title name="VAR">temp</title> <value name="LIST"> <block type="variables_get"> <title name="VAR">temp-stream</title> </block> </value> <statement name="DO"> <block type="controls_if" inline="false"> <value name="IF0"> <block type="logic_compare" inline="true"> <title name="OP">LT</title> <value name="A"> <block type="variables_get"> <title name="VAR">temp</title> </block> </value> <value name="B"> <block type="math_number"> <title name="NUM">60</title> </block> </value> </block> </value> <statement name="DO0"> <block type="text_print" inline="false"> <value name="TEXT"> <block type="variables_get"> <title name="VAR">temp</title> </block> </value> </block> </statement> </block> </statement> </block> </next> </block> </xml>


Iteration: Accumulate
---------------------


An example of processing that involves accumulating is to find the average of the forecasts. To find the average we need to know how many items there are in the data stream and what is the total temperature over all the forecasts. The following work space shows a Blockly program for this.

.. blockly:: blockly-bigdata6
   :submission:

   preload::
   <xml xmlns="http://www.w3.org/1999/xhtml"><block type="variables_set" inline="false" x="137" y="20"> <title name="VAR">temp-stream</title><value name="VALUE"><block type="weather_get_forecasts"> <title name="CITY">BLACKSBURG</title></block></value><next><block type="variables_set" inline="false"><title name="VAR">num-items</title><value name="VALUE"><block type="math_number"><title name="NUM">0</title></block></value><next><block type="variables_set" inline="false"><title name="VAR">total-temp</title><value name="VALUE"><block type="math_number"><title name="NUM">0</title></block></value><next><block type="controls_forEach" inline="false"><title name="VAR">temp</title><value name="LIST"><block type="variables_get"><title name="VAR">temp-stream</title></block></value><statement name="DO"><block type="variables_set" inline="false"><title name="VAR">num-items</title><value name="VALUE"><block type="math_arithmetic" inline="true"><title name="OP">ADD</title><value name="A"><block type="variables_get"><title name="VAR">num-items</title></block></value><value name="B"><block type="math_number"><title name="NUM">1</title></block></value></block></value><next><block type="variables_set" inline="false"><title name="VAR">total-temp</title><value name="VALUE"><block type="math_arithmetic" inline="true"><title name="OP">ADD</title><value name="A"><block type="variables_get"><title name="VAR">total-temp</title></block></value><value name="B"><block type="variables_get"><title name="VAR">temp</title></block></value></block></value></block></next></block></statement><next><block type="variables_set" inline="false"><title name="VAR">average-temp</title><value name="VALUE"><block type="math_arithmetic" inline="true"><title name="OP">DIVIDE</title><value name="A"><block type="variables_get"><title name="VAR">total-temp</title></block></value><value name="B"><block type="variables_get"><title name="VAR">num-items</title></block></value></block></value><next><block type="text_print" inline="false"><value name="TEXT"><block type="variables_get"><title name="VAR">average-temp</title></block></value></block></next></block></next></block></next></block></next></block></next></block></xml>



In this program two properties of the data stream are being accumulated as each item in the stream is examined. One property is the number of items in the stream. This is the property represented by the variable "num-items". The second property is the total of all of the temperatures in the data stream. This is the property represented by the variable "total-temp". On each step of the iteration a "set-to" block is used to update the properties. The "set-to" block updates the selected variable to the value indicated by whatever block is plugged into the "set-to" block. Thus, "set num-items to num-items + 1" means that the value of "num-items" in increased by one and "set total-temp to total-temp + temp" means that the value of total-temp is increased by the value of "temp" (the forecast temperature on this step of the iteration). An important part of the accumulating pattern is that the variables being used to accumulate the global properties are initialized. In this program the two variables "num-items" and "total-temp" are each initialized to zero. The initialization is necessary so that on the first iteration the two "set-to" blocks make sense. For example, with "num-items" initialized to zero the block "set num-items to num-items + 1" on the first step of the iteration makes sense (updating the value of num-items to the result of 0+1).

This pattern of data stream processing is called "accumulate" because on each iteration some variables are gathering increasingly accurate  values for selected global properties of the data stream. In this case, the program is accumulating an increasingly more accurate value for the number of items in the stream and the total of the forecast temperatures.

Exercise: Rewrite the above Blockly solution to replace the "change" blocks by "set...to" blocks.

Exercise: count the number of cool days and print this after the iteration.

Iteration: Transform
--------------------

The transform pattern produces a new data stream from a given data stream. Each item of the given data stream is changed in some way to generate each item of the new data stream stream. For example, each item in the  forecast stream is a temperature on the Fahrenheit scale. What might be needed is a data stream where each item is the same temperature but measured in the Celsius scale. The transform pattern can be used to produce the Celsius data stream from the Fahrenheit data stream. This pattern is illustrated in the Blockly program below.

.. blockly:: blockly-bigdata7
   :submission:

   ====
   * Lists
   lists_create_empty
   lists_setIndex



   preload::
   <xml xmlns="http://www.w3.org/1999/xhtml"><block type="variables_set" inline="false" x="37" y="37"><title name="VAR">Cstream</title><value name="VALUE"><block type="lists_create_empty"></block></value><next><block type="variables_set" inline="false"><title name="VAR">Fstream</title><value name="VALUE"><block type="weather_get_forecasts"><title name="CITY">BLACKSBURG</title></block></value><next><block type="text_print" inline="false"><value name="TEXT"><block type="variables_get"><title name="VAR">Fstream</title></block></value><next><block type="controls_forEach" inline="false"><title name="VAR">temp</title><value name="LIST"><block type="variables_get"><title name="VAR">Fstream</title></block></value><statement name="DO"><block type="variables_set" inline="false"><title name="VAR">celsius</title><value name="VALUE"><block type="math_round" inline="false"><title name="OP">ROUND</title><value name="NUM"><block type="math_arithmetic" inline="true"><title name="OP">DIVIDE</title><value name="A"><block type="math_arithmetic" inline="true"><title name="OP">MINUS</title><value name="A"><block type="variables_get"><title name="VAR">temp</title></block></value><value name="B"><block type="math_number"><title name="NUM">32</title></block></value></block></value><value name="B"><block type="math_number"><title name="NUM">1.8</title></block></value></block></value></block></value><next><block type="lists_setIndex" inline="true"><mutation at="false"></mutation><title name="MODE">INSERT</title><title name="WHERE">LAST</title><value name="LIST"><block type="variables_get"><title name="VAR">Cstream</title> </block></value><value name="TO"><block type="variables_get"><title name="VAR">celsius</title> </block></value></block></next></block></statement><next><block type="text_print" inline="false"><value name="TEXT"><block type="variables_get"><title name="VAR">Cstream</title> </block></value></block></next></block></next></block></next></block></next></block></xml>

The Blockly program creates a new list named "Cstream" to represent the data stream to be created. The "Cstream" list is initialized to be empty because it contains no items at the beginning. The forecast data stream is used to initialize the variable "Fstream". The "Fstream" list is printed. Each of the printed values will be in Fahrenheit. The iteration produces the transformed data stream, "Cstream". One each iteration:


* an item, denoted by "temp", is selected from the Fahrenheit data stream
* the value of "celsius" is set to the result of converting "temp" to the equivalent temperature on the Celsius scale. For ease of readability later, the result of the conversion is rounded to the nearest integer value.
* the value of "celsius" is added to the "Cstream" list that represents the Celsius data stream.

When the iteration is completed the "Cstream" list is printed. You can run the program and see the correspondence between each item in the original data stream and its transformed value in the new data stream.

Exercise. Revise the transform Blockly code shown above to convert the data into temperatures in the Kelvin scale.

Combining the Patterns
----------------------

The individual patterns of uniform, filter, accumulate, and transform can be combined. For example, might want to generate a data stream whose items are only the temperatures above 85 degrees, the hot temperatures, and where the temperatures in the generated data stream are in Celsius. The program to generate this data stream uses both a transform pattern and a filter pattern.
