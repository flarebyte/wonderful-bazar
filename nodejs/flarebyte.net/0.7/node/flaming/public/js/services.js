(function() {
  "use strict";
  var flamingAppServices;

  flamingAppServices = angular.module('flamingApp.services', ['ngResource']);

  flamingAppServices.value("version", "0.1");

  flamingAppServices.factory("ViewStatus", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/contacts", {}, actions);
    }
  ]);

}).call(this);
