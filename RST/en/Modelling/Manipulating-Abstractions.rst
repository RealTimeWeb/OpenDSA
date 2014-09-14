Manipulating Abstractions
=========================

We have seen how to form abstractions that represent objects in the real world by identifying their important properties. We have also seen that these abstractions can be "coded" in a programming language so that they can be communicated by a programmer to a computer. We now want to see how these abstractions can be manipulated. That is, we want to take our first look at the "coding" in a programming language that allows us to make our abstractions change in ways that we want. For our simple ecological model we will see the coding that creates the simulation of the turtles and grassy patches. 

The term "algorithms" refers to a precisely defined procedure for accomplishing some goal. We are interested in "computer algorithms", that is, procedures that precisely direct a computer to accomplish some goal. While the term "computer algorithm" is more descriptive we will simply use the shorter term "algorithm", knowing that what we have in mind are algorithms for computers to follow. 

As we will gradually see, computer algorithms are constructed out of four simple and basic abilities:

* calculation - the ability to do arithmetic and simple logic
* sequence - the ability to do one step after another
* decision - the ability to take alternative courses of action
* iteration - the ability to do some action over and over and over,...

Computers are designed to have these abilities and are able to perform them very rapidly. 

The creativity of programming is using these simple building blocks to create computing systems that play music, search the web, create virtual realities, fly planes, trade stocks, and many other things you can imagine (and maybe even some you cannot imagine). As we will learn by experience, exercising this creativity is challenging because the computer algorithm must be precise. This means, that it must be correct under all possible conditions. Discovering all of the possible conditions and handling them correctly is not easy but it can be learned. 

Algorithms for computers to follow are written in a programming language. We have seen already that programming languages can express the properties of abstractions. Specifically, we saw how the properties of agents and the global properties of a simulation were expressed in the NetLogo programming language. We will now see how algorithms can be expressed in the NetLogo programming language. As noted several times, keep in mind that NetLogo is only one of many programming languages. Later we will see two other languages in which algorithms can be written.

Calculation
-----------

Calculation is the easiest of the basic parts of an algorithm to understand. The ability of a computer to do arithmetic is the same as any human's ability except that the computer is faster and does not make mistakes. Computers are great at working with numbers. Programming languages include a full array of arithmetic operations: +, -, \*, / along with parenthesis to group expressions together. 


All calculation involves three elements: the generation of a mathematical result, the property whose value is set to that result, and some language symbol that identifies this as a calculation statement. In NetLogo calculation statements have the general form:

.. code::

   set property result


In NetLogo "set" is a keyword that identifies that this statement is a calculation. The "property" is the name of an agent's property or a global property. Finally, result is the outcome of calculating a mathematical expression. The effect of the statement is that the value of the property is set to result.


Perhaps the simplest form of calculation is an initialization. In this case a property is set to some predetermined value. Often the value is simply a constant. An example of an initialization in our simple ecological model is:

.. code:: 
 
   set age 0


which is a calculation to set the age property of a turtle to zero. This statement is performed as part of the model's setup operations. The goal is to make sure that all turtles start out as "young" turtles. Similarly, the initialization

.. code:: 
 
   set energy 2

sets the energy property of a turtle to a simple constant.


Another recurring kind of calculation is an update. The idea of an update is seen in real world situations. When you pay for a purchase using your debit card the card's balance is updated by subtracting the amount of the purchase from the debit card's current (before the purchase) balance with the result becoming the new (after the purchase) balance. When a turtle in our simple ecological model moves the turtle expends a unit of energy. Thus, the energy property of the turtle has to be updated. We can see this update in the NetLogo code as:

.. code:: 
 
   set energy energy - 1

This statement sets the energy property of a turtle to be an amount equal to one unit less than its previous value. More mechanically, the current value of the energy property is obtained, one is subtracted from this value and the result becomes the new value for the energy property. In the same way, the turtle ages and so its age property must be updated by increasing the value of the property by 1 time unit. The NetLogo code for this is:

.. code:: 
 
    set age age + 1

This statement sets the age property of a turtle to be an amount equal to one unit more than its previous value. More mechanically, the current value of the age property is obtained, one is added to this value, and the result becomes the new value for the age property. 


Calculations can be more complicated mathematically. The  model named GasLab Free Gas (in the NetLogo Models Library in the Chemistry & Physics section) has these calculations:

.. code:: 
 
   set energy (0.5 * mass * (speed ^ 2))
   set heading (theta - (atan v2l v2t))

While they are more involved they still follow the same form. 


In some cases a calculation is complicated enough that it is broken down into pieces. The same GasLab Free Gas model has this code:

.. code:: 
 

  let vcm (((mass * v1t) + (mass2 * v2t)) / (mass + mass2) )
  ...
  set v1t (2 * vcm - v1t)
  set v2t (2 * vcm - v2t)

The first statement, beginning with the keyword "let", computes a temporary result as the value of "vcm" which is then used in the each of the next two calculation statements. 

Sequence
--------

Arranging things in the right order is important. Sayings like "putting the cart before the horse" and the phrase "ready, fire, aim" are emblematic of the importance of proper order. The same is true in text that we read - shuffling the sentences in a paragraph is not likely to result in something that makes sense.




.. figure:: Cart-Before-Horse.png
   :align: center

   The Importance of Order



Ordering the steps in a program is equally important. A simple example of this is the code shown immediately above. In this code a value for *vcm* is calculated and then this value is used in the calculation of the values for *v1t* and *v2t*. Reordering the steps in this code so that the calculation of *vcm* comes after the the steps that calculate v1t and v2t is clearly wrong. 

Computers are designed to follow the order of steps given in the code they are executing. Unless the code says otherwise a computer will simply fetch the next line, execute that line of code, fetch the next line of code, and so on. 


Decisions
---------

For programs to be able to cope with even simple problems they usually have to be able to take alternative courses of action. That is, the program must adapt its behavior to changing circumstances. People adapt their behavior to changing circumstances all the time. Consider the image below of a traffic sign. This sign tells drives how to adapt their behavior to conform with legal driving conditions. One way to state what the sign says is that "if the light is flashing then the speed limit is 15 miles per hour." This form of "if...then..." expression is exactly what the designers of programming languages used to give the code that we write the ability to adapt to changing circumstances. 
 

.. figure:: School-Sign-Simple-Decision.png
   :align:  center

   A Traffic Control Sign
   

.. image:: School-Sign-Simple-Decision.png
   :align:  center


Similarly, the agents in the simple ecological model have rules that are cause the agents to change behavior depending on circumstances. These rules are also cast in a "if... then..." framework. One of the rules for a turtle in the simple ecological model is that it can only reproduce if its energy is above a given threshold. This is code in NetLogo as follows:

.. code:: 
 
   if energy > birth-energy [
      set number-turtles number-turtles + 1
      set energy energy - birth-energy
      ; other steps here but not shown
   ]


This code directs the turtle to check a certain condition, namely whether its energy is above the threshold specified for reproduction (e.g, birth-energy). If this condition is true then the turtle takes the actions specified, namely increasing the number of turtles and reducing its own energy level by the birth-energy. Notice that in the NetLogo programming language the "then" word does not appear but its sense is implied in NetLogo.

In general, a decision in NetLogo is of the form:

.. code:: 
 

   if condition [
      list of actions
   ]


which means that if the agent find the "condition" to be true then the agent will perform the list of actions given in the square brackets. Of course, when the condition is not true then the list of actions will not be performed. The "if" and the square brackets are part of the "syntax" of the NetLogo programming language. Be careful, omitting the square brackets or forgetting to match the brackets will cause NetLogo to complain - or worse, simply execute a rule other than what you intended.


Life can be complicated and so can the conditions that we need to test for. The traffic control sign that follows is an example of this. This sign has multiple conditions that all go together to determine if the speed limit is reduced to 40 miles per hour. These conditions are:

* the time of day is between 8 and 9:30AM
* the time of day is between 2:30 and 4PM
* the day is a school day

We would certainly understand from this sign that at 9AM on Tuesday the speed limit would be 40 MPH but that this would not be the limit if it were 9AM on a Saturday. Similarly, the speed limit would be 40 MPH at 3PM on Friday but that this would not be the limit if it were 3PM on a Sunday.


.. figure:: School-Sign-Complex-Decision.png
   :align: center

   A More Complex Traffic Control Sign


There are different ways of expressing the decision logic for this sign in the "if ... then ..." style. Warning: the code shown for this example is not meant to be completely valid NetLogo code. The details of how to write this correctly in NetLogo is not the point. This example is about the logical structure and its meaning.


One way is to begin coding the school sign logic is like this:

.. code:: 
 
   if day = school-day [
      ; other parts of decision here
   ]

This first step separates the decision into whether the current day is or is not a school day. If the condition is not true (i.e., the day is not a school day) then the sign does not apply and we can skip the rule. If, however, the current day is a school day we still need to apply the logic about the time of day. Lets first deal with the morning hours. We can account for this in our logic like this:

.. code:: 
 
   if day = school-day [
      if time in 8-9:30AM [
         set speed-limit 40
      ]
      ; more needed here
   ]


This step has refined the decision logic by adding the condition that the speed limit is 40 during the restricted morning hours (8-9:30AM). It is very important to notice the dependency created by this structure. Namely, the condition for the time being in the restricted morning hours is only tested if the current day is a school day. However, our rule is still incomplete because it does not handle the case for the restricted afternoon hours. We can add this condition like this:


.. code:: 
 

   if day = school-day [

      if time in 8-9:30AM [
         set speed-limit 40
      ]

      if time in 2:30-4PM [
         set speed-limit 40
      ]
   
   ] 


This step has completed the logic of the sign by accounting for the lower speed limit during the restricted afternoon hours. 

While the completed sign logic is correct, one aspect of it deserves a closer look. Notice that the two if statements that test the time of day are separate statements that will be executed in sequence (see discussion of sequence above). We can follow the execution of the code by using a visualization of the execution shown in the following figure. 


..  figure:: If-Statement-Flow-Chart.png
    :align: center

    Flow Chart of an If-Then Statement


In this figure the steps in the two separate decision statements are surrounded by dashed boxes to emphasize that they are two separate statements. The execution of the statements is shown by the arrowed lines. The execution starts at the top of the figure. The first condition is tested and if found to be true the execution proceeds to the right (indicated by the word true over the arrowed lined going to the right) otherwise the execution proceeds immediately to the next statement (following the arrowed lines labelled false). If the execution proceeds to the right it executes the set statement (setting the speed-limit to 40) and then also proceeds to the next statement. The second if statement is similarly executed. What is to be seen here is that the second test is always made regardless of whether the first test was true or not. 

In our complete sign logic the test for the time of day being in the afternoon is made even if the test for the time being in the morning is true. This "unnecessary" testing is harmless though possibly annoying. It is harmless because if the time is in the morning the second test will simply not be true and the execution will proceed. This situation might be annoying because we are making a test even though we know it will be false. We can structure the decision logic somewhat differently if we want.

One way to restructure the decision logic is to use an alternative expression of the form "if ... then ... else ..." which provides that the "then" part is executed only when the condition tested  is true and the "else" part is executed only when the condition tested is not true. In NetLogo a statement like this appears as:

.. code:: 
 
   ifelse condition 
     [ list of "then" actions ]
     [ list of "else" actions ]


The keyword "ifelse" and the square brackets are part of the NetLogo syntax. Remember that the square brackets have to be matched. The execution of this statement is illustrated by the following visualization similar to the one above.


..  figure:: IfElse-Statement-Flow-Chart.png
    :align: center

    Flowchart of an If-Then-Else Statement


This visualization shows that there is a strict choice being made between two alternative sets of actions. One and only one of the two alternative sets of actions will be executed depending on whether the condition being tested is true or false.  Regardless of which "branch" is taken the execution then proceeds to the next statement.

We can make use of this form of expression in structuring our sign logic. We want to be sure that the test for the afternoon restricted times are only made when the test for the morning restricted time is not true. That is, the afternoon time test should be the "else" part of the morning time test. The NetLogo style code for this is as follows:

.. code:: 
 

   if day = school-day [

      ifelse time in 8-9:30AM 

        [ set speed-limit 40 ]      ; "then" actions

        [ if time in 2:30-4PM       ; "else" actions
            [ set speed-limit 40 ]  
        ]
   ]
  
   
It may help to look at the visualization for this code. 



..  figure:: IfElse-Example-Flow-Chart.png
    :align: center

    Flowchart of If-Then-Else Code


In this visualization a dotted box is used to outline the "else" actions. Following the execution indicated in the visualization shows that the test for the afternoon times is not made when the test for the morning times is true.

There is a second way to restructure our traffic sign logic relies on the way which we might explain the sign's meaning to someone else. It would be natural to say something like "the speed limit is reduced on school days between 8-9:30AM or between 2:30-4PM". In this case a form of ... or ..." expression is being used. The meaning of this expression is that the condition is true if one or the other of the conditions is true. This corresponds well with the formal logical notion of "or" as well. A NetLogo style version of our sign logic can be written this way:

.. code:: 
 
   if day = school-day [

      if time in 8-9:30AM  or  time in 2:30-4PM

        [ set speed-limit 40 ]     

   ]


In this version of our sign logic there is only one test for time of day which uses the "or" form of expression. 

We have now seen three correct but different coding for the sign logic. This means that different programmers may come up with different ways to write a program that solves the same problem. This is part of the creativity of programming.



Iteration
---------


Repeating the same action over and over is a common occurrence in nature and in machines that people have built. For each of us the repetitive beating of our hearts and the repetitive breathing of our lungs is critical to life. The repetitive movement of pistons in steam and internal combustion engines gives the power to these sources of mechanical energy. The ability to perform the same set of steps over and over is important in most uses of computers. In programming languages the term "iteration" is often used to describe coding that produces repeated execution of some steps in the program.

..  figure:: NetLogo-Iteration-Sign.png
    :align: center

    Caution: Iteration Ahead    



Iteration is not mindless repetition of exactly the same thing. For example, calculating "2 + 2" over and over is not really meaningful. What makes iteration powerful is that the same steps are executed over and over but, on each repetition, the steps are performed on different data. 



We can see this pattern of iteration - repetition of the same steps but with different data - in the kinds of problems we have in this course. Here are some examples:

* In NetLogo the execution of a model involves executing a single simulation step repeatedly, but on each step the data (i.e., the properties of the agents) is different in some way. For example the agents have moved to a new location or the grass in a particular patch has been eaten.
* In a single simulation step of a NetLogo model each agent (turtle) must perform its rules and update its properties accordingly but the properties of different agents and the environment that different agents see can lead to different behaviors. For example, one turtle might have an energy level allowing it to reproduce while another turtle might be below the threshold to reproduce. Similarly, one turtle might be in a grass patch which eat can eat and increase its energy level while another agent is in a patch with no grass and cannot increase its energy level. In each case the rules are the same but the differences in the data (the properties of the agent and its environment) lead to different behaviors.
* In working with "big data" stream (that will be seen later) the same set of steps is usually applied to each piece of data. For example, one of the data streams has data on each earthquake that has occurred somewhere in the world. An earthquake is described by its magnitude and the location of where it happened. To find the biggest earthquake that has occurred in a particular location we can use this test: "is the earthquake at the desired location and is the earthquake larger than any earthquake at that location we have seen so far". Applying this test to each earthquake in the data stream is done by iteration.



Each of these example illustrates the key idea of iteration: performing the same steps but with different data.



A common form for expressing iteration in a programming language uses the idea of "for each".  In this form a set of data is identified, the set of turtles, the list of all earthquakes. The "for each" iteration means that a given set of steps is to be performed on each element in the data set, one element at a time. This might look like:



.. code::

   
   foreach t in turtles [ turtle-actions ]  

   
   foreach q in earthquakes [ quake-actions ]





The meaning of the turtle example is that each turtle is selected one at a time and the steps in turtle-actions are carried out for that turtle. Each turtle is selected exactly once and no turtle is ignored. In more detail, on each iteration the name "t" refers to the turtle being considered on the current iteration and the steps in turtle-actions are applied to whatever turtle is identified by "t". Similarly, the meaning of the earthquake example is that each earthquake is selected one a time and the steps in quake-actions are carried out for that earthquake. Each earthquakes is selected exactly once and not earthquake is ignored. In more detail, on each iteration the name "q" refers to the earthquake being consider on the current iteration and the steps in quake-actions are applied to whatever earthquake is identified by "q".



Different programming languages have different syntaxes for describing the "for each" form of iteration. Because NetLogo is designed to focus on set of agents (i.e., turtles and patches) the NetLogo programming language has a compact way of expressing the "for each" iteration over sets of agents. In NetLogo this is written as:



.. code::


   ask turtles [ turtle-actions ]

   ask patches [ patches-actions ]




The sense of this terminology is that the program is "asking" the turtles (one at a time) to perform the specified set of actions.   In other words, the meaning of "ask turtles" is the same as "foreach t in turtles". Similarly, for the meaning of "ask patches". A specific example of iteration in our simple ecological model is this code:



..  code::


   ask turtles [         ; apply this rule to all turtles one at a time

       right random 360

       forward 1

       set energy energy - 1

       set age age + 1

   ]    





In this code each turtle, one at a time, is asked to perform the four actions that move the turtle to a new location. The first two actions pick a random direction and move one step in that direction. The next two steps update the properties of the turtle by decreasing its energy and increasing its age.

Here is another example, this time iterating through the patches:



.. code::


   ask patches [           ; apply this rule to all patches one at a time

      if plant-energy = 0 [
        set regrow-time regrow-time - 1

        if regrow-time = 0 [

            set pcolor green

            set number-green-patches number-green-patches + 1

            set plant-energy energy-from-grass

        ]

      ]

   ]





In this code each patch is selected one at a time. The currently selected patch checks to see if it has no grass (i.e., its plant-energy is 0). If there is no grass then the time to regrow the grass is decreased and a test is made to see if it now time to regrow the grass (i.e., the regrow-time is 0). If it is time to regrow the grass then the patch changes its color property to green, increases the global property number-green patches, and changes its own plant-energy property to the current setting of the energy-from-grass slider.



There are other ways of expressing iteration. These are briefly described here. Some of these forms may be encountered later as we see different programming languages in this course and you may see these form if you learn other programming languages outside of this course. One alternative form of iteration "counting" iteration. This means that the iteration is repeated a fixed number of times over some range of numbers. Counting iteration might specify for example that the steps are repeated over the range 1 to 10, or 0 to 99. A second alternative for of iteration is "condition" iteration. This means that the iteration is repeated until a given condition is false. For example, in our simple ecological model we might want to stop the simulation if all of the turtles die. Expressing this as condition iteration yields something like "while number-turtles > 0 [ simulation-steps ]". This means that as long as the value of the global property number-turtles is greater than 0 the simulation steps would continue to be executed. Each of these forms of iteration is useful in different contexts depending on the nature of the iteration. 


