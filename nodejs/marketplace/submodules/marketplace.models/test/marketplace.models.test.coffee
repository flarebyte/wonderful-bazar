___ = require("underscore")
___.mixin require("underscore.string")
models = require("marketplace.models")
base= "http://marketplace.flarebyte.com/types"
JSV = require("JSV").JSV
corecount = 21
env = JSV.createEnvironment()
jsonschema = env.findSchema(env.getOption("latestJSONSchemaSchemaURI"))


exports.answer_model_should_work = (test) ->
  test.deepEqual(models.answer.id,"#{base}/types#Answer")
  test.deepEqual(___.keys(models.answer.properties).length, corecount+ 3)
  test.deepEqual(jsonschema.validate(models.answer).errors.length, 0)
  test.done()
  
exports.business_model_should_work = (test) ->
  test.deepEqual(models.business.id,"#{base}/types#Business")
  test.deepEqual(___.keys(models.business.properties).length, corecount+ 2)
  test.deepEqual(jsonschema.validate(models.business).errors.length, 0)
  test.done()
  
exports.characteristic_model_should_work = (test) ->
  test.deepEqual(models.characteristic.id,"#{base}/types#Characteristic")
  test.deepEqual(___.keys(models.characteristic.properties).length, corecount)
  test.deepEqual(jsonschema.validate(models.characteristic).errors.length, 0)
  test.done()
  
exports.comment_model_should_work = (test) ->
  test.deepEqual(models.comment.id,"#{base}/types#Comment")
  test.deepEqual(___.keys(models.comment.properties).length, corecount+3)
  test.deepEqual(jsonschema.validate(models.comment).errors.length, 0)
  test.done()
  
exports.copyright_model_should_work = (test) ->
  test.deepEqual(models.copyright.id,"#{base}/types#Copyright")
  test.deepEqual(___.keys(models.copyright.properties).length, corecount+ 4)
  test.deepEqual(jsonschema.validate(models.copyright).errors.length, 0)
  test.done()
  
exports.feature_model_should_work = (test) ->
  test.deepEqual(models.feature.id,"#{base}/types#Feature")
  test.deepEqual(___.keys(models.feature.properties).length, corecount)
  test.deepEqual(jsonschema.validate(models.feature).errors.length, 0)
  test.done()
  
exports.image_model_should_work = (test) ->
  test.deepEqual(models.image.id,"#{base}/types#Image")
  test.deepEqual(___.keys(models.image.properties).length, corecount+ 1)
  test.deepEqual(jsonschema.validate(models.image).errors.length, 0)
  test.done()
  
exports.markup_model_should_work = (test) ->
  test.deepEqual(models.markup.id,"#{base}/types#Markup")
  test.deepEqual(___.keys(models.markup.properties).length, corecount)
  test.deepEqual(jsonschema.validate(models.markup).errors.length, 0)
  test.done()
  
exports.offering_model_should_work = (test) ->
  test.deepEqual(models.offering.id,"#{base}/types#Offering")
  test.deepEqual(___.keys(models.offering.properties).length, corecount+ 10)
  test.deepEqual(jsonschema.validate(models.offering).errors.length, 0)
  test.done()
  
exports.organization_model_should_work = (test) ->
  test.deepEqual(models.organization.id,"#{base}/types#Organization")
  test.deepEqual(___.keys(models.organization.properties).length, corecount+ 3)
  test.deepEqual(jsonschema.validate(models.organization).errors.length, 0)
  test.done()
  
exports.people_model_should_work = (test) ->
  test.deepEqual(models.people.id,"#{base}/types#People")
  test.deepEqual(___.keys(models.people.properties).length, corecount+ 7)
  test.deepEqual(jsonschema.validate(models.people).errors.length, 0)
  test.done()
  
exports.permission_model_should_work = (test) ->
  test.deepEqual(models.permission.id,"#{base}/types#Permission")
  test.deepEqual(___.keys(models.permission.properties).length, corecount)
  test.deepEqual(jsonschema.validate(models.permission).errors.length, 0)
  test.done()
  
exports.product_or_service_model_should_work = (test) ->
  test.deepEqual(models.product_or_service.id,"#{base}/types#ProductOrServiceModel")
  test.deepEqual(___.keys(models.product_or_service.properties).length, corecount+ 1)
  test.deepEqual(jsonschema.validate(models.product_or_service).errors.length, 0)
  test.done()
  
exports.profile_model_should_work = (test) ->
  test.deepEqual(models.profile.id,"#{base}/types#Profile")
  test.deepEqual(___.keys(models.profile.properties).length, corecount)
  test.deepEqual(jsonschema.validate(models.profile).errors.length, 0)
  test.done()
  
exports.question_model_should_work = (test) ->
  test.deepEqual(models.question.id,"#{base}/types#Question")
  test.deepEqual(___.keys(models.question.properties).length, corecount+ 3)
  test.deepEqual(jsonschema.validate(models.question).errors.length, 0)
  test.done()
  
exports.role_model_should_work = (test) ->
  test.deepEqual(models.role.id,"#{base}/types#Role")
  test.deepEqual(___.keys(models.role.properties).length, corecount)
  test.deepEqual(jsonschema.validate(models.role).errors.length, 0)
  test.done()
  
exports.space_model_should_work = (test) ->
  test.deepEqual(models.space.id,"#{base}/types#Space")
  test.deepEqual(___.keys(models.space.properties).length, corecount)
  test.deepEqual(jsonschema.validate(models.space).errors.length, 0)
  test.done()
  
exports.stats_model_should_work = (test) ->
  test.deepEqual(models.stats.id,"#{base}/types#Stats")
  test.deepEqual(___.keys(models.stats.properties).length, corecount+ 1)
  test.deepEqual(jsonschema.validate(models.stats).errors.length, 0)
  test.done()
  
exports.tag_model_should_work = (test) ->
  test.deepEqual(models.tag.id,"#{base}/types#Tag")
  test.deepEqual(___.keys(models.tag.properties).length, corecount+ 1)
  test.deepEqual(jsonschema.validate(models.tag).errors.length, 0)
  test.done()
  
exports.type_model_should_work = (test) ->
  test.deepEqual(models.type.id,"#{base}/types#Type")
  test.deepEqual(___.keys(models.type.properties).length, corecount)
  test.deepEqual(jsonschema.validate(models.type).errors.length, 0)
  test.done()
  
exports.warranty_model_should_work = (test) ->
  test.deepEqual(models.warranty.id,"#{base}/types#Warranty")
  test.deepEqual(___.keys(models.warranty.properties).length, corecount+ 2)
  test.deepEqual(jsonschema.validate(models.warranty).errors.length, 0)
  test.done()














offering_valid =  
  about: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12",
  member: "http://localhost:3000/flarebyte-marketplace/id/offering",
  isPartOf: "http://localhost:3000/flarebyte-marketplace/id/dataset/offering",
  hasVersion: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12/versions/0001",
  isReplacedBy: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12/versions/0002",
  isVersionOf: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12",
  label: "offering 12 or any good alternative.",
  creator: "http://localhost:3000/flarebyte-marketplace/id/people/people12",
  abstract: "Lorem ipsum dolor sit amet, consectetur adipiscing elit",
  created: "2008-04-22T04:22:00Z",
  modified: "2008-04-22T04:22:00Z",
  available: "2008-04-22T04:22:00Z",
  issued: "2008-04-22T04:22:00Z",
  valid: "2008-04-22T04:22:00Z",
  language: "en",
  inbounds: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12/inbounds",
  outbounds: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12/outbounds",
  history: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12/history",
  stats: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12/stats",
  comments: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12/comments",
  body: "http://localhost:3001/flarebyte-marketplace/markup/all/12.md",
  image: "http://localhost:3001/flarebyte-marketplace/image/all/12",
  comment: "offering offering 12",
  hasBusinessFunction: "Sell",
  hasPriceSpecification: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12#price",
  validFrom: "2008-04-22T04:22:00Z",
  validThrough: "2008-04-22T04:22:00Z",
  eligibleRegions: ["GBR","FRA"],
  eligibleCustomerTypes: ["Reseller"],
  acceptedPaymentMethods: ["ByBankTransferInAdvance"],
  hasWarrantyPromise: "http://localhost:3000/flarebyte-marketplace/id/warranty/warranty2",
  availableAtOrFrom: "http://localhost:3000/flarebyte-marketplace/id/business/business2",
  UnitPriceSpecification:
    ID: "http://localhost:3000/flarebyte-marketplace/id/offering/offering12#price",
    hasUnitOfMeasurement: "C62",
    hasMaxCurrencyValue: 99,
    hasMinCurrencyValue: 44,
    hasCurrency: "Unit",
    validFrom: "2008-04-22T04:22:00Z",
    validThrough: "2008-04-22T04:22:00Z",
    valueAddedTaxIncluded: "true"
   type: "http://localhost:3000/flarebyte-marketplace/schema/types#Offering",
