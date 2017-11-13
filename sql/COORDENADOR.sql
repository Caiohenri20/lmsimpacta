CREATE TABLE COORDENADOR (
    usuario_id  integer not null,
    sala	varchar(3) not null,
    CONSTRAINT pk_coordenador primary key (usuario_id),
    CONSTRAINT fk_coordenador_usuario
    FOREIGN KEY (usuario_id)
    REFERENCES USUARIO (id)
);