/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function (s, t) {
    if (s.length !== t.length) {
      return false;
    }
    let replacements = {};
    let mapped = new Set();
    for (let i = 0; i < s.length; i++) {
      if (s[i] in replacements) {
        if (replacements[s[i]] !== t[i]) {
          return false;
        }
      } else {
        if (mapped.has(t[i])) {
          return false;
        } else {
          replacements[s[i]] = t[i];
          mapped.add(t[i]);
        }
      }
    }
    return true;
};
