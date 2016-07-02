package com.essay.medea;

import junit.framework.TestCase;

import com.essay.medea.impl.AccessApiImpl;
import com.essay.medea.impl.ElementImpl;
import com.essay.medea.impl.FactoryImpl;
import com.essay.medea.impl.JsonConverter;
import com.essay.medea.impl.SubjectAccessImpl;
import com.essay.medea.impl.ValidatorApiImpl;
import com.essay.medea.impl.ValidatorContextImpl;
import com.essay.medea.impl.XmlConverter;
import com.essay.medea.validators.ValidatorsBasic;

public class BuilderTest extends TestCase {
	private final static String GAMMA="Gam-ma7";
	private final static String GAMMA_="gam-ma7";
	public final static String[] TAGS = new String[]{"Alpha","Beta",GAMMA,"Delta","Epsilon","Zeta","Eta","Eta"}; 
	
	private Element createElementV1(Element start,String name,int attrNumber,int childrenNumber,int stop){
		Element r = start.addElement(name);
		if (start.getLevel()>stop) return r;
		
		for (int i=0;i<attrNumber;i++){
			r.setAttribute("k_"+TAGS[i], "v_"+TAGS[i]);
		}
			for (int i=0;i<childrenNumber;i++){
				createElementV1(r,name+"."+TAGS[i],attrNumber,childrenNumber,stop);
			}//end for
		
		return r;
	}
	
	private Element createElementV2(Element start,String name,int attrNumber,int childrenNumber,int stop){
		int level = start.getLevel();
		Element r = start.addElement(name);
		if (level>stop) return r;
		r.setAttribute(TAGS[level].toLowerCase(), "v_"+TAGS[level]);
		r.setAttribute("level", ""+level);
		
		if (true==true) {
			createElementV2(r,TAGS[level],attrNumber,childrenNumber,stop);
		}
		
		return r;
	}

	
	public void testBuildingScript(){
		Element root = FactoryImpl.create().createRoot("script");
		root.getAttributes().put("version", "1.0");
		createElementV2(root,"block",5,4,3);
		
		String json = JsonConverter.create().toString(root);
		System.out.print(json);
		System.out.println("------");
		String xml = XmlConverter.create().toString(root);

	}
	
	public void  testValidatorApi(){
		Element root = FactoryImpl.create().createRoot("script");
		root.getAttributes().put("version", "1.0");
		createElementV2(root,"block",5,4,3);
		
		ValidatorsBasic v = new ValidatorsBasic();
		ValidatorApi valApi = new ValidatorApiImpl();
		valApi.registerElementValidatorValue("/script",v.STRING);
		valApi.registerElementValidatorValue("/script/block",v.STRING);
		valApi.registerElementValidatorValue("/script/block/Alpha",v.STRING);
		valApi.registerElementValidatorValue("/script/block/Alpha/Beta",v.STRING);
		valApi.registerElementValidatorValue("/script/block/Alpha/Beta/"+GAMMA,v.STRING);
		valApi.registerElementValidatorValue("/script/block/Alpha/Beta/"+GAMMA+"/Delta",v.STRING);
		
		valApi.registerValueValidator("/script","version",v.STRING);
		valApi.registerValueValidator("/script/block","alpha",v.STRING);
		valApi.registerValueValidator("/script/block","level",v.INTEGER);
		valApi.registerValueValidator("/script/block/Alpha","beta",v.STRING);
		valApi.registerValueValidator("/script/block/Alpha","level",v.INTEGER);
		valApi.registerValueValidator("/script/block/Alpha/Beta",GAMMA_,v.STRING);
		valApi.registerValueValidator("/script/block/Alpha/Beta","level",v.INTEGER);
		valApi.registerValueValidator("/script/block/Alpha/Beta/"+GAMMA,"delta",v.STRING);
		valApi.registerValueValidator("/script/block/Alpha/Beta/"+GAMMA,"level",v.INTEGER);
		ValidatorContext context = new ValidatorContextImpl();
		
		/* attributes */
		assertTrue(valApi.validate(context, "/script/block/Alpha/Beta","level","12"));
		assertFalse(valApi.validate(context, "/script/block/Alpha/Beta","level","aa"));
		assertFalse(valApi.validate(context, "/script/block/Alpha/Beta","hello","aa"));
		
		/* nodes */
		assertTrue(valApi.validate(context, "/script/block/Alpha/Beta","12"));
		assertTrue(valApi.validate(context, "/script/block/Alpha/Beta","anything"));
		assertTrue(valApi.validate(context, "/script/block/Alpha/Beta",""));
		assertFalse(valApi.validate(context, "/script/block/Alpha/Beta2",""));
		
		/* whole */
		assertTrue(valApi.validate(context, root, true));
	}
	
	public void  testAccessValidatorApi(){
		Element root = FactoryImpl.create().createRoot("script");
		root.getAttributes().put("version", "1.0");
		createElementV2(root,"block",5,4,3);
		String R1="r1";
		String[] R23= new String[] {"r2","r3"};
		
		ValidatorsBasic v = new ValidatorsBasic();
		AccessApi accessApi = new AccessApiImpl();
		accessApi.registerRoleBasedValidator("/script",R1);
		accessApi.registerRoleBasedValidator("/script/block",R1);
		accessApi.registerRoleBasedValidator("/script/block/Alpha",R1);
		accessApi.registerRoleBasedValidator("/script/block/Alpha/Beta",R23);
		accessApi.registerRoleBasedValidator("/script/block/Alpha/Beta/"+GAMMA,R23);
		accessApi.registerRoleBasedValidator("/script/block/Alpha/Beta/"+GAMMA+"/Delta",R23);
		
		accessApi.registerRoleBasedAttributeValidator("/script","version",R1);
		accessApi.registerRoleBasedAttributeValidator("/script/block","alpha",R1);
		accessApi.registerRoleBasedAttributeValidator("/script/block","level",R1);
		accessApi.registerRoleBasedAttributeValidator("/script/block/Alpha","beta",R1);
		accessApi.registerRoleBasedAttributeValidator("/script/block/Alpha","level",R1);
		accessApi.registerRoleBasedAttributeValidator("/script/block/Alpha/Beta",GAMMA_,R23);
		accessApi.registerRoleBasedAttributeValidator("/script/block/Alpha/Beta","level",R23);
		accessApi.registerRoleBasedAttributeValidator("/script/block/Alpha/Beta/"+GAMMA,"delta",R23);
		accessApi.registerRoleBasedAttributeValidator("/script/block/Alpha/Beta/"+GAMMA,"level",R23);
		ValidatorContext context = new ValidatorContextImpl();
		
		SubjectAccess s1 = new SubjectAccessImpl(R1);
		SubjectAccess s2 = new SubjectAccessImpl("r2");
		SubjectAccess s13 = new SubjectAccessImpl("r1","r3");
		/* attributes */
		assertTrue(accessApi.validate(context, "/script/block/Alpha/Beta","level",s2));
		assertFalse(accessApi.validate(context, "/script/block/Alpha/Beta","level",s1));

		/* nodes */
		assertTrue(accessApi.validate(context, "/script/block/Alpha",s1));
		assertFalse(accessApi.validate(context, "/script/block/Alpha",s2));

		/* whole */
		context = new ValidatorContextImpl();
		assertTrue(accessApi.validate(context, root,s13,true));
		assertFalse(accessApi.validate(context,root,s1,true));
		System.out.println("\n\nmessages:"+context.getMessages());

		
		
	}
}
