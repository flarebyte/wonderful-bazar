jade = require("jade")
fs = require('fs')
views_path="/Users/olivier/Dropbox/flarebyte.com-ltd/software development/node/marketplace/views/readme.jade"

verify = (test, filename) ->
  if not filename
    test.done()
    return
    
  options = 
    filename: views_path
    locals: require (__dirname + "/given/#{filename}")
    
  expected = fs.readFileSync(__dirname + "/expected/#{filename}.xml", 'utf8')
  template = fs.readFileSync(__dirname + "/jade/#{filename}.jade", 'utf8')
  fn = jade.compile(template, options)
  result=fn(options.locals)
  test.deepEqual(result,expected)
  test.done()

module.exports.verify=verify

createExpected = (test, filename) ->
  if not filename
    test.done()
    return
    
  options = 
    filename: views_path
    locals: require (__dirname + "/given/#{filename}")
    
  template = fs.readFileSync(__dirname + "/jade/#{filename}.jade", 'utf8')
  fn = jade.compile(template, options)
  result=fn(options.locals)
  fs.writeFileSync(__dirname + "/expected/#{filename}.xml",result, 'utf8')
  test.done()

module.exports.createExpected=createExpected

create = (test, filename) ->
  if not filename
    test.done()
    return
  fs.writeFileSync(__dirname + "/given/#{filename}.coffee","", 'utf8')
  fs.writeFileSync(__dirname + "/jade/#{filename}.jade","", 'utf8')
  fs.writeFileSync(__dirname + "/expected/#{filename}.xml","", 'utf8')
  test.done()

module.exports.create=create