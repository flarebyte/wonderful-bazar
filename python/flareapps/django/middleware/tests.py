import unittest
from django.http import HttpRequest
from devicepick import DevicePickMiddleware

class MiddlewareTestCase(unittest.TestCase):
    def request(self, path, http_accept, user_agent):
        request=HttpRequest()        
        request.path=path        
        request.META["HTTP_ACCEPT"]=http_accept
        request.META["HTTP_USER_AGENT"]=user_agent
        return request
    
    def request_useragent(self, user_agent):
        request=self.request("/2007/08/picasso"," application/vnd.oma.drm.message, text/html, image/png, image/jpeg, image/gif, image/x-xbitmap, */*", user_agent)
        return request

class RestyleMiddlewareTestCase(MiddlewareTestCase):
    def setUp(self):
       self.middleware=DevicePickMiddleware()
   
    def testNokia6600(self):
        request=self.request_useragent("Nokia6600/1.0 (4.03.24) SymbianOS/6.1 Series60/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'nokia6600')
    
    def testNokia6230i(self):
        request=self.request_useragent("Nokia6230i/2.0 (03.25) Profile/MIDP-2.0 Configuration/CLDC-1.1")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'nokia6230i')

    def testNokia6630(self):
        request=self.request_useragent("Mozilla/4.0 (compatible; MSIE 5.0; Series60/2.8 Nokia6630/4.06.0 Profile/MIDP-2.0 Configuration/CLDC-1.1)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'nokia6630')

    def testSonyEricssonK310i(self):
        request=self.request_useragent("SonyEricssonK310i/R4DA Java/SEMC-Java/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UNTRUSTED/1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sonyericssonk310i')

    def testSonyEricssonT610(self):
        request=self.request_useragent("SonyEricssonT610/R501 Profile/MIDP-1.0 Configuration/CLDC-1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sonyericssont610')

    def testSonyEricssonK700i(self):
        request=self.request_useragent("SonyEricssonK700i/R2AG SEMC-Browser/4.0.3 Profile/MIDP-2.0 Configuration/CLDC-1.1")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sonyericssonk700i')

    def testSonyEricssonK800iv(self):
        request=self.request_useragent("SonyEricssonK800iv/R1CE Profile/MIDP-2.0 Configuration/CLDC-1.1 UNTRUSTED/1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sonyericssonk800iv')

    def testMotorolaV190(self):
        request=self.request_useragent("MOT-V190/0A.63.12R MIB/2.2.1 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Link/6.3.0.0.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'mot-v190')

    def testMotorolaV600(self):
        request=self.request_useragent("MOT-V600/0B.09.38R MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'mot-v600')

    def testMotorolaE680(self):
        request=self.request_useragent("MOT-E680/R51_G_0F.48.A2P MIB/2.2 Profile/MIDP-2.0 Configuration/CLDC-1.1")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'mot-e680')

    def testSamsung_sghd_600(self):
        request=self.request_useragent("samsung-sgh-d600/1.0 profile/midp-2.0 configuration/cldc-1.1 up.browser/6.2.3.3.c.1.101 (gui) mmp/2.0 untrusted/1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'samsung-sgh-d600')

    def testSamsung_sgh_E340(self):
        request=self.request_useragent("SAMSUNG-SGH-E340/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UP.Browser/6.2.3.3.c.1.101 (GUI) MMP/2.0 UP.Link/6.3.1.13.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'samsung-sgh-e340')

    def testSamsung_sgh_X660(self):
        request=self.request_useragent("SEC-SGHX660 UNTRUSTED/1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sec-sghx660')

    def testSonyEricssonT10(self):
        request=self.request_useragent("SonyEricssonT10/R1BC Java/SEMC-Java/2.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 UNTRUSTED/1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sonyericssont10')

    def testSiemensAL21(self):
        request=self.request_useragent("SIE-AL21/07 Profile/MIDP-1.0 Configuration/CLDC-1.0 UP.Browser/6.1.0.7.3.102 (GUI) MMP/1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sie-al21')

    def testiPhone(self):
        request=self.request_useragent("Mozilla/5.0 (iPhone; U; CPU iPhone OS 2_1 like Mac OS X; nl-nl) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F136 Safari/525.20")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'iphone')

    def testLG_KP500_Orange(self):
        request=self.request_useragent("LG-KP500-Orange/V10d Teleca/WAP2.0 MIDP-2.0/CLDC-1.1,LG-KP500-Orange/V10g Teleca/WAP2.0 MIDP-2.0/CLDC-1.1")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'lg-kp500-orange')

    def testLG_KP500_Teleca(self):
        request=self.request_useragent("LG-KP500 Teleca/WAP2.0 MIDP-2.0/CLDC-1.1")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'lg-kp500')

    def testAmaya(self):
        request=self.request_useragent("amaya/9.51 libwww/5.4.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'amaya')

    #http://www.avantbrowser.com/    
    def testAvantBrowser(self):
        request=self.request_useragent("Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Avant Browser [avantbrowser.com]; Hotbar 4.4.5.0)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'avant browser')

    #http://bluefish.openoffice.nl/
    def testBluefish(self):
        request=self.request_useragent("bluefish 0.6 HTML editor")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'bluefish')

    #http://caminobrowser.org/    
    def testCamino(self):
        request=self.request_useragent("Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en; rv:1.8.1.14) Gecko/20080409 Camino/1.6 (like Firefox/2.0.0.14)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'camino')

    def testModel(self):
        request=self.request_useragent("")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, '')

    #http://www.google.com/chrome    
    def testChrome(self):
        request=self.request_useragent("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.36 Safari/525.19")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'chrome')

    #http://curl.haxx.se/
    def testModel(self):
        request=self.request_useragent("curl/7.7.2 (powerpc-apple-darwin6.0) libcurl 7.7.2 (OpenSSL 0.9.6b)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'curl')

    #http://www.mozilla.com/en-US/firefox/firefox.html
    def testFirefox(self):
        request=self.request_useragent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8) Gecko/20051111 Firefox/1.5 BAVM/1.0.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'firefox/1')

    #Mozilla Fennec (mobile Firefox) on Nokia N800   
    def testModel(self):
        request=self.request_useragent("Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'fennec')

    #http://www.flock.com/    
    def testFlock(self):
        request=self.request_useragent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.3) Gecko/2008100716 Firefox/3.0.3 Flock/2.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'flock')

    #http://galeon.sourceforge.net/
    def testGaleon(self):
        request=self.request_useragent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.13) Gecko/20080208 Galeon/2.0.4 (2008.1) Firefox/2.0.0.13")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'galeon')

    #http://kmeleon.sourceforge.net/
    def testKMeleon(self):
        request=self.request_useragent("Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1.4) Gecko/20070511 K-Meleon/1.1")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'k-meleon')

    #http://www.konqueror.org/    
    def testKonqueror(self):
        request=self.request_useragent("Mozilla/5.0 (compatible; Konqueror/4.0; Linux) KHTML/4.0.5 (like Gecko)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'khtml/4')

    #http://lynx.browser.org/
    def testLynx(self):
        request=self.request_useragent("Lynx/2.8.5dev.16 libwww-FM/2.14 SSL-MM/1.4.1 OpenSSL/0.9.6b")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'lynx')

    #http://www.maxthon.com/
    def testMaxthon(self):
        request=self.request_useragent("Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; Maxthon; .NET CLR 1.1.4322)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'maxthon')

    #http://archive.ncsa.uiuc.edu/mosaic.html
    def testMosaic(self):
        request=self.request_useragent("PATHWORKS Mosaic/1.0 libwww/2.15_Spyglass")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'mosaic')

    #http://www.mozilla.com/en-US/
    def testSeaMonkey(self):
        request=self.request_useragent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1b1pre) Gecko/20080915000512 SeaMonkey/2.0a1pre")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'seamonkey')

    #http://www.microsoft.com/windows/internet-explorer/default.aspx
    def testMSIE8(self):
        request=self.request_useragent("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'msie 8')

    #http://browser.netscape.com/
    def testNavigator(self):
        request=self.request_useragent("Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'navigator')

    #http://www.omnigroup.com/applications/omniweb/
    def testOmniWeb(self):
        request=self.request_useragent("Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US) AppleWebKit/525.18 (KHTML, like Gecko, Safari/525.20) OmniWeb/v622.3.0.105198")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'omniweb')

    #http://www.opera.com/
    def testOperaMini(self):
        request=self.request_useragent("Opera/9.60 (J2ME/MIDP; Opera Mini/4.1.11320/608; U; en) Presto/2.2.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'opera mini')

    #http://www.apple.com/safari/
    def testSafari(self):
        request=self.request_useragent("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Version/3.1.2 Safari/525.21")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'safari/5')

    #http://getsongbird.com/
    def testSongbird(self):
        request=self.request_useragent("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1) Gecko/2008072921 Songbird/0.7.0 (20080819112708)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'songbird')

    #http://directory.fsf.org/project/wget/
    def testWget(self):
        request=self.request_useragent("Wget/1.8.1")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'wget')

    #http://www.avantgo.com/frontdoor/
    def testAvantGo(self):
        request=self.request_useragent("Mozilla/5.0 (Danger hiptop 3.4; U; AvantGo 3.2)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'avantgo 3.2')


    def testDoCoMo(self):
        request=self.request_useragent("DoCoMo/1.0/P502i/c10 (Google CHTML Proxy/1.0)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'docomo')

    def testPLink(self):
        request=self.request_useragent("Mozilla/4.0 (compatible; MSIE 5.0; PalmOS) PLink 2.56b")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'plink 2.56b')

    def testNetFront(self):
        request=self.request_useragent("Mozilla/5.0 (PDA; NF35WMPRO/1.0; like Gecko) NetFront/3.5")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'netfront')

    def testXiino(self):
        request=self.request_useragent("Xiino/1.0.9E [en] (v. 4.1; 153x130; g4)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'xiino')

    def testiPhone(self):
        request=self.request_useragent("Mozilla/5.0 (iPhone; U; CPU like Mac OS X; en) AppleWebKit/420+ (KHTML, like Gecko) Version/3.0 Mobile/1A543a Safari/419.3")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'iphone')

    def testBlackBerry8330(self):
        request=self.request_useragent("BlackBerry8330/4.3.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/105")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'blackberry8330')

    def testBlackBerry7130e(self):
        request=self.request_useragent("BlackBerry7130e/4.1.0 Profile/MIDP-2.0 Configuration/CLDC-1.1 VendorID/104")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'blackberry7130e')

    def testHP_iPAQ_h6300(self):
        request=self.request_useragent("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320; HP iPAQ h6300)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'hp ipaq h6300')

    def testHTCP3300(self):
        request=self.request_useragent("HTCP3300-Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'htcp3300-mozilla')

    def testLGE_MX380(self):
        request=self.request_useragent("LGE-MX380/1.0 UP.Browser/6.2.3.9 (GUI) MMP/2.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'lge-mx380')

    def testMotorola_a_lc(self):
        request=self.request_useragent("MOT-A-1C/01.01 UP.Browser/7.0.0.2.c.1.104 (GUI) MMP/2.0 UP.Link/5.1.2.16 ")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'mot-a-1c')

    def testNintendoWii(self):
        request=self.request_useragent("Opera/9.30 (Nintendo Wii; U; ; 2047-7; en)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'nintendo wii')

    def testPalm500v(self):
        request=self.request_useragent("Mozilla/4.0 (compatible; MSIE 6.0; Windows CE; IEMobile 6.12) /Palm 500v/v0100 UP.Link/6.3.1.13.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'palm 500v')

    def testPalmTreo500v(self):
        request=self.request_useragent("Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; PalmSource/Palm-D062; Blazer/4.5) 16;320x320")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'palm-d062')

    def testPocketPC(self):
        request=self.request_useragent("Mozilla/4.0 (compatible; MSIE 4.01; Windows CE; PPC; 240x320)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'msie 4')

    def testSAGEM_myX5_2(self):
        request=self.request_useragent("SAGEM-myX5-2/1.0 Profile/MIDP-2.0 Configuration/CLDC-1.0 UP.Browser/6.2.2.6.d.3 (GUI) MMP/1.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sagem-myx5-2')

    def testSamsung_sgh_e900(self):
        request=self.request_useragent("samsung sgh-e900 /netfront 3.2")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'samsung sgh-e900')

    def testSEC_SGHE600(self):
        request=self.request_useragent("SEC-SGHE600 UP.Link/6.3.1.12.0")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sec-sghe600')

    def testSIE_ME45(self):
        request=self.request_useragent("SIE-ME45/05 UP.Browser/5.0.1.1.102 (GUI)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sie-me45')

    def testSonyEricssonW850i(self):
        request=self.request_useragent("SonyEricssonW850i/R1ED Browser/NetFront/3.3 Profile/MIDP-2.0 Configuration/CLDC-1.1 ")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'sonyericssonw850i')

    def testPLAYSTATION3(self):
        request=self.request_useragent("Mozilla/5.0 (PLAYSTATION 3; 1.00)")
        r=self.middleware.process_request(request)        
        self.assertEquals(request.device_agent, 'playstation 3')
    
    def notestSerialize(self):
        r=self.middleware.serializeBrowserProfile()        
        print r

    

if __name__ == '__main__':
    unittest.main()

