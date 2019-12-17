---
layout: doc
title: Anti Evil Maid (AEM)
permalink: /de/doc/anti-evil-maid/
lang: de
ref: 131
redirect_from:
- /en/doc/anti-evil-maid/
- /doc/AntiEvilMaid/
- /wiki/AntiEvilMaid/
---

Installing and Using Anti Evil Maid (AEM) with Qubes OS
=======================================================

Background
----------

Please read [this blog article](https://blog.invisiblethings.org/2011/09/07/anti-evil-maid.html).

Requirements
----------

The current package requires a TPM 1.2 interface and a working Intel TXT engine.
If you cleaned your Intel Management Engine with e.g. [me_cleaner](https://github.com/corna/me_cleaner)
while installing [CoreBoot](https://www.coreboot.org/) then you are out of luck.
For now you have to choose between cleaning your BIOS and deploying Anti Evil Maid.

[Diskussion](https://groups.google.com/d/msg/qubes-users/sEmZfOZqYXM/j5rHeex1BAAJ)

Installing
----------

In Dom0 Anti-Evil-Maid installieren:

~~~
sudo qubes-dom0-update anti-evil-maid
~~~

Weitere Informationen zur Konfiguration sind in der [README] nachzulesen: (https://github.com/QubesOS/qubes-antievilmaid/blob/master/anti-evil-maid/README)

Security Considerations
-----------------------

Die [Qubes Sicherheitsrichtlinien](/de/doc/security-guidelines/) sehen vor, dass USB-Geräte zu keiner Zeit direkt mit der dom0 verbunden werden dürfen, da dies zu einer Kompromittierung des kompletten Systems führen kann. Jedoch ist es in den Voreinstellungen zur Installation und Nutzung von AEM erforderlich, ein USB-Gerät direkt mit der dom0 zu verbinden (siehe [Massenspeichergerät](https://en.wikipedia.org/wiki/USB_mass_storage_device_class)). (Alternativ kann AEM auf eine interne Festplatte installiert werden. Allerdings birgt dies enorme Sicherheitsrisiken, wie [hier] nachzulesen ist: (http://theinvisiblethings.blogspot.com/2011/09/anti-evil-maid.html).)Aus diesem Grund sind wir bei der Beachtung der Sicherheitsvorkehrungen ebenso auf die Selbstständigkeit jedes einzelnen Qubes-Benutzer angewiesen, denn jeder muss selbst entscheiden, wie einerseits dom0 vor potenziellen bösartigen USB-Sticks und andererseits das System vor Evil Maid-Angriffen zu schützen ist. Wenn man die praktische Durchführbarkeit von Angriffen wie z.B. bei [BadUSB](https://srlabs.de/badusb/) näher betrachtet und sich bewusst macht, dass Regierungen im alltäglichen Geschäft Hardware-Backdoors einsetzen, fällt diese Entscheidung nicht unbedingt leicht. Neue, abgefertigte USB-Sticks können von vornherein nicht als "sicher" angesehen werden (d.h., dass sich keine bösartige Mikrocontroller-Firmware darauf befindet). Deshalb ist es jedem einzelnen Qubes-Benutzer überlassen, das Risiko jedes potenziellen Angriffs auf sein oder ihr Sicherheitsmodell abzuwägen.

For example, a user who frequently travels with a Qubes laptop holding sensitive data may be at a much higher risk of Evil Maid attacks than a home user with a stationary Qubes desktop. If the frequent traveler judges her risk of an Evil Maid attack to be higher than the risk of a malicious USB device, she might reasonably opt to install and use AEM. On the other hand, the home user might deem the probability of an Evil Maid attack occurring in her own home to be so low that there is a higher probability that any USB drive she purchases is already compromised, in which case she might reasonably opt never to attach any USB devices directly to dom0. (In either case, users can--and should--secure dom0 against further USB-related attacks through the use of a [USBVM](/de/doc/security-guidelines/#creating-and-using-a-usbvm).)

Für weitere Informationen empfehlen wir, [diesen Leitfaden] durchzulesen: (https://groups.google.com/d/msg/qubes-devel/EBc4to5IBdg/n1hfsHSfbqsJ).

Known issues
------------

-   USB 3.0 isn't supported yet
-   [AEM is not compatible with having an SSD cache](https://groups.google.com/d/msgid/qubes-users/70021590-fb3a-4f95-9ce5-4b340530ddbf%40petaramesh.org)
