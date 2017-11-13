CREATE TABLE TURMA (
    id  integer identity(1,1) not null,
    disciplina_ofertada_id integer not null,
    identificador CHAR(1) not null,
    turno VARCHAR(15),
    professor_id integer,
	CONSTRAINT pk_turma PRIMARY KEY (id),
    CONSTRAINT uq_turma UNIQUE (disciplina_ofertada_id, identificador),
    CONSTRAINT fk_turma_disciplina_ofertada
    FOREIGN KEY (disciplina_ofertada_id) REFERENCES DISCIPLINA_OFERTADA (id),
    CONSTRAINT fk_turma_professor
    FOREIGN KEY (professor_id) REFERENCES PROFESSOR (usuario_id)
);