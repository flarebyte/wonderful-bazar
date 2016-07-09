###
GENERATED - DO NOT EDIT - Tue Jan 14 2014 22:25:31 GMT+0000 (GMT)

Copyright (c) 2013 Flarebyte.com Ltd. All rights reserved.
Creator: Olivier Huin
Contributors:
###

'use strict'
# Services
flamingAppServices = angular.module('flamingApp.services', ['ngResource'])
flamingAppServices.value "version", "0.1"

# List all profiles for the current user

flamingAppServices.factory "ListAllProfileService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/profile", {}, actions
]
# List all login options for the current user

flamingAppServices.factory "ListAllLoginOptionsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/login", {}, actions
]
# List all compose templates for the current user

flamingAppServices.factory "ListAllComposeTemplatesService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/compose", {}, actions
]
# List all messages to read for the current user

flamingAppServices.factory "ListAllMessagesToReadService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/to-read", {}, actions
]
# List all tasks to do for the current user

flamingAppServices.factory "ListAllTasksToDoService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/to-do", {}, actions
]
# List all important messages for the current user

flamingAppServices.factory "ListAllImportantMessagesService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/important", {}, actions
]
# List all recent messages for the current user

flamingAppServices.factory "ListAllRecentMessagesService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/recent", {}, actions
]
# List all shared messages for the current user

flamingAppServices.factory "ListAllSharedMessagesService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/shared", {}, actions
]
# List all messages for the current user

flamingAppServices.factory "ListAllMessagesService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/all", {}, actions
]
# List all news for the current user

flamingAppServices.factory "ListAllNewsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/news", {}, actions
]
# List all trash for the current user

flamingAppServices.factory "ListAllTrashService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/trash", {}, actions
]
# List all dashboards of the current user

flamingAppServices.factory "ListAllDashboardsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/dashboard", {}, actions
]
# List a selection of contacts of the current user

flamingAppServices.factory "ListASelectionOfContactsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/contacts", {}, actions
]
# List all contacts of the current user

flamingAppServices.factory "ListAllContactsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/contacts", {}, actions
]
# List all settings of the current user

flamingAppServices.factory "ListAllSettingsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/settings", {}, actions
]
# List all help items of the current user

flamingAppServices.factory "ListAllHelpItemsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/help", {}, actions
]
# List all faq items of the current user

flamingAppServices.factory "ListAllFaqItemsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/faq", {}, actions
]
# List all privacy items of the current user

flamingAppServices.factory "ListAllPrivacyItemsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/privacy", {}, actions
]
# List all terms for the current user

flamingAppServices.factory "ListAllTermsService",
["$resource", ($resource) ->
  actions=
    query:
      method: "GET"

  $resource "/api/terms", {}, actions
]
