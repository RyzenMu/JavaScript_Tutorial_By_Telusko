// var os = require('os')
// console.log("Platform: " + os.platform())
// console.log("Architecture:" + os.arch())
// console.log('OS Constants: ', os.constants)
// console.log('Ryzen Cpu details : ', os.cpus())

var fs = require('fs')
// const { text } = require('stream/consumers')
var files = fs.readdirSync('/media/a/719c6d20-e2dd-4446-a15a-421ae8936f12/home/ubuntu/Desktop/JavaScript_Tutorial_By_Telusko/')
console.log(files)

for (let i = 0; i<files.length; i++)
{
    try
    {
        // let video = document.createElement('video')
        // video.src = files[i]
        // let box = document.getElementById('new')
        // box.appendChild(video)
        // video.controls = true
        // console.log(video.src)
        console.log(files[i])

    }
    catch(err)
    {
        console.log('error found', i)
    }
}



