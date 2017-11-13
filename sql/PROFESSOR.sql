CREATE TABLE PROFESSOR (
    usuario_id  integer not null primary key,
    apelido varchar(3) not null,
    CONSTRAINT uq_professor UNIQUE (apelido),
    CONSTRAINT fk_professor_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES USUARIO (id)
);