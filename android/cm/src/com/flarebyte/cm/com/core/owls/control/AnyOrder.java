package com.flarebyte.cm.com.core.owls.control;

/**
 * Allows the process components (specified as a bag) to be executed in some
 * unspecified order but not concurrently. Execution and completion of all
 * components is required. The execution of processes in an Any-Order construct
 * cannot overlap, i.e. atomic processes cannot be executed concurrently and
 * composite processes cannot be interleaved. All components must be executed.
 * As with Split+Join, completion of all components is required.
 * 
 * @author olivier
 * 
 */
public interface AnyOrder {

}
