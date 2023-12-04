import {input, splitByLine, sum} from '../util.js'

const calibrate = lines => lines.map(s => {
    const n = s.replaceAll(/\D/g, '')
    return `${n[0]}${n[n.length-1]}`
})

console.log(sum(calibrate(splitByLine(input))))


//const digitMap = {
    //'one': 1,
    //'two': 2,
    //'three': 3,
    //'four': 4,
    //'five': 5,
    //'six': 6,
    //'seven': 7,
    //'eight': 8,
    //'nine': 9,
//}

//export const sanatize = s => {
    //let res = ''
    //let i = 0
    //const validDigits = Object.keys(digitMap)
    //while (i < s.length) {
        //res += s[i]
        //validDigits.forEach(d => {
            //if (res.includes(d)) {
                //res = res.replace(d, digitMap[d])+s[i]
            //}
        //})
        //++i
    //}
    //return res
//}

//export const reCalibrate = s => {
    //const nums = s.replace(/\D/g, '').split('')
    //if (nums.length === 0) return 0
    //return Number(`${nums[0]}${nums[nums.length-1]}`)
//}
//let p1 = 0
//let p2 = 0
//splitNewLine(input).forEach(s => {
    //p1 += reCalibrate(s)
    //p2 += reCalibrate(sanatize(s))
//})
//console.log(p1)
//console.log(p2)
