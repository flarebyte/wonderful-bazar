package com.flarebyte.cm.com.core.owls;

/**
 * Composite processes are decomposable into other (non-composite or composite)
 * processes; their decomposition can be specified by using control constructs
 * such as Sequence and If-Then-Else, which are discussed below. Because many of
 * the control constructs have names reminiscent of control structures in
 * programming languages, it is easy to lose sight of a fundamental difference:
 * a composite process is not a behavior a service will do, but a behavior (or
 * set of behaviors) the client can perform by sending and receiving a series of
 * messages. If the composite process has an overall effect, then the client
 * must perform the entire process in order to achieve that effect.
 * 
 * @author olivier
 * 
 */
public interface CompositeProcess {

}
