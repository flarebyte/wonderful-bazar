"use strict"

# Directives
angular.module("flamingApp.directives", []).directive "appVersion", (version) ->
  (scope, elm, attrs) ->
    elm.text version
