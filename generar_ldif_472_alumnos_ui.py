def genera_contenido_ldif_usuarios_alumnos(filename, base_dn, numero, nombre_base_usuario, grupo):
    """
    Genera un archivo LDIF con un número determinado de usuarios alumnos.
    :param filename: Nombre del archivo LDIF a generar.
    :param base_dn: Base DN del directorio.
    :param numero: Número de usuarios a crear.
    :param nombre_base_usuario: Prefijo para el nombre de usuario.
    :param grupo: Grupo al que se añadirán los usuarios.
    """
    try:
        with open(filename, "w") as f:
            for i in range(1, numero + 1):
                username = f"{nombre_base_usuario}{i}"
                dn = f"cn={username},ou={grupo},{base_dn}"
                ldif_content = f"""dn: {dn}
objectClass: inetOrgPerson
objectClass: posixAccount
objectClass: top
cn: {username}
sn: Alumno{i}
givenName: Alumno{i}
uid: {username}
uidNumber: {1000 + i}
gidNumber: 1000
homeDirectory: /home/{username}
loginShell: /bin/bash
userPassword: {username}123
"""
                f.write(ldif_content + "\n")
            print(f"LDIF con {numero} usuarios creado: {filename}")
    except Exception as e:
        print(f"Error al crear el archivo LDIF '{filename}': {e}")

# Llamar a la función para generar el archivo LDIF con 472 alumnos
genera_contenido_ldif_usuarios_alumnos(
    "usuarios_alumnos.ldif",
    "dc=instituto,dc=carsi,dc=org",
    472,
    "alumno",
    "alumnos"
)
