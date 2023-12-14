const perminations = (elements) => {
    if (elements.length === 0) return [[]];
    const firstEl = elements[0];
    const rest = elements.slice(1);
    
    const permsWithoutFirst = perminations(rest);
    const permsWithFirst = [];

    permsWithoutFirst.forEach(perm => {
        const permWithFirst = [...perm,firstEl];
        permsWithFirst.push(permWithFirst);
    });
    return [...permsWithoutFirst,...permsWithFirst];



}
const permutations = (elements) => {
    if (elements.length === 0) return [[]];
    const firstEl = elements[0];
    const rest = elements.slice(1);
    
    const permsWithoutFirst = permutations(rest);
    const allPermutations = [];

    permsWithoutFirst.forEach(perm => {
        for (let i = 0; i <= perm.length; i++) {
            const permWithFirst = [...perm.slice(0,i), firstEl,...perm.slice(i)];
            allPermutations.push(permWithFirst);
        }
        
    } );
    return allPermutations
}
// console.log(permutations(['a','b','c']))
let a = [1,2,3,4,5]

for (let i = 0; i <= a.length; i++) {
    console.log(i);
}
