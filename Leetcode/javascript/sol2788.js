/**
 * @param {string[]} words
 * @param {character} separator
 * @return {string[]}
 */
var splitWordsBySeparator = function(words, separator) {

    var result = [];

    for(let i of words){
        let temp = i.split(separator);
        temp = temp.filter(x => x.length > 0)
        result.push(...temp)
    }
    return result;
};