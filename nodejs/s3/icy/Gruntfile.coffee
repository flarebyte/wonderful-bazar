
module.exports = (grunt) ->
  buildPath = "/Users/olivier/icybuild"
  secretPath = "yg3xgk57l4jizb81ld6wnqef"
  s3region = "eu-west-1"
  s3flash = "ieflashflarebyte"
  s3media = "iemediaflarebyte"
  today = grunt.template.today("yyyy-mm-dd'T'HHMM")
  pathmedia = "#{buildPath}/#{s3media}/#{today}"
  pathflash = "#{buildPath}/#{s3flash}/#{secretPath}"
  debugS3=true

  # Project configuration.
  grunt.initConfig
    pkg: grunt.file.readJSON("package.json")
    clean:
      options:
        force: true
      build: ["/Users/olivier/icybuild"] #keep hard coded to avoid deleting disk by mistake
    copy:
      flash:
        expand: true
        cwd: "#{s3flash}"
        src: ['**/*.yaml']
        dest: "#{pathflash}/no"
      media_dev:
        expand: true
        cwd: "#{s3media}"
        src: ['**/*.js','**/*.css','!**/*.min.css','**/*.png','**/*.gif','**/*.ico','**/*.svg','!**/*.min.js']
        dest: "#{pathmedia}/no/dv"
      media_prod:
        expand: true
        cwd: "#{s3media}"
        src: ['**/*.js','**/*.css','!**/*.min.css','**/*.png','**/*.gif','**/*.ico','**/*.svg','!**/*.min.js']
        dest: "#{pathmedia}/no/pr"
    yaml:
      flash:
        options:
          ignored: /^_/
          space: 0
          constructors:
            '!include': (node, yaml) ->
              readPartialYAML node.value, yaml
        files: [{expand: true, cwd: "#{pathflash}/no/", src: ['**/*.yaml'], dest: "#{pathflash}/no/"}]
    compress:
      flash:
        options:
          mode: 'gzip'
        expand: true
        cwd: "#{pathflash}/no"
        src: ['**/*.json','**/*.yaml']
        dest: "#{pathflash}/gz"
      media:
        options:
          mode: 'gzip'
        expand: true
        cwd: "#{pathmedia}/no"
        src: ['**/*.css','**/*.js']
        dest: "#{pathmedia}/gz"

    fileregexrename:
      flash:
        options:
          replacements:[
            {pattern: new RegExp(".json.gz","g"), replacement: ".json"},
            {pattern: new RegExp(".yaml.gz","g"), replacement: ".yaml"},
          ]
        expand: true
        cwd: "#{pathflash}/gz"
        src: ['**/*.gz']
        dest: "#{pathflash}/gz"
      media:
        options:
          replacements:[
            {pattern: new RegExp(".css.gz","g"), replacement: ".css"},
            {pattern: new RegExp(".js.gz","g"), replacement: ".js"}
          ]
        expand: true
        cwd: "#{pathmedia}/gz"
        src: ['**/*.gz']
        dest: "#{pathmedia}/gz"

    s3:
      options:
        key: "***"
        secret: "***"
        region: "#{s3region}"
        debug: debugS3
      flash_n:
        options:
         bucket: "#{s3flash}"
         access: 'public-read'
        upload: [{rel: "#{pathflash}/", src:"#{pathflash}/no/**/*.*", dest:"icy/#{secretPath}"}]
      flash_gz:
        options:
          bucket: "#{s3flash}"
          access: 'public-read'
          headers:
            "Content-Encoding":"gzip"
        upload: [{rel: "#{pathflash}/", src:"#{pathflash}/gz/**/*.*", dest:"icy/#{secretPath}"}]
      media_n:
        options:
         bucket: "#{s3media}"
         access: 'public-read'
         headers:
            "Cache-Control":"public, max-age=31536000"
            "Expires":"Mon, 17 Apr 2023 21:31:12 GMT"
        upload: [{rel: "#{pathmedia}/", src:"#{pathmedia}/no/**/*.*", dest:"icy/#{today}"}]
      media_gz:
        options:
          bucket: "#{s3media}"
          access: 'public-read'
          headers:
            "Content-Encoding":"gzip"
            "Cache-Control":"public, max-age=31536000"
            "Expires":"Mon, 17 Apr 2023 21:31:12 GMT"
        upload: [{rel: "#{pathmedia}/", src:"#{pathmedia}/gz/**/*.*", dest:"icy/#{today}"}]
    uglify:
      media:
        options:
          report: 'min'
        expand: true
        cwd: "#{pathmedia}/no/pr"
        src: ['**/*.js']
        dest: "#{pathmedia}/no/pr"
    cssmin:
      media:
        options:
          report: 'min'
        expand: true
        cwd: "#{pathmedia}/no/pr"
        src: ['**/*.css']
        dest: "#{pathmedia}/no/pr"
    imagemin:
      media:
        options:
          report: 'min'
        expand: true
        cwd: "#{pathmedia}/no/pr"
        src: ['**/*.jpeg','**/*.jpg','**/*.png']
        dest: "#{pathmedia}/no/pr"
    svgo:
      media:
        expand: true
        cwd: "#{pathmedia}/no/pr"
        optimize:
          files: '*.svg'


  # Load the plugins.
  grunt.loadNpmTasks('grunt-contrib-clean')
  grunt.loadNpmTasks('grunt-contrib-copy')
  grunt.loadNpmTasks('grunt-yaml')
  grunt.loadNpmTasks('grunt-contrib-compress')
  grunt.loadNpmTasks('grunt-file-regex-rename')
  grunt.loadNpmTasks('grunt-contrib-uglify')
  grunt.loadNpmTasks('grunt-contrib-cssmin')
  grunt.loadNpmTasks('grunt-contrib-imagemin')
  grunt.loadNpmTasks('grunt-s3')
  grunt.loadNpmTasks('svgo-grunt')


  grunt.registerTask "flash", [
    "clean"
    "copy:flash"
    "yaml:flash"
    "compress:flash"
    "fileregexrename:flash"
    "s3:flash_n"
    "s3:flash_gz"
  ]

  grunt.registerTask "media", [
    "clean"
    "copy:media_dev"
    "copy:media_prod"
    "uglify:media"
    "cssmin:media"
    "imagemin:media"
    "svgo:media"
    "compress:media"
    "fileregexrename:media"
    "s3:media_n"
    "s3:media_gz"

  ]
