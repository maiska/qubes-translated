---
lang: bg
layout: doc
permalink: /bg/security/bulletins/
redirect_from:
- /bg/doc/security-bulletins/
- /bg/doc/SecurityBulletins/
- /bg/wiki/SecurityBulletins/
- /bg/trac/wiki/SecurityBulletins/
ref: 8
title: Qubes Security Bulletins
translated: 'yes'
---

Qubes Security Bulletins (QSBs)
===============================

Qubes Security Bulletins (QSBs) are published through the [Qubes Security Pack](/bg/security/pack/).

<table>
  <tr>
    <th title="Anchor Link"><span class="fa fa-link"></span></th>
    <th>Date</th>
    <th>Qubes Security Bulletin</th>
  </tr>
{% for qsb in site.data.qsb reversed %}
  <tr id="{{ qsb.qsb }}">
    <td><a href="#{{ qsb.qsb }}" class="fa fa-link black-icon" title="Anchor link to QSB row: QSB #{{ qsb.qsb }}"></a></td>
    <td>{{ qsb.date }}</td>
    <td><a href="https://github.com/QubesOS/qubes-secpack/blob/master/QSBs/qsb-{{ qsb.qsb }}-{{ qsb.date | date: '%Y' }}.txt">QSB #{{ qsb.qsb }}: {{ qsb.title | truncate: 68 }}</a></td>
  </tr>
{% endfor %}
</table>