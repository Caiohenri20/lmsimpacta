CREATE TABLE CURSO_TURMA (
    curso_id  integer not null,
    turma_id integer not null,
    CONSTRAINT pk_curso_turma primary key (curso_id, turma_id),
    CONSTRAINT fk_curso_turma_curso
    FOREIGN KEY (curso_id)
    REFERENCES CURSO (id),
    CONSTRAINT fk_curso_turma_turma
    FOREIGN KEY (turma_id)
    REFERENCES TURMA (id)
);