/**
 * @param {string[]} list1
 * @param {string[]} list2
 * @return {string[]}
 */
var findRestaurant = function (list1, list2) {
  let restaurants = {};
  const iterativeFunc = (value, index) => {
    if (value in restaurants) {
      restaurants[value].push(index);
    } else {
      restaurants[value] = [index];
    }
  }
  list1.forEach(iterativeFunc);
  list2.forEach(iterativeFunc);
  let ret = [];
  let minSum = -1;
  Object.keys(restaurants).forEach((key) => {
    if (restaurants[key].length === 2) {
      let indexSum = restaurants[key][0] + restaurants[key][1];
      if (minSum === -1) {
        minSum = indexSum;
        ret.push(key);
      } else if (minSum === indexSum) {
        ret.push(key)
      } else if (indexSum < minSum) {
        ret.length = 0;
        ret.push(key);
        minSum = indexSum;
      }
    }
  });
  return ret;
};
