# What is this?
Evolution/ artificial selection simulator, inspired by Heikegani crabs. 
From the wikipedia article:
"...according to this hypothesis, the crabs with shells resembling Samurai were thrown back to the sea by fishermen out of respect for the Heike warriors, while those not resembling Samurai were eaten, giving the former a greater chance of reproducing. 
Thus, the more closely the crabs resembled a samurai face, the more likely they would be spared and thrown back."

# How does it work?
To simulate this, we generate sprites based on mutations of an original 'DNA' matrix. Every sprite has an associated barcode like DNA from which it is drawn. By performing small mutations on this DNA we can draw a set of similar but distinct sprites. If we click the sprite that looks most like a face in each generation, the next generation will use the DNA of the face-like selecion to generate similar mutations. In this way we can progressively make the sprite look more like a face with each generation.

# Using the simulation

Run the code to generate a grid of sprites. User clicks preferred sprite (in this example we prefer sprites that look like human faces) and a new grid of sprites is generated based on the previous selection. Continue until either the number of simulation steps is reached or a key is pressed. The evolution is then displayed in reverse chronological order.
Some examples are shown below.

A face sprite and it's unique corresponding DNA matrix:

<p align="center">
<img src="https://github.com/scottgilmartin/Evolution_Simulator/blob/master/images/grump.png" alt="alt text" width="25%" height="25%" class=center>
<img src="https://github.com/scottgilmartin/Evolution_Simulator/blob/master/images/grump_dna_single.png" alt="alt text" width="25%" height="25%" class=center></p>

Moustached man:

<img src="https://github.com/scottgilmartin/Evolution_Simulator/blob/master/images/2.png" alt="alt text" width="60%" height="50%">

The entire evolution process:
<img src="https://github.com/scottgilmartin/Evolution_Simulator/blob/master/images/Mario.png" alt="alt text" width="100%" height="100%">

The simulator can be used in the same way to generate anything you can think of that is symmetrical. Here is an example of a dog face:

<img src="https://github.com/scottgilmartin/Evolution_Simulator/blob/master/images/Dog_evolve.png" alt="alt text" width="100%" height="100%">

