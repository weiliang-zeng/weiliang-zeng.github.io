---
title: "Syntaxe Markdown"
date: 2021-04-03T23:29:21+05:30
draft: false
github_link: "https://github.com/gurusabarish/hugo-profile"
author: "Gurusabarish"
tags:
  - Syntaxe Markdown
  - Exemple
  - échantillon
image: /images/post.jpg
description: ""
toc:
---

## Paragraphe

Xerum, quo qui aut unt expliquam qui dolut labo. Aque venitatiusda cum, voluptionse latur sitiae dolessi aut parist aut dollo enim qui voluptate ma dolestendit peritin re plis aut quas inctum laceat est volestemque commosa as cus endigna tectur, offic to cor sequas etum rerum idem sintibus eiur? Quianimin porecus evelectur, cum que nis nust voloribus ratem aut omnimi, sitatur? Quiatem. Nam, omnis sum am facea corem alique molestrunt et eos evelece arcillit ut aut eos eos nus, sin conecerem erum fuga. Ri oditatquam, ad quibus unda veliamenimin cusam et facea ipsamus es exerum sitate dolores editium rerore eost, temped molorro ratiae volorro te reribus dolorer sperchicium faceata tiustia prat.

Itatur? Quiatae cullecum rem ent aut odis in re eossequodi nonsequ idebis ne sapicia is sinveli squiatum, core et que aut hariosam ex eat.

## Citations

L'élément blockquote représente le contenu cité d'une autre source, éventuellement avec une citation qui doit se trouver dans un élément `footer` ou `cite`, et éventuellement avec des modifications en ligne telles que des annotations et des abréviations.

### Citation sans attribution

> Tiam, ad mint andaepu dandae nostion secatur sequo quae.
> **Notez** que vous pouvez utiliser la _syntaxe Markdown_ dans une citation.

### Citation avec attribution

> Ne communiquez pas en partageant la mémoire, partagez la mémoire en communiquant.
> — <cite>Rob Pike[^1]</cite>

[^1]: La citation ci-dessus est extraite de la [conférence](https://www.youtube.com/watch?v=PAAkCSZUG1c) de Rob Pike lors de Gopherfest, le 18 novembre 2015.

## Tableaux

Les tableaux ne font pas partie de la spécification Markdown de base, mais Hugo les prend en charge par défaut.

| Nom   | Âge |
| ----- | --- |
| Bob   | 27  |
| Alice | 23  |

### Markdown en ligne dans les tableaux

| Italique   | Gras       | Code     |
| ---------- | ---------- | -------- |
| _italique_ | **gras**   | `code`   |

## Blocs de code

### Bloc de code avec des backticks

```html
<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8" />
    <title>Exemple de document HTML5</title>
  </head>
  <body>
    <p>Test</p>
  </body>
</html>
```

### Bloc de code indenté de quatre espaces

    <!doctype html>
    <html lang="fr">
      <head>
        <meta charset="utf-8">
        <title>Exemple de document HTML5</title>
      </head>
      <body>
        <p>Test</p>
      </body>
    </html>

### Bloc de code avec le shortcode de surbrillance intégré de Hugo

{{< highlight html >}}

<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <title>Exemple de document HTML5</title>
  </head>
  <body>
    <p>Test</p>
  </body>
</html>
{{< /highlight >}}

## Types de listes

### Liste ordonnée

1. Premier élément
2. Deuxième élément
3. Troisième élément

### Liste non ordonnée

- Élément de liste
- Un autre élément
- Et un autre élément

### Liste imbriquée

- Fruits
  - Pomme
  - Orange
  - Banane
- Produits laitiers
  - Lait
  - Fromage

## Autres éléments — abbr, sub, sup, kbd, mark

<abbr title="Graphics Interchange Format">GIF</abbr> est un format d'image bitmap.

H<sub>2</sub>O

X<sup>n</sup> + Y<sup>n</sup> = Z<sup>n</sup>

Appuyez sur <kbd><kbd>CTRL</kbd>+<kbd>ALT</kbd>+<kbd>Suppr</kbd></kbd> pour terminer la session.

La plupart des <mark>salamandres</mark> sont nocturnes et chassent les insectes, les vers et autres petites créatures.
