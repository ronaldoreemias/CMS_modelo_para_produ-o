# CMS_modelo_para_produ-o
objetivo de criar um CMS funcional em python , a meta é construir usando Flask_ADMIN.....È o objetivo 
🛠️ Descrição do Funcionamento do CMS
Este projeto é um CMS (Sistema de Gerenciamento de Conteúdo) desenvolvido com Flask e SQLAlchemy, voltado para o cadastro e exibição de perfis personalizados. Ele permite:

🔍 Funcionalidades principais
Exibição pública de perfis divididos por categoria (topvip, vip, dacasa) na página inicial.

Área administrativa protegida por login, acessível apenas com credenciais fixas (admin/admin).

Cadastro de novos perfis via formulário no painel administrativo.

Listagem completa de registros com visualização no dashboard.

Persistência de dados em banco PostgreSQL, com modelo relacional definido pela classe Acompanhante.

🔐 Segurança e sessão
Utiliza Flask-Session para controle de login.

Protege rotas administrativas contra acesso não autorizado.

🧱 Estrutura técnica
Backend: Flask + SQLAlchemy

Banco de dados: PostgreSQL

Templates: HTML renderizados via render_template
