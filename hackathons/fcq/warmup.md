{% data src="fcq.clean.json" %}
{% enddata %}

# Warmup

Next, complete the following warmup exercises as a team.

## How many unique subject codes?

{% lodash %}
var codes = _.pluck(data,"Subject")
var ucodes = _.uniq(codes)
return ucodes.length
// TODO: replace with code that computes the actual result
//return 113
{% endlodash %}

They are {{ result }} unique subject codes.

## How many computer science (CSCI) courses?

{% lodash %}

var cs = _.pluck(data,"Subject")
var cs2 = _.filter(cs,function(n){
	return n == "CSCI"
})
return cs2.length
// TODO: replace with code that computes the actual result
//return 63
{% endlodash %}

They are {{ result }} computer science courses.

## What is the distribution of the courses across subject codes?

{% lodash %}
// TODO: replace with code that computes the actual result
var groups = _.groupBy(data,function(n){
	return n.Subject 
})
var result = _.mapValues(groups,function(n){
	return n.length
})
return result

return {"HIST": 78,"HONR": 20,"HUMN": 17,"IAFS": 20,"IPHY": 134}
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What subset of these subject codes have more than 100 courses?

{% lodash %}
// TODO: replace with code that computes the actual result
//var grps = _.groupBy(data, 'Subject')
//var ret = _.pick(_.mapValues(grps, function(d){
//    return d.length
//}), function(x){
//    return x > 100
//})
//return ret

var groups = _.groupBy(data,function(n){
	return n.Subject 
})
var counts = _.mapValues(groups,function(n){
	return n.length
})

var result = _.pick(counts,function(n){
	return	n > 100
}) 
return result


//return {"IPHY": 134,"MATH": 232,"MCDB": 117,"PHIL": 160,"PSCI": 117}
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What subset of these subject codes have more than 5000 total enrollments?

{% lodash %}
var groups = _.groupBy(data,function(n){
	return n.Subject 
})
var counts = _.mapValues(groups,function(n){
	return n.length
})

var subjects = _.pick(counts,function(n){
	return	n > 100
}) 
var list = _.keys(subjects)

groups = _.pick(groups,function(n,key){
	return _.includes(list,key)
})
var enrolls = _.mapValues(groups,function(n){
	sum = _.sum(n,"N.ENROLL")
	return sum
}) 
console.log(enrolls)

var result = _.pick(enrolls,function(n){
	return n > 5000
})
return result
// TODO: replace with code that computes the actual result
//return {"IPHY": 5507,"MATH": 8725,"PHIL": 5672,"PHYS": 8099,"PSCI": 5491}
{% endlodash %}

<table>
{% for key, value in result %}
    <tr>
        <td>{{key}}</td>
        <td>{{value}}</td>
    </tr>
{% endfor %}
</table>

## What are the course numbers of the courses Tom (PEI HSIU) Yeh taught?

{% lodash %}
var classWithTom = _.filter(data,function(n){
	var profs = n.Instructors
	found = _.find(profs,function(m){
		return _.includes(m.name,"YEH, PEI HSIU")
	})
	return found
})


return _.pluck(classWithTom,"Course")

// TODO: replace with code that computes the actual result
//return ['4830','4830']
{% endlodash %}

They are {{result}}.
