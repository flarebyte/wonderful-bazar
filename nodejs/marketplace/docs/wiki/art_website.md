= Art website: fe3l.com  =

== Summary ==

Fe3l.com should help a art lover:
 * to find art exhibitions in his city (London): http://fe3l.com/london
 * to share his opinions about art, museums, artists.
 * to organize a visit to museum or exhibitions: http://fe3l.com/TateModern
 * to discover famous or new artists: http://fe3l.com/artists
 * to commission painters, and to some extent to buy art works: http://fe3l.com/art

== Logo ==

Definition of Feel::
 * to be or become conscious of.
 * to be emotionally affected by: to feel one's disgrace keenly.
 * to have a particular sensation or impression of.

Ex: feel Islington, feel Picasso ...

Of course, the domain feel.com was not available and therefore we are using fe3l.com.
Unfortunately, a lot of people may type "feel" instead of "fe3l", and we need make it easy for them to remember the E3 instead of EE.
The logo should reflect this, and we should use the E and 3 as part of the logo.
From a graphical point of view the 3 can be seen as a E in a mirror.

Possible shapes for the logo: a '''heart''', ying&yang, etc ...



== URL Concepts ==

 * Each URL must be very short in order to be easily copied and sent by SMS.
 * If possible each URL should be meaningful.
 * Each document should have an unique ID. Even when the type is different, the ids should be different.

=== URL permanent links ===

 * topic link: updated with the latest news, often bookmarked by users or websites + feed ex: /drawing/ or /drawing/subject/
 * major link: updated with the latest news, often bookmarked by users or websites. ex: /place/tatemodern/ or /tatemodern/
 * oneshoot link: rarely updated. Base [alphabet without vowels] starting with number(year).
  * No checksum.
  * Predictable.
  * Example: /4wRpWj.
 * unique ID: First 2 characters=520 types=520 tables
  * gold=/1aA,
  * silver=/1aAB,
  * bronze=/1aABC.
  * rss.flarebyte.com/ or atom.artsite.com (hosted in the cloud).

==== Examples ====

 * [topic]/[search|who|what|where|when|why|how]{asc,desc}
 * [topic]/[people=p=1|subject=s=2|place=l=3|event=e=4|analysis=a=5|technique=t=6]
 * [topic]/[mail|feedback]
 * [topic]/[highlight|popular|editor|thread|photo|video|]
 * atom.artsite.com/[topic]
 * [topic,city]
 * [topic,country]
 * [topic,city,country]
 * [topic]?l="fr"


=== Document type ===

 * people.item,people.list,
 * subject.item,subject.list
 * place.item,place.list
 * event.item,event.list
 * analysis.item,analysis.list
 * technique.item,technique.list

See [FlarebyteCms Flarebyte CMS]

==== Examples ====

 * /p/pablopicasso,/people/picasso/
 * /l/tatemodern/,/place/tate,liverpool/
 * /s/impressionism/,/subject/4wRpWj/
 * /44wRpWj,/event/goodfriday,london/,/event/boxingday,newyork/,/e/today,/e/tomorrow,lyon
 * :::today,tonight,tomorrow,week,weekend,month,quarter
 * /54wRpWj,/analysis/4wRpWj
 * /64wRpWj,/technique/

Note: in order to be twitterable as such, url must not exceed 30 chars.


== Tables ==

=== Amazon Simple DB ===

==== Resources bucket ====

||uuid||date||resourcetype||url||rel||rev||mimetype||lang||charset||width||height||ratio||tags||coloration||rating||
||550e8400-e29b-41d4-a716-446655440000||2009-10-04||image||/myurl.jpg||print||no||text/html||fr||UTF-8||1280||640||2:1||fencing||black&white||3||

resource types:
 * image
 * video
 * audio
 * spreadsheet
 * chart
 * ...


== GUI ==
=== Access keys ===

We will encourage contextual behavior for the access keys, and we will assume that the users will use them often.
When possible, we will try to follow the [http://archive.cabinetoffice.gov.uk/e-government/resources/handbook/html/2-4.asp UK Government recommendations] (ex: Help, Search ..). See also [http://www.bbc.co.uk/accessibility/accesskeys/keys.shtml BBC recommendations]. However, we will give priority to the ease of use for our application.  

|| 1 - '''Home'''|| 2 - Next || 3 - '''Site map'''||
|| 4 - '''Search''' || 5 - loop accessibility || 6 - '''Help'''||
|| 7 - vote +1 || 8 -vote -1|| 9 - Share this||
|| * || 0 - Preferences || / ||


Listed below is the recommended UK Government access keys standard:

 * S - Skip navigation
 * 1 - Home page
 * 2 - What's new
 * 3 - Site map
 * 4 - Search
 * 5 - Frequently Asked Questions (FAQ)
 * 6 - Help
 * 7 - Complaints procedure
 * 8 - Terms and conditions
 * 9 - Feedback form
 * 0 - Access key details

In order to create a contextual access keys, we could accept link like:
 * /event/12YGGJKGK.search
 * /event/12YGGJKGK?action=search

== Art topics ==

 * /drawing/,
 * /illustration/
 * /painting/
 * /printmaking/
 * /sculpture/
 * /architecture/
 * /garden/
 * /installation/
 * /filmmaking/
 * /photo/
 * /conceptual/
 * /mixmedia/
 * /craft/
 * /deco/
 * /fashion/
 * /digital/
 * /graphic/
 * /etching/
 * /litho/
 * /screen/
 * /comic/
 * /typo/
 * /alternative/
 * /street/

== Advertising ==

 * SEO: robot should exclude ads.

=== Discover deal ===

 * Round robin ads. Old ads should be deleted. :
 * /discover/121

=== Bronze deal ===

 * Free mobile hosting.
 * Inline bottom ads.
 * /ads/dior
 * /ads/dior3

=== silver deal ===
 * Free mobile hosting.
 * Banner ads.
 * Choice of root: ads,brand,tm,ltd,plc,co
  * /tm/dior
  * /tm/dior/poison
  * /tm/dior/jadore
  * /tm/dior/dolcevita
  * /brand/sony

=== gold deal === 	

* /dior.mobi/poison
	...customization of the mobile site ..

== Search ==

 * /search/q="query"&hl="en". This should use open search.
 * /who/
 * /what/
 * /where/
 * /when/
 * /why/
 * /how/
 * /api/

== Topics ==

/highlight/
/opening/
/buzz/
/alert/

== Actions ==

 * /mail/from="07998436"&to="email@email.com"&l="gb"&subj="subject"&msg="what do you think ?"
 * /mail/from="07998436"&to="email@email.com"&l="gb"&cat="001"
 * /feedback/
 * /about/
 * /help/
 * /faq/
 * /subscribe/
 * /privacy/
 * /terms/
 * /advertise/
 * /perso/
 * /flarebyte/
 * /quiz/
 * /card/
 * /share/

== User preferences ==


{{{
#!python

userprefs.topics.drawing.visible=True
userprefs.topics.drawing.interest=3
userprefs.usability.fonts.size=14

}}}

== Semantic Tags ==

[SemanticTags]

== 100 richest cities ==

tokyo,newyork,losangeles,chicago,paris,london,osaka,mexico,philadelphia,washingtondc,boston,dallas,
buenosaires,hongkong,sanfrancisco,atlanta,houston,miami,s√£opaulo,seoul,toronto,detroit,madrid,seattle,
moscow,sydney,phoenix,minneapolis,sandiego,riodejaneiro,barcelona,shanghai,melbourne,istanbul,denver,
singapore,taipei,mumbai,rome,montreal,milan,baltimore,metromanila,stlouis,beijing,cairo,jakarta,stpetersburg,
pusan,kolkata,vienna,delhi,telaviv,santiago,cleveland,bangkok,tehran,portland,bogot√°,stpetersburg,guangzhou,
pittsburgh,riyadh,lisbon,vancouver,johannesburg,monterrey,stockholm,capetown,berlin,athens,birmingham,fukuoka,
manchester,lima,belohorizonte,guadalajara,hamburg,turin,lyon,jeddah,karachi,dhaka,munich,dublin,leeds,warsaw,
tianjin,bangalore,portoalegre,helsinki,naples,budapest,zurich,ankara,amsterdam,auckland,copenhagen,recife,rotterdam
