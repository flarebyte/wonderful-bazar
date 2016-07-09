(function() {
  "use strict";
  angular.module("flamingApp.directives", []).directive("appVersion", function(version) {
    return function(scope, elm, attrs) {
      return elm.text(version);
    };
  });

}).call(this);
