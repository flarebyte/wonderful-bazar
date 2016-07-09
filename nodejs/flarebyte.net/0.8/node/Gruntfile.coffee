module.exports = (grunt) ->
  
  # Project configuration.
  grunt.initConfig
    pkg: grunt.file.readJSON("package.json")
    coffeelint:
      all: allcoffee
    simplemocha:
      all:
        src: [
          "*/test/*.coffee"
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
  #grunt.loadNpmTasks "grunt-coffeelint"
  
  # Default task(s).
  grunt.registerTask "default", ["coffeelint","simplemocha"]