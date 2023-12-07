import {input as secretKey} from '../util.js'
import md5 from 'blueimp-md5'

const part2 = false

const mine = zeros => {
    let i = 1
    while (true) {
        if (md5(`${secretKey}${i}`).slice(0, 5) === zeros) break
        ++i
    }
    return i
}

if (!part2) console.log(mine('00000'))
if (part2) console.log(mine('000000'))
