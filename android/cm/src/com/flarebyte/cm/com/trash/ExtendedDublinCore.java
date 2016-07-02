package com.flarebyte.cm.com.trash;

import java.net.URI;

import android.net.Uri;

import com.flarebyte.cm.com.core.dc.DublinCore;

public interface ExtendedDublinCore extends DublinCore {
	/**
	 * The method by which items are added to a collection. Recommended best
	 * practice is to use a value from a controlled vocabulary. Example:
	 * AccrualMethod="Deposit"
	 * 
	 * @return
	 */
	public String getAccrualMethod();

	/**
	 * @see http://dublincore.org/groups/collections/accrual-method/
	 * @return
	 */
	public Uri getAccrualMethodAsUri();

	/**
	 * The frequency with which items are added to a collection. Recommended
	 * best practice is to use a value from a controlled vocabulary. Example:
	 * AccrualPeriodicity="Annual"
	 * 
	 * @return
	 */
	public String getAccrualPeriodicity();

	public Uri getAccrualPeriodicityAsUri();

	/**
	 * The policy governing the addition of items to a collection. Recommended
	 * best practice is to use a value from a controlled vocabulary. Example:
	 * AccrualPolicy="Active"
	 * 
	 * @return
	 */
	public String getAccrualPolicy();

	public URI getAccrualPolicyAsUri();

	/**
	 * An alternative name for the resource. The distinction between titles and
	 * alternative titles is application-specific.
	 * 
	 * @return
	 */

	public String getAudienceEducationLevel();

	public String getBibliographicCitation();

	@Override
	public String getConformsTo();

	public String getDateAccepted();

	public String getDateAvailable();

	public String getDateCopyrighted();

	public String getDateCreated();

	public String getDateIssued();

	public String getDateModified();

	public String getDateSubmitted();

	public String getDateValid();

	@Override
	public String getExtent();

	public String getHasFormat();

	public String getHasPart();

	public String getHasVersion();

	public String getIsFormatOf();

	public String getIsPartOf();

	public String getIsReferencedBy();

	public String getIsReplacedBy();

	public String getIsRequiredBy();

	public String getLicense();

	public String getMediator();

	public String getMedium();

	public String getReplaces();

	public String getRequires();

	public String getSpatialCoverage();

	public String getTableOfContents();

	public String getTemporalCoverage();

}
