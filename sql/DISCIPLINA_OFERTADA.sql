CREATE TABLE DISCIPLINA_OFERTADA (
    id integer not null,
    disciplina_id integer not null,
    ano smallint not null,
    semestre CHAR(1) not null
    CONSTRAINT uq_disciplina_ofertada UNIQUE (disciplina_id, ano, semestre),
    CONSTRAINT fk_disciplina_ofertada_disciplina
    FOREIGN KEY (disciplina_id) REFERENCES DISCIPLINA (id)
);