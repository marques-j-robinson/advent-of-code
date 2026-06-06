import {input} from '../util.js'
import {nums} from '../math.js'
import {sum, combination} from '../array.js'

const format = line => {
    const [rec, c] = line.split(' ')
    return {
        rec,
        recArr: rec.split(''),
        criteria: nums(c.split(',')),
    }
}

input.split('\n').map(format)
    .map(({rec, recArr, criteria}) => {
        for (let cId = 0; cId<criteria.length; ++cId) {
            const c = criteria[cId]
            console.log(c)
        }
    })
