package com.essay.models;

import java.util.Calendar;

public interface ObjValue {
	public Object getValue();
	public ObjType getObjType();
	public ObjUnit getObjUnit();
	/**/
	public ObjValue[] getObjValueArray();
	
	/**/
	public String getObjAsString();
	public Boolean getObjAsBoolean();
	public Integer getObjAsInteger();
	public Long getObjAsLong();
	public Float getObjAsFloat();
	public Calendar getObjAsCalendar();
	/**/
	public String[] getObjAsStringArray();
	public String[] getObjAsBooleanArray();
	public Integer[] getObjAsIntegerArray();
	public Long[] getObjAsLongArray();
	public Float[] getObjAsFloatArray();
	public Calendar[] getObjAsCalendarArray();
}
