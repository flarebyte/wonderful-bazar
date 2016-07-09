"use strict"

# Filters
angular.module("flamingApp.filters", []).filter "interpolate", (version) ->
  (text) ->
    String(text).replace /\%VERSION\%/g, version
