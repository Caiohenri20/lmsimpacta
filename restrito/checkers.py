

def check_aluno(usuario):
    return usuario and usuario.perfil == 'A'

def check_professor(usuario):
    return usuario and usuario.perfil == 'P'

def check_coordenador(usuario):
    return usuario and usuario.perfil == 'C'