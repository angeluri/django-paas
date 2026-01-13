#!/usr/bin/env python
import os
import sys

def main():
    # AJUSTA ESTA LÍNEA SEGÚN TU ESTRUCTURA:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings')
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y "
            "disponible en tu PYTHONPATH? ¿Activaste el entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()