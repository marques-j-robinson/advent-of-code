import {input as secretKey} from '../util.js'
import md5 from 'blueimp-md5'

let i

const mine = zeros => {
    i = 1
    while (true) {
        if (md5(`${secretKey}${i}`).slice(0, 5) === zeros) break
        ++i
    }
    return i
}

console.log(mine('00000'))
console.log(mine('000000'))
