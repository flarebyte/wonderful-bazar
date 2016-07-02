= Visual design guideline =

== Color palette ==

 * Each website must have a well defined color palette. Several websites can share the same color palette.
 * The selected palette should have a maximum of 20 colors. Start with a single color.
 * Select the colors from the X11 colors or the web-safe colors [http://en.wikipedia.org/wiki/Web_colors web colors].
 * All colour combinations MUST have brightness contrast >=125 and color contrast >=400 (Hewlett Packard colour contrast standard). You can check the color contrast between two colors using [http://www.hp.com/hpinfo/abouthp/accessibility/webaccessibility/color_tool.html Hewlett Packard's Color Contrast tool].
 * You MUST NOT use any colour combinations which will be indistinguishable by people with a form of colour-blindness [http://www.vischeck.com/vischeck/vischeckURL.php colour-blindness]
 * It is usually recommended to include a gradient of colors in the palette. Ex: aluminium colors in the Tango palette.
 * What the colors say about the site ?
 * How should visitors feel on the site ?

Ex: [http://tango.freedesktop.org/Tango_Icon_Theme_Guidelines Tango icon theme]

Tools:
 * [http://www.degraeve.com/color-palette/ Get a color palette that matches an image]
 * [http://www.netfront.fr/Services/rgb2pantone/ RGB to Pantone conversion]
 * [http://www.goffgrafix.com/pantone-rgb-100.php Pantone to RGB conversion]
 * [http://www.pantone.com/pages/pantone/colorfinder.aspx Check a Pantone colour]
 * [http://sobac.com/sobac/tangocolors.htm Html Tango colours]

== Fonts ==

Each website must have a well defined list of fonts known as '''favorite fonts'''.

=== Fonts for images ===

When selecting fonts for jpeg, gif, svg, etc.. images:
 * You can use any font (but preferably one of the favorite fonts). Make sure that the copyright of the font is compatible with the intended use. Save to the source repository the new font, copyright, and a readme file listing the applications/websites using this font.


=== Fonts for web pages ===


 * Fonts MUST be defined in the style sheets.
 * Every font-family CSS property MUST rely on a font stack instead of a single font.
 * A typical user may be using Windows, MacOS, Linux or a mobile browser.
 * You MUST include at least one safe font in your font stack as a last resort.
 * The most safe option is to use the generic font families as defined by the CSS: sans-serif, serif, monospace, cursive and fantasy. Sans-serif is regularly specified in CSS as the default as it is more easily readable on screens.
 * Considered as web safe: arial, arial black, comic sans ms, courier, courier new, georgia, helvetica, impact, palatino, times new roman, trebuchet ms, verdana .
 * Font sizes MUST NOT be specified in units that are not resizeable in all browsers, except for print stylesheets. You SHOULD use em or % for sizing [http://pxtoem.com/ PX to EM conversion].
 * Font-size SHOULD NOT be specified using keywords (e.g x-small) as they are rendered inconsistently across browsers.



Tools:
 * [http://www.typetester.org/ Comparison of the fonts for the screen]
 * [http://media.24ways.org/2007/17/fontmatrix.html Matrix of fonts]
 * [http://dustinbrewer.com/fonts-on-the-web-and-a-list-of-web-safe-fonts/ Web safe fonts]

== Icons ==

 * Icons MUST be created, maintained, and saved using [http://en.wikipedia.org/wiki/Scalable_Vector_Graphics Scalable Vector Graphics (SVG)]. However, many applications will use the exported version in jpeg, png, gif ...of these SVG images.
 * Common Filenaming  [http://standards.freedesktop.org/icon-naming-spec/icon-naming-spec-latest.html icons naming conventions]
 * All icons MUST have an easily distinguishable silhouette.
 * All icons are lit from above, with the light source slightly to the left.
 * (1) All icons are stroked with a thin outline (1 pixel for 48×48 pixel). The color of the outline is a dark variant of the key color of the icon.
 * (2) Use highlights to create a second inner outline of the object.
 * (3) Use glossy reflection on objects that have a reflective surface in real life (plastic, glass, some metal, et cetera).


[[Image(http://tango.freedesktop.org/images/0/0e/Unify-icon-elements.png)]]


There are four major icon sizes, an icon theme must address:
 * Large: 48×48 pixels.
 * Medium: 32x32 pixels
 * Small: 22x22 pixels.
 * Extra Small: 16×16 pixels.

Tools:
 * [http://www.inkscape.org/ inkscape]
 * [http://www.brandsoftheworld.com/ directory of logos]
 * [http://icons.mysitemyway.com/ Royalty Free Icons]

== Logos ==

Properties of a good logo:
 * A customer should be able to '''describe''' it with words and to '''remember''' it easily. In other words, you have to keep it simple.
 * The logo has to be effective without color. In other words, think shape first and leave the choice of colors for the very end.
 * The logo should be scalable, and still recognizable when printed on a pen or pin badge.
 * Dimensions:
  * The logo alone should fit in a square.
  * The logo + website.com name should able to be printed on a plaque 200mm x 400 mm (ratio 2:1) - for example -
  * The logo + website.com name should able to be printed on a 4.4cm x 1.61 (ratio 2.7:1) - for example -
 * Choose only 2 or 3 colors. Keep in mind that we may have to be able to print it on white,black or transparent backgrounds. In some cases, we may want to choose a color scheme for white backgrounds and a different one for black backgrounds.


=== Notes concerning flarebyte.com logo ===

 * The logo represents a sun with a flare. The flare looks like a F.
 * The logo is still recognizable on a white,black or transparent background.


== Layout ==

 * Layout should help to create a general feeling.
 * Layout should help to increase readability.

== Usability ==

 * Things that look the same should act the same.
 * Things that look different should act different.
 * Error messages should actually mean something to the user and tell the user how to fix the problem.
 * Every action should have a reaction.
 * Everyone makes mistakes, so every mistake should be fixable. Support undo and redo. Users often choose system functions by mistake ...
 * Consistency, consistency, consistency.
 * Minimize the need for a mighty memory.
 * Keep it simple.
 * The best journey is the one with fewest steps.
 * You should always know how to find out what to do next.
 * Allow users to tailor frequent actions.
 * Aesthetic and minimalist design: Dialogues should not contain information which is irrelevant or rarely needed.
 * Help and documentation: Even though it is better if the system can be used without documentation, it may be necessary to provide help and documentation. Any such information should be easy to search, focused on the user's task, list concrete steps to be carried out, and not be too large.

== Accessibility ==

Web accessibility refers to the practice of making websites usable by people of all abilities and disabilities.

 * Text Alternatives: Provide text alternatives for any non-text content so that it can be changed into other forms people need, such as large print, braille, speech, symbols or simpler language.
 * Time-based Media: Provide alternatives for time-based media.
 * Adaptable: Create content that can be presented in different ways (for example simpler layout) without losing information or structure.
 * Distinguishable: Make it easier for users to see and hear content including separating foreground from background.
 * Keyboard Accessible: Make all functionality available from a keyboard.
 * Enough Time: Provide users enough time to read and use content.
 * Seizures: Do not design content in a way that is known to cause seizures (Web pages MUST NOT contain anything that flashes more than three times in any one second period).
 * Navigable: Provide ways to help users navigate, find content, and determine where they are.
 * Predictable: Make Web pages appear and operate in predictable ways.
 * Input Assistance: Help users avoid and correct mistakes.
 * Compatible: Maximize compatibility with current and future user agents, including assistive technologies.

[http://www.w3.org/TR/WCAG20/ Web Content Accessibility Guidelines (WCAG) 2.0]

== CSS ==

 * The presentation of any page employing CSS MUST degrade gracefully (re: Browser Support) in browsers that do not support, or provide only partial support for style sheets.
 * Any usage of CSS MUST be valid according to a published W3C recommendation:
 * The file size of attached style sheets SHOULD be kept as low as possible. For the purpose of page weight calculations, all attached style sheet files will be taken into account.
 * Inline styles SHOULD NOT be used, as it is generally preferable to define styles in an attached style sheet.
 * Colours SHOULD be specified using hex pair RGB values, such as #336699, or short Hex values, such as #369.
 * Margins, borders and padding: negative values MUST NOT be used to move content outside the visible body of the page, because this would obscure the page meaning if images were turned off (image replacement).
 * Style sheets MUST NOT be used to modify the appearance of the toolbar or global site elements.
 * You MUST validate CSS using the [http://jigsaw.w3.org/css-validator/ W3C CSS Validation Service]

== Browser Devices ==

=== General considerations ===

==== Ratio ====
Most screen displays respect a ratio close to the aesthetic [http://en.wikipedia.org/wiki/Golden_ratio Greek golden ratio]: approximately 1.618034. This golden ratio can also be approximated to 4/3 or even better to 16/9.

==== Width ====

In a curious way, the width of many screens seems to satisfy the 10x(2^n^) equation.
Examples: 320, 640, 1280.

==== Usable Display ====

The usable screen display is smaller than the physical mobile screen display because a small portion of the screen has to be used by the browser. Therefore we recommend to use the [FlarebyteDimension flarebyte width] which satisfies the (3^2^)x(2^n^) equation.
Examples:  288, 576, 1152.


=== Desktop ===

 * You MUST validate web pages using:
     * [http://validator.w3.org/ W3C Markup Validation Service]

|| Name || Resolution ||
|| Netbook || 800 ||
|| Desktop || 1024 ||
|| Panorama || 1280+ ||

Tools:
 * [http://www.anybrowser.org/campaign/abdesign.html]

=== Mobile devices ===

In fact, it's entirely possible to group many devices with similar screen widths together and to end up with five distinct device screen width groupings:

|| Name || Resolution ||
|| tiny || 84, 96, 101, 128, 130, 132 ||
|| small || 160, 176 ||
|| medium || 208, 220, 240 ||
|| large || 320, 360, 480+ ||


[[Image(http://mobiforge.com/files/screensizes.png)]]

 * You MUST validate mobile web pages using:
     * [http://validator.w3.org/mobile/ W3C mobileOK Checker]
     * [http://ready.mobi/launch.jsp?locale=en_EN mobiReady testing tool]
     * [http://www.mobileawesomeness.com/ Mobile awesomeness]

[http://www.bbc.co.uk/guidelines/futuremedia/technical/css.shtml BBC CSS guidelines]
[http://codebeautifier.com/ CSS Formatter and Optimiser]
