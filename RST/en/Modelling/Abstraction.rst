Abstraction
===========


Dealing with Complexity
-----------------------

The world is complex, so people often form simple representations of real-world artifacts and phenomenon to deal with their complexity. These simplified representations focus on the essential aspects of something and hide less important aspects.  The simplification reduces the complexity to a level where one of the following can take place:

* understanding,
* explanation,
* expression,
* planning,
* analysis, or
* manipulation

What is essential or not essential to a simplified representation depends on the purpose or goal that one has in mind. Just as "Beauty is in the eye of beholder", so also "what is essential is in the purpose of the user." **A simplified representation made for one purpose may be useless for another purpose!**

People use simplified representations in everyday life. Maps are a good example. The map of the Washington D.C. Metro system (see the :ref:`following image <metro-map>` ) is a simplified representation of the more complex reality that forms the "real world" transportation system. This is a simplified representation designed to help travellers plan and complete a journey on the transportation system from a starting station to a destination station. It is a simplified representation because it deliberately does not include a great deal of the complexity of the actual Metro system. For example, the map does not:

* Include facts about schedule or cost,
* Have the location of any station,
* Show which parts are above ground and which are below ground,
* Show the interior layout of the train cars.

You can easily think of many other things about the Metro system that the map does not show. However, the map serves a useful purpose -- navigating between stations -- and the simplification is critical to serving this purpose. Of course, it is not useful for other purposes. For example, the map is not drawn to scale, so it is not useful to the task of figuring out how much track is needed between two stations. You can likely think of other tasks for which this map is not useful.

.. _metro-map:

.. figure:: /Images/Metro-Map.png
   :align: center

   An Abstraction of the DC Metro System


The relationship between a real artifact and its simplified representation is illustrated in a painting by Rene Magritte done in the late 1920s. This painting is shown in the following image. The painting, titled the :ref:`Treachery of Images <pipe>`, depicts a smoking pipe and has the seemingly contradictory caption painted by Magritte that is French for "This is not a pipe." Magritte is quoted as saying about this painting that:

*"The famous pipe. How people reproached me for it! And yet, could you stuff my pipe? No, it's just a representation, is it not? So if I had written on my picture "This is a pipe", I'd have been lying!* -- Rene Magritte

.. _pipe:

.. figure:: /Images/Magritte-Pipe.png
   :align: center

   An Abstraction of a Pipe [#]_


Of course, Magritte is correct that the painting of a pipe is not the same as the actual pipe; it is merely a simplified representation of a pipe. It is a simplified representation because it includes some of the properties of the real pipe (shape, appearance) but the painting does not show the actual dimensions of the pipe, what it is made of, what it weighs, etc.

**Summary**: Simplified representations reduce the complexity of an entity to make it easier to work with.

.. mchoicemf:: modelling-abstraction-complexity
   :answer_a: A way of describing things based on a context
   :answer_b: A sequence of instructions to the computer
   :answer_c: A pipe
   :correct: a
   :feedback_a: Excellent!
   :feedback_b: That's an Algorithm, which we will learn about later. Although we often put Abstractions into a computer, in general Abstractions can be used anywhere (e.g., to make a subway map).
   :feedback_c: That was just a philosophical example. Read the last two paragraphs a bit more closely!

   An abstraction is...

.. mchoicemf:: modelling-abstraction-maps
   :answer_a: How much does the pipe cost?
   :answer_b: Does the pipe smell like smoke?
   :answer_c: How much does the pipe weigh?
   :answer_d: What color is this pipe?
   :correct: d
   :feedback_a: There is no price listed on the painting, so it's not clear from just the painting how much it costs.
   :feedback_b: Smelling a picture of a pipe on your computer screen will not tell you what it smells like in real life.
   :feedback_c: You cannot tell just by looing at that pipe how much it weighs. How do you know if the original pipe had a steel interior?
   :feedback_d: You can easily see what color the pipe is because of this painting.

   Consider the abstraction of the pipe picture above. Which of the following questions can be answered with this abstraction?

Abstractions in Computing
-------------------------


An :term:`abstraction` is a simplified representation of an entity that is used in a computation. The term "entity" is chosen because abstractions can be formed about anything:

* People
* Places
* Actions
* Objects
* Events
* Processes
* ...

This means that abstraction is a powerful and basic tool.

A crucial fact is that to be able to compute with abstractions, the abstractions have to be expressed in terms of information -- something that computers are built to deal with. While Magritte could make his simplified representation using oil and canvas, we cannot get oil and canvas into a computer (or at least, we don't recommend it!).  This use of :term:`abstraction` - to simplify representations of real-world artifacts - is only one way in which the idea of abstraction is used in computation. We will later see different uses of abstraction in computation.

Making an abstraction of an entity means selecting the entity's properties that can be expressed as information. The information is what we compute about. A simple example is a book. Its properties might include:

* The title
* The author
* The publisher

A book has many other properties as well:

* Its genre
* How many pages it has
* Whether it is hardcover
* Its price
* Its dimensions
* The table of contents
* The dedication
* The cover artwork
* The ISBN number

Even this longer list is by no means exhaustive. You could likely think of many other properties of a book.

.. fillintheblank:: modelling-abstraction-book
    :correct: .*
    :feedback: ('.*', "Now check what your classmates said!")

    Another property of a book is :textfield:`book-property::medium`.

However, we are usually not interested in enumerating all the properties of an entity. We usually want to reduce the number of properties to all those and only those properties that are relevant to our purpose. If our purpose in representing a book is that of a librarian then such properties as title, author and ISBN number are relevant while the book's dimensions, dedication, and cover art are not relevant. The properties that are relevant are those that are important for the work that the librarian does. Similarly, if we were developing an automated library system the relevant properties are the ones that would need to be included in our book abstraction. However, if our purpose is that of a delivery company shipping the books to purchasers then the only properties above that are relevant for the book abstraction are the book's weight and dimensions. The book abstraction of the delivery company might also include other properties such as the customers address, the delivery date, a tracking number, and the current location of the book in the delivery system.

While the term "abstraction" can seem very vague, the use of abstractions in computation is very concrete. Abstractions can be seen behind the web pages of sites that deal with various kinds of entities. For example, the following image shows a part of the amazon.com web page for a Harry Potter book. Notice that this web page demonstrates an abstraction of the book because it displays properties of the book that Amazon found relevant for their purposes of selling books. The properties shown on this part of the web page include several properties named above: title, author, cover art, and price.


.. figure:: /Images/Amazon-Harry-Potter-Book.png
   :align: center

   Amazon's Abstraction of a Book


Another web page that represents a different abstraction of the same Harry Potter book is given on the Virginia Tech Library System. The image below shows how a librarian might define the relevant properties of this book. As with the Amazon web page, the Virginia Tech Library System web page also shows the title and author of the book.


.. figure:: /Images/VT-Library-Harry-Potter-Book.png
   :align: center

   The VT Library Abstraction of a Book


However, the abstractions of the Harry Potter book by Amazon and the Virginia Tech library are not the same. The Amazon abstraction contains a price while the library abstraction does not. Also, the Virginia Tech library abstraction contains a "call number" (a code of where to find the book in the library) while the Amazon abstraction does not contain this property.


.. mchoicemf:: modelling-abstraction-check
   :answer_a: True
   :answer_b: False
   :correct: b
   :feedback_a: A good abstraction should only have relevant properties!
   :feedback_b: Good!

   A good abstraction has both relevant and irrelevant properties.

**Summary:**

* Abstractions are simplified representations that are used in computing.
* An abstraction gives all of the relevant properties of an entity.
* What properties are relevant depends on the purpose for which the abstraction will be used.
* There can be different abstractions for the same entity when the abstractions are used for different purposes.

.. [#] Torczyner, Harry. Magritte: Ideas and Images. p. 71.
