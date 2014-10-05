NetLogo
=======

Exploring NetLogo Models
------------------------

NetLogo is an application using simulation to explore phenomenon in a wide variety of subjects.  The figure below shows the initial display that is presented when NetLogo is run. As we explore NetLogo further we will learn more about some of the NetLogo interface.


First, note the "File" menu in the upper left corner. We will see next how to find pre-developed NetLogo simulation models under the File menu. Also, note the large black area. This is the main simulation display. When a simulation model is run the visualization of the model will be shown in this display area.


.. figure:: /Images/CT-Class-Model-First-Screen.png
   :align:  center

   The Windows NetLogo Display

The appearance of NetLogo will be slightly different on different platforms. The figure above shows the appearance of NetLogo on a Windows system. For comparison, the appearance of NetLogo on a Mac system is shown below. The two version are very similar with only small differences due to the way each system arranges some of its menus and buttons. Notice that in the Mac version the "File" menu is located at the top of the display rather than directly attached to the NetLogo window as in the Window's display. Also notice that the NetLogo menus (Interface, Info, and Code) are  at the top middle on the Mac display while they are at the upper left in the Windows version. For brevity the figures used will be those from a Windows system.

.. figure:: /Images/CT-Class-Model-First-Screen-Mac.png
   :align:  center

   The Mac NetLogo Display


NetLogo contains a large number of models that have already been developed in different subject matter areas. To explore the model library select the "Models Library" option under the File menu as shown in the next figure.


.. figure:: /Images/NetLogo-Model-Library.png
   :align:  center

   Opening the NetLogo Model Library


When the "Models Library" option is selected a new window will show the index of the sample models. This window is shown in the following figure. As you can see there are sample models in art, biology, mathematics, social science, and other fields. In all there are over 100 sample models. The models library also contains a collection of Curricular Models, models that have been developed for use in specific courses. The community of NetLogo users has also developed other models that they have made available. You can see these models by clicking on the "Go to User Community Models web page" button at the bottom of the Models Library page. This will send your browser to a web page that describes each model and has a link for downloading the model.


.. figure:: /Images/NetLogo-Model-Library-List.png
   :align:  center

   The Top Level of the NetLog Model Library


By clicking on the "+" sign next to a folder icon the models in that folder can be seen. The next figure shows the expanded folder for the Biology models. Notice that the expanded Biology folder contains some items that have a grey circle icon followed by a name. These entries are NetLogo models that can be run. The first two NetLogo models in the Biology folder are named AIDS, and Ant Lines. The Biology folder also contains another folder (named Evolution). This folder can also be expanded by clicking on the "+" sign next to the folder's name. Expanding the Evolution folder will show other models (shown as a grey circle followed by a name) and other folders.


.. figure:: /Images/NetLogo-Model-Library-Biology.png
   :align:  center

   Expanding a Folder in the Library


By clicking on the name of NetLogo model you can see a description of the model. For example, clicking on the AIDS model gives the description of this model as shown in the next figure. The description has a short text explanation of the model. As you can see this model simulates the spread of AIDS within a population. Above the text explanation is a representative image of the main simulation display for this model. The individuals in the population are shown in the simulation display area as people-shaped icons.


.. figure:: /Images/NetLogo-Model-Library-AIDS.png
   :align:  center

   A Quick Overview of a NetLogo Model


To find out more about a library model you can download the model by clicking on the "Open" button (at the bottom of the previous figure). The AIDS library model will appear as shown in the next figure. You will see here a collection of user interface controls (button, sliders, graphs). We will learn more in the next section about what control like this do in NetLogo.


.. figure:: /Images/NetLogo-Model-Library-AIDS-Initial-Screen.png
   :align: center

   Opening a NetLogo Model


However, we can learn more about the model by reading the authors description of the model. This description can be seen by selecting the "Info" tab near the top of the NetLogo window. The description for the AIDS model is shown in the following figure.


.. figure:: /Images/NetLogo-Model-Library-AIDS-Initial-Screen.png
   :align:  center

   Looking at the Description in the "Info" Tab


In this figure you can see the first section of the AIDS model description. A typical model description has these sections:

* WHAT IS IT?  - a general understanding of what the model is trying to show or explain.

* HOW IT WORKS - the rules the agents use to create the overall behavior of the model.

* HOW TO USE IT - a description of each of the items in the interface tab.

* THINGS TO NOTICE - suggestions for things to observe while running the model.

* THINGS TO TRY - suggestions for things the user can do to control the model (move sliders, set switches, etc.) especially if these illustrate interesting conditions or patterns of behavior.

* EXTENDING THE MODEL - things to add or change in the model's implementation to make the model more complicated, realistic, or meaningful, etc.

* NETLOGO FEATURES - any interesting or unusual features of NetLogo that the model uses in its implementation.

* RELATED MODELS - other models in the NetLogo Models Library or elsewhere that deal lwith related concerns.

* CREDITS AND REFERENCES - where to find the model on the web and other credits, citations, and links related to the model.



You should now be able to explore the NetLogo model library. In a similar way you can explore the User Community Models using your web browser.



Running a NetLogo Model
-----------------------

.. download_list:: modelling-netlogo-model
   :files: CT-Class-Model.nlogo

   The example model can be downloaded from here.

Our next goal is to learn how to run a NetLogo model. Later we will look behind the scene at the programming that makes this model work. The model we will study is a simple ecological model that explores a population of turtles who feed on a renewable resource (grass) to survive and multiply. This model can be used to explore such issues as whether a given population size is sustainable, what happens to the population under different assumptions about the quality of the grass on which the turtles feed, and how the renewable resource is affected by the changes in the size of the turtle population. This is a simple model, of course, and you could likely think of other factors that a more comprehensive model might include.

When run, the CT-Class-Model presents the initial window shown in the next figure. You should recognize the main simulation display window (the black panel in the center right of the window).  On the left side of the display that are some controls (two buttons, an on-off switch, and three sliders. Below these controls are three additional "monitors" that give information during a run of the simulation.


.. figure:: /Images/CT-Class-Model-First-Screen.png
   :align:  center

   A Simple Ecological Model


Before the simulation can be run it must be initialized by pressing the "Setup" button (upper left among the controls). Pressing the "Setup" button tells NetLogo to use the current settings of the on/off switch and the sliders for the simulation run. For this first run we will use the initial settings. When the Setup button has been pressed (click on) the window appears as shown in the following figure. Three things have changed. First, the main simulation display area is no longer a black blank area. Instead, the background color is green, representing the grass, and a collection of turtles, represented by variously colored oval-like shapes. The turtles are placed at randomly chosen places in the environment. The number of turtles initially created is determined by the topmost slider. This slider has the label "number" and shows the current setting for the slider on the right part of the slider. As you can see, the slider is currently set at 77.  Second, notice that the two monitors on the bottom left have changed. One monitor, labelled "count turtles" shows 77, the current number of turtles. The other monitor is labelled "green patches" and has the number 1089. NetLogo divides the simulation display into a grid of "patches" that is 33 by 33 (thus a total of 1089). The third monitor, labelled "Totals" at it top is currently blank. This area will show a graph of turtles and patches as the simulation progresses. At this point we are ready to begin the simulation.


.. figure:: /Images/CT-Class-Model-Setup-Button.png
   :align: center

   Initializing the Model using the Setup Button


To run the simulation, simply press the "Go" button. Notice that the "Go" button changed its color to indicate that is now pressed "down". As long as the "Go" button is pressed down the simulation will continue to run. To stop the simulation, press the "Go" button again. Notice that the "Go" button changes back to its original color indicating that it is in the "up" position. Whenever the "Go" button is in the up position the simulation is stopped. Pressing the "Go" button again resumes the simulation. If you want to restart a running simulation simply press the "Go" button, putting the Go button in the up position, and press the "Setup" button.

When our simple NetLogo model simulation is running four areas are constantly being updated. The figure below shows the NetLogo simulation of our simple model when the model has been stopped after a few steps in the simulation. First, the main simulation panel now shows both green and black patches. In our model a patch is black when the grass has been eaten by a turtle and the grass has not had time to grow back. The set of black and green patches constantly changes as the turtles move around to find new grass to eat, changing a green patch to black, and the grass grows back, changing a black patch to green. You will also see in this display that the number of turtles changes and that the location of each turtle changes. These changes represent growth in the turtle population by breeding of well-fed turtles and the search of turtles for new grassy patches to eat. Second, the number of turtles, currently 484, is shown in the "count turtles" monitor. Third, the number of patches with grass, currently 85, is shown in the "green patches" monitor. Fourth, both the number of turtles and the number of green patches is shown in the graph in the "Totals" monitor. This graph shows the changes over time in the size of the turtle population and the number of grassy patches. The number of turtles is shown by the black line in the graph and the number of grassy patches is shown by the green line in the graph. As you can see, the turtles rapidly consumed many of the grassy patches and the number of turtles grew rapidly and then diminished slightly in number. The decline in the number of turtles is due to the death of turtles that cannot find grass to replenish their energy level.


.. figure:: /Images/CT-Class-Model-Running.png
   :align:  center

   Running the Model using the Go Button


You should now be able to run a NetLogo model and, by manipulating the controls in the model's user interface, be able to explore the behavior of the model under different conditions.


Agents-Based Modelling
----------------------

One way to organize a computational model is called agent-based modelling. In agent-based modelling the  principal entities of interest are "agents" which operate in an "environment". There are usually a few "types" (or "kinds") of agents with many individual agents of each type. For example, in our simple ecological model there are two types of agents: turtles and grassy patches. The model also has numerous turtles and many grassy patches.

The agents have, or own, a certain set of properties that describe their condition or features. All of the agents of a particular type (or kind) have the same properties but may have different values for these properties. For example, two turtle agents each have a *location* property but they two turtles are probably at different locations. Similarly, all grassy patch agents have an energy but some grassy patches may have more energy than others.

The agents' actions are determined by a set of "rules". The rules tell an agent how to change itself over time, how to interact with other agents, and how to react to changes in its environment. The agent's rules determine the *behavior* of the specific agent. The rules and properties of an agent allow the agent to behave differently at different times. For example, if the agent represents a "person", the agent may have an *age* property and rules that allow the agent to behave differently when it is is older than when it is younger. A "younger" person may be able to run faster than an "older" person. The general form of a rule is:

.. code::

   condition -> action(s)

which means that when a stated condition is true the agent takes a particular action. For example, in our simple ecological simulation one rule for a turtle might be:

..  code::

   "when on patch with grass" -> "eat grass"

This rule says that whenever the turtle agent finds itself on a grassy patch with grass then the turtle should eat the grass. We will see later how such rules can be represented in a computer using NetLogo's programming language.


Agents may be mobile, that is, capable of changing their location in the environment. For example, animals that are foraging for food or vehicles moving in a city are agents of this kind. Other agents may not be mobile, that is, they always are at the same location in the environment. For example, plants that are eaten by foraging animals, geographic features (lakes, mountains), or structures (buildings, streets) are agents of this kind. Agents that are mobile often have rules that define how they move about in the environment. These rules may allow for undirected ("random") movement or more purposeful movement ("move to the nearest location with edible plants" or "turn right at the next intersection"). Agents that are not mobile often have rules that describe how they change over time or in reaction to other agents. For example, a plant agent may have rules that describe how long it takes to regrow after being eaten or how much nutritional value it has given the rain and soil conditions.

The environment describes what the world around the agents looks like. For simplicity, the environment is often divided into basic units. NetLogo, for example, divides the world into a rectangular grid. Each element of the grid is a basic unit. In NetLogo these basic units are called "patches". The basic units of the environment also have properties and rules.


An example of an agent-based system is the simple ecological model that represents a population of turtles in an environment of grassy patches. The figure below shows the NetLogo simulation display for this model. One property of a turtle in this model is the turtle's age. The age is interesting to represent because it affects when the turtle can reproduce or how long the turtle can live. The environment consists of grassy patches. Properties of each patch is the nutritional value of the grass and the length of time needed to regrow the grass after it has been eaten by a turtle. The rules for a turtle determine how it moves around in the environment in search of grass to eat, whether it reproduces, and whether it survives or dies in a given condition. These rules are based on the turtles own properties (e.g., its age) and the environment (whether there is grass where the turtle is). The patches' rules determine what level of nutrition it has when eaten and when it is regrown after being eaten.


.. figure:: /Images/CT-Class-Model-Simulation-Display.png
   :align:  center

   The Simulated Agents in the Simple Ecological Model


More examples of agent-based systems will be described below. You can also explore other models in the NetLogo library.


A computational tool for agent-based system proceeds in a step-by-step fashion. Each "step" corresponds to the passage of some time. In NetLogo, each step corresponds to the "tick" of an imaginary clock. At each step, the rules of the agents and the environment are evaluated and the properties of the agents and the environment are updated. Because the computation is driven by the rules of the agents and the environment, the term rule-based systems is also used to describe this form of computation. In the blackjack system a step might consist of the dealer agent placing a card on the table in front of a player and the player deciding whether to stop or ask for another card. In the ecological simulation a step might consist of all the turtles moving a new location and eating grass if it is available at their current location.


Simulation plays an important role in agent-based modelling systems. Once the properties and rules for the agents and the environment have been defined a computational tool allows us to see how the system of agents changes and evolves. The figure above shows one example of the NetLogo simulation of the simple ecological system. One aspect of simulation system is the role of randomness. For example, in a simulation of the blackjack system there is a randomness inherent in the shuffling of the cards. It would easy to win if the cards were always dealt in the same order. When the cards are shuffled they are arranged in a random order. This is, after all, the purpose of shuffling. Non-random arrangement of the card deck often results in fights in Western movies. In the ecological model the turtles start out at random places in the environment and move around randomly thereafter. Because of this randomness, one simulation, often called a "run", will be different in detail from the next simulation of the same system with the same setting. This is realistic because one round of blackjack is different from the next round.


Aside from changes to the basic properties and rules, an agent-based model often has certain "parameters." These parameters define initial conditions, boundary conditions, or settings against which rules are evaluated. For example, in a blackjack simulation the parameters might define the number of players or the number of chips a player has (initial conditions), how many hands will be played (a boundary condition), or the card count at which the dealer "stands" (a setting). In the ecological model the parameters might define how many turtles are present at the beginning (an initial condition), the number of time steps in the simulation (a boundary condition), or the energy that the turtles gets from eating grass (a setting). By exploring the effects of different parameter settings, insight can be gained into the model. These insights can be the basis for human actions or policies in the real world.

.. mchoicemf:: modelling-netlogo-parameters
   :answer_a: A collection of rules that describe how an agent moves
   :answer_b: Properties that can be changed to control a simulation
   :answer_c: A way of describing things based on a context
   :answer_d: A turtle
   :answer_e: Defines how a simulation begins
   :correct: b
   :feedback_a: Although agents have rules, they are not parameters.
   :feedback_b: Good!
   :feedback_c: That's an Abstraction, not a parameter.
   :feedback_d: Read over the chapter a bit more closely.
   :feedback_e: Although some parameters define initial conditions, not all parameters do.

   A parameter is...

.. mchoicemf:: modelling-netlogo-agents
    :answer_a: Agents have rules and properties
    :answer_b: The environment is composed of Patches
    :answer_c: Patches have rules and properties
    :answer_d: Grass patches all have the same properties
    :answer_e: Agents have the same properties
    :correct: e
    :feedback_a: All agents have rules and properties!
    :feedback_b: As mentioned, these patches are laid out in a rectangular grid.
    :feedback_c: The grass patches in the example had an "age" and a rule that turtles on top of them would eat them.
    :feedback_d: Although individual patches may have different values for the same property, all grass patches have the same types of properties -- for example, age or color!
    :feedback_e: Good! Although agents that are of the same type (e.g., two Turtles) will always have the same type of properties, two agents of a different type (e.g., a Turtle and a Grass Patch) will have different properties.

    Which of the following is not true?



Emergent Behavior
-----------------

Agent-based system are often used to explore what is called "emergent behavior" of complex systems. The behavior of an individual agent is well understood - its behavior is encoded in its set of rules. For example, the rules for the turtles in the simple ecological model can be defined. However, the "system" formed by many (hundreds, thousands, millions) of agents interacting with each other and their environment also has a behavior. The system's behavior is characterized by global properties of the agents and the environment. For example, in the simple ecological model, global properties might be how many turtles there are, how much energy is in the grassy patches, etc. We are often interested in knowing what happens over a long period of time. For example, does the turtle population stabilize at some level? does it wildly oscillate? or do the turtles die out. This long term behavior "emerges" over time. For many interesting systems it is not always easy, and may not currently be possible, to predict mathematically the "emergent" behavior given the knowledge of the rules for the agents and the environment. Thus, simulations of agent-based models are used to explore a system's emergent behavior.


Unfortunately, no single simulation run of an agent-based model completely reveals the emergent behavior for two reasons. First, each simulation has some amount of random decision-making that makes each simulation run different from other simulation runs of the same model. Even though each simulation run is driven by some measure of randomness, systems often exhibit long-term behavior that is strikingly similar across different simulation runs. For example, we might see that a given blackjack "system" (i.e., the rules for a player agent) tends to lead to the loss of all chips very rapidly whereas another system tends toward oscillations in the number of chips over time but does not cause the player to go "bust." In the ecological system we might observe that certain parameter settings almost always leads to extinction of the turtle population (too many turtles and not enough nutrition in the grass) while other parameter settings lead to a sustainable population of turtles and grassy patches. Second, agent-based models often have parameters that describe the initial condition of the simulation. For example, in the simple ecological model one parameter is the number of turtles that the simulation starts with. Another parameter determines how much energy the grass contains. Intuitively, a simulation run with a few turtles in a very lush environment (one where the grass has a high energy level) is likely to show a different long-term behavior than a simulation run with many turtles in a very barren environment (one where the grass has little energy). Discovering the emergent behavior involves studying many simulation scenarios for each of a variety of parameter settings.



There are many examples where agent-based modelling is used to explore the emergent behavior of complex systems. Among these examples are the following.

* economics: The national economy consists of numerous kinds of economic "agents" each making decisions to improve their material well being. Agents include individual persons making decisions on purchasing goods and services, institutions (banks, investment firms) that seek return on their investments, business providing goods and services, and governments whose policies regulate the fairness of the marketplace. While it is possible to model potential behaviors of these individual types of agents, the number of agents and the complexity of their possible interactions makes it impossible to mathematically determine overall measures of the economy (gross national product, income levels, bank stability). However, agent-based modelling can be used to study the emergent behavior of an economic model. Such a model could be used by regulatory agencies to study the potential impacts of various policies on economic growth or by businesses to determine the best strategies for managing its resources in the market place. Here are some other places that describe how agent-based modelling is applied to economics:

  *   `Agent-Based Computational Economics <http://www2.econ.iastate.edu/tesfatsi/ace.htm>`_ .

  *  `The economy needs agent-based modelling <http://www.nature.com/nature/journal/v460/n7256/full/460685a.html>`_ .

  *   `New model army  <http://www.economist.com/news/finance-and-economics/21569752-efforts-are-under-way-improve-macroeconomic-models-new-model-army>`_ .

Many other examples can be found.

* natural resource management: As the world's population grows there is increasing attention given to how renewable natural resources are used. Natural resources include forests, fisheries, grass lands and the wildlife in these habitats. Computational agent-based models can be used to study the impact of different usage patterns and their impacts on the sustainability of the resources. The agents model the behavior of resources users (timber companies, fishing fleets, cattle producers) and the elements of the resource itself (acres of a forest, characteristics of fish habitats, square miles of grasslands). The emergent behavior can be studied to find patterns of use that avoid extinction of the resource and identify "tipping points" where the sustainability is lost.  Some example of this use of agent-based model are:

     * `Agents, individuals, and networks: modeling methods to inform natural resource management in regional   landscapes <http://www.ecologyandsociety.org/vol17/iss3/art32/>`_.

     *  `Agent Based Modelling in Natural Resource Management <http://www.insisoc.org/INSISOC/INSISOC_archivos/ABMbook/ABMbook.htm>`_.

     *  `An agent-based simulation model of a nutrient trading market for natural resources management <http://www.sciencedirect.com/science/article/pii/S0895717710005170>`_ .


* epidemiology: In an increasing connected world with travel to virtual anywhere in the world possible in a day the ability to detect and control the spread of infectious diseases is an important national and international issue. The current (in 2014) outbreak of the Ebola virus in West Africa is but one example of this need. Even within develop countries the spread of flu viruses is a significant concern. Agent-based models can be used to assess various tracking and containment protocols. What is the best way to use a limited supply of vaccine? Should everyone in the immediately affected area be vaccinated leaving the rest of the population exposed? Should only those in immediate contact with an infected person be vaccinated reserving the majority of the supply to treat other outbreaks? In an agent-based model the agents represent people who, when in proximity, can receive from  or transmit to the infection others. Here are some example of this use of agent-based models and emergent behavior:

   *  `A New Tool for Epidemiology: The Usefulness of Dynamic-Agent Models in Understanding Place Effects on Health <http://aje.oxfordjournals.org/content/168/1/1.abstract>`_ .

   *  `An agent-based approach for modeling dynamics of contagious disease spread <http://www.ij-healthgeographics.com/content/8/1/50>`_ .

   *   `An Agent-Based Spatially Explicit Epidemiological Model in MASON <http://jasss.soc.surrey.ac.uk/9/1/3.html>`_ .


* molecular modelling: Understanding the properties of organic and inorganic materials at the molecular level is important to answering basic questions in many fields of science. In an agent-based system each atom or molecule is modelled by an agent. The physical interactions is defined by the rules that the agents follow in interacting with other agents. In chemistry notions of self-assembly of molecules can be studied. In biology various kinds of diseases can be studied using this technique. Here are others:

     * `An agent-based approach for modeling molecular self-organization <http://www.pnas.org/content/102/2/255.full>`_ .

     *  `An Agent-based Modeling Apprach for Stochastic Molecular Events of Biochemical Networks <http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5750731&tag=1>`_ .

     *  `An Artificial Intelligence Approach for Modeling Self-assembly: Agent-based Simulations of Rigid Molecules <http://pubs.acs.org/doi/abs/10.1021/jp9030442>`_ .

     *  `Multi-scale agent-based brain cancer modeling and prediction... <http://www.biomedcentral.com/1471-2105/13/218>`_ .



* artistic performance: The performing and visual arts intersect with agent-based modelling ideas in interesting ways. In one case the notion of dancers behaving according to a set of rules that defined one dancers movements in response to other dancers and the environment. This form of dance is termed "flock logic" because it derives from agent-based models of flocking behavior in animals. In the visual arts, the term "generative art" refers to creations that involve a computational element. One form of generative art uses agent-based techniques in creative ways. The *Processing* system for generative art is based on agent-based ideas.

     *  `Flock Logic <http://www.princeton.edu/~flocklogic/>`_ .
     *  `OpenProcessing <http://www.openprocessing.org/>`_ .
     *  `Generative Art: a practical guide to using processing <http://zenbullets.com/book.php>`_ .

Many other kinds of systems have been studies through agent-based modelling in economics, social sciences, the arts, chemistry, physics, and others. The NetLogo library contains over 100 such models. A quick search on the web will yield a wide variety of other uses of this computational technique (see for example `OpenABM <http://www/openabm.org>`_  and `RunTheModel <http://www.runthemodel.com/>`_ .

.. mchoicemf:: modelling-netlogo-emergent
    :answer_a: Easy to predict
    :answer_b: Hard to predict
    :correct: b
    :feedback_a: If it was easy to predict, than we wouldn't need computers!
    :feedback_b: That's why we have computers run simulations!

    A simulation with emergent behavior is...
