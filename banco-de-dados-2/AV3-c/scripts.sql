-- Criar tabela Aluno_log
CREATE TABLE Aluno_log(
	matricula integer,
	cpf integer,
	nome varchar(255),
	email varchar(255),
	numContato varchar(255),
	versao integer
);

-- Criar tabela Aluno
CREATE TABLE Aluno(
	matricula integer,
	cpf integer,
	nome varchar(255),
	email varchar(255),
	numContato varchar(255)
);



/*
 * Inserir: Quando insere em aluno, deleta em aluno e manda a versao antiga para a log
 * 
 * Update: Quando atualizar, mover a versao antiga para a tabela log
 * 
 * Delete: Quando excluir, mover o registro para a tabela log
 * 
 * */

-- Cria trigger de update
create trigger AtualizaAluno before update on Aluno for each row 
begin
	set @versao = coalesce((select max(a.versao) from Aluno_log a where a.matricula=new.matricula), 0) + 1;
	insert into Aluno_log (matricula, cpf, nome, email, numContato, versao)
	values (old.matricula, old.cpf, old.nome, old.email, old.numContato, @versao);
end;

-- Dropa trigger de update
drop trigger AtualizaAluno;



-- Como a Trigger de INSERT não dá pra fazer, criamos uma procedure que o usuário
-- vai utilizar sempre que ele quiser inserir algo na tabela Aluno.

-- Por que não dá pra fazer a trigger de insert? É porque as triggers não podem
-- alterar os registros da tabela que elas fazem parte. Neste caso, a trigger de
-- INSERT, que faz parte da tabela Aluno, não pode excluir um registro da Aluno

-- Cria a procedure de inserir aluno
create procedure InserirAluno(
	-- Parâmetros
	IN prMatricula INTEGER, 
	IN prCpf INTEGER, 
	IN prNome VARCHAR(255), 
	IN prEmail VARCHAR(255),
	IN prNumContato VARCHAR(255)
)
begin
	-- Corpo da procedure
	-- Deleta a versão antiga de Aluno
	delete from Aluno a where a.matricula = prMatricula;

	-- Insere a versão nova em Aluno
	insert into Aluno (matricula, cpf, nome, email, numContato)
	values (prMatricula, prCpf, prNome, prEmail, prNumContato);
end;

-- Dropa a procedure
drop procedure InserirAluno;



-- Cria trigger de delete
create trigger ExcluiAluno before delete on Aluno for each row 
begin 
	set @versao = coalesce((select max(a.versao) from Aluno_log a where a.matricula=old.matricula), 0) + 1;
	insert into Aluno_log (matricula, cpf, nome, email, numContato, versao)
	values (old.matricula, old.cpf, old.nome, old.email, old.numContato, @versao);
end;

-- Dropa trigger de delete
drop trigger ExcluiAluno;



-- TESTES

delete from Aluno;

delete from Aluno_log;	

update Aluno
set matricula = 1, cpf = 111111111, nome = 'JOÃO', email = 'joao@email.com', numContato = 56789
where matricula = 1


insert into Aluno (matricula, cpf, nome, email, numContato)
values
(1, 111111111, 'AAA', 'aaa@email.com', 12345),
(2, 222222222, 'BBB', 'bbb@email.com', 12345),
(3, 333333333, 'CCC', 'ccc@email.com', 12345);

call InserirAluno(1, 123456789, 'JOÃO', 'joao@email.com', 56789);