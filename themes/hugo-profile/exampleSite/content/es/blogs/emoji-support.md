---
title: "Soporte de Emoji"
date: 2021-04-03T22:53:58+05:30
draft: false
github_link: "https://github.com/gurusabarish/hugo-profile"
author: "Gurusabarish"
tags:
  - Soporte de Emoji
  - Muestra
  - ejemplo
image: /images/post.jpg
description: ""
toc: 
---

Los emoji se pueden habilitar en un proyecto Hugo de varias maneras. :zap:

## Soporte de Emoji

La función [emojify](https://gohugo.io/functions/emojify/) se puede llamar directamente en las plantillas o [Shortcodes en línea](https://gohugo.io/templates/shortcode-templates/#inline-shortcodes).

Para habilitar emoji globalmente, establece ```enableEmoji``` en ```true``` en la [configuración](https://gohugo.io/getting-started/configuration/) de tu sitio y luego puedes escribir códigos abreviados de emoji directamente en los archivos de contenido; por ejemplo:

La [Hoja de trucos de Emoji](http://www.emoji-cheat-sheet.com/) es una referencia útil para los códigos abreviados de emoji.

<hr>

**N.B.** Los pasos anteriores habilitan los caracteres y secuencias de emoji del Estándar Unicode en Hugo, sin embargo, la representación de estos glifos depende del navegador y la plataforma. Para estilizar los emoji, puedes usar una fuente de emoji de terceros o una pila de fuentes; por ejemplo:

```
.emoji {
  font-family: Apple Color Emoji, Segoe UI Emoji, NotoColorEmoji, Segoe UI Symbol, Android Emoji, EmojiSymbols;
}
```
