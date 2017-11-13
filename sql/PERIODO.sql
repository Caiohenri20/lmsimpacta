CREATE TABLE PERIODO (
    id integer identity(1,1) not null,
    grade_curricular_id integer not null,
    numero tinyint not null,
	CONSTRAINT pk_periodo_ PRIMARY KEY (id),
    CONSTRAINT periodo_unique UNIQUE (grade_curricular_id, numero),
    CONSTRAINT fk_periodo_grade_curricular
    FOREIGN KEY (grade_curricular_id)
    REFERENCES GRADE_CURRICULAR (id)
);

