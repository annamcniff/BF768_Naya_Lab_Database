
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
start integer,
end integer,
length integer,
abs_summit integer,
pileup integer,
n_log10_pval integer,
fold_enrichment integer,
n_log10_qval integer,
sid integer not null,
cid varchar(2) not null,
primary key(pid),
foreign key(sid) references SAMPLE(sid),
foreign key(cid) references CHROMOSOME(cid)); 

CREATE TABLE S_CHROM(
sid integer not null,
cid varchar(2) not null,
primary key(sid, cid),
foreign key(sid) references SAMPLE(sid),
foreign key(cid) references CHROMOSOME(cid)); 

