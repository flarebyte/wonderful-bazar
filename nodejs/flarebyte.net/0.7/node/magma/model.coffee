'use strict'
CT = require('magma-constant')

REQUIRED= "required"
OPTIONAL= "optional"
AUTO= "auto"
CTX= "ctx"

BOOL= "boolean"
INT= "int"
FLOAT= "float"
DATETIME= "date-time"
ENGLISH= "en-stem"
PROF= "profile"
SOUND= "phonetic"
NO= "no"

pkGenerator= (ctx, record) ->
  return record.id

exports.pkGenerator= pkGenerator

MODEL=
  __meta:
    domain:         "message"
    recordType:     CT.TYPE_MESSAGE_ID
    idLength:       CT.LEN_MESSAGE_ID
    pkGenerator:    pkGenerator
  
  created:              [AUTO, DATETIME]
  updated:              [OPTIONAL, DATETIME]
  addressCountry:       [REQUIRED,NO]
  addressLocality:      [OPTIONAL,SOUND]
  confidential:         [REQUIRED,BOOL]
  documentId:           [OPTIONAL,NO]
  documentModelId:      [OPTIONAL,NO]
  documentType:         [OPTIONAL,NO]
  draft:                [REQUIRED,BOOL]
  editable:             [REQUIRED,BOOL]
  language:             [OPTIONAL,NO]
  messageType:          [REQUIRED,NO]
  relDocumentId:        [OPTIONAL,NO]
  relDocumentModelId:   [OPTIONAL,NO]
  relDocumentType:      [OPTIONAL,NO]
  shareable:            [REQUIRED,BOOL]
  userMessage:          [REQUIRED,ENGLISH]
  validFrom:            [REQUIRED,DATETIME]
  validThrough:         [REQUIRED,DATETIME]
  recipients:           [REQUIRED,PROF]
  hideRecipients:       [REQUIRED, BOOL]
  #Locked
  messageRef:           [AUTO, NO]
  parentMessageRef:     [AUTO, NO]
  from:                 [REQUIRED, PROF]
  technicalMessage:     [REQUIRED, ENGLISH]
  questionMessage:      [OPTIONAL, ENGLISH]
  helpMessage:          [REQUIRED, ENGLISH]
  answerFormat:         [OPTIONAL, NO]
  statusFormat:         [OPTIONAL, NO]
  inbound:              [REQUIRED, BOOL]
  #Receive
  userTags:             [OPTIONAL,NO]
  read:                 [REQUIRED,BOOL]
  todo:                 [REQUIRED,BOOL]
  spam:                 [REQUIRED,BOOL]
  important:            [REQUIRED,BOOL]
  deleted:              [REQUIRED,BOOL]
  archived:             [REQUIRED,BOOL]
  status:               [REQUIRED, NO]
  answer:               [OPTIONAL, ENGLISH]



exports.MODEL= MODEL
