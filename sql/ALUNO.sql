CREATE TABLE ALUNO (
    usuario_id  integer not null,
    curso_id integer not null,
    CONSTRAINT pk_aluno primary key (usuario_id),
    CONSTRAINT fk_aluno_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES USUARIO (id),
    CONSTRAINT fk_aluno_curso
    FOREIGN KEY (curso_id)
    REFERENCES CURSO (id)
);