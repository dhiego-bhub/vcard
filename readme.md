# Cartão de Visitas Virtual - Streamlit

![Banner do Projeto](https://via.placeholder.com/1200x300/bc0a53/FFFFFF/?text=Cart%C3%A3o+de+Visitas+Virtual)

## 📌 Sobre o Projeto

Este é um aplicativo web de cartão de visitas virtual desenvolvido com Streamlit. Ele permite criar e compartilhar um cartão de visitas digital profissional com funcionalidades como:

- Salvar contato diretamente no smartphone (Android e iPhone)
- QR Code para compartilhamento rápido
- Links para redes sociais
- Design responsivo e elegante
- Cores personalizáveis

## 🚀 Demo

Acesse a demonstração ao vivo aqui: [Link para a sua aplicação Streamlit](https://seu-cartao-virtual.streamlit.app/)

## 📋 Pré-requisitos

- Python 3.7+
- Git

## 🔧 Instalação

1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/cartao-virtual.git
cd cartao-virtual
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação localmente:
```bash
streamlit run app.py
```

## 📝 Personalização

### Edite suas informações

Abra o arquivo `app.py` e localize o dicionário `info`. Substitua com suas informações:

```python
info = {
    "nome": "Seu Nome",
    "cargo": "Seu Cargo", 
    "empresa": "Nome da Sua Empresa",
    "foto": "URL_DA_SUA_FOTO",  # Substitua pela URL da sua foto
    "telefone": "+55 11 99999-9999",
    "email": "seuemail@empresa.com.br",
    "site": "www.seusite.com.br",
    "endereco": "Sua Rua, 123 - Bairro - Cidade/UF",
    "instagram": "seu_instagram",
    "linkedin": "seu_linkedin",
    "twitter": "seu_twitter",
    "facebook": "seu_facebook",
    "whatsapp": "+5511999999999",  # Formato sem espaços ou caracteres especiais
    "logo": "URL_DO_SEU_LOGO"  # Substitua pela URL do logo da empresa
}
```

### Modifique as cores

As cores padrão são:
- Cor principal (Primary): `#bc0a53` (Rosa/Vermelho)
- Cor secundária (Secondary): `#4c4c4c` (Cinza)

Para mudar, edite estas variáveis no início do arquivo:

```python
# Cores do escritório
cor_principal = "#bc0a53"  # Rosa/Vermelho
cor_secundaria = "#4c4c4c"  # Cinza
```

## 📱 Como usar

### Para compartilhar seu cartão:

1. Compartilhe o URL da aplicação Streamlit
2. Ou compartilhe o QR Code que aparece no cartão

### Para salvar o contato no celular:

1. Clique no botão "SALVAR CONTATO"
2. Um arquivo .vcf será baixado automaticamente
3. Abra o arquivo no seu dispositivo para adicionar aos contatos

## 🌐 Deploy no Streamlit Cloud

1. Faça fork deste repositório para sua conta GitHub
2. Acesse [Streamlit Cloud](https://streamlit.io/cloud)
3. Clique em "New app"
4. Selecione o repositório, o branch (main) e o arquivo (app.py)
5. Clique em "Deploy!"

## 📂 Estrutura do Projeto

```
cartao-virtual/
├── app.py              # Aplicação principal
├── requirements.txt    # Dependências do projeto
├── README.md           # Este arquivo
└── .gitignore          # Arquivos ignorados pelo git
```

## 📄 Arquivo requirements.txt

```
streamlit
pillow
qrcode
```

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- [Streamlit](https://streamlit.io/) por tornar a criação de aplicativos web em Python tão fácil
- [Font Awesome](https://fontawesome.com/) pelos ícones utilizados
- [Onda SVG](https://getwaves.io/) pelo gerador de ondas SVG

---

Feito com ❤️ e Python
