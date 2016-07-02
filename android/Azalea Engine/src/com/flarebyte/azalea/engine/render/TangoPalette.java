package com.flarebyte.azalea.engine.render;

import android.graphics.Color;
import android.graphics.Paint;

public class TangoPalette {
	public final static int BUTTER1=0;
	public final static int BUTTER2=1;
	public final static int BUTTER3=2;
	public final static int ORANGE1=3;
	public final static int ORANGE2=4;
	public final static int ORANGE3=5;
	public final static int CHOCOLATE1=6;
	public final static int CHOCOLATE2=7;
	public final static int CHOCOLATE3=8;
	public final static int CHAMELEON1=9;
	public final static int CHAMELEON2=10;
	public final static int CHAMELEON3=11;
	public final static int SKY_BLUE1=12;
	public final static int SKY_BLUE2=13;
	public final static int SKY_BLUE3=14;
	public final static int PLUM1=15;
	public final static int PLUM2=16;
	public final static int PLUM3=17;
	public final static int SCARLET_RED1=18;
	public final static int SCARLET_RED2=19;
	public final static int SCARLET_RED3=20;
	public final static int ALUMINIUM1=21;
	public final static int ALUMINIUM2=22;
	public final static int ALUMINIUM3=23;
	public final static int ALUMINIUM4=24;
	public final static int ALUMINIUM5=25;
	public final static int ALUMINIUM6=26;
	
	
	public final static void createPalette(RenderingContext context){
		Paint[] paintPalette = context.createPaintArray(30);
		context.paintPalette=paintPalette;
		classicPaint(paintPalette[BUTTER1],"#fce94f");
		classicPaint(paintPalette[BUTTER2],"#edd400");
		classicPaint(paintPalette[BUTTER3],"#c4a000");

		classicPaint(paintPalette[ORANGE1],"#fcaf3e");
		classicPaint(paintPalette[ORANGE2],"#f57900");
		classicPaint(paintPalette[ORANGE3],"#ce5c00");

		classicPaint(paintPalette[CHOCOLATE1],"#e9b96e");
		classicPaint(paintPalette[CHOCOLATE2],"#c17d11");
		classicPaint(paintPalette[CHOCOLATE3],"#8f5902");

		classicPaint(paintPalette[CHAMELEON1],"#8ae234");
		classicPaint(paintPalette[CHAMELEON2],"#73d216");
		classicPaint(paintPalette[CHAMELEON3],"#4e9a06");

		classicPaint(paintPalette[SKY_BLUE1],"#729fcf");
		classicPaint(paintPalette[SKY_BLUE2],"#3465a4");
		classicPaint(paintPalette[SKY_BLUE3],"#204a87");

		classicPaint(paintPalette[PLUM1],"#ad7fa8");
		classicPaint(paintPalette[PLUM2],"#75507b");
		classicPaint(paintPalette[PLUM3],"#5c3566");

		classicPaint(paintPalette[SCARLET_RED1],"#ef2929");
		classicPaint(paintPalette[SCARLET_RED2],"#cc0000");
		classicPaint(paintPalette[SCARLET_RED3],"#a40000");

		classicPaint(paintPalette[ALUMINIUM1],"#eeeeec");
		classicPaint(paintPalette[ALUMINIUM2],"#d3d7cf");
		classicPaint(paintPalette[ALUMINIUM3],"#babdb6");
		classicPaint(paintPalette[ALUMINIUM4],"#888a85");
		classicPaint(paintPalette[ALUMINIUM5],"#555753");
		classicPaint(paintPalette[ALUMINIUM6],"#2e3436");
	
	}
	
	public final static void classicPaint(Paint paint, String colorString ){
		paint.setDither(true);
		paint.setStyle(Paint.Style.STROKE);
		paint.setStrokeJoin(Paint.Join.ROUND);
		paint.setStrokeCap(Paint.Cap.ROUND);
		paint.setStrokeWidth(1);
		paint.setColor(Color.parseColor(colorString));
	}
}
