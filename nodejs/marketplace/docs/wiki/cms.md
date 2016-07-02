= Flarebyte CMS =

== Server Side ==

=== Service ===

A client calls the Data service (CMS) by calling an url such as:

https://flarebyte.info/ds/$domain/$version/script.$format


Ex: https://flarebyte.info/ds/fe31com/V1.23/script.json
ex: https://flarebyte.info/ds/fe31com-starbucks/V1.23/script.xml

Each domain can have different validation rules for types and security.

Each call should include the authorization of the user (Oauth).


=== History ===

Any modification to a record is saved in the history in order to facilitate recovery of data.

=== Security ===

==== Internal Identifiers ====

Internal identifier are only available to the CMS, and no client-side softwares should have access to them.

Usually, they should be UUID. Ex: f72c81a0-df49-11df-85ca-0800200c9a66

Each record is divided into zones available only to a specific ID and scope:

List of internal identifiers:

RID: root uuid, allows access to all zones. Ex: RID-f72c81a0-df49-11df-85ca-0800200c9a66
SID: scope id, allows only access to ...

SID: site uuid, allows to share data.
AID: application uuid, allows access to the application only zone.
WID: webclient uuid, allows access to the webclient zone.
BID: brand uuid, allows access to the brand zone. Ex: Starbucks.

Uses Cases:
As the Starbucks brand, I want to define a list of facilities (ex: WC, wifi, etc ...). Each Starbucks can select the available facilities in their shop.

Each keys in the database, should starts by a prefix indicating the zone: Ex: z12:/company/name

Issues ...

Zones:

 * root zone: The zone used by internal tools. Read-Write, Read-only.


==== External Identifiers ====

External identifiers are:

 * slugs: Ex: tate_modern (better) or TateModern
 * XID: a 15 digits number. Ex: 123456789012345

Note: This represents 1 Tera of records which a chance of collision less than 0,1%. In other words, we should be able to generate them without using counters or database lookups.

Public identifiers should only allow give access to public information.

==== Private identifiers ====

Private identifiers (PID) are very secure identifiers with the following properties:

 * They are unique for a user. Two different users linking to the same object (same IID), will receive two different PID.
 * They are not sharable between users, and can be only used by the user who have received them.
 * They have a limited life time. Ex: expire on the dd/mm/yyyy, usually 10 days.
 * They include a validation graph using the last n digits of IID. Ex: user=45B3

Ex:

f72c81a0-df49-11df-85ca-0800200c9a66;05/10/2010;me=45B3,team=64D5

PID should be encrypted and may be compressed.

== Script ==

The script language is written in [http://jsonml.org/ jsonML]. Therefore, it should be compatible with both xml and json.
Here are a few reasons:
 * json should be faster to parse.
 * json has a simpler structure and should be easier to parse with default client libraries.
 * we intend to validate the script, so an xml like structure may be a good start.
 * "ordered-dictionary" like structure.

Unless we detect performances issues, we should use nodes rather than attributes, to facilitate the writing of validation rules.

=== Validation ===

The script is validated using rules attached to xpath.
There are validation rules:
 * validation of the types. Ex: date, boolean...
 * validation of access right. Ex: starbuck.admin

When possible, validation should avoid making any lookup to the database. If such case, try to use Private identifier.

Most common type of value:

 * basic type: string of 16 chars.
 * external identifier (XID)
 * private identifiers (PID)

Some value can be generated using the eval approach:

Ex:

{{{
#!xml
<comment>
<date>
<eval>now</eval>
</date>
<comment>
}}}

=== Entities ===

An entity section is a fragment of the script which can be push directly to the database.


{{{
#!xml
<data>
<museum>
<label>Tate Modern</label>
<geo>
<latitude>1.535353</latitude>
<longitude>2.7347377</longitude>
</geo>
<telephone>
<type>Home</type>
<number>+4412345678</number>
<telephone>
<telephone>
<type>Work</type>
<number>+4412345678</number>
<telephone>
</museum>
<data>
}}}

Translates to xpath-value:

 * /museum/label: Tate modern
 * /museum/geo/latitude: 1.535353
 * /museum/geo/longitude: 2.7347377
 * /museum/telephone[1]/type: Home
 * /museum/telephone[1]/number: +4412345678
 * /museum/telephone[2]/number: Work
 * /museum/telephone[2]/number: +4412345678

=== Features ===

 * Audit Trails
 * Content Approval
 * Granular Privileges
 * Login History
 * Versioning
 * Undo
 * Advanced Caching
 * Content Scheduling: state: to_publish, publish_state, published
 * Content Staging
 * Sub-sites/ Roots
 * Themes / Skins
 * Trash
 * Web Statistics: asynchronous counter.
 * Workflow Engine: Copy.
 * Content Reuse
 * Metadata
 * Multi-site Deployment
 * Multi-lingual Content

=== Uses cases ===

[FlarebyteCmsUseCases Use Cases]
