# Instalación de Python para el curso de Data Science

## 📘 Instalación en entornos Windows

Estas instrucciones permiten instalar todo lo necesario para trabajar con Python y GeoPandas **sin errores** en Windows.

---

### 1️⃣ Descargar e instalar Miniforge

1. Abrir este enlace:  
   👉 [https://github.com/conda-forge/miniforge/releases/latest](https://github.com/conda-forge/miniforge/releases/latest)
2. Buscar el instalador para Windows:  
   **`Miniforge3-Windows-x86_64.exe`**  
   *(No el `.zip`, no el de ARM)*
3. Hacer doble clic en el archivo descargado y seguir estos pasos:
   - Cuando pregunte “Add Miniforge3 to PATH?”, dejar la opción **NO marcada**.
   - Dejar marcada la opción **Register Miniforge3 as my default Python**.
   - Aceptar y terminar la instalación.

---

### 2️⃣ Descargar el archivo del entorno del curso

1. El profesor les dará un archivo llamado `environment.yml`.
2. Guardar este archivo en una carpeta fácil de encontrar, por ejemplo:  
   `C:\curso_ds`

---

### 3️⃣ Crear el entorno del curso

1. Abrir el menú Inicio de Windows.
2. Buscar y abrir **Miniforge Prompt** (es como una ventana negra con texto).
3. En la ventana, escribir (y luego Enter):

   ```bash
   cd C:\curso_ds
   ```

4. Crear el entorno del curso con:

   ```bash
   conda env create -f environment.yml
   ```

📌 **Este paso puede tardar varios minutos** dependiendo de la conexión a Internet.  
Es normal que aparezca mucha información en pantalla.

---

### 4️⃣ Activar el entorno y abrir JupyterLab

1. En la misma ventana, escribir:

   ```bash
   conda activate curso_ds
   ```

2. Luego abrir JupyterLab con:

   ```bash
   jupyter lab
   ```

3. Se abrirá una ventana en el navegador.  
   Allí podrán crear y ejecutar notebooks de Python.

---

### 5️⃣ Cómo usarlo en el futuro

Cada vez que quieran trabajar en el curso:

1. Abrir **Miniforge Prompt**.
2. Activar el entorno:

   ```bash
   conda activate curso_ds
   ```

3. Abrir JupyterLab:

   ```bash
   jupyter lab
   ```

---

✅ **Con esto tendrán todo listo para trabajar en el curso sin problemas de instalación**.


## 🐧 Instalación de Miniforge y entorno del curso en Linux

Estas instrucciones están pensadas para usuarios Linux que ya manejan entornos de Python, pero que quieren aislar `conda` para un curso sin interferir con su entorno habitual (por ejemplo, `uv`, `pyenv`, `virtualenv`).

---

### 1️⃣ Descargar e instalar Miniforge en una carpeta aislada

Recomendado instalarlo en una ruta propia, por ejemplo `~/miniforge_curso`:

```bash
wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
bash Miniforge3-Linux-x86_64.sh
```

Cuando aparezca el mensaje:

```
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
   run the following command when conda is activated:

conda config --set auto_activate_base false

You can undo this by running `conda init --reverse $SHELL`? [yes|no]
[no] >>>
```

**Elegir `no`** para evitar que `conda` modifique tu `~/.bashrc` o `~/.zshrc`.

El instalador mostrará algo como:

```
You have chosen to not have conda modify your shell scripts at all.
To activate conda's base environment in your current shell session:

eval "$(/home/usuario/miniforge3/bin/conda shell.YOUR_SHELL_NAME hook)" 

To install conda's shell functions for easier access, first activate, then:

conda init

Thank you for installing Miniforge3!
```

---

### 2️⃣ Activar conda manualmente cuando sea necesario

En lugar de tenerlo siempre activo, se carga sólo cuando se necesite:

Si usas **bash**:
```bash
eval "$(/home/usuario/miniforge3/bin/conda shell.bash hook)"
```

Si usas **zsh**:
```bash
eval "$(/home/usuario/miniforge3/bin/conda shell.zsh hook)"
```

---

### 3️⃣ Crear el entorno del curso

Asumiendo que tenés el archivo `environment.yml`:

```bash
conda env create -f environment.yml
```

Activar el entorno:
```bash
conda activate curso_ds
```

---

### 4️⃣ Abrir JupyterLab

```bash
jupyter lab
```

---

### 5️⃣ Desactivar el entorno

```bash
conda deactivate
```

---

### 6️⃣ Tip opcional: script de inicio rápido

Podés crear un script `iniciar_curso.sh` para automatizar todo:

```bash
#!/bin/bash
eval "$(/home/usuario/miniforge3/bin/conda shell.bash hook)"
conda activate curso_ds
jupyter lab
```

Dar permisos y ejecutarlo:
```bash
chmod +x iniciar_curso.sh
./iniciar_curso.sh
```

---

✅ Con esto, `conda` queda completamente aislado y sólo se activa cuando vos lo decidís.