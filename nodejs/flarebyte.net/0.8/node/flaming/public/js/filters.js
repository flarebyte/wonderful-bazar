(function() {
  "use strict";
  angular.module("flamingApp.filters", []).filter("interpolate", function(version) {
    return function(text) {
      return String(text).replace(/\%VERSION\%/g, version);
    };
  });

}).call(this);
