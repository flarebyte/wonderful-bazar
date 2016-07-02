package com.flarebyte.cm.trash.admin;

import java.net.URI;

public interface TaskBox extends Box {

	public TaskIterator filter(String... options);

	public Task get(URI taskId, String... options);

}
