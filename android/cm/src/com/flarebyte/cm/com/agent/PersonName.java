package com.flarebyte.cm.com.agent;

import com.flarebyte.cm.lang.TimePeriod;

/**
 * The PersonName represents a name for a Person
 * 
 * @author olivier
 * 
 */
public interface PersonName {

	/**
	 * The last name in Western countries—this is the only mandatory component
	 * of the name and the only one used if a Person has but a single name
	 * 
	 * @return
	 */
	public String getFamilyName();

	/**
	 * The first name in Western countries—this can include hyphenated names
	 * (e.g., Jean-Paul) and names including more than one word (e.g., Kwai Lin)
	 * 
	 * @return
	 */
	public String getGivenName();

	/**
	 * Any name other than the given name and the family name
	 * 
	 * @return
	 */
	public String[] getMiddleNames();

	/**
	 * A name that the person is commonly known by—this is often a contraction
	 * of one of the other names (e.g., "Jim" is short for "James," "Bill" is
	 * short for "William")
	 * 
	 * @return
	 */
	public String getPreferredName();

	/**
	 * An honorific such as Mr., Miss, Dr., Rev., and so on.
	 * 
	 * @return
	 */
	public String[] getPrefixes();

	/**
	 * Each suffix may be:
	 * 
	 * A generational label (e.g., Jr., III)
	 * 
	 * A qualification (e.g., BSc., bachelor of sciences; Ph.D., doctor of
	 * philosophy)
	 * 
	 * A title (e.g., FRSC, Fellow of the Royal Society of Chemistry; Bart,
	 * Baronet; KG, Knight of the Garter)
	 * 
	 * @return
	 */
	public String getSuffix();

	/**
	 * The period when the person name is valid
	 * 
	 * @return
	 */
	public TimePeriod getValidity();

}
