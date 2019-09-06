# Visual Search Algorithm Learning Aid

Christopher Clarke 15456478

Aidan McGivern 15414228

CA326 Third Year Project

  
  
  
  
  
  
  
  
  
  
  
  
  

# 0\. Table of contents

1\. Introduction  3

1.1 Overview  3

1.2 Glossary  3

2\. System Architecture  4

3\. High-Level Design  4

4\. Problems and Resolution  8

5\. Installation Guide  8
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

# 1\. Introduction

## 1.1 Overview

The visual search algorithm learning aid is a program which is design to help students studying computer science learn how different algorithms work. The program does this by showing the different algorithms solving different puzzles. The program uses three different algorithms. They are breadth first search, iterative deepening depth first search and a star. The two puzzles that are solved using the algorithms are the eight puzzle and the word game. We chose this project in order to create a learning tool that can effectively demonstrate to students how different AI searching algorithms behave while solving the problem. The strengths, weaknesses and efficiency of the set of algorithms will be presented on screen, in a user-friendly manner for easy, fast and most importantly, effective learning.

## 1.2 Glossary

Pygame - python module including sound and graphical libraries.

  

Eight puzzle - sliding tile puzzle, aim is to have all tiles in specific sequence

  

Word game - puzzle to turn one word into another word by changing one letter at a time.

  

GUI - Graphical user interface

  

Search tree - A search tree is a data structure where the values of the nodes on the left are always less than the parent node and the values on of the nodes on the right are

greater than the parent node.

  

# 2\. System Architecture

Our main file is our GUIMain file. This file utilises several different modules and classes that we have built such as our Tree module, EPSearch EPBoard and WGSearch. GUIMain contains all the graphic instructions and gathers what data to show from the modules it uses.

For example, in solving an eight puzzle, it creates an EPSearch object which contains the algorithms. EPSearch uses EPBoard objects to go through the algorithms.A Queue class was employed to store the openLists. It is a hierarchical class system.

# 3\. High-Level Design

This section should set out the high-level design of the system. It should include system models showing the relationship between system components and the systems and its environment. These might be object-models, DFD, etc. Unlike the design in the Functional

Specification - this description must reflect the design of the system as it is demonstrated.

  

![](https://lh3.googleusercontent.com/R0HQo2f18hD-MmcHX27a_fOe4x3BYT8LlU3aAgIveC9H79YKkOh9PCwN-uA3_XN7fPE4b88BL5NZW8ABitNobPb5YZjnCWCgcAh-98gsZkXGG5YyVnIkTp4AnxQrKqJxGlQup-RT)![](https://lh4.googleusercontent.com/Bty7Qq0WXNtz52ZOVBJXwNss6WZwSVR6RyndsW5T72ADXHQezzUvXCfHVTwTK8JLz2OUNNdmEkImL7BhWvSYhDkrVGfGm8EMBpque6KfgKeeBFbbl2v3F5nARe_Pt1wOQEl0txrG)

![](https://lh3.googleusercontent.com/B80DXFn_UPRuh4_XiyJj-pDoHDSkYJ1IZ_iPyv897xO0KC1CR4GAAj9PHQhc-MPS4lgzCABQMZK466ECAgzeJPLdiPolvvkwCRDw8ygSkqFQwlUbKnA-MoKsKHO21rtvOgNi6A7r)

![](https://lh4.googleusercontent.com/_xIEKpcj8ojYrLEgWzhUvMNLQbtp7UfG1b8Xrv5_Y4Ltov72E6eo-2ygDIcv3aytB-k3Z34GtrTdlLIOD4p9cRNtdPgA72jxpI8Rpc9b4W7ANJ6NMNSHE1Lnzo0kGb8uxDTPoj4t)

![](https://lh4.googleusercontent.com/eY4Qb0Flvxc09kRR7FAQhrpbkfEacPi_LVXLCERGiU9z3mxWomKwsAl2NuIn2buWwkY7J4hdR54OgbvL8k1v8_sWW5wll_28EXJG_xSsWyUtvwMTtBcsDs_FjniJKoSy0Tb6gZc_)![](https://lh4.googleusercontent.com/aCLuCOXGMCK6-LPuhD4gdQBqlchIfBS3maN-_4B0ulQuPViuwu7CYp2VXd4Uo-7M8A3EapzFcL5Mi7-YZ_pGCHRvTQZLzHGUkat829xj-g30UcSahnjj7PLNf86RjfdB9I6DdF5T)

# 4\. Problems and Resolution

Main problems encountered:

Integrating algorithms to the GUI.

Retrieving the valid path from node to node.

Displaying this data in a meaningful manner.

Displaying stats.

  

Resolution of problems:

When the algorithms were designed in the back end and they worked we thought that was the hard part over, however it was more difficult to reflect what these algorithms told us graphically. Once the solve button is hit it begins a while loop which repeatedly steps through one iteration of the chosen algorithm, then retrieves the board being examined and shows it on screen in a board image.

  

The path was derived by giving each board a parent instance attribute and providing that attribute when the object is instantiated in the getChildren board method. When the path is called, each parent is goes up the chain til the starting board giving us a path.

  

On the right side of the screen we have a tree structure made up of dots each of which represents a node/board.

  

Stats are gathered as the algorithms work. Things like time taken, nodes expanded and depth of current node They are then displayed in the stat box below the board on the left of the screen.

# 5\. Installation Guide

Download all assets and files from gitlab, execute GUIMain.py.