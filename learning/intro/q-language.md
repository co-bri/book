# Q: Which programming language is the top favorite among the students in our class?

## Data

* Manually gather data and make a table in Markdown


| Language | # of Students | 
| ---------|:-------------:| 
| Assembly | 0 |
| Javascript 	| 3|
| Python 	| 9|
| C		| 6|
| Java		| 4|
| Ruby		| 1|
| Haskell	| 1|
| C++		| 2|
| C#		| 1|



((more rows to complete the table))

## Answer

((The most popular langauge is Python))

## Visualization

* Create a barchart using SVG
{% set numbers = [3,9,6,4,1,1,2,1] %}

<svg width="500" height="200">
{% for number in numbers %}
    <rect x="{{loop.index * 20}}" width="15" height={{number*10}} style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
{% endfor %}
</svg>

<!-- extend this into a barchart -->
{% svg %}
<rect x="0" width="20" height="001" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="0" width="20" height="030" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="0" width="20" height="090" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="0" width="20" height="060" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="0" width="20" height="040" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="0" width="20" height="010" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="0" width="20" height="010" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="0" width="20" height="020" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="0" width="20" height="010" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />

{% endsvg %}
