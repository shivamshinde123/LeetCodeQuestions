/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function (fn, t) {

    return async function (...args) {
        let timeoutId;

        // Timeout promise
        const timeoutPromise = new Promise((_, reject) => {
            timeoutId = setTimeout(() => {
                reject("Time Limit Exceeded");
            }, t);
        });

        // Function promise (fn may be async or sync)
        const functionPromise = (async () => {
            try {
                const result = await fn(...args);
                clearTimeout(timeoutId); // cleanup
                return result;
            } catch (err) {
                clearTimeout(timeoutId); // cleanup
                throw err;
            }
        })();

        // Race between fn execution and timeout
        return Promise.race([timeoutPromise, functionPromise]);

    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */