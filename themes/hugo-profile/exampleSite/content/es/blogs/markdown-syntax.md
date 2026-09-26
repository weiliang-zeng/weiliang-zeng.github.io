---
title: "Sintaxis de Markdown"
date: 2021-04-03T23:29:21+05:30
draft: false
github_link: "https://github.com/gurusabarish/hugo-profile"
author: "Gurusabarish"
tags:
  - Sintaxis de Markdown
  - Muestra
  - ejemplo
image: /images/post.jpg
description: ""
toc:
---

## Párrafo

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## Citas en bloque

El elemento blockquote representa contenido que se cita de otra fuente, opcionalmente con una cita que debe estar dentro de un elemento `footer` o `cite`, y opcionalmente con cambios en línea como anotaciones y abreviaturas.

### Cita en bloque sin atribución

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **Nota** que puedes usar _sintaxis de Markdown_ dentro de una cita en bloque.

### Cita en bloque con atribución

> No comuniques compartiendo memoria, comparte memoria comunicando.
> — <cite>Rob Pike[^1]</cite>

[^1]: La cita anterior se extrae de la [charla](https://www.youtube.com/watch?v=PAAkCSZUG1c) de Rob Pike durante Gopherfest, 18 de noviembre de 2015.

## Tablas

Las tablas no forman parte de la especificación principal de Markdown, pero Hugo las admite de forma predeterminada.

| Nombre  | Edad |
| ------- | ---- |
| Bob     | 27   |
| Alice   | 23   |

### Markdown en línea dentro de tablas

| Cursiva   | Negrita     | Código   |
| --------- | ----------- | -------- |
| _cursiva_ | **negrita** | `código` |

## Bloques de código

### Bloque de código con acentos graves

```html
<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <title>Ejemplo de documento HTML5</title>
  </head>
  <body>
    <p>Prueba</p>
  </body>
</html>
```

### Bloque de código con cuatro espacios

    <!doctype html>
    <html lang="es">
      <head>
        <meta charset="utf-8">
        <title>Ejemplo de documento HTML5</title>
      </head>
      <body>
        <p>Prueba</p>
      </body>
    </html>

### Bloque de código con el shortcode de resaltado interno de Hugo

{{< highlight html >}}

<!doctype html>
<html lang="es">
  <head>
    <meta charset="utf-8">
    <title>Ejemplo de documento HTML5</title>
  </head>
  <body>
    <p>Prueba</p>
  </body>
</html>
{{< /highlight >}}

## Tipos de lista

### Lista ordenada

1. Primer elemento
2. Segundo elemento
3. Tercer elemento

### Lista desordenada

- Elemento de lista
- Otro elemento
- Y otro elemento

### Lista anidada

- Fruta
  - Manzana
  - Naranja
  - Plátano
- Lácteos
  - Leche
  - Queso

## Otros elementos — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> es un formato de imagen de mapa de bits.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Presiona <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Supr</kbd></kbd> para finalizar la sesión.

La mayoría de las <mark>salamandras</mark> son nocturnas y cazan insectos, gusanos y otras criaturas pequeñas.
