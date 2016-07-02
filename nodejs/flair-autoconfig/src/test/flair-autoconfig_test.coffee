'use strict'

cfg = require('../lib/flair-autoconfig.js')
beta = require('../test/b/beta.js')
alpha = require('../test/a/alpha.js')


###
======== A Handy Little Mocha Reference ========
https://github.com/visionmedia/should.js
https://github.com/visionmedia/mocha

###

describe 'flair-autoconfig', ()->
  describe '#findStart()', ()->

    it 'finds node_modules when present', ()->
      cfg.findStart(["a","node_modules","x","y","z"]).should.eql(0)
      cfg.findStart(["a","b","node_modules","x","y","z"]).should.eql(1)
      cfg.findStart(["a","b","c","node_modules","x","y","z"]).should.eql(2)

    it 'ignores node_modules at the beginning', ()->
      cfg.findStart(["node_modules","x","y","z"]).should.eql(3)
 
    it 'picks the last part when node_modules is absent', ()->
      cfg.findStart(["node_modules","x","y","z"]).should.eql(3)

  describe '#fromPath()', ()->

    it 'finds last part when node_modules is absent', ()->
      cfg.fromPath('/a/b/c/d/e/f','/').should.eql(['f'])
      cfg.fromPath('/a/b/c/d/e/f.js','/').should.eql(['f'])

    it 'finds parts node_modules is present', ()->
      cfg.fromPath('/a/b/c/node_modules/d/e/f','/').
      should.eql(['c','d','e','f'])

    it 'ignores node_modules,lib,src parts', ()->
      cfg.fromPath('/a/b/c/node_modules/d/src/e/lib/f','/').
      should.eql(['c','d','e','f'])

  describe '#deleteExt()', ()->

    it 'deletes .coffee and .js when present as extension', ()->
      cfg.deleteExt('script.js').should.eql('script')
      cfg.deleteExt('script.coffee').should.eql('script')
    
    it 'does not delete .coffee and .js when not at the end', ()->
      cfg.deleteExt('script.js.more').should.eql('script.js.more')
      cfg.deleteExt('script.coffee.more').should.eql('script.coffee.more')

    it 'does not delete -coffee and -js', ()->
      cfg.deleteExt('script-js').should.eql('script-js')
      cfg.deleteExt('script-coffee').should.eql('script-coffee')

  describe '#getBasename()', ()->

    it 'get the script base name from current process', ()->
      basename = cfg.getBasename()
      basename.should.eql("grunt")

  describe '#moduleName()', ()->

    it 'get the current module name from current process', ()->
      betaname = beta.name
      alphaname = alpha.name
      alphaname.should.eql("alpha")
      betaname.should.eql("beta")


  describe '#makeName()', ()->

    it 'get the name based on current process', ()->
      name = cfg.makeName('/a/b/c/node_modules/d/e/f','/')
      name.should.eql('c--d--e--f--grunt')
