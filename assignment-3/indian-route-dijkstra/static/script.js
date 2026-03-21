async function findRoute(){

let start = document.getElementById("start").value
let goal = document.getElementById("goal").value

let res = await fetch("/route",{

method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({start:start,goal:goal})

})

let data = await res.json()

document.getElementById("result").innerHTML =

"Path: " + data.path.join(" → ") +
"<br><br>Distance: " + data.distance + " km"

}
