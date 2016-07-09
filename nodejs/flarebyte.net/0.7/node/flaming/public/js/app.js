/*
GENERATED - DO NOT EDIT - Tue Jan 14 2014 22:25:31 GMT+0000 (GMT)

Copyright (c) 2013 Flarebyte.com Ltd. All rights reserved.
Creator: Olivier Huin
Contributors:
*/


(function() {
  'use strict';
  var flamingApp, modules;

  modules = ["flamingApp.controllers", "flamingApp.filters", "flamingApp.services", "flamingApp.directives", "jmdobry.angular-cache"];

  flamingApp = angular.module("flamingApp", modules);

  flamingApp.config(function($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);
    $routeProvider.when("/profile", {
      templateUrl: "partials/profile",
      controller: "ProfileCtrl"
    });
    $routeProvider.when("/login", {
      templateUrl: "partials/login",
      controller: "LoginCtrl"
    });
    $routeProvider.when("/compose", {
      templateUrl: "partials/compose",
      controller: "ComposeCtrl"
    });
    $routeProvider.when("/to-read", {
      templateUrl: "partials/to_read",
      controller: "ToReadCtrl"
    });
    $routeProvider.when("/to-do", {
      templateUrl: "partials/to_do",
      controller: "ToDoCtrl"
    });
    $routeProvider.when("/important", {
      templateUrl: "partials/important",
      controller: "ImportantCtrl"
    });
    $routeProvider.when("/recent", {
      templateUrl: "partials/recent",
      controller: "RecentCtrl"
    });
    $routeProvider.when("/shared", {
      templateUrl: "partials/shared",
      controller: "SharedCtrl"
    });
    $routeProvider.when("/all", {
      templateUrl: "partials/all",
      controller: "AllCtrl"
    });
    $routeProvider.when("/news", {
      templateUrl: "partials/news",
      controller: "NewsCtrl"
    });
    $routeProvider.when("/trash", {
      templateUrl: "partials/trash",
      controller: "TrashCtrl"
    });
    $routeProvider.when("/dashboard", {
      templateUrl: "partials/dashboard",
      controller: "DashboardCtrl"
    });
    $routeProvider.when("/contacts", {
      templateUrl: "partials/contacts",
      controller: "ContactsCtrl"
    });
    $routeProvider.when("/settings", {
      templateUrl: "partials/settings",
      controller: "SettingsCtrl"
    });
    $routeProvider.when("/help", {
      templateUrl: "partials/help",
      controller: "HelpCtrl"
    });
    $routeProvider.when("/faq", {
      templateUrl: "partials/faq",
      controller: "FaqCtrl"
    });
    $routeProvider.when("/privacy", {
      templateUrl: "partials/privacy",
      controller: "PrivacyCtrl"
    });
    return $routeProvider.when("/terms", {
      templateUrl: "partials/terms",
      controller: "TermsCtrl"
    });
  });

}).call(this);
