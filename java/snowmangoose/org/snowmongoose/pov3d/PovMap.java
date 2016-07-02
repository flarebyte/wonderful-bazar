/*
 * Created on Jul 12, 2005
 *
 */
package org.snowmongoose.pov3d;


/**
 * @author Oliver Huin
 *
 */
public class PovMap {
	int size = 0;
	int capacity = 16;
	double [] keys = new double[16];
	String [] names = new String[16];
	Object [] arguments = new Object[16];
	 
	 public void put(double key, String name, Object[] arguments){
	 	this.size++;
	 	ensureCapacity(this.size);
	 	this.keys[this.size-1]=key;
	 	this.names[this.size-1]=name;
	 	this.arguments[this.size-1]=arguments;
	 	
	 }
	 
	 public int size() {
	 	return this.size;
	 }
	 
	 public double getKey(int index) {
	 	return keys[index];
	 }
	 
	 public String getName(int index) {
	 	return names[index];
	 }
	 public Object[] getArguments(int index){
	 	return (Object[]) this.arguments[index];
	 }
	 
	 public void ensureCapacity(int size) {
	 	if (size<=capacity) return;
	 	capacity = size +16;
	 	double [] newKeys =  new double[capacity];
		String [] newNames = new String[capacity];
		Object [] newArguments = new Object[capacity];
		System.arraycopy(this.keys,0,newKeys,0,this.keys.length);
		System.arraycopy(this.names,0,newNames,0,this.names.length);
		System.arraycopy(this.arguments,0,newArguments,0,this.arguments.length);
		this.keys=newKeys;
		this.names = newNames;
		this.arguments = newArguments;
	 }
	 
	 
	
	 
}
