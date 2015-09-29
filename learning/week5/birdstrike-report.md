{% data src="/Users/brian/bmckean/birdstrikes/b3.json" %}
{% enddata %}

# Report

As a team, answer a subset of the questions submitted during the hackathon.
But instead of using Tableau, you will need to write Javascript/Lodash code
to derive your answers. Similar to before, each team member is responsible for
one question. But everyone should work together to come up with a good solution.
Your answer should consist of Lodash code and a brief writeup.
Utilize `_.map`, `_.filter`, `_.group` ...etc. Do not se any for loop.

This time, the data is not already prepared for you in a nice JSON format. You
will need to do it on your own, replacing the placeholder `birdstrike.json` with
real data.

# (Question 1) by Brian McKean (co-bri)
# Which airport has the most bird hits? by zhya215
{% lodash %}
names = _.filter(data,function(n){
        return n["Airport: Name"] != "UNKNOWN"
})
airports = _.groupBy(names,function(n){
        return n["Airport: Name"]
})
var incidents  = _.mapValues(airports,function(n){
        return  n.length
})
big = _.max(incidents)
most = _.pick(incidents,function(n){
        return n == big
})
return most

{% endlodash %}
{% for key, value in result %}
        The worse airport is {{key}} with {{value}} incidents
{% endfor %}


# (Question 2) by Karen Blakemore kjblakemore 
# What airports have the most expensive average accident? (satchelspencer)
{% lodash %}
names = _.filter(data,function(n){
        return n["Airport: Name"] != "UNKNOWN"
})
airports = _.groupBy(names,function(n){
        return n["Airport: Name"]
})

var avgcost  = _.mapValues(airports,function(n){
        var number =  n.length
	var costs = _.pluck(n,"Cost: Total $")
	cost2 = _.map(costs, _.parseInt);
	var totalCost = _.sum(cost2)
	return (totalCost/number)
})
// Create sorted list 
var sorted = 
    _.sortByOrder(
        _.pairs(avgcost),
        function(d) {return d[1]},
        'desc')

// Just return top 10
return _.take(sorted, 10)

{% endlodash %}
<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

# (Question 3) by Ming Liew 
# Which airline have to incur most repair cost due to damage ? ( sumi6109)

{% lodash %}
airlines = _.groupBy(names,function(n){
        return n["Aircraft: Airline/Operator"]
})

var cost  = _.mapValues(airlines,function(n){
        var costs = _.pluck(n,"Cost: Total $")
        cost2 = _.map(costs, _.parseInt);
        var totalCost = _.sum(cost2)
        return totalCost
})

big = _.max(cost)
maxairline = _.pick(cost,function(n){
        return n == big
})
return maxairline
{% endlodash %}

{% for key, value in result %}
        The airline with the highest amount of damage is {{key}} with ${{value}} in damage
{% endfor %}
# (Question 4) by Matt Schroeder 
# Which plane model strikes the most birds? (twagar95)

{% lodash %}

names = _.filter(data,function(n){
        return n["Aircraft: Make/Model"] != "UNKNOWN"
})

planes = _.groupBy(names,function(n){
        return n["Aircraft: Make/Model"]
})
var incidents  = _.mapValues(planes,function(n){
        return  n.length
})
big = _.max(incidents)
most = _.pick(incidents,function(n){
        return n == big
})
return most

{% endlodash %}
{% for key, value in result %}
        The worse plane model is {{key}} with {{value}} incidents
{% endfor %}



# (Question 5) by (Name)

{% lodash %}
return "[answer]"
{% endlodash %}
