module.exports = (grunt) ->
  #TODO
  # Test coverage
  allmodules=[]
  bumps = ["package.json"]
  fm = "node_modules/magma-"
  fbumps = ("#{fm}-#{module}/package.json" for module in allmodules)
  bumps = bumps.concat fbumps

  allcoffee=[
    "*.coffee",
    "routes/*.coffee",
    "#{fm}*/lib/*.coffee",
    "#{fm}*/test/*.coffee"
  ]
  
  # Project configuration.
  grunt.initConfig
    pkg: grunt.file.readJSON("package.json")
    coffeelint:
      all: allcoffee
    simplemocha:
      all:
        src: [
          "#{fm}*/test/*.coffee"
        ]
        options:
          globals: ['should']
          timeout: 5000
          ignoreLeaks: false
          #grep: '**/*.js'
          ui: 'bdd'
          reporter: 'tap'

    bumpup: bumps

  # Load the plugins.
  grunt.loadNpmTasks "grunt-coffeelint"
  grunt.loadNpmTasks('grunt-bumpup')
  grunt.loadNpmTasks 'grunt-simple-mocha'

  # Default task(s).
  grunt.registerTask "default", ["simplemocha"]