/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
        const results = new Array(functions.length); // result length is equal to the functions length
        let counter = 0;
        functions.forEach((func, index) => {
            func().then((result) => {
                results[index] = result
                counter += 1
                if (counter === functions.length){
                    resolve(results)
                }
            }).catch((error) => {
                reject(error)
            })
        })
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */