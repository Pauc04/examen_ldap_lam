def genera_contenido_ldif_multiples_unidades_organizativas(filename, lista_ou_name, base_dn):
    """Genera un archivo LDIF con múltiples unidades organizativas."""
    try:
        with open(filename, "w") as f:
            for ou_name in lista_ou_name:
                ldif_content = f"""dn: ou={ou_name},{base_dn}
objectClass: organizationalUnit
ou: {ou_name}

"""
                f.write(ldif_content)
            print(f"LDIF con múltiples unidades organizativas creado: {filename}")
    except Exception as e:
        print(f"Error al crear el archivo LDIF '{filename}': {e}")

# Lista inicial de unidades organizativas
unidades_organizativas = [
    "directores",
    "profesores",
    "alumnos"
]

# Comprobación básica del funcionamiento
genera_contenido_ldif_multiples_unidades_organizativas("unidades.ldif", unidades_organizativas, "dc=instituto,dc=carsi,dc=org")

# Ampliación de la lista con las nuevas unidades organizativas
unidades_adicionales = [
    "personalnodocente", "eso1", "eso2", "eso3", "eso4",
    "bach1ciencias", "bach1humanidades", "bach2ciencias", "bach2humanidades",
    "profesoreseso", "profesoresbach", "profesoreseso1", "profesoreseso2",
    "profesoreseso3", "profesoreseso4", "profesoresbach1ciencias",
    "profesoresbach1humanidades", "profesoresbach2ciencias", "profesoresbach2humanidades"
]

# Unimos las listas y generamos el LDIF actualizado
unidades_organizativas.extend(unidades_adicionales)
genera_contenido_ldif_multiples_unidades_organizativas("unidades_completas.ldif", unidades_organizativas, "dc=instituto,dc=carsi,dc=org")
