# ChangeCalculator

This (tiny) project was inspired by a JavaScript course project found at www.freecodecamp.org !

Specifically, [this](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/javascript-algorithms-and-data-structures-projects/cash-register) project ('Cash Register').

I don't think the original author was intending for students to use a recursive solution, but it seemed appropriate for the problem presented.

The behaviour of this recursive function is somewhat similar to that of a search tree.  It is not 'smart', i.e: it will not find the solution in the _fewest_ coins, it will just find the _first_ solution and return it:

Desired Change: 8

Available Coins: 5, 4, 4, 1, 1, 1

Returns: 1, 1, 1, 5 (A human would probably give you 4, 4)