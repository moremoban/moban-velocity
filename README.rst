================================================================================
moban-velocity
================================================================================

.. image:: https://api.travis-ci.org/moremoban/moban-velocity.svg
   :target: http://travis-ci.org/moremoban/moban-velocity

.. image:: https://codecov.io/github/moremoban/moban-velocity/coverage.png
   :target: https://codecov.io/github/moremoban/moban-velocity
.. image:: https://badge.fury.io/py/moban-velocity.svg
   :target: https://pypi.org/project/moban-velocity

.. image:: https://pepy.tech/badge/moban-velocity/month
   :target: https://pepy.tech/project/moban-velocity/month

.. image:: https://img.shields.io/github/stars/moremoban/moban-velocity.svg?style=social&maxAge=3600&label=Star
    :target: https://github.com/moremoban/moban-velocity/stargazers


With `airspeed` for Python 3, this library allows moban users to have velocity
template in their next documentation endeavour.

Given the following data.json:

.. code-block::

   {"people":
       [
           {"name": "Bill", "age": 100},
           {"name": "Bob", "age": 90},
           {"name": "Mark", "age": 25}
       ]
   }

And given the following velocity.template:

.. code-block::

   Old people:
   #foreach ($person in $people)
    #if($person.age > 70)
     $person.name
    #end
   #end
   
   Third person is $people[2].name

**moban** can do the template:

.. code-block:: bash

   $ moban --template-type velocity -c data.json -t velocity.template
   Velocity-templating vo.t to moban.output
   Velocity-templated 1 file.
   $ cat moban.output
   Old people:

   Bill
 
   Bob
 
 
   Third person is Mark




Installation
================================================================================


You can install moban-velocity via pip:

.. code-block:: bash

    $ pip install moban-velocity


or clone it and install it:

.. code-block:: bash

    $ git clone https://github.com/moremoban/moban-velocity.git
    $ cd moban-velocity
    $ python setup.py install
