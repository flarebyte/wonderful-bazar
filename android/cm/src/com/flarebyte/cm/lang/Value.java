package com.flarebyte.cm.lang;

import java.util.Calendar;
import java.util.List;

public interface Value {
	public Boolean getBoolean();

	public Boolean getBoolean(boolean defaultValue);

	public Boolean[] getBooleanArray();

	public List<Boolean> getBooleanList();

	public Calendar getCalendar();

	public Calendar[] getCalendarArray();

	public Character getCharacter();

	public Character[] getCharacterArray();

	public Float getFloat();

	public Float[] getFloatArray();

	public Integer getInteger();

	public Integer[] getIntegerArray();

	public Long getLong();

	public Long[] getLongArray();

	public String getString();

	public String[] getStringArray();

	public String getUnit();

	public Object getValue();

}
