package com.flarebyte.cm.com.core.dc;

import java.net.URI;
import java.util.Calendar;

import com.flarebyte.cm.com.core.Concept;
import com.flarebyte.cm.com.core.dc.vocabulary.Term;
import com.flarebyte.cm.lang.TimePeriod;

public interface ValueAccessor {
	/**
	 * Gets the given term as Calendar object. (date)
	 * 
	 * @param term
	 * @return
	 */
	public Calendar getAsCalendar(Term term);

	/**
	 * If a term is a concept, retrieves it.
	 * 
	 * @param term
	 * @return
	 */
	public Concept getAsConcept(Term term);

	public Concept[] getAsConceptArray(Term term);

	/**
	 * Gets the given term as a String.
	 * 
	 * @param term
	 * @return
	 */
	public String getAsString(Term term);

	public String[] getAsStringArray(Term term);

	/**
	 * Returns a TimePeriod
	 * 
	 * @param startTerm
	 * @param endTerm
	 * @return
	 */
	public TimePeriod getAsTimePeriod(Term startTerm, Term endTerm);

	/**
	 * Gets the given term as an Uniform Resource Identifier (URI).
	 * 
	 * @param term
	 * @return
	 */
	public URI getAsUri(Term term);

	public URI[] getAsUriArray(Term term);

}
