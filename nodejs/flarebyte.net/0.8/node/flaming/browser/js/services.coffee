"use strict"

# Services
#angular.module("flamingApp.services", []).value "version", "0.1"

flamingAppServices = angular.module('flamingApp.services', ['ngResource'])
flamingAppServices.value "version", "0.1"

flamingAppServices.factory "ViewStatus",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/contacts", {}, actions

]