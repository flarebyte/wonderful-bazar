package com.flarebyte.cm.com.agent;

/**
 * A Group represents a collection of individual agents (and may itself play the
 * role of a Agent, ie. something that can perform actions).
 * 
 * This concept is intentionally quite broad, covering informal and ad-hoc
 * groups, long-lived communities, organizational groups within a workplace,
 * etc. Some such groups may have associated characteristics which could be
 * captured in RDF (perhaps a homepage, name, mailing list etc.).
 * 
 * @author olivier
 * 
 */
public interface Group extends Agent {
	public AgentIterator get(String... options);
}
