// var os = require('os')
// console.log("Platform: " + os.platform())
// console.log("Architecture:" + os.arch())
// console.log('OS Constants: ', os.constants)
// console.log('Ryzen Cpu details : ', os.cpus())

const fs = require('fs')
// // const { text } = require('stream/consumers')
const files = fs.readdirSync('/media/a/719c6d20-e2dd-4446-a15a-421ae8936f12/home/ubuntu/Desktop/JavaScript_Tutorial_By_Telusko/')
// document.write(files)

// for (let i = 0; i<files.length; i++)
// {
//    document.write('hello')
// }

document.write('Hello World - 14/10/2022')

for (let i = 0; i <= 5; i++) 
{
    let video = document.createElement('video')
    video.src = 'History of JavaScript.mp4'
    let box = document.getElementById('new')
    box.appendChild(video)
    video.controls = true
}




