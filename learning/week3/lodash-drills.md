# Lodash Drill

Complete the following Lodash exercises. The goal is to become really good at
functional programming paradigm (e.g., `_.map`, `_.filter`, `_.all`, `_.any` ...etc) and
a number of really useful Lodash methods (e.g., `_.find`, `_.pluck` ... etc).

* enter your solution in the `solution` block
* utilize lodash functions as much as possible
* no `for/while` loop is allowed

Familiarity with programming in this way will not only make you a super productive
programmer but also will pave the way for you to learn MapReduce and MongoDB.

# Examples

{% lodashexercise %}

{% title %}

How many people?

{% data %}

[{name: 'John'}, {name: 'Mary'}, {name: 'Joe'}, {name: 'Ben'}]

{% output %}

4

{% solution %}

return data.length

{% endlodashexercise %}


{% lodashexercise %}

{% title %}

What are the names?

{% data %}

[{name: 'John'}, {name: 'Mary'}, {name: 'Joe'}, {name: 'Ben'}]

{% output %}

['John', 'Mary','Joe','Ben']

{% solution %}

return _.map(data, function(d){
    return d.name
})

{% endlodashexercise %}

# Exercises

{% lodashexercise %}

{% title %}

What names begin with the letter J?

{% data %}

[{name: 'John'}, {name: 'Mary'}, {name: 'Joe'}, {name: 'Ben'}]

{% output %}

['John','Joe']

{% solution %}

var names = _.map(data, function(d){
    return d.name
})
var Jnames = _.filter(names, function(n){
	return _.startsWith(n,'J')
})
return Jnames

{% endlodashexercise %}



{% lodashexercise %}

{% title %}

How many Johns?

{% data %}

[{name: 'John'}, {name: 'John'}, {name: 'John'}, {name: 'Ben'}]

{% output %}

3

{% solution %}
var Johns = _.filter(data,function(n){
	return n.name == 'John'
})
return Johns.length

{% endlodashexercise %}




{% lodashexercise %}

{% title %}

What are all the first names?

{% data %}

[{name: 'John Smith'}, {name: 'Mary Kay'}, {name: 'Peter Pan'}, {name: 'Ben Franklin'}]

{% output %}

["John","Mary","Peter","Ben"]

{% solution %}
console.log(data)
var names = _.pluck(data,'name')

console.log(names)
var fnames = _.map(names,function(n){
	return 	n.split(" ")[0]
})
console.log(fnames)
return fnames

{% endlodashexercise %}







{% lodashexercise %}

{% title %}

What are the first names of Smith?

{% data %}

[{name: 'John Smith'}, {name: 'Mary Smith'}, {name: 'Peter Pan'}, {name: 'Ben Smith'}]

{% output %}

["John","Mary","Ben"]

{% solution %}
var names = _.pluck(data,'name')
var snames = _.filter(names,function(n){
	return 	n.split(" ")[1] == 'Smith'
})
console.log(names)
console.log(snames)
var fnames = _.map(snames,function(n){
	return 	n.split(" ")[0]
})
console.log(fnames)
return fnames
{% endlodashexercise %}


{% lodashexercise %}

{% title %}

Change the format to lastname, firstname

{% data %}

[{name: 'John Smith'}, {name: 'Mary Kay'}, {name: 'Peter Pan'}]

{% output %}

[{name: 'Smith, John'}, {name: 'Kay, Mary'}, {name: 'Pan, Peter'}]

{% solution %}
var rnames = _.map(data,function(n){
	console.log(n)
	var n2 = n.name.split(" ")[1]+', '+n.name.split(" ")[0]
	var n3 = {'name':n2}
	return n3
})
console.log(rnames)
return rnames
{% endlodashexercise %}



{% lodashexercise %}

{% title %}

How many women?

{% data %}

[{name: 'John Smith', gender: 'm'}, {name: 'Mary Smith', gender: 'f'}, {name: 'Peter Pan', gender: 'm'}, {name: 'Ben Smith', gender: 'm'}]

{% output %}

1

{% solution %}
var women = _.filter(data,function(n){
	return n.gender == 'f'	
})
return women.length

{% endlodashexercise %}







{% lodashexercise %}

{% title %}

How many men whose last name is Smith?

{% data %}

[{name: 'John Smith', gender: 'm'}, {name: 'Mary Smith', gender: 'f'}, {name: 'Peter Pan', gender: 'm'}, {name: 'Ben Smith', gender: 'm'}]

{% output %}

2

{% solution %}

var smiths = _.filter(data,function(n){
	return n.name.split(" ")[1] == 'Smith'	
})
var smithMen =  _.filter(smiths,function(n){
	return n.gender == 'm'
})
return smithMen.length

{% endlodashexercise %}



{% lodashexercise %}

Are there more men than women?

{% data %}

[{name: 'John Smith', gender: 'm'}, {name: 'Mary Smith', gender: 'f'}, {name: 'Peter Pan', gender: 'm'}, {name: 'Ben Smith', gender: 'm'}]

{% output %}

true

{% solution %}

var women = _.filter(data,function(n){
	return n.gender == 'f'	
})
var men = _.filter(data,function(n){
	return n.gender == 'm'	
})
return men.length > women.length
{% endlodashexercise %}







{% lodashexercise %}

{% title %}

What is Peter Pan's gender?

{% data %}

[{name: 'John Smith', gender: 'm'}, {name: 'Mary Smith', gender: 'f'}, {name: 'Peter Pan', gender: 'm'}, {name: 'Ben Smith', gender: 'm'}]

{% output %}

'm'

{% solution %}
var pp = _.find(data,function(n){
	return n.name == 'Peter Pan'
})
return pp.gender
{% endlodashexercise %}





{% lodashexercise %}

{% title %}

What is the oldest age?

{% data %}

[{name: 'John Smith', age: 54}, {name: 'Mary Smith', age: 42}, {name: 'Peter Pan', age: 15}, {name: 'Ben Smith', age: 35}]

{% output %}

54

{% solution %}
var names = _.sortBy(data,function(n){
	return n.age;
})
console.log(names)
oldest =  _.last(names)
return oldest.age 

{% endlodashexercise %}



{% lodashexercise %}

{% title %}

Is it true everyone is younger than 60?

{% data %}

[{name: 'John Smith', age: 54}, {name: 'Mary Smith', age: 42}, {name: 'Peter Pan', age: 15}, {name: 'Ben Smith', age: 35}]

{% output %}

true

{% solution %}

// use _.all
return _.all(data,function(n){
	return n.age < 60
})

{% endlodashexercise %}




{% lodashexercise %}

{% title %}

Is it true someone is not an adult (younger than 18)?

{% data %}

[{name: 'John Smith', age: 54}, {name: 'Mary Smith', age: 42}, {name: 'Peter Pan', age: 15}, {name: 'Ben Smith', age: 35}]

{% output %}

true

{% solution %}

// use _.some
return _.some(data,function(n){
	return n.age < 18
})

{% endlodashexercise %}




{% lodashexercise %}

{% title %}

How many people whose favorites include food?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

3

{% solution %}
var foodies = _.filter(data,function(n){
	console.log(n)
	return _.includes(n.favorites,'food')
	
})
console.log(foodies)
return foodies.length

{% endlodashexercise %}





{% lodashexercise %}

{% title %}

Who are over 40 and love travel?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Joe Johnson', age: 46, favorites: ['travel', 'movies']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

['Mary Smith', 'Joe Johnson']

{% solution %}
var over40 = _.filter(data,function(n){
	return n.age > 40;
})
console.log(over40)
var over40travel = _.filter(over40,function(n){
	return _.includes(n.favorites,'travel');
})
var names = _.pluck(over40travel,'name')
return names


{% endlodashexercise %}




{% lodashexercise %}

{% title %}

Who is the oldest person loving food?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Joe Johnson', age: 46, favorites: ['travel', 'movies']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

'John Smith'

{% solution %}
var foodies = _.filter(data,function(n){
	console.log(n)
	return _.includes(n.favorites,'food')
	
})
var sortFoodies = _.sortBy(foodies,'age')
console.log(sortFoodies)
return _.last(sortFoodies).name

{% endlodashexercise %}



{% lodashexercise %}

{% title %}

What are all the unique favorites?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Joe Johnson', age: 46, favorites: ['travel', 'movies']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

[
  "food",
  "movies",
  "travel",
  "minecraft",
  "pokemo",
  "craft"
]

{% solution %}

// hint: use _.pluck, _.uniq, _.flatten in some order
var faves = _.pluck(data,'favorites')
console.log(faves)
faves = _.flatten(faves)
console.log(faves)
faves = _.uniq(faves)
console.log(faves)
return faves
{% endlodashexercise %}



{% lodashexercise %}

{% title %}

What are all the unique last names?

{% data %}

[{name: 'John Smith', age: 54, favorites: ['food', 'movies']},
 {name: 'Mary Smith', age: 42, favorites: ['food', 'travel']},
 {name: 'Peter Pan', age: 15, favorites: ['minecraft', 'pokemo']},
 {name: 'Joe Johnson', age: 46, favorites: ['travel', 'movies']},
 {name: 'Ben Smith', age: 35, favorites: ['craft', 'food']}]

{% output %}

[
  "Smith",
  "Pan",
  "Johnson"
]

{% solution %}
var names = _.pluck(data,'name')
var lastNames = _.map(names,function(n){
	return n.split(" ")[1]
})
var ulnames = _.uniq(lastNames)
return ulnames

{% endlodashexercise %}
