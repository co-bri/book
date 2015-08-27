Q: What programming languages have the most packages?

## Data

* Manually collect data from online resources

((Markdown table))

## Top five
| Language | # of Packages (2013)|
| ---------|:-------------:|
| Java          | 56697|
| Ruby          | 55035|
| Python        | 32180|
| Javascript    | 27688|
| Perl		| 24092|

{% svg %}

<!-- barchart with five bars -->
{% set numbers = [56697,55035,32180,27688,24092] %}
<svg width="500" height="200">
{% for number in numbers %}
    <rect x="{{loop.index * 20}}" width="17" height="{{number/1000}}" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
{% endfor %}
</svg>
{% endsvg %}

## Top one

{% svg %}
<!-- same barchart, but the top is highlighted, using css -->
<rect x="0" width="20" height="57" style="fill:rgb(0,125,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="22" width="20" height="55" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="44" width="20" height="32" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="66" width="20" height="28" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />
<rect x="88" width="20" height="24" style="fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)" />

{% endsvg %}
