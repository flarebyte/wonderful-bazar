package com.flarebyte.cm.com.agent;

import com.flarebyte.cm.lang.TimePeriod;

/**
 * Most countries or states require a company to register with a designated body
 * (e.g., Companies House in the United Kingdom) before they are permitted to
 * start trading.
 * 
 * Each Company has an organizationName that is registered with the designated
 * body. This often includes a postfix that indicates its legal status, for
 * example, PLC (United Kingdom), Inc. (United States), or AG (Germany). You can
 * set the value of the use attribute of OrganizationName to "legal name" to
 * capture this (see Figure 4.10).
 * 
 * In many countries, Companies are allowed to trade under more than one name.
 * You can model these as separate otherOrganizationNames and identify them by
 * setting use to "trading name".
 * 
 * 
 * @author olivier
 * 
 */
public interface OrganizationName {
	public String getName();

	public TimePeriod getValidity();

}
