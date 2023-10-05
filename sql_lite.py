
from sqlalchemy.orm import *
from sqlalchemy import *
import sqlalchemy as s
from sqlalchemy.sql.functions import *

engine = s.create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
Base = declarative_base()

class Client(Base):
    __tablename__ = 'client'

    id_cliente = s.Column(s.Integer, primary_key=True, autoincrement=True)
    nome = s.Column(s.String(20), nullable=False)
    cpf = s.Column(s.String(11), nullable=False, unique=True)
    endereco = s.Column(s.String(25), nullable=False)

    account = relationship('Account', back_populates='client')

    def __repr__(self):
        return f'id_cliente={self.id_cliente}\nnome={self.nome}\ncpf={self.cpf}\nendereco={self.endereco}'

class Account(Base):
    __tablename__ = 'account'

    id_conta = s.Column(s.Integer, primary_key=True, autoincrement=True)
    tipo = s.Column(s.String(20), nullable=False)
    agencia = s.Column(s.String(5), nullable=False, unique=True)
    nro_conta = s.Column(s.Integer, nullable=False, unique=True)
    saldo = s.Column(s.Float, nullable=False)
    id_cliente = s.Column(s.Integer, s.ForeignKey('client.id_cliente'))

    client = relationship('Client', back_populates='account')

    def __repr__(self):
        return f'id_conta={self.id_conta}\ntipo={self.tipo}\nagencia={self.agencia}\nnro_conta={self.nro_conta}' \
               f'\nsaldo={self.saldo}\nid_cliente={self.id_cliente}'

Base.metadata.create_all(engine)


with Session(engine) as session:
    cliente_01 = Client(
        nome='Pedro Cardoso',
        cpf='78965412345',
        endereco='Rua Salvador 25',
        account=[Account(
            tipo='Conta Poupança',
            agencia='0001',
            nro_conta='123-7',
            saldo=2500
            )]
    )
    cliente_02 = Client(
        nome='Rafael Peixoto',
        cpf='12365478942',
        endereco='Rua Campinas 102',
        account=[Account(
            tipo='Conta Corrente',
            agencia='0010',
            nro_conta='321-5',
            saldo=5000
        )]
    )
    cliente_03 = Client(
        nome='Carlos Marques',
        cpf='12365478947',
        endereco='Rua Napoli 802',
        account=[Account(
            tipo='Conta Corrente',
            agencia='1000',
            nro_conta='371-5',
            saldo=5050
        )]
    )
    cliente_04 = Client(
        nome='João Carvalho',
        cpf='54397851463',
        endereco='Rua Santiago 96',
        account=[Account(
            tipo='Conta Salário',
            agencia='0017',
            nro_conta='761-1',
            saldo=1500
        )]
    )
    cliente_05 = Client(
        nome='Carla Santos',
        cpf='96325874154',
        endereco='Rua Natal 54',
        account=[Account(
            tipo='Conta Poupança',
            agencia='0006',
            nro_conta='542-9',
            saldo=20000
        )]
    )
    cliente_06 = Client(
        nome='Tiago Silva',
        cpf='15795348625',
        endereco='Rua Rio Branco 2365',
        account=[Account(
            tipo='Conta Corrente',
            agencia='0027',
            nro_conta='953-6',
            saldo=7400
        )]
    )
    cliente_07 = Client(
        nome='João Barbosa',
        cpf='75195385297',
        endereco='Rua Alagoas 7',
        account=[Account(
            tipo='Conta Corrente',
            agencia='0025',
            nro_conta='458-3',
            saldo=5500
        )]
    )
    cliente_08 = Client(
        nome='Bruno Dias',
        cpf='95175396312',
        endereco='Rua Brasília 13',
        account=[Account(
            tipo='Conta Corrente',
            agencia='0725',
            nro_conta='634-5',
            saldo=3750
        )]
    )
    cliente_09 = Client(
        nome='Matheus Silva',
        cpf='14796365241',
        endereco='Rua Amazonas 22',
        account=[Account(
            tipo='Conta Poupança',
            agencia='0305',
            nro_conta='520-5',
            saldo=15000
        )]
    )
    cliente_10 = Client(
        nome='Marta Vasconcelos',
        cpf='96478525695',
        endereco='Rua Rio de Janeiro 47',
        account=[Account(
            tipo='Conta Corrente',
            agencia='5305',
            nro_conta='201-7',
            saldo=50000
        )]
    )
    cliente_11 = Client(
        nome='Fernando Carvalho',
        cpf='45871973628',
        endereco='Rua Amapá 63',
        account=[Account(
            tipo='Conta Corrente',
            agencia='1327',
            nro_conta='254-8',
            saldo=75600
        )]
    )
    cliente_12 = Client(
        nome='Paula Guimarães',
        cpf='95175345796',
        endereco='Rua Santa Catarina 27',
        account=[Account(
            tipo='Conta Salário',
            agencia='0508',
            nro_conta='997-8',
            saldo=3000
        )]
    )
    cliente_13 = Client(
        nome='Ana Beatriz',
        cpf='15320096582',
        endereco='Rua São Paulo 987',
        account=[Account(
            tipo='Conta Corrente',
            agencia='0989',
            nro_conta='556-1',
            saldo=12500
        )]
    )
    cliente_14 = Client(
        nome='Bianca Siqueira',
        cpf='22654397520',
        endereco='Rua Bahia 41',
        account=[Account(
            tipo='Conta Corrente',
            agencia='3879',
            nro_conta='721-3',
            saldo=7400
        )]
    )
    cliente_15 = Client(
        nome='Juliana Pereira',
        cpf='12085246397',
        endereco='Rua Minas Gerais 2',
        account=[Account(
            tipo='Conta Poupança',
            agencia='0183',
            nro_conta='258-3',
            saldo=120000
        )]
    )
    cliente_16 = Client(
        nome='Carolina Sampaio',
        cpf='14851679542',
        endereco='Rua Belo Horizonte 91',
        account=[Account(
            tipo='Conta Corrente',
            agencia='1122',
            nro_conta='335-4',
            saldo=26000
        )]
    ) 


session.add_all([cliente_01, cliente_02, cliente_03, cliente_04, cliente_05, cliente_06, cliente_07, cliente_08,
                     cliente_09, cliente_10, cliente_11, cliente_12, cliente_13, cliente_14, cliente_15, cliente_16])
session.commit()    



#Recuperando usuários a partir de condição de filtragem
stmt = select(Client).where(Client.nome.in_(['Tiago', 'Juliana', 'João']))
for cliente in session.scalars(stmt):
  print(cliente)

#Recuperando informações de maneira ordenada
print(select(Client).order_by(Client.nome.desc()))

order = select(Client).order_by(Client.endereco.desc())
for i, result in enumerate (session.scalars(order)):
  print(f'Resultado {i}: {result}')


# Dados das pessoas que possuem Conta Corrente
corrente = select(Account).where(Account.tipo.in_(['Conta Corrente']))
for cli in session.scalars(corrente):
  print(cli)

# Nomes, números da conta e saldos maiores que R$5.000 ordenados por saldo em ordem crescente
stmt_03 = select(Client.nome, Account.nro_conta, Account.saldo).join_from(Client, Account).where(Account.saldo >= 5000).order_by(Account.saldo.asc())

