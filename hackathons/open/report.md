{% data src="/Users/brian/bmckean/EconData/econ.json" %}
{% enddata %}
# Small Group Assignment
Use only Javascript and SVG to produce a data analysis / visualization report.

# Authors

This report is prepared by
* [Brian McKean](http://co-bri.github.io/book/hackathons/index.html)
* [Ming Liew](link to github account)

 [Data Source http://www.bls.gov/cew/datatoc.htm](http://www.bls.gov/cew/datatoc.htm)


<a name="top"/>
<div id="autonav"></div>
{% viz %}

{% title %}

What are the top 5 counties in colorado in terms of annual wages in 2014
by Brian
{% solution %}

var coloCounties = _.filter(data,function(n){
	return (_.includes(n["Area"],"County") )  && ( n["Ownership"] == "Total Covered") && ( n["St Name"] == "Colorado") 
})

counties = _.groupBy(coloCounties, function(n){
	return n["Area"]	
})
pay = _.mapValues(counties, function(n){
	var y =  _.pluck(n,"Annual Average Pay")
	y = y.toString()
	var x = _.parseInt(y.split(',').join(''))
	return x
})
// Finally, convert object to array type and sort by pay 
var sortPay = 
   _.sortByOrder(
      _.pairs(pay),
        function(d) {return d[1]},
        'desc')
var top5 =  _.take(sortPay, 5)


function computeX(d, i) {
    return 0
}

function computeHeight(d, i) {
    return 20
}

function computeWidth(d, i) {
//    return 20 * i + 100
        return d[1]/1000
}

function computeY(d, i) {
    return 20 * i
}

function computeColor(d, i) {
    return 'red'
}


function computeLabel(d, i) {
	name = d[0].split(' ')
    	return name[0]+':  $'+d[1]
}
var viz = _.map(top5, function(d, i){
            return {
                x: computeX(d, i),
                y: computeY(d, i),
                height: computeHeight(d, i),
                width: computeWidth(d, i),
                color: computeColor(d, i),	
		label: computeLabel(d, i)
            }
         })
//console.log(viz)

var result = _.map(viz, function(d){
         // invoke the compiled template function on each viz data
         return template({d: d})
     })
return result.join('\n')

{% template %}


<g transform="translate(0 ${d.y})">
    <rect
         width="${d.width}"
         height="20"
         style="fill:${d.color};
                stroke-width:3;
                stroke:rgb(0,0,0)" />
        <text x="80" y="15">${d.label}</text>
</g>




{% endviz %}



{% viz %}

{% title %}
By state what is the average number of empoyees per employer?
By Mingqi Liew

{% solution %}
var S = _.filter(data,function(x){
    return _.contains(x["Area Type"], "State") && _.contains(x["Ownership"],"Total Covered");
});
var group = _.groupBy(S, function(x){
	return x["St Name"];
});
var a = _.map(group, function(x,values){
	
})

var map = _.map(group, function(x,value){
	var est = _.pluck(x,"Annual Average Establishment Count");
	var emp = _.pluck(x,"Annual Average Employment");
	var str_est = est.toString();
	var str_emp = emp.toString();
	var est_n = _.parseInt(str_est.split(",").join(""));
	var emp_n = _.parseInt(str_emp.split(",").join(""));
	var diff = emp_n/est_n;
	return {"state": value, "est": diff};
});

console.log(map);

function computeX(d, i) {
    return i*10;
}

function computeHeight(d, i) {

    return d.est *10 ;
}

function computeWidth(d, i) {
    return 10;
}

function computeY(d, i) {
    return 0;
}

function computeColor(d, i) {
    return 'green'
}

var viz = _.map(map, function(d, i){
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
         return template({d: d});
     })
return result.join('\n')

{% template %}

<rect x="${d.x}"
      y="${d.y}"
      height="${d.height}"
      width="${d.width}"
      style="fill:${d.color};
             stroke-width:3;
             stroke:rgb(0,0,0)" />

{% endviz %}

