---
title: "Support des Emoji"
date: 2021-04-03T22:53:58+05:30
draft: false
github_link: "https://github.com/gurusabarish/hugo-profile"
author: "Gurusabarish"
tags:
  - Support des Emoji
  - Exemple
  - échantillon
image: /images/post.jpg
description: ""
toc: 
---

Les emoji peuvent être activés dans un projet Hugo de plusieurs façons. :zap:

## Support des Emoji

La fonction [emojify](https://gohugo.io/functions/emojify/) peut être appelée directement dans les modèles ou les [Shortcodes en ligne](https://gohugo.io/templates/shortcode-templates/#inline-shortcodes).

Pour activer les emoji globalement, définissez ```enableEmoji``` sur ```true``` dans la [configuration](https://gohugo.io/getting-started/configuration/) de votre site, puis vous pouvez taper les codes abrégés d'emoji directement dans les fichiers de contenu; par exemple :

La [Feuille de triche Emoji](http://www.emoji-cheat-sheet.com/) est une référence utile pour les codes abrégés d'emoji.

<hr>

**N.B.** Les étapes ci-dessus activent les caractères et séquences emoji du standard Unicode dans Hugo, cependant le rendu de ces glyphes dépend du navigateur et de la plateforme. Pour styliser les emoji, vous pouvez utiliser une police emoji tierce ou une pile de polices; par exemple :

```
.emoji {
  font-family: Apple Color Emoji, Segoe UI Emoji, NotoColorEmoji, Segoe UI Symbol, Android Emoji, EmojiSymbols;
}
```
