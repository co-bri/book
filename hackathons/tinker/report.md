# Q: What are the number of commits

## Data

(( a table with manually collected numbers))

| Project    | # of Commits | 
|----------|:-------------:|
| 1. fouber/blog| 83 |
| 2. michaeldfallen/gitradar    | 106|
| 3. flarun/flarum     | 156|
| 4. girliemac/RPi-KittyCam  |10 |
| 5. chneukirchen/nq         | 4|


## Visualization

{% set gitProjects = [["fouber/blog",83], ["michaeldfallen/gitradar",106],
	["flarun/flarum",156],["girliemac/RPi-KittyCam",10],
	["chneukirchen/nq",4]]
%}

<svg width="500" height="200">
{% for project in gitProjects %}
    <rect x="{{loop.index * 20}}" width="15" height={{project[1]}} style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
{% endfor %}
</svg>



## Recommendation

We used SVG as it allows easy graphical presentation of a sall amount of data.  A
Bar chart can be easily drawn from a set of data points
