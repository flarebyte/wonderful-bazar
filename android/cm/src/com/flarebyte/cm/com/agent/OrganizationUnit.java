package com.flarebyte.cm.com.agent;

public interface OrganizationUnit extends Organization {
	public OrganizationUnitIterator getChildren();

	public Organization getParent();

	public OrganizationUnit getParentAsOrganizationUnit();

}
