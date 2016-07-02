data_ports =
  HTTP_TEST: 2000
  HTTP_ID: 3000
  HTTP_SCHEMA: 3010
  HTTPS_SCHEMA: 3011
  HTTP_DATA: 3020
  HTTPS_DATA: 3021
  HTTP_MEDIA: 3030
  HTTPS_MEDIA: 3031
  HTTP_HISTORY: 3040
  HTTPS_HISTORY: 3041

editions = ["gbr","fra","can","eur"]
spaces = ["flarebyte-home","flarebyte-marketplace","flarebyte-account","flarebyte-answers","flarebyte-admin"]
web_port = 4000
web_hosting = {}
for space in spaces
  web_hosting[space]={}
  for edition in editions
    web_port = web_port + 10
    ssl_web_port = web_port + 1
    data=
      server_name: "http://localhost:#{web_port}"
      secure_server_name: "https://localhost:#{ssl_web_port}"
      base_url: edition
      PORTS:
        HTTP: web_port
        HTTPS: ssl_web_port
    web_hosting[space][edition]=data

settings =
  data_hosting:
    PORTS: data_ports
    HTTP_ID: "http://localhost:#{data_ports.HTTP_ID}"
    HTTP_SCHEMA: "http://localhost:#{data_ports.HTTP_SCHEMA}"
    HTTPS_SCHEMA: "https://localhost:#{data_ports.HTTPS_SCHEMA}" 
    HTTP_DATA: "http://localhost:#{data_ports.HTTP_DATA}"
    HTTPS_DATA: "https://localhost:#{data_ports.HTTPS_DATA}"
    HTTP_MEDIA: "http://localhost:#{data_ports.HTTP_MEDIA}"
    HTTPS_MEDIA: "https://localhost:#{data_ports.HTTPS_MEDIA}"
    HTTP_HISTORY: "http://localhost:#{data_ports.HTTP_HISTORY}"
    HTTPS_HISTORY: "https://localhost:#{data_ports.HTTPS_HISTORY}"
  web_hosting: web_hosting

module.exports=settings