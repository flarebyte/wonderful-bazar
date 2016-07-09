###
GENERATED - DO NOT EDIT - Tue Jan 14 2014 22:25:31 GMT+0000 (GMT)

Copyright (c) 2013 Flarebyte.com Ltd. All rights reserved.
Creator: Olivier Huin
Contributors:
###

'use strict'
# Controllers
flamingAppControllers = angular.module('flamingApp.controllers', [])

flamingAppControllers.controller "ProfileCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.profile = ListAllProfileService.query()
]

flamingAppControllers.controller "LoginCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.login = ListAllProfileService.query()
]

flamingAppControllers.controller "ComposeCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.compose = ListAllProfileService.query()
]

flamingAppControllers.controller "ToReadCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.toRead = ListAllProfileService.query()
]

flamingAppControllers.controller "ToDoCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.toDo = ListAllProfileService.query()
]

flamingAppControllers.controller "ImportantCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.important = ListAllProfileService.query()
]

flamingAppControllers.controller "RecentCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.recent = ListAllProfileService.query()
]

flamingAppControllers.controller "SharedCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.shared = ListAllProfileService.query()
]

flamingAppControllers.controller "AllCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.all = ListAllProfileService.query()
]

flamingAppControllers.controller "NewsCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.news = ListAllProfileService.query()
]

flamingAppControllers.controller "TrashCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.trash = ListAllProfileService.query()
]

flamingAppControllers.controller "DashboardCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.dashboard = ListAllProfileService.query()
]

flamingAppControllers.controller "ContactsCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.contacts = ListAllProfileService.query()
]

flamingAppControllers.controller "SettingsCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.settings = ListAllProfileService.query()
]

flamingAppControllers.controller "HelpCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.help = ListAllProfileService.query()
]

flamingAppControllers.controller "FaqCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.faq = ListAllProfileService.query()
]

flamingAppControllers.controller "PrivacyCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.privacy = ListAllProfileService.query()
]

flamingAppControllers.controller "TermsCtrl",
["$scope", "ListAllProfileService", ($scope, ListAllProfileService) ->
  $scope.terms = ListAllProfileService.query()
]

