{% import './data.html' as data %}

# Report

As a class, we brainstormed and came up with a long list of further questions we can ask based
on the "self-introduction" data. Out of these questions, our team chose to tackle on
the following:

# How many of the students are CS majors? 

{% lodash %}
var x = _.filter(data.comments, function(n){
        return _.includes(n.body,"CS");
});

var countCS = _.size(x)
var y = _.filter(data.comments, function(n){
        return _.includes(n.body,"Computer Science");
});
var countComputerScience = _.size(y)

return (countCS + countComputerScience)
{% endlodash %}
The number of CS majors in the class is {{result}}

# How many peoples names start with A?
{% lodash %}
var y = _.filter(data.comments, function(n){
	var text = n.body
	var text2 = _.first(text.split("\r\n"))
	var text3 = _.last(text2.split("Name:"))
        return text3.charAt(1) == 'A'
});
var z = _.size(y)
return z 
{% endlodash %}
There are {{result}} students names start with A

# How many of the students are not CS majors? 
{% lodash %}
var x = _.filter(data.comments, function(n){
        return _.includes(n.body,"CS");
});

var countCS = _.size(x)
var y = _.filter(data.comments, function(n){
        return _.includes(n.body,"Computer Science");
});
var countComputerScience = _.size(y)
return (data.comments.length - (countCS + countComputerScience))
{% endlodash %}
There are {{result}} students in the class who are not CS majors

# What is the user id for the login zhya215?

{% lodash %}
var y = _.filter(data.comments, function(n){
        return _.includes(n.user,"zhya215");
});
z = _.pluck(y,"id")
return z
{% endlodash %}

The user with id zhya215 is {{result}}

