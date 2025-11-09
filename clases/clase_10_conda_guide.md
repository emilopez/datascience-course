# Guía rápida de Conda para Data Science

## 🌟 Conceptos básicos

**Conda** es un gestor de paquetes y entornos que permite:
- Crear entornos aislados para diferentes proyectos
- Instalar paquetes de Python y otros lenguajes
- Manejar dependencias automáticamente

---

## 📦 Comandos esenciales

### Gestión de entornos

```bash
# Ver todos los entornos instalados
conda env list

# Crear un entorno nuevo (con Python específico)
conda create -n mi_proyecto python=3.11

# Crear entorno desde archivo YAML
conda env create -f environment.yml

# Activar un entorno
conda activate mi_proyecto

# Desactivar el entorno actual
conda deactivate

# Eliminar un entorno completo
conda env remove -n mi_proyecto
```

### Instalación de paquetes

```bash
# Instalar un paquete
conda install pandas

# Instalar múltiples paquetes
conda install numpy pandas matplotlib

# Instalar versión específica
conda install pandas=2.0.0

# Instalar desde un canal específico
conda install -c conda-forge geopandas

# Buscar paquetes disponibles
conda search pandas
```

### Ver información

```bash
# Listar paquetes instalados en el entorno actual
conda list

# Ver información de un paquete
conda list pandas

# Actualizar un paquete
conda update pandas

# Actualizar todos los paquetes
conda update --all
```

---

## 📄 Exportar e importar entornos

### Exportar tu entorno actual

```bash
# Exportar a archivo YAML
conda env export > mi_entorno.yml

# Exportar solo paquetes instalados manualmente
conda env export --from-history > mi_entorno.yml
```

### Importar un entorno

```bash
# Crear entorno desde YAML
conda env create -f mi_entorno.yml

# Actualizar entorno existente desde YAML
conda env update -f mi_entorno.yml
```

---

## 🔧 Ejemplo de archivo environment.yml

```yaml
name: proyecto_analisis
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - pandas=2.0.3
  - numpy=1.24.3
  - matplotlib=3.7.1
  - seaborn=0.12.2
  - jupyterlab=4.0.2
  - scikit-learn=1.3.0
  - geopandas=0.13.2
```

---

## 💡 Tips útiles

### Workflow recomendado

```bash
# 1. Crear y activar entorno
conda create -n analisis_ventas python=3.11
conda activate analisis_ventas

# 2. Instalar paquetes necesarios
conda install pandas numpy matplotlib jupyterlab

# 3. Trabajar en tu proyecto
jupyter lab

# 4. Al terminar, exportar el entorno
conda env export > environment.yml

# 5. Desactivar
conda deactivate
```

### Resolver conflictos de dependencias

```bash
# Si hay conflictos, probar instalar de a uno
conda install pandas
conda install numpy
conda install matplotlib

# Usar mamba (más rápido para resolver dependencias)
conda install mamba -c conda-forge
mamba install geopandas
```

### Limpiar caché y paquetes

```bash
# Limpiar paquetes descargados
conda clean --all

# Ver espacio usado
conda clean --all --dry-run
```

---

## 🚨 Diferencias con pip

| Característica | conda | pip |
|---|---|---|
| Instala | Python y otros | Solo Python |
| Resuelve dependencias | Mejor | Básico |
| Entornos | Incluido | Necesita virtualenv |
| Velocidad | Más lento | Más rápido |

### Usar pip dentro de conda

```bash
# Si un paquete no está en conda
conda activate mi_entorno
pip install nombre-paquete

# Exportar incluyendo pip
conda env export > environment.yml
```

---

## 📌 Atajos de productividad

```bash
# Alias útiles para .bashrc o .zshrc
alias ca='conda activate'
alias cda='conda deactivate'
alias cel='conda env list'
alias cin='conda install'
alias clist='conda list'

# Ejemplo de uso
ca curso_ds_2025
cin pandas
```

---

✅ **Con estos comandos tenés todo lo necesario para gestionar tus proyectos de Data Science con Conda**.