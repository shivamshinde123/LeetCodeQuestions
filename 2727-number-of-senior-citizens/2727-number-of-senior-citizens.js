/**
 * @param {string[]} details
 * @return {number}
 */
var countSeniors = function(details) {
  let age_counter = 0  
  for (let detail of details){
    let age = parseInt(detail.slice(11, 13))
    if (age > 60){
        age_counter++
    }
  }  
  return age_counter
};