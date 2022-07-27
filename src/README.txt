===================================================================
BasicAddonBuilder for OpenOffice.org 
$ Version: 0.6.4 $

Copyright (C) 2006-2008 Paolo Mantovani

Readme
===================================================================

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

(See the included file COPYING)


Abstract
--------
BasicAddonBuilder is an OpenOffice.org extension that allows you to
export a StarBasic library in the OpenOffice.org Extension format, 
ready for deployment. BasicAddonBuilder does not require special 
skills or a deep knowledge of extensions specifications.
A wizard-style dialog will guide you through the process, allowing 
you to define in a graphical way all menu and toolbars that will be
added to the OpenOffice.org user interface in order to launch macros
from your StarBasic library.
The exported extension (AKA UNO package) will be ready to install in 
any PC running OpenOffice.org 2.0 or above, using the Extension manager.
(Menu Tools->Extension manager...)

* See the file INSTALL for installation instructions.


Requirements
------------
OpenOffice.org 2.2 or above
Java Runtime Environment (JRE)


Known issues
------------
* Missing documentation
The following features are not yet supported:
* Dependances management of the generated extension
* Import/export of BasicAddonBuilder projects


Localization
------------
If you are willing to help me localizing the user interface in your 
language, please download the file named "BAB translation pack.zip" in 
the "Localization" folder.
This is a zip archive containig some files that you shoud edit and send 
me via email, so I can integrate them in the next release of BasicAddonBuilder, 
in detail:

* BAB_strings.ods:
This is a Calc document with a single table that contains all the text messages 
that are shown in the BasicAddonBuilder dialogs

The first column contains the default text to translate
Each of the following columns contains a different localization, and the first cell 
of the column must contain the locale ID.
Use the first empty column on the right to put translation in your language and send 
me the file so I can integrate your localization in the next release.
The document contains also some macros. I created these macros in order to convert 
automatically text translations from the Calc document to an xcu file, that is a special
xml file that is read from BasicAddonBuilder for loading localized strings.

You normally don't need to use these macros, so you can ignore them, except if you want
to rebuild BasicAddonBuilder your own (and you really know what you're doing)

* pkg-desc/ folder:
This folder contains text files with the tool-tip text that is shown when you put the 
mouse cursor on the extension name in the extension manager dialog.
Create a new file named pkg-description.<your-lang>
where <your-lang> is a two-letter language code as described in ISO-639-1
The file must contain the translation of the pkg-description.default file, also contained
in the same folder.

* registration/ folder:
This folder contains translations of the LGPL license.
http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html
These are shown when the user performs the installation of BasicAddonBuilder.
If the license is available in your language, please send me a link so I can integrate it. 


Homepage:
---------
Current versions of BasicAddonBuilder for OpenOffice.org are always available at:
http://extensions.services.openoffice.org/project/BasicAddonBuilder
http://www.paolo-mantovani.org/downloads/BasicAddonBuilder/


Acknowledgements:
-----------------
Many thanks to
Ariel Constenla-Haile
Bart Aimar
Bill Hibbert
Cor Nouws
Laurent Godard
Leif Lodahl
Marco Antonioli
Mathias Bauer
Michael Cziebalski
Philippe Allart
Thomas Krumbein
Yves Dutrieux
Derby Russell
and other, who helped me with suggestions, bug reports, testing and translations.


Links:
----------
OpenOffice.org wiki:
http://wiki.services.openoffice.org/wiki/Extensions_Packager

Linux.com article:
http://www.linux.com/feature/120875


Contacting author
-----------------
Please send your suggestions and bug reports to 
Paolo Mantovani <paolomantovani@openoffice.org>. Any feedback is welcome!

