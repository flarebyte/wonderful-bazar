package com.flarebyte.cm.com.core.dc;

import java.net.URI;
import java.util.Calendar;

import android.net.Uri;

import com.flarebyte.cm.com.core.Compilable;
import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Term;

/**
 * @see http://dublincore.org/documents/usageguide/elements.shtml Calendar TODO:
 *      getCreated(); getPlannedArchivage();
 *      getPlannedDeletion();getPrivacyType() Junk/Read/Editable/Locale/Junk
 *      votes/Previous
 * 
 * @author olivier
 * 
 */
public interface DublinCore extends ValueAccessor, Compilable {
	/**
	 * A summary of the resource.
	 * 
	 * @return
	 */
	public String getAbstract();

	/**
	 * An alternative title for the resource.
	 * 
	 * @return
	 */
	public String getAlternativeTitle();

	/**
	 * Links to another ResourceDescription (dublin core) object
	 * 
	 * @param term
	 * @return
	 */
	public DublinCore getAsDublinCore(Term term);

	public DublinCore[] getAsDublinCoreArray(Term term);

	/**
	 * A class of entity for whom the resource is intended or useful. A class of
	 * entity may be determined by the creator or the publisher or by a third
	 * party.Example: Audience="elementary school students"
	 * 
	 * @return
	 */
	public String getAudience();

	public URI getAudienceAsUri();

	/**
	 * The concept associated this dublin core.
	 * 
	 * @return null or the concept
	 */
	public Concept getConcept();

	/**
	 * An established standard to which the described resource conforms.
	 * 
	 * @return
	 */
	public String getConformsTo();

	public URI getConformsToAsUri();

	/**
	 * An entity responsible for making contributions to the content of the
	 * resource. Examples of a Contributor include a person, an organization or
	 * a service. Typically, the name of a Contributor should be used to
	 * indicate the entity.
	 * 
	 * @return
	 */
	public String getContributor();

	public String[] getContributorArray();

	public URI getContributorAsUri();

	public URI[] getContributorAsUriArray();

	/**
	 * The extent or scope of the content of the resource. Coverage will
	 * typically include spatial location (a place name or geographic
	 * co-ordinates), temporal period (a period label, date, or date range) or
	 * jurisdiction (such as a named administrative entity). Recommended best
	 * practice is to select a value from a controlled vocabulary (for example,
	 * the Thesaurus of Geographic Names [Getty Thesaurus of Geographic Names,
	 * http://www. getty.edu/research/tools/vocabulary/tgn/]). Where
	 * appropriate, named places or time periods should be used in preference to
	 * numeric identifiers such as sets of co-ordinates or date ranges. Example:
	 * Coverage="17th century", Coverage="Boston, MA". For more complex
	 * applications, see DCMI Period, DCMI Box or DCMI Point.
	 * 
	 * @return
	 */
	public String getCoverage();

	public URI getCoverageAsUri();

	/**
	 * Element Description: An entity primarily responsible for making the
	 * content of the resource. Examples of a Creator include a person, an
	 * organization, or a service. Typically the name of the Creator should be
	 * used to indicate the entity. Examples: Creator="Shakespeare, William",
	 * Creator="Internal Revenue Service. Customer Complaints Unit"
	 * 
	 * @return
	 */
	public String getCreator();

	public String[] getCreatorArray();

	/**
	 * Example: http://en.wikipedia.org/wiki/William_Shakespeare
	 * 
	 * @return
	 */
	public URI getCreatorAsUri();

	public URI[] getCreatorAsUriArray();

	/**
	 * A date associated with an event in the life cycle of the resource.
	 * Typically, Date will be associated with the creation or availability of
	 * the resource. Recommended best practice for encoding the date value is
	 * defined in a profile of ISO 8601 [Date and Time Formats, W3C Note,
	 * http://www.w3.org/TR/NOTE- datetime] and follows the YYYY-MM-DD format.
	 * Example: Date="1998-02-16"
	 * 
	 * @return
	 */
	public String getDate();

	public Calendar getDateAsCalendar();

	/**
	 * An account of the content of the resource. Description may include but is
	 * not limited to: an abstract, table of contents, reference to a graphical
	 * representation of content or a free-text account of the content.
	 * 
	 * @return
	 */
	public String getDescription();

	/**
	 * The size or duration of the resource.
	 * 
	 * @return
	 */
	public String getExtent();

	/**
	 * The physical or digital manifestation of the resource. Typically, Format
	 * may include the media-type or dimensions of the resource. Examples of
	 * dimensions include size and duration. Format may be used to determine the
	 * software, hardware or other equipment needed to display or operate the
	 * resource.Example: Format="image/gif", Format="40 x 512 pixels"
	 * 
	 * @return
	 */
	public String getFormat();

	/**
	 * @see http://www.iana.org/assignments/media-types/index.html
	 * @return
	 */
	public URI getFormatAsUri();

	/**
	 * An unambiguous reference to the resource within a given context.
	 * Recommended best practice is to identify the resource by means of a
	 * string or number conforming to a formal identification system. Examples
	 * of formal identification systems include the Uniform Resource Identifier
	 * (URI) (including the Uniform Resource Locator (URL), the Digital Object
	 * Identifier (DOI) and the International Standard Book Number (ISBN).
	 * 
	 * @return
	 */
	public String getIdentifier();

	public URI getIdentifierAsUri();

	/**
	 * A process, used to engender knowledge, attitudes and skills, that the
	 * resource is designed to support. Instructional Method will typically
	 * include ways of presenting instructional materials or conducting
	 * instructional activities, patterns of learner-to-learner and
	 * learner-to-instructor interactions, and mechanisms by which group and
	 * individual levels of learning are measured. Instructional methods include
	 * all aspects of the instruction and learning processes from planning and
	 * implementation through evaluation and feedback.Example:
	 * InstructionalMethod="Experiential learning"
	 * 
	 * @return
	 */
	public String getInstructionalMethod();

	public Uri getInstructionalMethodAsUri();

	/**
	 * A related resource that references, cites, or otherwise points to the
	 * described resource.
	 * 
	 * @return
	 */
	public DublinCore getIsReferencedByAsRD();

	public DublinCore[] getIsReferencedByAsRDArray();

	public URI getIsReferencedByAsUri();

	public URI[] getIsReferencedByAsUriArray();

	/**
	 * A related resource that supplants, displaces, or supersedes the described
	 * resource.
	 * 
	 * @return
	 */
	public DublinCore getIsReplacedByAsRD();

	public DublinCore[] getIsReplacedByAsRDArray();

	public URI getIsReplacedByAsUri();

	public URI[] getIsReplacedByAsUriArray();

	/**
	 * A related resource that requires the described resource to support its
	 * function, delivery, or coherence.
	 * 
	 * @return
	 */
	public DublinCore getIsRequiredByAsRD();

	public DublinCore[] getIsRequiredByAsRDArray();

	public URI getIsRequiredByAsUri();

	public URI[] getIsRequiredByAsUriArray();

	/**
	 * A related resource of which the described resource is a version, edition,
	 * or adaptation.
	 * 
	 * @return
	 */
	public DublinCore getIsVersionOfAsRD();

	public URI getIsVersionOfAsUri();

	/**
	 * A language of the intellectual content of the resource
	 * 
	 * @return
	 */
	public String getLanguage();

	public URI getLanguageAsUri();

	/**
	 * A statement of any changes in ownership and custody of the resource since
	 * its creation that are significant for its authenticity, integrity and
	 * interpretation. The statement may include a description of any changes
	 * successive custodians made to the resource. Example:
	 * Provenance="This copy once owned by Benjamin Spock."
	 * 
	 * @return
	 */
	public String getProvenance();

	/**
	 * The entity responsible for making the resource available. Examples of a
	 * Publisher include a person, an organization, or a service. Typically, the
	 * name of a Publisher should be used to indicate the entity.
	 * 
	 * @return
	 */
	public String getPublisher();

	public URI getPublisherAsUri();

	/**
	 * A reference to a related resource. Recommended best practice is to
	 * reference the resource by means of a string or number conforming to a
	 * formal identification system. Example: Relation="Shaw's play Pygmalion"
	 * [Relationship described is IsBasedOn]
	 * 
	 * @return
	 */
	public String getRelation();

	/**
	 * Information about rights held in and over the resource. Typically a
	 * Rights element will contain a rights management statement for the
	 * resource, or reference a service providing such information. Rights
	 * information often encompasses Intellectual Property Rights (IPR),
	 * Copyright, and various Property Rights. If the rights element is absent,
	 * no assumptions can be made about the status of these and other rights
	 * with respect to the resource. Example: Rights="Access limited to members"
	 * 
	 * @return
	 */
	public String getRights();

	public URI getRightsAsUri();

	/**
	 * A person or organization owning or managing rights over the resource.
	 * Recommended best practice is to use the URI or name of the Rights Holder
	 * to indicate the entity.Example: RightsHolder="University of Bath"
	 * 
	 * @return
	 */
	public String getRightsHolder();

	public Uri getRightsHolderUri();

	/**
	 * A Reference to a resource from which the present resource is derived. The
	 * present resource may be derived from the Source resource in whole or
	 * part. Recommended best practice is to reference the resource by means of
	 * a string or number conforming to a formal identification system. Example:
	 * Source="Image from page 54 of the 1922 edition of Romeo and Juliet"
	 * 
	 * @return
	 */
	public String getSource();

	/**
	 * The topic of the content of the resource. Typically, a Subject will be
	 * expressed as keywords or key phrases or classification codes that
	 * describe the topic of the resource. Recommended best practice is to
	 * select a value from a controlled vocabulary or formal classification
	 * scheme.
	 * 
	 * @return
	 */
	public String getSubject();

	/**
	 * The name given to the resource. Typically, a Title will be a name by
	 * which the resource is formally known.
	 * 
	 * @return
	 */
	public String getTitle();

	/**
	 * The nature or genre of the content of the resource. Type includes terms
	 * describing general categories, functions, genres, or aggregation levels
	 * for content. Recommended best practice is to select a value from a
	 * controlled vocabulary (for example, the DCMIType vocabulary ). To
	 * describe the physical or digital manifestation of the resource, use the
	 * FORMAT element. Example: Type="Image"
	 * 
	 * @return
	 */
	public String getType();

	/**
	 * The nature or genre of the content of the resource.
	 * 
	 * @see http://dublincore.org/documents/dcmi-type-vocabulary/
	 * @return
	 */

	public URI getTypeAsUri();

}
