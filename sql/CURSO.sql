CREATE TABLE CURSO (
    id    integer identity(1,1) not null,
    sigla varchar(5) not null,
    nome  varchar(50) not null,
	coordenador_id integer not null,
	CONSTRAINT pk_curso PRIMARY KEY (id),
    CONSTRAINT un_curso_sigla UNIQUE (sigla),
    CONSTRAINT un_curso_nome UNIQUE (nome),
	CONSTRAINT fk_curso_coordenador FOREIGN KEY (coordenador_id) REFERENCES COORDENADOR (usuario_id)
);