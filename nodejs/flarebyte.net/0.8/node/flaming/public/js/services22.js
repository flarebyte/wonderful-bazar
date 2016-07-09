/*
GENERATED - DO NOT EDIT - Tue Jan 14 2014 22:25:31 GMT+0000 (GMT)

Copyright (c) 2013 Flarebyte.com Ltd. All rights reserved.
Creator: Olivier Huin
Contributors:
*/


(function() {
  'use strict';
  var flamingAppServices;

  flamingAppServices = angular.module('flamingApp.services', ['ngResource']);

  flamingAppServices.value("version", "0.1");

  flamingAppServices.factory("ListAllProfileService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/profile", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllLoginOptionsService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/login", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllComposeTemplatesService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/compose", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllMessagesToReadService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/to-read", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllTasksToDoService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/to-do", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllImportantMessagesService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/important", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllRecentMessagesService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/recent", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllSharedMessagesService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/shared", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllMessagesService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/all", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllNewsService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/news", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllTrashService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/trash", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllDashboardsService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/dashboard", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListASelectionOfContactsService", [
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

  flamingAppServices.factory("ListAllContactsService", [
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

  flamingAppServices.factory("ListAllSettingsService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/settings", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllHelpItemsService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/help", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllFaqItemsService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/faq", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllPrivacyItemsService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/privacy", {}, actions);
    }
  ]);

  flamingAppServices.factory("ListAllTermsService", [
    "$resource", function($resource) {
      var actions;
      actions = {
        query: {
          method: "GET"
        }
      };
      return $resource("/api/terms", {}, actions);
    }
  ]);

}).call(this);
