package com.flarebyte.cm.com.core.dc.dsp;

/**
 * @see http://dublincore.org/architecturewiki/DescriptionSetProfile. The DCMI
 *      Description Set Profile specification describes an information model and
 *      XML expression of a "Description Set Profile" (DSP). The term
 *      description set and the associated concepts used in this specification
 *      are defined as in the DCMI Abstract model.A DSP is a way of describing
 *      structural constraints on a description set. It constrains the resources
 *      that may be described by descriptions in the description set, the
 *      properties that may be used, and the ways a value surrogate may be
 *      given.A DSP can be used for many different purposes, such as: as a
 *      formal representation of the constraints of a Dublin Core Application
 *      Profile, as configuration for databases as configuration for metadata
 *      editing tools etc.A DSP contains the formal syntactic constraints only,
 *      and will need to be combined with human-readable information, usage
 *      guidelines, version management, etc. in order to be used as an
 *      application profile.
 * @author olivier
 * 
 */
public interface DescriptionSetProfile {
	DescriptionTemplateIterator getDescriptionTemplates();
}
