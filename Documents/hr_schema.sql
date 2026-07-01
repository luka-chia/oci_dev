-- ========================================================================
-- 1. 配置运行时变量（代替原本的 Bash 环境变量）
-- ========================================================================
-- 如果有 OCI IAM 域名后缀，请在此处填写（例如：oracleidentitycloudservice）
-- 如果没有，请保持原本的空字符串 ''
DEFINE OCI_USERNAME_DOMAIN = ''
DEFINE MARVIN_USERNAME     = 'marvin'
DEFINE EMMA_USERNAME       = 'emma'

-- ========================================================================
-- 2. SQL*Plus 运行环境设置
-- ========================================================================
SET ECHO ON
SET SERVEROUTPUT ON
SET LINESIZE 180
WHENEVER SQLERROR EXIT SQL.SQLCODE

-- ========================================================================
-- 3. 清理并重建 HR 用户
-- ========================================================================
BEGIN
  EXECUTE IMMEDIATE 'DROP USER hr CASCADE';
EXCEPTION
  WHEN OTHERS THEN
    IF SQLCODE != -1918 THEN
      RAISE;
    END IF;
END;
/

-- 创建无需密码认证的局部/内部用户（23c 新特性 NO AUTHENTICATION）
CREATE USER hr NO AUTHENTICATION
  DEFAULT TABLESPACE data
  QUOTA UNLIMITED ON data;

-- ========================================================================
-- 4. 创建员工表
-- ========================================================================
CREATE TABLE hr.employees (
  employee_id   NUMBER PRIMARY KEY,
  first_name    VARCHAR2(50),
  last_name     VARCHAR2(50),
  job_code      VARCHAR2(10),
  department_id NUMBER,
  ssn           VARCHAR2(20),
  photo         BLOB,
  phone_number  VARCHAR2(30),
  salary        NUMBER(10,2),
  user_name     VARCHAR2(128),
  manager_id    NUMBER
);

-- ========================================================================
-- 5. 插入初始化样本数据
-- ========================================================================
INSERT INTO hr.employees VALUES (1, 'Grace', 'Young', 'CEO', NULL, '111-11-1111', NULL, '555-100-0001', 235000, 'grace', NULL);
INSERT INTO hr.employees VALUES (2, 'Marvin', 'Morgan', 'SWE_MGR', 1, '222-22-2222', NULL, '555-100-0002', 175000, '&MARVIN_USERNAME', 1);
INSERT INTO hr.employees VALUES (3, 'Emma', 'Baker', 'SWE2', 1, '333-33-3333', NULL, '555-100-0003', 120000, '&EMMA_USERNAME', 2);
INSERT INTO hr.employees VALUES (4, 'Charlie', 'Davis', 'SWE1', 1, '444-44-4444', NULL, '555-100-0004', 95000, 'charlie', 2);
INSERT INTO hr.employees VALUES (5, 'Dana', 'Lee', 'SWE3', 1, '555-55-5555', NULL, '555-100-0005', 130000, 'dana', 2);
INSERT INTO hr.employees VALUES (6, 'Bob', 'Smith', 'SALES_REP', 2, '666-66-6666', NULL, '555-100-0006', 145000, 'bob', 1);
INSERT INTO hr.employees VALUES (7, 'Fiona', 'Chen', 'HR_REP', 3, '777-77-7777', NULL, '555-100-0007', 92000, 'fiona', 1);

-- ========================================================================
-- 6. 根据域名变量动态更新 user_name 后缀
-- ========================================================================
UPDATE hr.employees
   SET user_name =
       CASE
         WHEN '&OCI_USERNAME_DOMAIN' IS NOT NULL
          AND LENGTH('&OCI_USERNAME_DOMAIN') > 0
          AND user_name NOT LIKE '%@%'
         THEN user_name || '@&OCI_USERNAME_DOMAIN'
         ELSE user_name
       END;
COMMIT;

-- ========================================================================
-- 7. 格式化并验证查询结果
-- ========================================================================
COLUMN first_name FORMAT a12
COLUMN last_name FORMAT a12
COLUMN user_name FORMAT a45

SELECT employee_id, first_name, last_name, user_name, manager_id
FROM hr.employees
ORDER BY employee_id;

EXIT;