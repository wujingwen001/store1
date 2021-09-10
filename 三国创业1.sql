DROP DATABASE IF EXISTS company;
CREATE DATABASE IF NOT EXISTS company CHARACTER SET utf8;
USE company;

DROP TABLE IF EXISTS `t_dept`;
CREATE TABLE `t_dept` (
  `deptno` INT(11) NOT NULL,
  `dname` VARCHAR(20) DEFAULT NULL,
  `loc` VARCHAR(40) DEFAULT NULL,
  PRIMARY KEY (`deptno`),
  KEY `index_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

LOCK TABLES `t_dept` WRITE;
INSERT INTO `t_dept` VALUES (10,'董事部','江东'),(20,'公关部','四川'),
			    (30,'武统部','咸阳'),(40,'财务部','洛阳');
UNLOCK TABLES;

DROP TABLE IF EXISTS `t_employees`;
CREATE TABLE `t_employees` (
  `empno` INT(11) NOT NULL,
  `ename` VARCHAR(20) DEFAULT NULL,
  `job` VARCHAR(40) DEFAULT NULL,
  `MGR` INT(11) DEFAULT NULL,
  `hiredate` DATE DEFAULT NULL,
  `sal` DOUBLE(10,2) DEFAULT NULL,
  `comm` DOUBLE(10,2) DEFAULT NULL,
  `deptno` INT(11) DEFAULT NULL,
  PRIMARY KEY (`empno`),
  KEY `fk_deptno` (`deptno`),
  CONSTRAINT `fk_deptno` FOREIGN KEY (`deptno`) REFERENCES `t_dept` (`deptno`)
) ENGINE=INNODB DEFAULT CHARSET=utf8;

LOCK TABLES `t_employees` WRITE;
INSERT INTO `t_employees` VALUES (7369,'周瑜','高级公关',7566,'1981-03-21',1800.00,NULL,20),
				 (7499,'张飞','武装教习',7698,'1982-03-21',2600.00,300.00,30),
				 (7521,'关二爷','武装副司令',7698,'1983-03-21',2250.00,500.00,30),
				 (7566,'孙权','经理',7839,'1981-03-21',3975.00,NULL,10),
				 (7654,'黄忠','武装司令',7698,'1981-03-21',2250.00,1400.00,30),
				 (7698,'刘备','经理',7839,'1984-03-21',3850.00,NULL,10),
				 (7782,'曹操','经理',7839,'1985-03-21',3450.00,NULL,10),
				 (7788,'许褚','武装上将',7782,'1981-03-21',4000.00,NULL,30),
				 (7839,'汉献帝','董事长',NULL,'1981-03-21',6000.00,NULL,10),
				 (7844,'魏延','武装上将',7698,'1989-03-21',2500.00,0.00,30),
				 (7876,'黄盖','人事专员',7566,'1998-03-21',2100.00,NULL,20),
				 (7902,'荀彧','分析员',7782,'2005-03-12',4000.00,NULL,20),
				 (7934,'甘宁','中级公关',7782,'1981-03-21',2300.00,NULL,20),
				 (7952,'马超','武装大校',7698,'2001-03-21',2750.00,0.00,30),
				 (7953,'吕布','武装教习',7698,'2001-03-21',2750.00,0.00,30);
UNLOCK TABLES;

-- 查询出部门编号为30的所有员工
SELECT empno,ename,deptno FROM t_employees WHERE deptno=30;
-- 所有经理的姓名、编号和部门编号
SELECT empno,ename,deptno FROM t_employees WHERE job='经理';
-- 找出奖金高于工资的员工
SELECT empno,ename FROM t_employees WHERE comm>sal;
-- 找出奖金高于工资60%的员工
SELECT empno,ename FROM t_employees WHERE comm>0.6*sal;
-- 找出部门编号为10中所有经理，和部门编号为20中所有分析员的详细资料
SELECT * FROM t_employees WHERE (deptno=10 AND job='经理') OR (deptno=20 AND job='分析员');
-- 找出部门编号为10中所有经理，部门编号为20中所有分析员，还有即不是经理又不是武装上将但其工资大或等于3000的所有员工详细资料
SELECT * FROM t_employees WHERE (deptno=10 AND job='经理') OR (deptno=20 AND job='分析员') OR (job!='经理' AND job!='武装上将' AND sal>=3000);
-- 无奖金或奖金低于1000的员工
SELECT empno,ename,comm FROM t_employees WHERE comm<1000 OR comm IS NULL;
-- 查询名字由三个字组成的员工
SELECT ename FROM t_employees WHERE ename LIKE '___';
-- 查询2000年以及以后入职的员工
SELECT empno,ename,hiredate FROM t_employees WHERE hiredate LIKE '200%';
-- 查询所有员工详细信息，用编号升序排序
SELECT * FROM t_employees ORDER BY empno ASC;
-- 查询所有员工详细信息，用工资降序排序，如果工资相同使用入职日期升序排序
SELECT * FROM t_employees ORDER BY sal DESC,hiredate ASC;
-- 查询每个部门的平均工资
SELECT deptno,AVG(sal) FROM t_employees GROUP BY deptno;
-- 查询每个部门的雇员数量
SELECT deptno,COUNT(empno) FROM t_employees GROUP BY deptno;
-- 查询每种工作的最高工资、最低工资、人数
SELECT job,MAX(sal),MIN(sal),COUNT(empno) FROM t_employees GROUP BY job;
















