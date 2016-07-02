package com.essay.factories;

import java.io.InputStream;

import com.essay.models.Script;

public interface ScriptBuilder {
	public Script buildScript(String script);
	public Script buildScript(InputStream is);
}
