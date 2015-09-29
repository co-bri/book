{% data src="/Users/brian/bmckean/EconData/econ.json" %}
{% enddata %}
# Report

# This section is the in-class assignment to pick a topic and outline steps for analysis
## Topic: Cars
## Group: Brian McKean, Ming Liew, Karen Blakemore, Matt Schroder
 Steps
 - Collect
 - Decompile
 - Extract
 - Stats
 - Diff 

 For examining the subject of cars we chose to look at
 - 1) Model with the most sales
 - 2) Average Selling Price of Models
 We then will get data to see if auto characteristics are 
 related to these two factors
 - Collect: Use a web sites like: Edmunds.com, kbb.com, consumerreports.org, http://www.nhtsa.gov/
 - Decompile: Data probably does not need to decompiled
 - Extract: Extract from dat the information we're looking for
 - Stats: In addition to Units sold by year, make and model and Average Sale price
We look for: HP, Engine Type, Color, Fuel, Body Style, MPG, Drive Train, 
 - Diff: Look for difference by make, model & year for stats to see if
there are correlations to units sold or average sales price

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
 What is the distribution of employer size per state?
by Ming
{% endviz %}
