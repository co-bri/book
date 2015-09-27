{% vizexercise %}

{% title %}

Display bars horizontally

{% data %}

[{name: 'China', pop: 1393783836},
 {name: 'India', pop: 1267401849},
 {name: 'USA', pop: 322583006},
 {name: 'Indonesia', pop: 252812243}]

{% solution %}
function computeY(d, i) {
    return i * 20
}

function computeWidth(d, i) {
	c = _.find(data,function(n){
		return n['name'] == 'China'	
	})	
	cp = c['pop']
	pop = d.pop
	h = 300 * pop/cp
 	return h 
}

function computeX(d, i) {
	startX = 0
	return startX
}

function computeColor(d, i) {
	color = 'red'
	if (_.includes(d,'USA')){
		color = 'red'
	}
	return color

}

function computeHeight(d, i) {
    return 20
}


var viz = _.map(data, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d, i),
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
      y="${d.y}"
     width="${d.width}"
     height="${d.height}"
     style="fill:${d.color};
            stroke-width:3;
            stroke:rgb(0,0,0)" />

{% output %}

<rect x="0"
      y="0"
     width="300"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="0"
      y="20"
     width="272.79736274685854"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="0"
      y="40"
     width="69.43322149418297"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />
<rect x="0"
      y="60"
     width="54.415663993968145"
     height="20"
     style="fill:red;
            stroke-width:3;
            stroke:rgb(0,0,0)" />

{% endvizexercise %}
