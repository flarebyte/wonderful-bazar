/*
GENERATED - DO NOT EDIT - Tue Jan 14 2014 19:51:51 GMT+0000 (GMT)

Copyright (c) 2013 Flarebyte.com Ltd. All rights reserved.
Creator: Olivier Huin
Contributors:
*/


(function() {
  'use strict';
  var flamingAppControllers;

  flamingAppControllers = angular.module('flamingApp.controllers', []);

  flamingAppControllers.controller("ProfileCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.profile = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("LoginCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.login = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("ComposeCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.compose = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("ToReadCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.toRead = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("ToDoCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.toDo = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("ImportantCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.important = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("RecentCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.recent = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("SharedCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.shared = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("AllCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.all = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("NewsCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.news = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("TrashCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.trash = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("DashboardCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.dashboard = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("ContactsCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.contacts = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("SettingsCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.settings = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("HelpCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.help = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("FaqCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.faq = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("PrivacyCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.privacy = ViewStatus.query();
    }
  ]);

  flamingAppControllers.controller("TermsCtrl", [
    "$scope", "ViewStatus", function($scope, ViewStatus) {
      return $scope.terms = ViewStatus.query();
    }
  ]);

}).call(this);
