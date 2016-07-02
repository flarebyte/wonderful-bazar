package com.flarebyte.cm.trash;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.net.URI;
import java.net.URL;
import java.util.Calendar;
import java.util.Currency;
import java.util.Locale;

import android.net.Uri;

public interface Value {
    public BigDecimal getBigDecimal();

    public BigDecimal getBigDecimal(BigDecimal defaultValue);

    public BigDecimal[] getBigDecimalArray();

    public BigDecimal[] getBigDecimalArray(BigDecimal[] defaultValue);

    public BigInteger getBigInteger();

    public BigInteger getBigInteger(BigInteger defaultValue);

    public BigInteger[] getBigIntegerArray();

    public BigInteger[] getBigIntegerArray(BigInteger[] defaultValue);

    public Boolean getBoolean();

    public Boolean getBoolean(Boolean defaultValue);

    public Boolean[] getBooleanArray();

    public Boolean[] getBooleanArray(Boolean[] defaultValue);

    public Byte getByte();

    public Byte getByte(Byte defaultValue);

    public Byte[] getByteArray();

    public Byte[] getByteArray(Byte[] defaultValue);

    public Calendar getCalendar();

    public Calendar getCalendar(Calendar defaultValue);

    public Calendar[] getCalendarArray();

    public Calendar[] getCalendarArray(Calendar[] defaultValue);

    public Character getCharacter();

    public Character getCharacter(Character defaultValue);

    public Character[] getCharacterArray();

    public Character[] getCharacterArray(Character[] defaultValue);

    @SuppressWarnings("rawtypes")
    public Class getDataTypeAsClass();

    public Currency getDataTypeAsCurrency();

    public Uri getDataTypeAsUri();

    public Double getDouble();

    public Double getDouble(Double defaultValue);

    public Double[] getDoubleArray();

    public Double[] getDoubleArray(Double[] defaultValue);

    public Float getFloat();

    public Float getFloat(Float defaultValue);

    public Float[] getFloatArray();

    public Float[] getFloatArray(Float[] defaultValue);

    public IndirectBinary getIndirectBinary();

    public IndirectBinary[] getIndirectBinaryArray();

    public IndirectBitmap getIndirectBitmap();

    public IndirectBitmap[] getIndirectBitmapArray();

    public IndirectString getIndirectString();

    public IndirectString[] getIndirectStringArray();

    public Integer getInteger();

    public Integer getInteger(Integer defaultValue);

    public Integer[] getIntegerArray();

    public Integer[] getIntegerArray(Integer[] defaultValue);

    public Locale getLanguageAsLocale();

    public Long getLong();

    public Long getLong(Long defaultValue);

    public Long[] getLongArray();

    public Long[] getLongArray(Long[] defaultValue);

    public Number getNumber();

    public Number getNumber(Number defaultValue);

    public Number[] getNumberArray();

    public Number[] getNumberArray(Number[] defaultValue);

    public Short getShort();

    public Short getShort(Short defaultValue);

    public Short[] getShortArray();

    public Short[] getShortArray(Short[] defaultValue);

    public String getString();

    public String getString(String defaultValue);

    public String[] getStringArray();

    public String[] getStringArray(String[] defaultValue);

    public Uri getUri();

    public Uri getUri(Uri defaultValue);

    public URI getURI();

    public URI getURI(URI defaultValue);

    public Uri[] getUriArray();

    public Uri[] getUriArray(Uri[] defaultValue);

    public URI[] getURIArray();

    public URI[] getURIArray(URI[] defaultValue);

    public URL getURL();

    public URL getURL(URL defaultValue);

    public URL[] getURLArray();

    public URL[] getURLArray(URL[] defaultValue);

    public Object getValue();

    public Object getValue(Object defaultValue);

    public Value[] getValueArray();

    public Value[] getValueArray(Value[] defaultValue);

}
