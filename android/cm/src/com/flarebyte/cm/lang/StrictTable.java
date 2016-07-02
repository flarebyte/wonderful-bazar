package com.flarebyte.cm.lang;

public interface StrictTable extends Iterable<StrictRecord> {
	public StrictRecord getRecord(int row);
}
