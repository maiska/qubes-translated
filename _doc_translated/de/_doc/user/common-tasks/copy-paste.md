---
layout: doc
title: Copy and Paste
permalink: /de/doc/copy-paste/
lang: de
ref: 96
redirect_from:
- /en/doc/copy-paste/
- /doc/CopyPaste/
- /wiki/CopyPaste/
---

Copy and Paste between domains
==============================

Qubes unterstützt vollständig ein sicheres Kopieren-und-Einfügen-Verfahren zwischen Domains. Um die Zwischenablage von einer Domain A zu einer Domain B zu kopieren, führen Sie bitte folgende Schritte aus:

1.  Click on the application window in domain A where you have selected text for copying. Then use the *app-specific* hot-key (or menu option) to copy this into domain's local clipboard (in other words: do the copy operation as usual, in most cases by pressing Ctrl-C).
2.  Then (when the app in domain A is still in focus) press Ctrl-Shift-C magic hot-key. This will tell Qubes that we want to select this domain's clipboard for *global copy* between domains.
3.  Now select the destination app, running in domain B, and press Ctrl-Shift-V, another magic hot-key that will tell Qubes to make the clipboard marked in the previous step available to apps running in domain B. This step is necessary because it ensures that only domain B will get access to the clipboard copied from domain A, and not any other domain that might be running in the system.
4.  Now, in the destination app use the app-specific key combination (usually Ctrl-V) for pasting the clipboard.

Beachten Sie, dass die globale Zwischenablage nach Schritt \#3 gelöscht wird, um ein unabsichtliches Leck in eine andere Domain zu verhindern, falls der Benutzer später Strg+Umschalt+V aus Versehen drücken sollte.

Dieser 4-schrittige Prozess könnte kompliziert aussehen, aber nach ein wenig Übung ist er wirklich sehr einfach und schnell. Gleichzeitig gibt er dem Benutzer die volle Kontrolle darüber, wer Zugriff auf die Zwischenablage hat.

Beachten Sie, dass nur einfaches Kopieren/Einfügen von reinem Text zwischen AppVMs unterstützt wird. Dies wird ein wenig detaillierter in [dieser Nachricht](https://groups.google.com/group/qubes-devel/msg/57fe6695eb8ec8cd) diskutiert.

On Copy/Paste Security
----------------------

The scheme is *secure* because it doesn't allow other VMs to steal the content of the clipboard. However, one should keep in mind that performing a copy and paste operation from *less trusted* to *more trusted* domain can always be potentially insecure, because the data that we insert might potentially try to exploit some hypothetical bug in the destination VM (e.g. the seemingly innocent link that we copy from untrusted domain, might turn out to be, in fact, a large buffer of junk that, when pasted into the destination VM's word processor could exploit a hypothetical bug in the undo buffer). This is a general problem and applies to any data transfer between *less trusted to more trusted* domains. It even applies to copying files between physically separate machines (air-gapped) systems. So, you should always copy clipboard and data only from *more trusted* to *less trusted* domains.

See also [this article](https://blog.invisiblethings.org/2011/03/13/partitioning-my-digital-life-into.html) for more information on this topic, and some ideas of how we might solve this problem in some future version of Qubes.

Und [diese Nachricht](https://groups.google.com/group/qubes-devel/msg/48b4b532cee06e01) von qubes-devel.

Copy/Paste between dom0 and other domains
-----------------------------------------

See ["Copying from (and to) dom0"](/de/doc/copy-from-dom0/).

Clipboard automatic policy enforcement
--------------------------------------

The Qubes clipboard [RPC policy] is configurable in:

~~~
/etc/qubes-rpc/policy/qubes.ClipboardPaste
~~~

Sie können dieses Regelwerk konfigurieren, um Benutzerfehler zu verhindern. Wenn Sie sich zum Beispiel sicher sind, dass Sie niemals *in* Ihre »Schatzkammer«-VM etwas einzufügen wünschen (und es wird sehr empfohlen, es nicht zu tun), dann sollten Sie das Regelwerk wie folgt bearbeiten:

~~~
$anyvm  vault   deny
$anyvm  $anyvm  ask
~~~

Shortcut Configuration
----------------------

Die Kopieren/Einfügen-Tastenkürzel sind konfigurierbar in:

~~~
/etc/qubes/guid.conf
~~~

VMs müssen neugestartet werden, damit Änderungen in `/etc/qubes/guid.conf` wirksam werden.


[RPC policy]: /de/doc/rpc-policy/

