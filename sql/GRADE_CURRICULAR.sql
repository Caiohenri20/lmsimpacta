CREATE TABLE GRADE_CURRICULAR (
    id integer identity not null ,
    curso_id integer not null,
    ano smallint not null,
    semestre char(1) not null,
	CONSTRAINT pk_grade_curricular PRIMARY KEY (id),
    CONSTRAINT un_grade_curricular UNIQUE (ano, semestre, curso_id),
    CONSTRAINT fk_grade_curricular_curso
    FOREIGN KEY (curso_id)
    REFERENCES CURSO (id)
);
