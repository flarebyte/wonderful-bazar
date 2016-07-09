#
# * Serve JSON to our AngularJS client
#

exports.getMyUserAccount = (req, res) ->
  r=
    loginEmail: "charles.baudelaire@gmail.com"
  res.json r

exports.getMyAgreements = (req, res) ->
  r=
    loginEmail: "charles.baudelaire@gmail.com"
  res.json r

exports.getIndividualProfile = (req, res) ->
  id= "1234/m5/001300614b4907b1259c90f2a3a84414"
  r=
    givenName: "Given"

  res.json r

exports.getBusinessProfile = (req, res) ->
  id= "1234/m5/001300614b4907b1259c90f2a3a84414"
  r=
    legalName: "Flarebyte.com Ltd"
  res.json r

exports.searchProfile = (req, res) ->
  term= "olivier"
  r=
    loginEmail: "charles.baudelaire@gmail.com"
  res.json r

exports.searchSpace = (req, res) ->
  term= "olivier"
  r=
    loginEmail: "charles.baudelaire@gmail.com"

  res.json r

exports.searchDoc = (req, res) ->
  term= "olivier"
  r=
    loginEmail: "charles.baudelaire@gmail.com"

  res.json r

exports.getDoc = (req, res) ->
  id= "1234/m5/001300614b4907b1259c90f2a3a84414"
  r=
    legalName: "Flarebyte.com Ltd"
  res.json r

