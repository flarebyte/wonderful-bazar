package com.essay.factories;

import java.util.List;

import com.essay.models.Block;
import com.essay.models.Script;

import junit.framework.TestCase;

public class ScriptBuilderTest extends TestCase {
	public void test(){
		ScriptBuilder builder = null;
		String json_script="insert script";
		Script script=builder.buildScript(json_script);
	}
}
