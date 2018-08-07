/**
 * Definition for an interval.
 * function Interval(start, end) {
 *     this.start = start;
 *     this.end = end;
 * }
 */
/**
 * @param {Interval[]} intervals
 * @return {Interval[]}
 */
var merge = function (intervals) {
  let ret = [];
  intervals.sort((a, b) => {
    if (a.start < b.start) {
      return -1;
    } else if (a.start > b.start) {
      return 1;
    } else if (a.end > b.end) {
      return -1;
    } else {
      return 0;
    }
  });
  let currInterval = null;
  intervals.forEach((interval) => {
    if (!currInterval) {
      currInterval = interval;
      ret.push(currInterval);
    } else {
      if (interval.start <= currInterval.end) {
        currInterval.end = Math.max(interval.end, currInterval.end);
      } else {
        currInterval = interval;
        ret.push(currInterval);
      }
    }
  })
  return ret;
};