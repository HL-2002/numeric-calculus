# Paso a paso para crear tu rama y añadir tus archivos

### clonar repo
```bash
git clone  "https://github.com/HL-2002/numeric-calculus"
```

### traer los cambios del repo
```bash
git pull
```

### Creación de nueva rama 

```bash
git checkout -b "tu-nombre"
```
o  si ya la creaste

```bash
git checkout "tu_rama"
```


### Añadir tus archivos y subir al repo

Trabaja tus propios archivos, y cuando estés listo añádelos al repo local:
```bash
git add archivo_nombre # añadir archivo de forma individual 
git add . # añadir todos los archivos 
```

Tras añadir los archivos, confirma los cambios:
```bash
git commit -m "mensaje de confirmación"
```

subir los cambios al repo en github:
```bash
git push --set-upstream origin tu_rama
```

