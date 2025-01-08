# testing
Este proyecto pretende mostrar un ejemplo de como configurar un entorno en el que poder realizar códigos y pruebas.

1. Dividimos el entorno en 2 carpetas
   
    1.1 src: código
   
    1.2 test: donde tendremos todos los archivos test_*.py para poder hacer las pruebas

2. Instalaremos utilizando pip: pytest y pytest-spec
3. A la misma altura de las carpetas src y test creamos el archivo de configuración de pytest 'pytest.ini', con la siguiente configuración: ![alt text](images/image.png)
4. Configuramos las pruebas y las ejecutamos mediante pytest en terminal, teniendo el siguiente resultado:  ![alt text](images/image-1.png)
