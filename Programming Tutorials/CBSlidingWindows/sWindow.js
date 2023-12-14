function longest_sub(str,k) {
    let windowStart = 0,
        letterFrequencies = {},
        longestSubstrSoFar = 0

    for (let windowEnd = 0; windowEnd < str.length; windowEnd++) {
        let windowEndChar = str[windowEnd]

        if (!letterFrequencies[windowEndChar]) {
            letterFrequencies[windowEndChar] = 0
        }
        letterFrequencies[windowEndChar] +=1
        while (Object.keys(letterFrequencies).length > k) {
            let windowStartChar = str[windowStart]
            letterFrequencies[windowStartChar]--
            if (letterFrequencies[windowStartChar]===0) {
                delete letterFrequencies[windowStartChar]
            }
            windowStart++
        }
        longestSubstrSoFar = Math.max(longestSubstrSoFar,windowEnd-windowStart+1)
    }
    return longestSubstrSoFar
}
console.log(longest_sub('acccpbbebi',3))