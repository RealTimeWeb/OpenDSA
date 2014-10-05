Coding an Abstraction
=====================


We have seen how to capture an abstraction of a real world object by identifying the properties that are important about that object for some purpose that we have in mind. We have also worked with representing an abstraction by writing down its properties in text. We have also defined abstractions for the turtles and patches of grass in our simple ecological model. However, we now face the challenge of getting the abstraction into a computer so that we can, ultimately, be able to manipulate that abstraction in some useful way. We will see later how to manipulate the abstraction using computation. Our goal now is simply to see how an abstraction can be represented inside a computer.

.. figure:: /Images/Abstraction-Into-Computer.png
   :align:  center

   Getting an Abstraction into a Computer


People represent abstractions for a computer using a programming language. What is written in the programming language is the **"code"** for the computer to following. Hence, **"coding"** is often the term used for the process of writing in a programming language. NetLogo has a programming language which is used to build simulation models such as our simple ecological model. We will see later that programming languages are also used to describe how these abstractions are manipulated. There are many programming languages. We will see parts of three different programming languages in this course, but there are many more. While there are many programming languages they all embody a few key ideas. We will see these key ideas in each of the three languages that are used in the course.

.. mchoicemf:: coding-abstraction-code
   :answer_a: Coding is to code what writing is to text.
   :answer_b: NetLogo uses many programming language.
   :answer_c: Code is used to represent abstractions in computers.
   :correct: b
   :feedback_a: Please read over the last paragraph again!
   :feedback_b: NetLogo only has one programming language (which is also named NetLogo).
   :feedback_c: No, read over the first paragraph again.

   Which of the following is not true?

An implementation of a computational model consists of two closely connected components: the code written in a programming language and the user interface. In NetLogo these two components can be seen in the *Code* and *Interface* tabs, respectively. The connections between the code and the user interface is shown in the following figure.

.. figure:: /Images/NetLogo-Interface-Code.png
   :align: center

   Relationship Between the Code and the User Interface

The user interface has *controls* for the user to set input parameters. The input parameters are used by the code together with the code's own programmed algorithms to compute results. These results are the output data from the code which the user interface renders as various forms of visualizations (graphs, charts, numeric boxes). The user interfaces are themselves created by programming. Here we focus only on the programming of the computational model itself. Some specific examples of these connections are described below as we learn more about the code.

It is now time to look behind the scenes at how our simple ecological model is programmed. In other words, we want to see how the abstractions of the turtles and the patches of grass are written in the NetLogo programming language. To look at the programming for a NetLogo model just select the Code tab near the top-left of the NetLogo window. The next figure shows the code for our simple ecological model.

.. figure:: /Images/CT-Class-Model-Code-Tab.png
   :align: center

   The Programming for the Ecological Model in the Code Tab


For now we want to focus on this part of the code:

.. code::

   ; the properties of the abstractions of the turtles and the grassy patches

   turtles-own[
     energy
     age
     ]

   patches-own [
     plant-energy
     regrow-time
     ]


The first line of this part of the code is a NetLogo comment. Comments have no meaning to the computer and are intended to be descriptive to people (like us) who are reading the code and trying to understand what the code is supposed to be about. The comment above indicates that what follows defines the properties of our two key agents.

.. mchoicemf:: coding-abstraction-comments
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: Comments are ignored by the computer, but their purpose is to explain code to people who read them!
   :feedback_b: Great! Comments are useful to people, even if they are not useful for computers.

   True or false: Comments have no purpose, because the computer ignores them.

In NetLogo the properties of an agent are thought of as being "owned" by the agent. Hence, the term "turtles-own" is the way to state that the following list of properties are those of a turtle. The list of properties for the agent are given in the list that begins with "[" and ends with "]". We can now understand that the our turtle agents possess two properties: energy and age. We have described earlier that the energy level of a turtle is related to its survival, a turtle dies when its energy level is depleted to zero, and its ability to reproduce, a turtle must have a sufficiently high energy level to reproduce. The age property records how long the turtle has survived (measured in the number of simulation steps that it has lived through). We can also see that the abstraction for the patches of grass is defined by two properties: plant-energy and regrow-time. The plant-energy is the amount of energy acquired by a turtle that eats the grass and the regrow-time is the amount of time (again, measured in simulation steps) that must pass before the grass regrows and can be eaten again. Each turtle that is created will have its own energy level and its own age. While the energy levels and ages will differ between turtles, the important idea is that all turtles have an energy level and an age. Similarly, each patch of grass will have a plant-energy and a regrow-time. Equally important is that we now have a way to represent our abstractions in a form that a computer can deal with.

.. mchoicemf:: coding-abstraction-properties
   :answer_a: Energy, age
   :answer_b: Energy, regrow-time
   :answer_c: Energy, shell-color
   :answer_d: Energy
   :correct: a
   :feedback_a: Yes, turtles have both Energy *and* age; you cannot have a turtle without both!
   :feedback_b: No, regrow-time is a property of patches!
   :feedback_c: Shell-color might make sense to be a property of a turtle, but it is not listed in our coded abstraction above.
   :feedback_d: No, Energy is only one of the properties of a turtle. A turtle has two properties!

   What are the properties of a turtle?

The simple ecological model allows the energy property of each turtle to be seen. The user interface contains an On/Off control with the label "show energy?". This control is initially in the "Off" position. By clicking on the switch (currently to the left of the word "Off") you can set the switch to the "On" position. This is shown in the next figure. When the simulation is run each turtle will be annotated with a number representing the currently value for the energy property of that turtle. The figure below shows the display after the simulation has been run for a short time. Notice in this figure that the "show-energy?" switch is set to the "On" position. Also not the energy value for each turtle. For example, the group of turtles in the upper left hand corner have energy values of 5, 40, 2, 12, and 13. By changing the user interface and the model's code we could display the turtles age or either of the properties of the grassy patches.

.. figure:: /Images/CT-Class-Model-Turtle-Energy.png
   :align:  center

   Showing the Turtle's Energy


Another part of the code to observe are these lines at the top:

..  code::

   ; quantities that measure the state of the simulation; changes at each time step

   globals [
     number-turtles
     number-green-patches
   ]


Aside from the properties of each agent we would also like to know something about the "state of the simulated world" as the simulation progresses. These overall measures are defined in the NetLogo language as a list of "globals". The term "globals" reflects that these are properties of the simulation itself, hence global to all of the individual agents in the simulation. At each step in the simulation these global properties will be updated to reflect the current state of the simulated environment. In the case of our simple ecological model the two global properties are the number of turtles that are alive at the current step in the simulation (the property number-turtles) and the number of grassy patches that have edible grass for turtles to eat (the property number-green-patches).

.. mchoicemf:: coding-abstraction-running
   :answer_a: Patches
   :answer_b: Abstractions
   :answer_c: Turtles
   :answer_d: Properties
   :correct: d
   :feedback_a: Although the patches change over time, they are not the only thing that changes!
   :feedback_b: Abstractions are coded in the computer, but they are not the thing that changes when the simulation runs.
   :feedback_c: Although the turtles change over time, they are not the only thing that changes!
   :feedback_d: Yes! Properties, such as the number of patches or the turtles energy, change over time.

   A running simulation change *what* over time?

When the simulation is run, it is the value of these global properties that are shown by the simulation's user interface (the two monitors at the bottom show the current values and the graph shows how these properties have changed over time throughout the simulation). To see the correspondence between the global properties and these user interface monitors we can examine each monitor in more detail. To see the details of a monitor left-click on the monitor causing a menu to appear. Choose the "Edit" option from this menu. The user interface will display a new window that gives the details for the monitor. For example, left-clicking and selecting the "Edit" option for the "count turtles" monitor leads to what is shown in the following figure.


.. figure:: /Images/CT-Class-Model-Count-Turtles-Monitor.png
   :align:  center

   The Monitor for the Number of Turtles


Notice that in the "Reporter" field the name of the global property "number-turtles" appears. This simply means that the monitor at each step in the simulation will show the corresponding value of this global property. To close the monitor window click the "Cancel" button in the monitor window. Try performing these steps on the "green patches" monitor. You should see that the "green patches" monitor displays the value of the global property "number-green-patches".

The plot monitor in the user interface for our simple ecological model shows the values of the two global properties over time. To see this we can examine the details of the plot monitor using the same two steps of left-clicking on the monitor and selecting the "edit" option. The following figure shows the new window that appears with the details of the plot monitor.


.. figure::  /Images/CT-Class-Model-Plot-Monitor.png
   :align:   center

   The Plot Monitor


Notice the middle of this window in the area labelled "Plot pens". The first line indicates that the black pen named turtles is to plot the value of the global property "number-turtles". The second line indicates that the green pen named grass is to plot the value of the global property "number-green-patches".

A bit of terminology: because the properties of the agents and the global properties are often variable properties the term "variable" is often used as a shorthand. We will start to use these two terms interchangeably hereafter.

.. mchoicemf:: coding-abstraction-variable
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: Don't get confused by the terminology here! This isn't like algebra! Properties/Variables change over time, as the simulation runs.
   :feedback_b: Variables/Properties change over time, so they are different from variables in algebra!

   In Computer Science, variables are unknown quantities that have a fixed value.

It is important to separate the basic concepts from how these basic concepts appear in NetLogo. There are two basic concepts in this section. The first basic concept is that the properties of abstractions can be represented in a programming language. NetLogo has a particular way of expressing these properties but other programming languages may, and likely do, have different ways of expressing the same properties. The second basic concept is that a user interface can show the values of any property. This allows us to peer "inside" the computer" to see the changes that are being made to properties. Of course, these changes are being made rapidly so graphs or other visualizations that show the changes over time are often used. Again, NetLogo has a particular set of user interface monitors but other user interface frameworks may have different ways of displaying the same information.

**Summary:**

* Abstractions are coded into a computer using a programming language.
* A model has Code and a User Interface.
* When the program is running, its "state" changes over time.
* The user interface for a model can show the current value of properties.
