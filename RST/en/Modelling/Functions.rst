Functions
=========



Natural and man-made systems often have a structure that involves specialized parts that operate together. Even simple living organisms have a distinct nucleus that interacts with the other parts of the organism. In more sophisticated creatures there are a variety of highly specialized organs each of which performs a specific function and which interacts with, at least some of, the other organs. In humans the heart and the lungs are very different from each other, each having a specific purpose, and they interact to pump oxygen enriched blood throughout the body. Man-made machines take advantage of this same organizing principle. An automobile has an engine and a transmission which are very different mechanically but which interact to provide power to the automobile's wheels.




Programmers also take advantage of the idea that a software system can be built out of specialized parts that interact in a certain way to create the desired functionality. The advantage of this approach are several:

* intelligibility - For even relatively small programs it is difficult for the human reader to understand what the program is doing. This task quickly becomes impossible for programs that are measured in hundreds of thousands or millions of lines of code. The only hope is to provide a structure of interacting parts so that the parts can be understood individually and then the assembly of these parts can be understood.
* reuse within - In a given program the same actions may be needed at different places in the code. As we will see, having a part that performs actions it is possible to avoid having to repeat the statement of the actions (the code) at all the places where it is needed.
* reuse across - A part developed for one program can be used in another program that needs the same function that the part provides. This makes it easier to develop new program out of existing parts. Many software systems rely on "libraries" of highly reusable components.
* replacement for improvement - In a system of interacting parts it is possible to replace one of the parts with a "better" part whether this a heart transplant or getting new tires for your car. In a software system one part could be replaced by one that is more reliable than the previous version (i.e., some bug in the previous version is fixed) or is more efficient (i.e., runs faster).
* replacement for change - A function often encapsulates a particular action (e.g., convert a temperature from Fahrenheit to Celsius). If we want to change the action currently performed by a function (e.g., convert a Fahrenheit temperature to the corresponding temperature on the Kelvin scale) it is possible to make that change in the function itself and then this change will be "automatically" in effect whenever the function is used.
* construction - An assembly line is an efficient way to construct automobiles because many workers can be involved in the construction of a single vehicle, each working at a different stage of the assembly process. As the partially completed automobile moves down the assembly line new parts are added until the automobile is complete. Similarly, the construction of a large program involves the work of many programmers. To organize their work efficiently different programmers are assigned to construct different parts of the system. These parts are then composed to create the overall system.



To take advantage of the idea of programming a software system out of specialized parts we need to learn how to define these parts and how to connect them together.




A function is the name given to the basic building block of a program. The names procedure or subroutine are also used for this building block. The key elements of a functions are:

* name - each function has a distinct name
* body - each function has a body that gives the code to be executed by this function.



Each programming language will have its own syntax for defining a function. In NetLogo a function is specified as:



.. code::

   to name

     body

   end




where the "to" keyword is used to denote the beginning of a function and the "end" keyword denotes the end of the function definition. Stylistically, function names in NetLogo are often verbs (denoting an action) so the reading "to name" is often readable. For example, the simple ecological model has functions that are named "move-turtles" and "eat-grass". So it is meaningful to read the code as "to move-turtles do this" and "to eat-grass do this".




An example of a NetLogo function in the simple ecological model is the move-turtles function which is defined as:



.. code::


   ; rule for a turtle to move

   to move-turtles

     ask turtles [         ; apply this rule to all turtles one at a time

       right random 360

       forward 1

       set energy energy - 1

       set age age + 1

     ]

   end





We saw the body of this earlier in discussing iteration. The only new thing that is seen here is how the code for the iteration is defined as a function with the name move-turtles. Be sure to note that the definition of the function begins with the keyword "to" and ends with the keyword "end" - everything in between is the body of the function.




To actually execute the actions that are defined in a function the function must be "called" or "invoked". Whenever the function is called (or invoked) the actions defined by the function are executed. In NetLogo a function is called simply by giving its name. For example, here is the code that is executed when the "Go" button is in the down state.



..  code::


    ; the actions to be taken when the Go button is "down"


    to Go

      if ticks >= 500 [stop]

      move-turtles              ; call/invoke the move-turtles function

      eat-grass

      reproduce

      check-death

      regrow-grass

      tick

    end




The important thing to see in this code is that calling/invoking the move-turtles function is as simple as writing a line of code that has the name of the function. You can also see that several other functions are also called/invoked: eat-grass, reproduce, check-death, and regrow-grass. These are all functions whose code is defined by the model's creator. It is also the case that "tick" and "stop" are also functions, but ones implemented by the builders of NetLogo itself.




The code above also illustrates an important aspect of building software - that one function can call/invoke another function. Notice that the Go function calls the move-turtle function and the other functions also shown. As the code for a program grows larger it is a common practice to draw a "call graph" showing which function call which other functions. A call graph for our simple ecological model is shown in the next figure.



..  figure::  /Images/CT-Class-Model-Call-Graph.png
    :align:   center

    A Call Graph





The call graph provides a map to the hierarchical organization of the program. The purpose of a call graph is similar to the use of diagrams of physical systems to show how the parts of the system relate to each other. For example, the figure below show relationship information among the parts of a piece of furniture.



..  figure:: /Images/Exploding-Diagram.png
    :align:  center

    An Exploding Diagram





If you learn more about software and its development you will see that the call graphs for larger systems are much more complex than the one for our simple system. Also, you will see that there are other graphical representations of the structure of a program to help programmers understand how the system in organized.


