.. This file is part of the OpenDSA eTextbook project. See
.. http://algoviz.org/OpenDSA for more details.
.. Copyright (c) 2012-2013 by the OpenDSA Project Contributors, and
.. distributed under an MIT open source license.

.. avmetadata::
   :author: OpenDSA & CompThink Contributors
   :satisfies:
   :topic:


Introduction to Blockly
=======================

In this section we will learn how to develop algorithms in a visual programming language called Blockly. In a visual programming language the basic elements of the language are represented by graphical icons. The graphical icons can be selected, copied, and moved around in a workspace to create a complete program in the visual language. There are many visual programming languages. Blockly is used here because it suits well our needs for learning about computational thinking. Blockly is so named because each of its graphical icons is referred to as a "block."



Blockly is a real programming language: programs written in Blockly can be directly executed and they can be directly translated into the code of standard programming languages. In particular, we will see the translation of Blockly into Python. We will also make use of blocks that allow us to begin manipulating real-time and large-scale data collections. We will see in the following examples how Blockly represents the basic elements of a programming language: calculation, sequence, decision, and iteration.



The Blockly programming environment consists of an area containing the palette of predefined blocks and a work area. Any block in the palette can be selected and dropped into the work area. We will see more of the mechanics in the coming examples. An important feature of Blockly is that its blocks are designed to "snap together" so that only syntactically correct arrangements of the blocks are allowed. This feature of Blockly allows us to sidestep temporarily the syntax issues in programming and focus on the logical structure of the code we are trying to create. Blocks may also have options that can be selected to change the behavior of the block in some way.


Calculation
-----------


To see how Blockly can be used to construct simple calculations we will use the simple plane seat calculator problem that is shown in the figure below. At the top of the figure you will that we are currently working on the first of three levels of this problem. The goal is to build a Blockly program that calculates the number of  seats on the aircraft shown in the figure. The slider just below the plane's fuselage is a control that allows for additional rows of seats be added to the plane. In the figure the slider is set for 5 rows. As can be seen, each row has four seats. This is a trivial problem but is useful to illustrate the mechanics of putting Blockly blocks together to make a simple program - in this case a program that does a simple calculation.

..  figure::  Blockly-Plane-Seat-Calculator-Problem.png
    :align:   center

    The Blockly Plane Seat Calculator Problem





The Blockly programming environment for this problem is shown in the next figure. The palette of available blocks is shown in the gray area on the left. The work area is to the right. Currently in the work area is a block named "seats =". Our goal is to use the blocks from the palette to create a calculation that correctly determines the number of seats on the airplane.

..  figure::  Blockly-Plane-Seat-Work-Space.png
    :align:   center

    The Blockly Plane Seat Work Space

There are four blocks in the palette. The top-most block can represent a number. The number currently represented is 0, but you can click on the number either in the palette or in the work space and change the number to any integer. The middle two blocks perform simple arithmetic. These two blocks are currently set so that they perform addition and multiplication. By clicking on the option icon next to the "+" or "x" signs you can change the arithmetic operation that the block performs. You should observe that arithmetic blocks have two "holes" in them. These holes are where we want to place the two values that will be used by the arithmetic operation. The bottom-most block, named "rows" will have whatever value is currently indicated by the slider control.  Initially, the slider is selecting 5 rows and the block label is "rows (5)." As you move the slider you will see that the number in parenthesis in the block's label changes accordingly.




To form a calculation, blocks from the palette are copied into the work space and composed. The calculation that computes the number of seats is "4 x rows" (e.g., if there are five rows then there are 20 seats). One way to create the correct calculation is by four steps. The workspace after each step is shown in the figure below.



1. drag a copy of the multiplication block into the work space and connect it with the "seats =" block.

2. drag a copy of the "rows" block into the work space and insert it into one of the holes in the multiplication block.

3. drag a copy of the number block into the work space and change its number to 4,

4. insert the number block it into the remaining hole in the multiplication block.





..  figure:: Blockly-Plane-Seat-Level1-Steps.png
    :align: center

    The Steps to Create the Level 1 Calculation





This Blockly calculation is complete because there are no remaining holes. You can execute this program by moving the slider (to change the value of the roles block) and see that the airplane display is updated with the correct number of sets.




In this simple calculation there was only one level of "nesting". That is, each hole in a block was filled by a block that did not itself have holes. For more complicated calculations it will be necessary to use higher levels of nesting (blocks within blocks within blocks...). For example, consider calculating the result of:



.. code:

   4 x (rows - 4) + (4 x 2)




for an airplane that has four seats in all but four rows and those rows have only 2 seats. In this case three levels of nesting are needed.




Exercise - figure out what the "^" operation does.

Exercise - do level 2 of the plane seat calculator

Exercise - do level 3 of the plane seat calculator





Sequence
--------


An example of moving through a maze is used to illustrate how Blockly can represent a sequence of actions. The first level of the maze problem is shown in the figure below. On the left is the maze. The maze contains an avatar and a highlighted path from the starting point of the avatar to a goal. The intention, of course, is to devise a Blockly program that will move the avatar along the path to the goal. On this level there are three blocks in the palette: a "move forward" block that causes the avatar in the maze to move forward one step in the direction it is facing, and two "turn" blocks that are intially set to turn the avatar to the left or right. Once our program has been assembled we can test whether it works by pressing the "Run Program" button.


.. figure:: Blockly-Maze-Level1.png
   :align:  center

   The Blockly Maze (Level 1)

Notice that each of the block has a notch at the top and a bump at the bottom. The bump at the bottom of one block will fit into the notch at the top of another block. In this way blocks can be "stacked up" in the sequence which we want to execute the blocks when the Blockly program is run. In this simple example all that is needed is to have the avatar move forward twice. This can be done by stacking up two "move forward" blocks. When this program is executed the avatar moves to the goal. In this case the "turn" blocks are not needed.

The important thing to notice is how to describe a sequence of actions in Blockly: by arranging that the bottom of one block fits into the top of the block below it.

Maze level 2 is similar but involves the use of the "turn" blocks.


Iteration
---------


Remember that iteration gives the programmer the power to cause an action to repeated over and over. On each iteration something has changed so that the repetition is not mindlessly the same. In the maze examples level 3 introduces the use of iteration. The figure below show the Blockly maze at level 3.

.. figure:: Blockly-Maze-Level3.png
   :align: center

   The Blockly Maze (level 3)


The new block introduced in this example is the "repeat until do" block. This is a form of condition iteration, meaning that the iteration continues (repeats) up to the point (until) a condition is achieved. In the case of the block here, the condition is reaching the goal (as denoted by the goal icon).  Notice that the "repeat until do" block has a gap into which another block can be inserted. As you might suspect, the meaning of the "repeat until do" block is that whatever block is inserted will be repeatedly executed until the condition is achieved.

In solving this level of the maze we could, of course, just use sequence and "stack up" as many "move forward" blocks as are needed to reach the goal state. This is not an acceptable solution because it is not a strategy that will work well in practice when there are hundreds, thousands, or millions of times that a step needs to be repeated. Moreover, the maze (albeit artificially) limits the number of blocks that can be used in a solution. In this case, only one additional block can be used in the work space. The block constrain is artificial, but it does force the use of iteration, which is the point of this level.

What is to be repeated in an iteration may, in general, be more than one block. This is the case on some of the next maze levels. To get two blocks to "plug into" the gap in the "repeat until do" block you must first compose the two blocks together in a sequence. These two blocks can then be moved as a unit into the gap in the "repeat until do" block. In a similar way, as many blocks as are needed can be composed into a sequence before being inserted into the gap of the "repeat until do" block.

Exercise - do level 3
Exercise - do level 4
Exercise - do level 5




Decisions
---------

The mazes seen so far have been relatively simple in that navigating the avatar to the goal only required a fixed pattern of actions to be repeated. More complex mazes require more ability to assess the avatar's current circumstances and move accordingly. Such programming needs the "intelligence" offered by decisions.

The sixth maze level is complicated enough that it cannot reasonably be solved without decisions. This maze is shown in the figure below. As you cna see, this is a "left turn only" maze. There are, of course, many such possible mazes. The level 6 maze requires decisions because the avatar will need to make four left hand turns to reach the goal. However, the distance between these turns is different in each case. So, we cannot simply rely on repetition to guide the avatar. We could, of course, simply arrange a sequence of "move" and "turn" blocks that works for this specific maze. But this is not an interesting solution because it will not work on any other maze. It is also not realistic because, in practice, we want to be able to write programs that work for all cases - not just a single case.


.. figure:: Blockly-Maze-Level6.png
   :align:  center

   The Blockly Maze (level 6)


The new block in the palette for level 6 is an "if do" block. The meaning of this block is that the "path" immediately in front of the avatar is tested according to the optional setting. The optional setting on this block allow the test to evaluate three different possibilities: ahead, to the left, to the right. TheThe result of each test is either true or false. For example, in the initial state the condition "path ahead" is true and the other two conditions are false. When the avatar is at the first turn, the condition "path ahead" is false while the condition "path to the left" is true. In this particular maze the condition "path to the right" is never true. If the result of the test is true then the statement(s) in the "do" gap are performed. If the result of the test is false then the statement(s) in the "do" gap are not performed.

One way to think about the logic for the avatar is that the avatar acts according to two rules:

* if the path ahead is true then move forward
* if the path to the left is true then turn left

Notice that we do need a third rule for checking if the path is to the right because this is a left turn onlymaze. The avatar repeatedly applies these two rules until it reaches the goal. We can program this logic in Blockly as shown in the next figure.

.. figure:: Blockly-Maze-Level6-Solution1.png
   :align: center

   First Solution for Maze (Level 6)


Try this solution to convince yourself that it works.

We can argue that the code for our avatar is correct. At each step the next location ahead of the avatar is either straight or a corner. These are the only two possibilities in this kind of maze. If the next location is straight then the avatar moves forward. Since this is not a corner it does not turn. If the next location is a corner then the avatar move forward to the corner and turns. In each of these cases the actions of the avatar are correct. Since the avatar code is correct in all of the (two) possibilities it must be correct overall.

Exerecise: exchange the order of the two if statements in the code. See that this also work. Develop an argument similar to that above to argue that the code for this avatar is correct.



A different way to think about the logic for the avatar is that the avatar acts according to these rules:

* move ahead
* if the path to the left is true then turn left


The avatar repeatedly applies these two rules until it reaches the goal. This logic for the avatar can be programmed in Blockly as shown in the next figure. We can argue that this version of the code for the avataris correct. At each step the next location ahead of the avatar is either straight or a corner. If the next location is straight then the avatar moves ahead and does not turn. If the next location is a corner then the avatar moves to corner and turns. Again, these are the only two cases and the avatar acts correctly in each.


.. figure:: Blockly-Maze-Level6-Solution2.png
   :align: center

   Second Solution for Maze (Level 6)



Exercise: exchange the order of the if statement and the move state in the code. See that this also work. Develop an argument similar to that above to argue that the code for this avatar is correct.


Exercise: Do level 7 of the maze

Exercise: Do level 8 of the maze



In more complicated mazes the avatar's programming relies on logic where the avatar needs to do one or other of two things. This kind of logic is needed for the maze presented in level 9 that is shown in the figure below. Notice that a new block has been added, an "if do else" block. The meaning of this block is that the condition is tested and is either true or false. If the condition is true the blocks in the "do" gap are performed. If the condition is false the blocks in the "else" gap are performed. In no case are the blocks in both gaps performed.

.. figure:: Blockly-Maze-Level9.png
   :align:  center

   The Blockly Maze (level 9)


A general strategy for maze walking is to keep the same hand on the wall at all times. A "right hand" strategy means that you keep your right on the wall at all times. A "left hand" strategy means that you keep your left hand on the wall at all times. These strategies work for many, but not all, mazes. One issue when using these strategies is that you can reach a dead end (there are several in the level 9 maze) and must be able to recover so that the avatar does not get "stuck" in the dead end. Properly dealing with dead ends in the maze requires more sophisticated logic than was needed for the earlier mazes.

A solution for the level 9 maze using a "right hand" strategy is shown in the next figure.


.. figure:: Blockly-Maze-Level9-Solution.png
   :align: center

   Second Solution for Maze (Level 9)


We can analyze this program as follows. At each step the avatar is in one of four possible conditions

* a right hand turn is available,
* the path forward is available,
* it is at a corner with a left hand turn, or
* it is at a dead end.

Because we are following a right hand rule there is a preference among these conditions. For example, if the avatar could go ahead or make a right turn, the right hand rule gives preference to turning right. Because of this preference, the first two conditions must be ordered. That is, the second condition is only tested when we know the first condition is false. In terms of our programming, the test for the path forward is then in the "else" part of the test for the availability of a right hand turn. Similarly, the last two conditions are only relevant when we know that no right hand turn is available and no straight path is available. In either case the only action possible is to turn left. If we are at a corner with a left hand turn we will then be pointed in the correct direction. If we are in a dead end then the next iteration will also the avatar to make another left hand turn, thus reversing course out of the dead end.

The important thing to take away from this example is the role of nested  "if then else" statements to convey preferences among the available actions - that is, to insure that some conditions are tested only if other conditions are known to be false (in this case) or true.



Exercise: draw a flow chart of the logic for the above solution

Exercise: develop a solution for level 9 using a left hand rule

Exercise: develop a Blockly solution for level 10
