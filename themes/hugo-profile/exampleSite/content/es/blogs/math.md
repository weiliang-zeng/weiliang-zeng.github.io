---
title: "Renderizar Matemáticas con Mathjax"
date: 2022-12-09T19:53:33+05:30
draft: false
author: "Gurusabarish"
tags:
  - Sintaxis de Markdown
  - Mathjax
  - ejemplo
image: /images/mathjax.png
description: ""
toc: true
mathjax: true
---

## Mathjax

Las ecuaciones matemáticas se pueden renderizar usando la sintaxis de [Mathjax](https://www.mathjax.org) con soporte de símbolos AMS.

Opcionalmente, habilita esto por página agregando `mathjax: true` a tu frontmatter.

Luego, usa `$$ ... $$` en una línea por sí sola para renderizar una ecuación de bloque:

$$ | Pr_{x \leftarrow P_{1}} [A(x) = 1] - Pr_{x \leftarrow P_{2}} [A(x) = 1] | < \text{negligible} $$

La versión sin procesar es:

```
$$ | Pr_{x \leftarrow P_{1}} [A(x) = 1] - Pr_{x \leftarrow P_{2}} [A(x) = 1] | < \text{negligible} $$
```


Escribe ecuaciones en línea con `\\( ... \\)` , como \\( x^n / y \\) . ¡Es fácil!

```
Escribe ecuaciones en línea con `\\( ... \\)` , como \\( x^n / y \\) . ¡Es fácil!
```

