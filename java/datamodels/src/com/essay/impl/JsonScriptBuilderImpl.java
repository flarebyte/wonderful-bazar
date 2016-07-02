package com.essay.impl;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;
import java.util.Map;

import org.codehaus.jackson.JsonFactory;
import org.codehaus.jackson.JsonParseException;
import org.codehaus.jackson.JsonParser;
import org.codehaus.jackson.JsonToken;
import org.codehaus.jackson.map.JsonMappingException;
import org.codehaus.jackson.map.ObjectMapper;

import com.essay.factories.ScriptBuilder;
import com.essay.factories.ScriptFactory;
import com.essay.models.Script;

public class JsonScriptBuilderImpl implements ScriptBuilder {
	ScriptFactory scriptFactory=null;
	@Override
	public Script buildScript(String script) {
		ObjectMapper mapper = new ObjectMapper();
		try {
			List<Object> userData = mapper.readValue(script, List.class);
		} catch (JsonParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (JsonMappingException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return null;
	}//end method
	@Override
	public Script buildScript(InputStream is) {
		// TODO Auto-generated method stub
		return null;
	}

}
