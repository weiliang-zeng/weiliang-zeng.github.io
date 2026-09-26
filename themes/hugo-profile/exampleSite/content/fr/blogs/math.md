---
title: "Rendre les Mathématiques avec Mathjax"
date: 2022-12-09T19:53:33+05:30
draft: false
author: "Gurusabarish"
tags:
  - Syntaxe Markdown
  - Mathjax
  - exemple
image: /images/mathjax.png
description: ""
toc: true
mathjax: true
---

## Mathjax

Les équations mathématiques peuvent être rendues en utilisant la syntaxe [Mathjax](https://www.mathjax.org) avec le support des symboles AMS.

Activez ceci de manière optionnelle page par page en ajoutant `mathjax: true` à votre frontmatter.

Ensuite, utilisez `$$ ... $$` sur une ligne par elle-même pour rendre une équation de bloc:

$$ | Pr_{x \leftarrow P_{1}} [A(x) = 1] - Pr_{x \leftarrow P_{2}} [A(x) = 1] | < \text{negligible} $$

La version brute est:

```
$$ | Pr_{x \leftarrow P_{1}} [A(x) = 1] - Pr_{x \leftarrow P_{2}} [A(x) = 1] | < \text{negligible} $$
```


Écrivez des équations en ligne avec `\\( ... \\)` , comme \\( x^n / y \\) . C'est facile!

```
Écrivez des équations en ligne avec `\\( ... \\)` , comme \\( x^n / y \\) . C'est facile!
```

