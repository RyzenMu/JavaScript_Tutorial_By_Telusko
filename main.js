let tag = document.createElement('h3')
let text = document.createTextNode('Hi da')
let element = document.getElementById('new')
tag.appendChild(text)
element.appendChild(tag)

let tag1 = document.createElement('h2')
let text1 = document.createTextNode('This is thw sencond message')
let element1 = document.getElementById('new')
tag1.appendChild(text1)
element1.appendChild(tag1)

for (let i = 0; i <= 0; i++) 
{
    let video = document.createElement('video')
    video.src = 'History of JavaScript.mp4'
    let box = document.getElementById('new')
    box.appendChild(video)
    video.controls = true
}




