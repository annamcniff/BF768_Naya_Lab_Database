
use Team_I; 


CREATE TABLE SAMPLE(
sid integer not null auto_increment,
timepoint enum('Profileration', 'Differentiation'),
cell_line varchar(100),
replicate enum('A', 'B', 'C'),
type enum('ATAC', 'CUT&RUN'),
primary key(sid)); 

CREATE TABLE CHROMOSOME(
cid varchar(2) not null,
primary key(cid)); 

CREATE TABLE PEAK(
pid integer not null auto_increment,
cid varchar(5) not null,
start integer,
end integer,
length integer,
abs_summit integer,
pileup integer,
fold_enrichment integer,
score integer, 
signalValue float, 
pvalue float, 
qvalue float, 
peak integer,
sid integer not null,
primary key(pid),
foreign key(sid) references SAMPLE(sid),
foreign key(cid) references CHROMOSOME(cid)); 

CREATE TABLE S_CHROM(
sid integer not null,
cid varchar(2) not null,
primary key(sid, cid),
foreign key(sid) references SAMPLE(sid),
foreign key(cid) references CHROMOSOME(cid)); 

CREATE TABLE gene(
gid int not null auto_increment,
symbol varchar(20) not null,
cid varchar(5) not null,
start int not null,
end int not null,
primary key(gid),
foreign key (cid) references CHROMOSOME (cid)
);

CREATE TABLE gene_set(
gsid int not null auto_increment,
description varchar(100),
primary key(gsid)
);

