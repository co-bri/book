{% vizexercise %}

{% title %}

Color the bar corresponding to USA

{% data %}

[{name: 'China', pop: 1393783836},
 {name: 'India', pop: 1267401849},
 {name: 'USA', pop: 322583006},
 {name: 'Indonesia', pop: 252812243}]

{% solution %}

function computeX(d, i) {
    return i * 20
}

function computeY(d, i) {
    return 0
}
function computeHeight(d, i) {
	c = _.find(data,function(n){
		return n['name'] == 'China'	
	})	
	cp = c['pop']
	pop = d.pop
	h = 400 * pop/cp
 	return h 
}

function computeColor(d, i) {
	color = 'red'
	if (_.includes(d,'USA')){
		color = 'blue'
	}
	return color

}

var viz = _.map(data, function(d, i){
            return {
		y: computeY(d, i),
                x: computeX(d, i),
                height: computeHeight(d, i),
                color: computeColor(d, i)
            }
         })
console.log(viz)

var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')

{% template %}

<rect x="${d.x}"
      y="0"
     width="20"
     height="${d.height}"
     style="fill:${d.color};
            stroke-width:3;
            stroke:rgb(0,0,0)" />

{% output %}

<rect x="0"
      y="0"
     width="20"
     height="400"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="20"
      y="0"
     width="20"
     height="363.7298169958114"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="40"
      y="0"
     width="20"
     height="92.57762865891063"
     style="fill:blue;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="60"
      y="0"
     width="20"
     height="72.5542186586242"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />

{% endvizexercise %}
