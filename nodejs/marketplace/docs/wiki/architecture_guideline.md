== Architecture guidelines ==

=== Service Oriented Architecture ===

We are looking to promote a scalable service oriented architecture. The services could be implemented using different programming languages, but should be able to interact smartly.
The overall idea is to create a synergy based on this collection of services.

We will be trying to take into account the following architectural principles:

    * Service loose coupling – Services maintain a relationship that minimizes dependencies.
    * Service contract – Services adhere to a communications agreement.
    * Service abstraction – Services hide logic from the outside world.
    * Service reusability – Logic is divided into services with the intention of promoting reuse.
    * Service composability – Collections of services can be coordinated and assembled to form composite services.
    * Service autonomy – Services have control over the logic they encapsulate.
    * Service discoverability – Services are designed to be outwardly descriptive so that they can be found and assessed via available discovery mechanisms.
    * Service Relevance – Functionality is presented at a granularity recognized by the user as a meaningful service.

[FlareServices]

Each service, the following characteristics should be described:
 * Persitence, retention period, availability, response time, security, access frequency, business value.

=== Development stack ===

|| Stack || Use || Benefits || Complexity || Cost ||
|| Linux || Deployment || Reliable || *** || *** ||
|| Python || Programming || OO, powerful || ** || ** ||
|| Java || Programming || OO, fast || *** || *** ||
|| Django || Programming || RAD || ** || ** ||
|| Subversion || Versioning || better than cvs || ** || ** ||
|| PostgreSQL || Database || search, geo, custom || *** || *** ||
|| Restful services || Standard || flexible and fast || ** || ** ||
 











