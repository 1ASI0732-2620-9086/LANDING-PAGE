# CI de la landing académica

Este repositorio contiene HTML estático. Es distinto de la landing React
`PersonalProjects5443/LANDING-PAGE-MAX`; sus pruebas React no se copian aquí.

El workflow **MAX Academic Landing CI**, `.github/workflows/ci.yml`, se ejecuta
al publicar `ci/max-tests-actions`, al abrir o actualizar un pull request hacia `main`, al hacer push a `main`
y mediante ejecución manual cuando el workflow esté disponible en la rama por defecto.

## Ejecutar y revisar

```powershell
python scripts/test_ci.py
```

Comprueba siete contratos: metadatos para español/móvil, identificadores únicos,
navegación interna, archivos locales, HTTPS en enlaces externos, destino de
los accesos a MAX y servicio HTTP local bajo el prefijo de proyecto de Pages.
No inicia sesión en producción ni verifica la disponibilidad de imágenes/CDN externos.
Los enlaces legales `#` actuales siguen siendo placeholders; no se presentan como páginas funcionales.

Artefactos de Actions:

- `landing-academic-reports-<SHA>`: resumen JSON y reporte JUnit XML.
- `landing-academic-candidate-<SHA>`: `index.html`, `public/`, commit y SHA-256.

No se necesita ningún secreto para CI. Se requieren Actions y las acciones de
checkout/upload-artifact permitidas en la configuración del repositorio.

## Publicación existente

La API de GitHub confirmó Pages con `build_type=legacy`, origen `main` y carpeta `/`.
Fusionar a `main` puede activar ese despliegue existente, independiente del CI nuevo.
Este workflow no lo sustituye, no modifica Pages y no realiza despliegues.
Abrir el pull request hacia `main` permite revisar CI sin fusionarlo.
