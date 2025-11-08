/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // Optimal solution - keep track of minimal value and find the profit at each step

    let max_profit = 0
    let min_price = Number.POSITIVE_INFINITY

    for (let i = 0; i < prices.length; i++){
        if (prices[i] < min_price){
            min_price = prices[i]
        }

        let profit = prices[i] - min_price

        if (profit > max_profit){
            max_profit = profit
        }
    }

    if (max_profit < 0){
        max_profit = 0
    }

    return max_profit


};