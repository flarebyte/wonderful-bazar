spaces_any = ["flarebyte-home","flarebyte-marketplace","flarebyte-answers","flarebyte-admin","flarebyte-account"]
settings = 
  rdftype_to_domain:
    "answer": "answer"
    "offering": "offering"
    "people": "people"
    "business": "business"
  web_hosting:
    "flarebyte-marketplace": 
      "gbr":
        title: "British data marketplace"
        short_title: "Marketplace"
        edition_name: "Great Britain"
        data_icon: "marketplace"
        currency_code: "GBP"
        language_code: ["en"]
        brand:
          website:
            title: "Flarebyte.com Ltd"
            homepage: "http://flarebyte.com/gbr"
          tagline: "Boost your data"
          logo: 
            id: "00001"
            version: "v1"
        footer_title: "Powered by Flarebyte.com Semantic Engine"
        footerA:[{short_title:"About", homepage:"/about"},{short_title:"Creators & Partners", homepage:"/partners"},{short_title:"Developers", homepage:"/developers"}]
        footerB:[{short_title:"Copyright", homepage:"/copyright"},{short_title:"Terms", homepage:"/terms"},{short_title:"Privacy", homepage:"/privacy"}]
          
        spaces: ["flarebyte-home","flarebyte-marketplace","flarebyte-account"]
        more_spaces: ["flarebyte-answers","flarebyte-admin"]
      "fra":
        title: "Place de marche de donnees"
        short_title: "Commerce"
        edition_name: "France"
        data_icon: "marketplace"
        currency_code: "EUR"
        language_code: ["fr"]
        spaces: spaces_any
      "can":
        title: "Canadian Marketplace"
        short_title: "Marketplace"
        edition_name: "Canada"
        data_icon: "marketplace"
        currency_code: "CAN"
        language_code: ["en"]
        spaces: spaces_any
      "eur":
        short_title: "European Marketplace"
        edition_name: "Europe"
        currency_code: "EUR"
        data_icon: "marketplace"
        language_code: ["en"]
        spaces: spaces_any
     "flarebyte-account": 
      "gbr":
        title: "Account"
        short_title: "Account"
        edition_name: "Great Britain"
        data_icon: "account"
        currency_code: "GBP"
        language_code: ["en"]
        spaces: spaces_any
      "fra":
        title: "Compte"
        short_title: "Compte"
        edition_name: "Great Britain"
        data_icon: "account"
        currency_code: "EUR"
        language_code: ["fr"]
        spaces: spaces_any
      "can":
        title: "Account"
        short_title: "Account"
        edition_name: "Canada"
        data_icon: "account"
        currency_code: "CAN"
        language_code: ["en"]
        spaces: spaces_any
      "eur":
        short_title: "Account"
        edition_name: "Account"
        data_icon: "account"
        currency_code: "EUR"
        language_code: ["en"]
        spaces: spaces_any
    "flarebyte-home": 
      "gbr":
        title: "Flarebyte.com"
        short_title: "Flarebyte.com"
        edition_name: "Great Britain"
        data_icon: "business-logo"
        currency_code: "GBP"
        language_code: ["en"]
        spaces: spaces_any
      "fra":
        title: "Flarebyte.com"
        short_title: "Flarebyte.com"
        edition_name: "France"
        data_icon: "business-logo"
        currency_code: "EUR"
        language_code: ["fr"]
        spaces: spaces_any
      "can":
        title: "Flarebyte.com"
        short_title: "Flarebyte.com"
        edition_name: "Canada"
        data_icon: "business-logo"
        currency_code: "CAN"
        language_code: ["en"]
        spaces: spaces_any
      "eur":
        short_title: "Flarebyte.com"
        edition_name: "Flarebyte.com"
        data_icon: "business-logo"
        currency_code: "EUR"
        language_code: ["en"]
        spaces: spaces_any
    "flarebyte-answers": 
       "gbr":
        title: "Answers"
        short_title: "Answers"
        edition_name: "Great Britain"
        data_icon: "answers"
        currency_code: "GBP"
        language_code: ["en"]
        spaces: spaces_any
      "fra":
        title: "Answers"
        short_title: "Answers"
        edition_name: "France"
        data_icon: "answers"
        currency_code: "EUR"
        language_code: ["fr"]
        spaces: spaces_any
      "can":
        title: "Answers"
        short_title: "Answers"
        edition_name: "Canada"
        data_icon: "answers"
        currency_code: "CAN"
        language_code: ["en"]
        spaces: spaces_any
      "eur":
        short_title: "Answers"
        edition_name: "Answers"
        data_icon: "answers"
        currency_code: "EUR"
        language_code: ["en"]
        spaces: spaces_any
    "flarebyte-admin": 
      "gbr":
        title: "Admin"
        short_title: "Admin"
        edition_name: "Great Britain"
        data_icon: "admin"
        currency_code: "GBP"
        language_code: ["en"]
        spaces: spaces_any
      "fra":
        title: "Admin"
        short_title: "Admin"
        edition_name: "Great Britain"
        data_icon: "admin"
        currency_code: "EUR"
        language_code: ["fr"]
        spaces: spaces_any
      "can":
        title: "Admin"
        short_title: "Admin"
        edition_name: "Canada"
        data_icon: "admin"
        currency_code: "CAN"
        language_code: ["en"]
        spaces: spaces_any
      "eur":
        title: "Admin"
        short_title: "Admin"
        edition_name: "Europe"
        data_icon: "admin"
        currency_code: "EUR"
        language_code: ["en"]
        spaces: spaces_any
  
module.exports=settings