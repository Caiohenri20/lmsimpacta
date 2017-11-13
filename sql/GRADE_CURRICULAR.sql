CREATE TABLE GRADE_CURRICULAR (
    id integer not null primary key,
    curso_id integer not null,
    ano smallint not null,
    semestre char(1) not null,
    CONSTRAINT grade_unique UNIQUE (ano, semestre, curso_id),
    CONSTRAINT fk_grade_curricular_curso
    FOREIGN KEY (curso_id)
    REFERENCES CURSO (id)
);