let num1 = 0
let num2 = 1

document.getElementById("num1-el").textContent = num1
document.getElementById("num2-el").textContent = num2

let totalSum = document.getElementById("sum-el").textContent 

function addTogether() {
    let result = num1 + num2
    totalSum.textContent = "Sum: " + result
}

function subtractFrom() {
    let result = num1 - num2
    totalSum.textContent = "Sum: " + result

}

function multipliedBy() {
    let result = num1 * num2
    totalSum.textContent = "Sum: " + result

}

function dividedBy() {
    let result = num1 / num2
    totalSum.textContent = "Sum: " + result

}