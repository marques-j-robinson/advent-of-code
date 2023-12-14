import {nums} from './math.js'

export const permute = arr => {
    let result = []

    if (arr.length === 0) return []
    if (arr.length === 1) return [arr]

    for (let i = 0; i<arr.length; i++) {
        const currentNum = arr[i]
        const remainingNums = arr.slice(0, i).concat(arr.slice(i + 1));
        const remainingNumsPermuted = permute(remainingNums);

        for (let j = 0; j<remainingNumsPermuted.length; j++) {
            const permutedArray = [currentNum].concat(remainingNumsPermuted[j])
            result.push(permutedArray);
        }
    }

    return result
}

export const pairs = arr => {
    let result = []
    for (let i = 0; i<arr.length; i++) {
        const cur = arr[i]
        for (let j = i+1; j<arr.length; j++) {
            const next = arr[j]
            const newVal = [cur, next]
            if (!result.includes(newVal)) {
                result.push([cur, next])
            }
        }
    }
    return result
}

export function* combination(arr) {
  if (arr.length === 1) {
    yield arr;
    return;
  }

  yield [arr[0]];
  for (const c of combination(arr.slice(1))) {
    yield c;
    yield [arr[0], ...c];
  }
}

export const sum = arr => nums(arr).reduce((acc, i) => acc+i, 0)
export const product = arr => nums(arr).reduce((acc, i) => acc*i, 1)
