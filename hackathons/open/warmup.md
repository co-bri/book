# Warmup

Complete this warmup exercise to get an idea how to put all the different pieces
together to generate an end-to-end data analysis viz report.

<a name="top"/>
<div id="autonav"></div>

{% data src="../fcq/fcq.clean.json" %}
{% enddata %}

{% viz %}

{% title %}

What is the distribution of courses across colleges?

{% solution %}

var groups = _.groupBy(data, function(d){
    return d['CrsPBAColl']
})

// TODO: add real code to convert groups (which is an object) into an array like below
// This array should have a lot more elements.
var counts = [{"name": "AS","count": 3237},
    {"name": "BU","count": 378},
    {"name": "EB","count": 139},
    {"name": "EN","count": 573}]
console.log(counts)


count2= _.mapValues(groups,function(n){
	return _.size(n)
})
console.log(count2)
var count4 = []
count3 = _.forEach(count2,function(v,k,n){
	count4.push({"name":k,"count":v})
})
console.log(count3)
console.log(count4)
counts = count4

// TODO: modify the code below to produce a nice vertical bar charts

function computeX(d, i) {
    return 0
}

function computeHeight(d, i) {
    return 20
}

function computeWidth(d, i) {
//    return 20 * i + 100
	return d.count
}

function computeY(d, i) {
    return 20 * i
}

function computeColor(d, i) {
    return 'red'
}

var viz = _.map(counts, function(d, i){
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

<rect x="0"
      y="${d.y}"
      height="20"
      width="${d.width}"
      style="fill:${d.color};
             stroke-width:3;
             stroke:rgb(0,0,0)" />

{% endviz %}
