/*
GENERATED - DO NOT EDIT - Tue Jan 14 2014 22:25:31 GMT+0000 (GMT)

Copyright (c) 2013 Flarebyte.com Ltd. All rights reserved.
Creator: Olivier Huin
Contributors:
*/


(function() {
  'use strict';
  var flamingAppControllers;

  flamingAppControllers = angular.module('flamingApp.controllers', []);

  flamingAppControllers.controller("ProfileCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.profile = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("LoginCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.login = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("ComposeCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.compose = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("ToReadCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.toRead = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("ToDoCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.toDo = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("ImportantCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.important = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("RecentCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.recent = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("SharedCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.shared = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("AllCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.all = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("NewsCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.news = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("TrashCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.trash = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("DashboardCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.dashboard = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("ContactsCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.contacts = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("SettingsCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.settings = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("HelpCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.help = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("FaqCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.faq = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("PrivacyCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.privacy = ListAllProfileService.query();
    }
  ]);

  flamingAppControllers.controller("TermsCtrl", [
    "$scope", "ListAllProfileService", function($scope, ListAllProfileService) {
      return $scope.terms = ListAllProfileService.query();
    }
  ]);

}).call(this);
