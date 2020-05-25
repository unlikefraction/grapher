# Grapher

This is a Graphing Library for
- Educations
- Scientific/Mathematical Research
- Graph Analysis

It helps you to graph any number of equations onto one single graph. This makes it easy for determining the relation between some graphs and understaing better solutions.

# Example
<img src="https://i.imgur.com/t4NX73q.png">

Code for it:<br>
`g = Grapher(['cos(x)', '1 - ((x^2)/factorial(2)) + (x^4)/factorial(4)'], lb=-3, ub=3, lol='lower center', title='Taylor Polynomial for cos(x)')`<br>
`g.plot()`<br>

# Features
- Code Tolerance. So, `sin(x)` is the best way to write but `sinx` is also acceptable. Similar for all Trignometriic Functions.
- Build in functions for commonly used Mathmatical Operations. Eg: sin, cos, tan, cosec, sec, cot, log, ln, factorial, sqrt, cbrt and constants like pi and e.

<br>

# Usage

Grapher(fx, lb=-10, ub=10, step=0.01, label=True, grid=False, xlabel='x', title=None, lol='upper left', linestyle='-', mode='light', style=None)

`fx` = An Array for functions to be graphed.<br>
Eg:<br>
['sinx', 'cosx']<br>
This is the only required argument.
### Output:
`
g = Grapher(['sinx', 'cosx'])
g.plot()
`
<img src="https://i.imgur.com/jFuA5Oq.png">
#
`lb=-10, ub=10`<br>
They define the Lower Bound and the Upper Bound of the Function. Mathematically the domain of the function.
<br>
`step=0.01`<br>
This is by how much the next number is more than the other. Try to keep it low for a better and more accurate result. <br>
Step of 0.01 is a preety good step for accuracy. But 0.001 is even better. But decreasing it too low may cause the program to slow down as a lot of computation needs to be done.<br>
Therefore 0.01 is probably the sweet spot. But you know better for your own given equation and comutational speed.
<br><br>
#### Now Comes the features for customization of the looks of the graph.
`label=True`<br>
It is just the legend on the Graph. It helps to keep track of the function by color coding them.
<br>
`grid=False`<br>
This makes grid on the graph for better precision.
<br>
`xlabel='x', title=None`<br>
xlabel is the label of the X-axis of the graph. When set to some value Eg: 'Month', ylabel is set to f (Month) automatically.<br>
To change the ylabel, do g.ylabel = 'Your Y Label here.'
<br>
Title is the overall title of the page. Eg: 'Comparing cos(x) with its 4th order Taylor Polynomial.'
<br>

`lol='upper left'`<br>
lol stands for Location of Legend. It takes standard values as by matplotlib.
<br>

`linestyle='-'`<br>
This is the style of line that you want to have for your graph. (Values same as matplotlib.)
<br>
`mode='light'`<br>
This has 2 Options. light/dark. Dark will make it with a black background and light text and graph lines.
<img src="https://i.imgur.com/a00YFpx.png">
<br>
`style=None`<br>
If you want more customization, then you can give a string of any style available for matplotlib. This can be used to make your Graphs look beautiful.
<br>

# Functions Available
There is a list of predefined common functions that you can use from.<br>
If you want more functionality, then you can use your command with np.command or math.command.<br>
<br>
Functions available to you.
- sin(x)
- cos(x)
- tan(x)
- cosec(x)
- sec(x)
- tan(x)
- log(x, base=10)
- ln(x)
- sqtr(x)
- cbrt(x)
### Some Commonly used constants
- pi
- e
<br>
You can use them all easily just by typing them, without even thinking about how are they getting called.
<br>
# Sample:
some equations like, `['sinx', 'cosx', 'e^x', 'pi^tan(x)']` will work without any issue.
<br>
<img src="https://i.imgur.com/Ii8Cj7K.png">

# Contribution
You have a lot of ways to contribute to this library. It doesnt work with multiple variables, just x and f(x).<br>
We still dont have 3d graphs, you can help in implimeneting it. Just clone this repo, add featues and request for a Merge.<br>

