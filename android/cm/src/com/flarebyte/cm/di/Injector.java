package com.flarebyte.cm.di;

public interface Injector<S, R> {

	public R get(S services);

}
