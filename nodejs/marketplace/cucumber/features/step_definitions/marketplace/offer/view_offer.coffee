WorldFactory = require("marketplace.world").WorldFactory  

ViewOfferDefinitionsWrapper = ->
  @World2 = new WorldFactory
  
  @Given /^that I am logged or not$/, (callback) =>
     callback()

  @When /^I choose to view a valid "([^"]*)"$/, (domain, callback) =>
    domains = 
      offer:
          url: "/gbr/offers/offering-0-or-any-good-alternative./offering0"
    @World2.visitPublicMarketplace(domains[domain].url, callback)

  @Then /^the application should display the "([^"]*)" page$/, (arg1, callback) =>
    callback.pending()

  @Then /^the application should display the buying options$/, (callback) =>
    callback.pending()

  @When /^I choose to view an expired "([^"]*)"$/, (arg1, callback) =>
    callback.pending()

  @Then /^the application should not display the buying options$/, (callback) =>
    callback.pending()

  @When /^I choose to view a "([^"]*)" through an old link$/, (arg1, callback) =>
    callback.pending()

  @Then /^the application should redirect me to the latest "([^"]*)" page$/, (arg1, callback) =>
    callback.pending()

module.exports = ViewOfferDefinitionsWrapper