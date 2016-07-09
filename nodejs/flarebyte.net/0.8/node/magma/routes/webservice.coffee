#
# f/view.post/123456789
#
'use strict'

magma_rendering = require('magma-rendering')

exports.viewget = (req, res) ->
  magma_rendering.viewget(req,res)

exports.viewput = (req, res) ->
  magma_rendering.viewput(req,res)

exports.viewpost = (req, res) ->
  magma_rendering.viewpost(req,res)

exports.viewdel = (req, res) ->
  magma_rendering.viewdel(req,res)
