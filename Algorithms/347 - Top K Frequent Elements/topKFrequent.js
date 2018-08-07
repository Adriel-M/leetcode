/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  let ret = [];
  let freqs = {};
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in freqs) {
      freqs[nums[i]]++;
    } else {
      freqs[nums[i]] = 1;
    }
  }
  let numFreqs = {};
  for (let key in freqs) {
    if (freqs.hasOwnProperty(key)) {
      if (freqs[key] in numFreqs) {
        numFreqs[freqs[key]].push(parseInt(key));
      } else {
        numFreqs[freqs[key]] = [parseInt(key)];
      }
    }
  }

  for (let i = nums.length; i > 0 && ret.length < k; i--) {
    if (i in numFreqs) {
      while (ret.length < k && numFreqs[i].length > 0) {
        ret.push(numFreqs[i].pop());
      }
    }
  }
  return ret;
};