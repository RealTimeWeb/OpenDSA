.. This file is part of the OpenDSA eTextbook project. See
.. http://algoviz.org/OpenDSA for more details.
.. Copyright (c) 2012-2013 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. avmetadata::
   :author: OpenDSA & CompThink Contributors
   :satisfies:
   :topic:


Functions
=========

We saw in NetLogo the utility of organizing code into functions. Each function is defined by a name and a body of code. The code in the function is executed whenever the name of the function is used as a statement that is executed; this action is termed "calling" or "invoking" the function. The advantages of organizing  large program into a collection of functions were seen earlier and are summarized as:

* intelligibility - easier to understand a large program that is built of functions
* reuse within - the function can be called from several different places reducing the overall size of the program
* replacement - the body of the function can be replaced by better code that has the same effect or different code that changes the meaning of the program in a disciplined way
* reuse across - using functions from a previous program in building a new program
* construction - a useful way of having many programmers work on the same program at once by having each one working on developing the code for different functions.

We want to see now not only how to define and use functions in Blockly but also to see new aspects of functions that make them more powerful and useful.

Basic Functions
^^^^^^^^^^^^^^^

The Blockly environment shown next includes in the palette of blocks a "Functions" category. The Functions category has three initial blocks:

* to *do something* - define a function whose name replaces *do something*
* to *do something...return* - similar to the previous block with the added ability to *return* a specified value
* *if...return...* - another way to specify the return value

We will look at a series of examples that illustrate the ideas of functions.

The first example uses the Blockly code that illustrated how to transform data streams. In the Blockly environment below the transform code has been restructured to use a function. Notice that there are two separate sections of Blockly code. The lower section is the definition of the function named *convert*. The upper section of code is called the *main* program. The body of the *convert* function is just the code from the original example that does the transformation (i.e., generating a new data stream of Celsius temperatures from the existing data stream of Fahrenheit temperatures. The upper section is all of the rest of the Blockly code from the original example with one addition. Between the two *print* blocks is a new block that has the name *convert*. This is a "call block" that causes the body of the convert function to be executed. Run the example code below and confirm that it produces the same output as the original example.


.. blockly:: blockly-bigdata8
   :submission:

   * Lists
   lists_create_empty
   lists_setIndex
   ====
   functions

   preload::
   <xml xmlns="http://www.w3.org/1999/xhtml"><block type="variables_set" inline="false" x="11" y="14"><title name="VAR">Cstream</title><value name="VALUE"><block type="lists_create_empty"></block></value><next><block type="variables_set" inline="false"><title name="VAR">Fstream</title><value name="VALUE"><block type="weather_get_forecasts"><title name="CITY">BLACKSBURG</title></block></value><next><block type="text_print" inline="false"><value name="TEXT"><block type="variables_get"><title name="VAR">Fstream</title></block></value><next><block type="procedures_callnoreturn"><mutation name="convert"></mutation><next><block type="text_print" inline="false"><value name="TEXT"><block type="variables_get"><title name="VAR">Cstream</title> </block></value></block></next></block></next></block></next></block></next></block> <block type="procedures_defnoreturn" x="7" y="203"><mutation></mutation><title name="NAME">convert</title><statement name="STACK"><block type="controls_forEach" inline="false"><title name="VAR">temp</title><value name="LIST"><block type="variables_get"><title name="VAR">Fstream</title></block></value><statement name="DO"><block type="variables_set" inline="false"><title name="VAR">celsius</title><value name="VALUE"><block type="math_round" inline="false"><title name="OP">ROUND</title><value name="NUM"><block type="math_arithmetic" inline="true"><title name="OP">DIVIDE</title><value name="A"><block type="math_arithmetic" inline="true"><title name="OP">MINUS</title><value name="A"><block type="variables_get"><title name="VAR">temp</title></block></value><value name="B"><block type="math_number"><title name="NUM">32</title></block></value></block></value><value name="B"><block type="math_number"><title name="NUM">1.8</title></block></value></block></value></block></value><next><block type="lists_setIndex" inline="true"><mutation at="false"></mutation><title name="MODE">INSERT</title><title name="WHERE">LAST</title><value name="LIST"><block type="variables_get"><title name="VAR">Cstream</title></block></value><value name="TO"><block type="variables_get"><title name="VAR">celsius</title></block></value></block></next></block></statement></block></statement></block> </xml>



It is important to understand the specific way in which the code using a program with a function executes. The execution of such a program begins with the first statement in the main program. The example code above executes in response to the "Run" button as follows starting with the first statement in the main program:

1. the *set Cstream to...* block is executed
2. the *set Fstream to...* block is executed
3. the *print Fstream* block is executed
4. the *convert* call block is executed, which causes the function to be called
    4.1. the *for each item...* iteration in the *convert* function is executed; each iteration adds another item to the *Cstream* list
	4.2. when the iteration is completed all of the statements in the function have been executed and the function is said to return
5. the *print Cstream* block is executed

The figure below shows this sequence of events graphically. The arrows represent the "flow of control" between the upper section of code and the function. When the call block is executed the "flow of control" causes the function to begin execution. When the function has completed its execution the "flow of control" returns and the statement immediately after the call block executes.


..  figure::  /Images/Blockly-Function-Call-Return.png
    :align:   center

    Calling and Returning from a Function

One detail about the Blockly code is how the "call" block for a function is created. When a function definition block is placed in the work space a call block for that function is created automatically in the Function category. When the function definition block is renamed the call block for that function is automatically renamed as well.

Functions with Parameters
^^^^^^^^^^^^^^^^^^^^^^^^^

The *convert* function defined in the example above is perfectly functional but poorly designed. The poor design comes from the fact that its definition is tied to the specific names *Fstream* and *Cstream*. The function will only convert the stream *Fstream* to the stream *Cstream*. We can see the limitation of this design if we want to produce a table of the temperatures in different cities organized so that the Celsius temperatures for all of the cities are printed first followed by the corresponding Fahrenheit temperatures. Using the existing *convert* function the code for the main program for two cities would be structured as follows:

.. code::

   set Cstream to empty list

   set Fstream to get forecasts for "Blacksburg, VA"
   convert
   print Cstream

   set Fstream to get forecasts for "Seattle, WA"
   convert
   print Cstream

   set Fstream to get forecasts for "Blacksburg, VA"
   print Fstream
   set Fstream to get forecasts for "Seattle, WA"
   print Fstream


In this code it is necessary to read each stream twice. To use the *convert* function for the second city the data stream for the first city must be overwritten because *Fstream* can only refer to one or the other of these two streams. What is needed is a function that is more flexible - one which is not tied to the actual name of the variable denoting the data stream. In other words, the function should be able to convert a data stream represented by a list regardless of what the variable for the list is named.


To add the desired flexibility the function should be defined and called with a *parameter* that denotes the data stream to be converted. The Blockly environment below shows the new definition and call of the *convert* function with a parameter. We will see later the steps in Blockly to create the definition block and the call block that are shown here. Run this Blockly program to convince yourself that it does generate the same output as the previous conversion program.


.. blockly:: blockly-bigdata9
   :submission:

   * Lists
   lists_create_empty
   lists_setIndex
   ====
   functions

   preload::
   <xml xmlns="http://www.w3.org/1999/xhtml"><block type="variables_set" inline="false" x="1" y="1"><title name="VAR">Cstream</title><value name="VALUE"><block type="lists_create_empty"> </block></value><next><block type="variables_set" inline="false"><title name="VAR">Fstream</title><value name="VALUE"><block type="weather_get_forecasts"><title name="CITY">BLACKSBURG</title> </block></value><next><block type="text_print" inline="false"><value name="TEXT"> <block type="variables_get"><title name="VAR">Fstream</title></block></value><next><block type="procedures_callnoreturn" inline="false"><mutation name="convert"><arg name="TheStream"> </arg></mutation><value name="ARG0"><block type="variables_get"><title name="VAR">Fstream</title></block></value><next><block type="text_print" inline="false"><value name="TEXT"><block type="variables_get"><title name="VAR">Cstream</title> </block></value> </block></next> </block></next></block></next></block></next> </block><block type="procedures_defnoreturn" x="-23" y="198"> <mutation><arg name="TheStream"> </arg></mutation><title name="NAME">convert</title><statement name="STACK"><block type="controls_forEach" inline="false"><title name="VAR">temp</title><value name="LIST"><block type="variables_get"><title name="VAR">TheStream</title></block></value><statement name="DO"><block type="variables_set" inline="false"><title name="VAR">celsius</title><value name="VALUE"><block type="math_round" inline="false"><title name="OP">ROUND</title><value name="NUM"><block type="math_arithmetic" inline="true"><title name="OP">DIVIDE</title><value name="A"><block type="math_arithmetic" inline="true"><title name="OP">MINUS</title><value name="A"><block type="variables_get"><title name="VAR">temp</title></block></value><value name="B"><block type="math_number"><title name="NUM">32</title></block></value></block></value><value name="B"><block type="math_number"><title name="NUM"> 1.8</title> </block> </value> </block></value></block></value><next><block type="lists_setIndex" inline="true"><mutation at="false"></mutation><title name="MODE">INSERT</title><title name="WHERE">LAST</title><value name="LIST"><block type="variables_get"><title name="VAR">Cstream</title></block></value><value name="TO"><block type="variables_get"><title name="VAR">celsius</title> </block> </value> </block> </next></block></statement></block></statement></block></xml>


The definition of the *convert* function has two changes. First, note that the definition block, in addition to giving the name of the function, also has *with TheStream*. The name *TheStream* is the name of the parameter. Second, the name of the parameter is used in the iteration block to denote whatever stream is being converted. This definition of the  *convert* function is no longer tied to the specific name *Fstream* as its input.

The call block has also has one important change. In addition to giving the name of the function to call (i.e., *convert*) the call block also has a slot named *TheStream*, the name of the parameter that must be provided when the function is called. Currently, the slot named *TheStream* has *Fstream* plugged into it so that this version of the function performs the same conversions as before.

The better design can be seen in revisiting the example above we want to produce a table of the temperatures in different cities organized so that the Celsius temperatures for all of the cities is printed first followed by the corresponding Fahrenheit temperatures. This code can now be written as:

.. code::

   set Cstream to empty list

   set Fstream to get forecasts for "Blacksburg, VA"
   convert (Fstream)
   print Cstream

   set Gstream to get forecasts for "Seattle, WA"
   convert (Gstream)
   print Cstream

   print Fstream
   print Gstream


Notice that the data stream for Blacksburg and the data stream for Seattle are represented by different lists, one named *Fstream* and one named *Gstream*. Each stream is only read once. In this example, the notation *convert (Fstream)* is used to represent the call block where *Fstream* is plugged into the call block slot  and *convert (Gstream)* is used to represent the call block where *Gstream* is plugged into the call block slot.

The important point is that the *convert* function with a parameter is now much better designed because it can work with any input data stream regardless of the name of the variable used to denote that list.

Creating the function definition and call blocks for functions with parameters requires some explanation. Notice that the *to do something* function definition block as an icon of a star on a blue background in the left corner. When clicked this icon presents a display for adding parameters to the call. The top part of the following figure shows this display. The left side of the display contains a *input name x* block that denotes a generic parameter with the name *x*. The right part of the display contains an *inputs* block with a slot into which the parameter can be plugged and renamed.  The bottom part of the following figure shows that the generic parameter block can be dragged and inserted into the *inputs* slot and the generic name *x* can be changed. In this case the parameter name was changed to *TheStream*. The name of the function was also changed from *do something* to *convert*. To complete the function definition just click on the star icon again to close the display.


.. figure:: /Images/Blockly-Functions-Parameter-Definition.png
   :align:  center

   Adding Parameters to a Function Definition


When you have completed the function definition a corresponding call block will automatically be created and added to the "Functions" menu.



Functions with a Return Value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The design of the *convert* function can be further improved by recognizing that the *convert* function has a single output - the list representing a stream of temperature values in Celsius. In our previous examples the name of this output was tied to the name *Cstream*. Just as we would like the function to operate without being tied to a specific name for its inputs so also it would be desirable to have its output not tied to a specific name.

A function can be defined to "return" a single value. The Blockly example that follows shows a revised version of the *convert* function so that it returns its single value.

.. blockly:: blockly-bigdata10
   :submission:

   * Lists
   lists_create_empty
   lists_setIndex
   ====
   functions

   preload::
   <xml xmlns="http://www.w3.org/1999/xhtml"><block type="variables_set" inline="false" x="-118" y="-90"><title name="VAR">Fstream</title><value name="VALUE"><block type="weather_get_forecasts"><title name="CITY">BLACKSBURG</title></block></value><next><block type="text_print" inline="false"><value name="TEXT"><block type="variables_get"><title name="VAR">Fstream</title></block></value><next><block type="variables_set" inline="false"><title name="VAR">Cstream</title><value name="VALUE"><block type="procedures_callreturn" inline="false"><mutation name="convert"><arg name="TheStream"></arg></mutation><value name="ARG0"><block type="variables_get"><title name="VAR">Fstream</title></block></value></block></value><next><block type="text_print" inline="false"><value name="TEXT"><block type="variables_get"><title name="VAR">Cstream</title></block></value></block></next></block></next></block></next></block><block type="procedures_defreturn" inline="false" x="-126" y="58"><mutation><arg name="TheStream"></arg></mutation><title name="NAME">convert</title><statement name="STACK"><block type="variables_set" inline="false"><title name="VAR">TempStream</title><value name="VALUE"><block type="lists_create_empty"></block></value><next><block type="controls_forEach" inline="false"><title name="VAR">temp</title><value name="LIST"><block type="variables_get"><title name="VAR">TheStream</title></block></value><statement name="DO"><block type="variables_set" inline="false"><title name="VAR">celsius</title><value name="VALUE"><block type="math_round" inline="false"><title name="OP">ROUND</title><value name="NUM"><block type="math_arithmetic" inline="true"><title name="OP">DIVIDE</title><value name="A"><block type="math_arithmetic" inline="true"><title name="OP">MINUS</title><value name="A"><block type="variables_get"><title name="VAR">temp</title></block></value><value name="B"><block type="math_number"><title name="NUM">32</title></block></value></block></value><value name="B"><block type="math_number"><title name="NUM">1.8</title></block></value></block></value></block></value><next><block type="lists_setIndex" inline="true"><mutation at="false"></mutation><title name="MODE">INSERT</title><title name="WHERE">LAST</title><value name="LIST"><block type="variables_get"><title name="VAR">TempStream</title></block></value><value name="TO"><block type="variables_get"><title name="VAR">celsius</title></block></value></block></next></block></statement></block></next></block> </statement><value name="RETURN"><block type="variables_get"><title name="VAR">TempStream</title></block></value></block></xml>


There are three significant things to notice about the revised example.

  1.  The *convert* function has a definition block with an additional slot named *return*. When the function completes it is the value of the variable in this slot that is provided to the calling block.
  2.  To keep the return value from being tied to a fixed name the *convert* function itself defines the name of the return value. In this case, the variable *TempStream* is defined and used only in the *convert* function.
  3.  The block that calls the *convert* function must show what to do with the value returned to it when the call on the function completes. In this example, the call block is inserted into the slot of the *set Cstream to* block. This means that the value returned by the *convert* function will be assigned to *Cstream*.

You should run the above example to convince yourself that it works correctly.

To define a function definition block with a return value use the *to "do something" return* block in the Functions category. The parameter for this block can be added in the same way as before (by clicking on the icon that is a star on a blue background).

Cohort Exercise: Define a function for the Fahrenheit-Celsius conversion and use this function to modify the example code above.


