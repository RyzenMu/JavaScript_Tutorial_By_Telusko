// var os = require('os')
// console.log("Platform: " + os.platform())
// console.log("Architecture:" + os.arch())
// console.log('OS Constants: ', os.constants)
// console.log('Ryzen Cpu details : ', os.cpus())

var fs = require('fs')
var files = fs.readdirSync('/media/a/719c6d20-e2dd-4446-a15a-421ae8936f12/home/ubuntu/Desktop/JavaScript_Tutorial_By_Telusko/')
console.log(files)
