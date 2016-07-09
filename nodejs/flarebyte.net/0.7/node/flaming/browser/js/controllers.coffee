###
GENERATED - DO NOT EDIT - Tue Jan 14 2014 19:51:51 GMT+0000 (GMT)

Copyright (c) 2013 Flarebyte.com Ltd. All rights reserved.
Creator: Olivier Huin
Contributors:
###

'use strict'
# Controllers
flamingAppControllers = angular.module('flamingApp.controllers', [])

flamingAppControllers.controller "ProfileCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.profile = ViewStatus.query()
]

flamingAppControllers.controller "LoginCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.login = ViewStatus.query()
]

flamingAppControllers.controller "ComposeCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.compose = ViewStatus.query()
]

flamingAppControllers.controller "ToReadCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.toRead = ViewStatus.query()
]

flamingAppControllers.controller "ToDoCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.toDo = ViewStatus.query()
]

flamingAppControllers.controller "ImportantCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.important = ViewStatus.query()
]

flamingAppControllers.controller "RecentCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.recent = ViewStatus.query()
]

flamingAppControllers.controller "SharedCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.shared = ViewStatus.query()
]

flamingAppControllers.controller "AllCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.all = ViewStatus.query()
]

flamingAppControllers.controller "NewsCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.news = ViewStatus.query()
]

flamingAppControllers.controller "TrashCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.trash = ViewStatus.query()
]

flamingAppControllers.controller "DashboardCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.dashboard = ViewStatus.query()
]

flamingAppControllers.controller "ContactsCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.contacts = ViewStatus.query()
]

flamingAppControllers.controller "SettingsCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.settings = ViewStatus.query()
]

flamingAppControllers.controller "HelpCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.help = ViewStatus.query()
]

flamingAppControllers.controller "FaqCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.faq = ViewStatus.query()
]

flamingAppControllers.controller "PrivacyCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.privacy = ViewStatus.query()
]

flamingAppControllers.controller "TermsCtrl",
["$scope", "ViewStatus", ($scope, ViewStatus) ->
  $scope.terms = ViewStatus.query()
]

