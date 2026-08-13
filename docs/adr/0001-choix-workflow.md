# ADR-0001 : Choix du workflow Git

## Statut
Accepté — 2026-08-12

## Contexte

La plateforme data est développée par une équipe de 4 personnes : 2 data
engineers, 1 analyste data et 1 profil DevOps. L'équipe maîtrise les commandes
Git de base mais n'a jamais pratiqué la revue de code par Pull Request.

Aucune intégration continue n'est en place à ce jour ; sa mise en œuvre fait
partie du périmètre de la mission. La couverture de tests automatisés est
aujourd'hui partielle.

L'infrastructure comporte deux environnements : développement et production.
Une seule version de la plateforme est exploitée à la fois — il n'existe pas
de version antérieure à maintenir en parallèle.

L'objectif de livraison est hebdomadaire, avec une mise en production
déclenchée manuellement après validation métier.

## Options considérées

### Git Flow
Cinq types de branches (`main`, `develop`, `feature/*`, `release/*`,
`hotfix/*`).

Avantages : permet de maintenir plusieurs versions simultanément et d'isoler
la stabilisation d'une livraison du développement en cours. Adapté aux
logiciels distribués dont l'éditeur ne contrôle pas la date de mise à jour.

Inconvénients : complexité élevée pour une petite équipe. Un correctif urgent
doit être fusionné dans deux branches, ce qui multiplie les risques d'oubli.
Les branches de fonctionnalité vivent plusieurs semaines et génèrent des
conflits importants à la fusion.

### GitHub Flow
Deux types de branches : `main`, toujours déployable, et des branches de
fonctionnalité de courte durée fusionnées par Pull Request.

Avantages : modèle simple, rapide à enseigner, un seul état de vérité. La
Pull Request introduit naturellement la revue de code, absente de nos
pratiques actuelles. Le correctif urgent n'est pas un cas particulier.

Inconvénients : ne gère pas la coexistence de plusieurs versions en
production. Suppose une fréquence de déploiement soutenue, faute de quoi
`main` accumule du travail non livré.

### GitLab Flow
GitHub Flow complété par des branches représentant les environnements.

Avantages : permet de savoir précisément ce qui est déployé dans chaque
environnement.

Inconvénients : la valeur ajoutée est faible avec seulement deux
environnements. Les fusions supplémentaires introduisent une charge que
l'équipe n'est pas en mesure d'absorber aujourd'hui.

### Trunk-Based Development
Tous les développeurs poussent sur `main` plusieurs fois par jour ; les
branches vivent moins de 24 heures et les fonctionnalités incomplètes sont
masquées par des feature flags.

Avantages : intégration réellement continue, conflits de fusion quasi
inexistants, découplage entre déploiement et activation.

Inconvénients : exige une couverture de tests automatisés élevée, une CI
rapide et une infrastructure de feature flags. Aucun de ces prérequis n'est
réuni. Adopter ce modèle aujourd'hui exposerait la production à des
régressions non détectées.

## Décision

Nous retenons **GitHub Flow** : une branche `main` maintenue déployable en
permanence, et des branches de fonctionnalité de courte durée intégrées
exclusivement par Pull Request.

## Justification

Ce choix découle directement du contexte décrit ci-dessus.

Une seule version étant exploitée en production, la complexité de Git Flow ne
répondrait à aucun besoin réel : nous paierions un coût de coordination sans
contrepartie.

L'absence d'intégration continue et la couverture de tests partielle
disqualifient le Trunk-Based Development, dont la sécurité repose entièrement
sur l'automatisation des tests.

Avec deux environnements seulement, GitLab Flow ajouterait des fusions
supplémentaires pour une visibilité que le versionnage par tags apporte déjà.

Enfin, l'équipe n'ayant jamais pratiqué la revue de code, GitHub Flow présente
un avantage pédagogique déterminant : la Pull Request en est le mécanisme
central, et son adoption fait progresser l'équipe sur la revue en même temps
que sur le versionnage.

## Conséquences

### Positives
- Modèle assimilable en une demi-journée de formation.
- La revue de code devient systématique et non optionnelle.
- Un correctif urgent suit le circuit normal, sans procédure d'exception.
- Les branches courtes réduisent fortement les conflits de fusion.
- La protection de `main` empêche structurellement les poussées directes.

### Négatives
- La garantie « `main` toujours déployable » repose sur une CI qui n'existe
  pas encore. Tant qu'elle n'est pas opérationnelle, cette garantie n'est
  qu'une convention, appliquée par la discipline de l'équipe.
- La revue par Pull Request ralentit mécaniquement le rythme de fusion. Avec
  une équipe de 4 personnes, l'indisponibilité d'un relecteur devient un point
  de blocage.
- Le modèle ne prévoit rien pour maintenir une version antérieure. Si un
  client venait à exiger le maintien d'une version figée, cette décision
  devrait être révisée.
- L'objectif hebdomadaire est en tension avec le principe : plus l'intervalle
  entre deux livraisons s'allonge, plus l'écart entre `main` et la production
  se creuse.

## Révision

Cette décision sera réexaminée si l'une des conditions suivantes survient :
- mise en production d'une seconde version à maintenir en parallèle ;
- couverture de tests supérieure à 80 % et CI d'une durée inférieure à 10
  minutes, ouvrant la voie au Trunk-Based Development ;
- ajout d'un troisième environnement, justifiant une évaluation de GitLab
  Flow.
