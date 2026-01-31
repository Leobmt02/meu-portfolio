from django.shortcuts import render

def home(request):
    profile = {
        "name": "Leonardo Matias",
        "headline": "",
        "bio": "Sou estudante de Engenharia da Computação e, desde o início da graduação, desenvolvi interesse por automação de processos e análise de dados. Sempre fui movido pela curiosidade de entender como as informações circulam dentro das empresas e como é possível tornar processos mais eficientes por meio da tecnologia. Atualmente, atuo como estagiário na TechnipFMC, criando soluções com Python, Power BI e Power Platform.",
        "location": "Vila Velha, Espírito Santo, Brasil",
        "email": "l.bandeiramatias@gmail.com",
        "linkedin": "https://www.linkedin.com/in/mleonardobandeira/",
        "instagram": "https://www.instagram.com/leobmatias",
    }

    experiences = [
        {
            "company": "TechnipFMC",
            "role": "Estagiário",
            "period": "Ago 2024 - Presente",
            "description": """Atuo no laboratório de caracterização de materiais com foco na automação de processos, análise de dados e suporte a rotinas de gestão. Minha atuação combina competências técnicas e administrativas para otimizar o fluxo de trabalho da área.

Na frente de automação, desenvolvi uma ferramenta de alta performance para ensaios mecânicos, utilizando bibliotecas como Pandas (com processamento via chunking) e Matplotlib. Essa solução permitiu processar grandes volumes de dados de forma eficiente, otimizando tanto o tempo de análise quanto a gestão de arquivos do laboratório.

Expandindo para Business Intelligence, utilizei a Power Platform para criar aplicativos no Power Apps voltados à gestão de horas e ao controle de equipamentos. Essas ferramentas automatizaram o cálculo de KPIs de performance e disponibilidade, além de monitorar o uso e prever gastos, integrando tudo a relatórios gerenciais no Power BI.

Além da parte técnica, implementei um sistema de melhoria contínua gamificado (uma "lojinha virtual") para engajar os colaboradores na proposição de inovações. Complementarmente, presto apoio operacional à equipe de calibração na gestão de equipamentos e conduzo rotinas administrativas, como o acompanhamento de requisições de compras e o contato com fornecedores."""
        },
        {
            "company": "V&L Artes em Coroas Fúnebres",
            "role": "Assistente Administrativo / Gestão de Produção",
            "period": "Jan 2020 - Jul 2024",
            "description": "Atuei na parte administrativa, negociando com fornecedores e buscando clientes. Auxiliei na gestão da linha de produção e na garantia da qualidade dos produtos."
        }
    ]

    education = [
        {
            "institution": "FAESA",
            "degree": "Engenharia da Computação",
            "period": "2022 - 2026"
        }
    ]

    skills = [
        {"name": "Python", "icon": "fa-brands fa-python"},
        {"name": "Django", "icon": "fa-solid fa-code"},
        {"name": "Power BI", "icon": "fa-solid fa-chart-bar"},
        {"name": "Power Apps", "icon": "fa-solid fa-mobile-screen"},
        {"name": "Power Automate", "icon": "fa-solid fa-robot"},
        {"name": "Excel", "icon": "fa-solid fa-file-excel"},
        {"name": "Data Analysis", "icon": "fa-solid fa-magnifying-glass-chart"},
        {"name": "Pandas", "icon": "fa-solid fa-database"}, # Using database icon for Pandas generic
        {"name": "Matplotlib", "icon": "fa-solid fa-chart-line"},
        {"name": "SQL", "icon": "fa-solid fa-database"},
        {"name": "N8N", "icon": "fa-solid fa-diagram-project"},
    ]

    languages = [
        {"name": "Português", "level": "Nativo", "icon": "🇧🇷"},
        {"name": "Inglês", "level": "Intermediário", "icon": "🇺🇸"},
    ]

    certifications = [
        {
            "name": "White Belt Six Sigma",
            "issuer": "RL&Associados",
            "date": "Concluído",
            "icon": "fa-solid fa-certificate",
            "certificate_url": "https://drive.google.com/file/d/1Lv-KOdDbeoXk19-cbwGrUjWwDuOL4wPG/view?usp=drive_link",
        },
        {
            "name": "Green Belt Six Sigma",
            "issuer": "RL&Associados",
            "date": "Em andamento",
            "icon": "fa-solid fa-hourglass-half",
            "certificate_url": "",
        },
        {
            "name": "Power Apps Maker",
            "issuer": "TechnipFMC",
            "date": "Concluído",
            "icon": "fa-solid fa-mobile-screen",
            "certificate_url": "https://www.credly.com/badges/c4dc7e14-0bf3-4719-9405-f5743f1e60d3/linked_in_profile",
        },
        {
            "name": "Power Automate Maker",
            "issuer": "TechnipFMC",
            "date": "Concluído",
            "icon": "fa-solid fa-robot",
            "certificate_url": "https://www.credly.com/badges/748d2e18-13db-4970-a729-df0a297b53b9/linked_in_profile",
        },
        {
            "name": "Google Data Analytics",
            "issuer": "Google / Coursera",
            "date": "Em andamento",
            "icon": "fa-brands fa-google",
            "certificate_url": "",
        },
    ]

    projects = [
        {
            "title": "Dashboard Comercial",
            "category": "Power BI",
            "description": "Dashboard Comercial de Gestão de Performance e Presença Nacional. O objetivo foi desenvolver uma solução que não apenas mostrasse números, mas permitisse uma análise profunda da performance comercial, geográfica e individual da equipe de vendas (Jan/22 a Mar/24). Utilizei o ecossistema Microsoft (Power BI Desktop, Power Query para ETL e DAX avançado) para criar uma experiência fluida e responsiva. Um desafio interessante foi modelar os dados para relacionar corretamente vendedores, clientes e lojas, além de otimizar a performance para lidar com o volume de transações.",
            "tags": ["Power BI", "ETL", "DAX", "Analytics", "Dashboard"],
            "media_type": "video",
            "media_url": "/static/portfolio/videos/dashboard_vendas.mp4",
            "is_confidential": False,
        },
        {
            "title": "Automação de Ensaios Laboratoriais",
            "category": "Python",
            "description": "Desenvolvi uma aplicação em Python utilizando Pandas e Matplotlib para automatizar o tratamento de dados de ensaios mecânicos. A solução resolveu um gargalo crítico: os arquivos de dados eram tão volumosos que o Excel não conseguia processá-los, tornando a análise manual inviável. Com a automação, o tempo de processamento foi drasticamente reduzido, aumentando significativamente a eficiência na entrega de relatórios técnicos.",
            "tags": ["Python", "Pandas", "Matplotlib", "Automação", "Big Data"],
            "media_type": "confidential",
            "media_url": "",
            "is_confidential": True,
            "company": "TechnipFMC",
        },
        {
            "title": "Sistema de Apontamento de Horas",
            "category": "Power Apps",
            "description": "Desenvolvi no Power Apps um sistema de apontamento de horas que auxilia o planejamento na alocação de custos da equipe. Integrado ao aplicativo, criei um dashboard no Power BI para acompanhamento de indicadores de disponibilidade, performance e qualidade das atividades realizadas, proporcionando visibilidade total sobre a produtividade do time.",
            "tags": ["Power Apps", "Power BI", "Power Automate", "Gestão", "KPIs"],
            "media_type": "confidential",
            "media_url": "",
            "is_confidential": True,
            "company": "TechnipFMC",
        },
        {
            "title": "Sistema de Gestão de Equipamentos",
            "category": "Power Apps",
            "description": "Desenvolvi um sistema completo no Power Apps para gestão de equipamentos do laboratório, registrando todo o histórico de serviços realizados (manutenções preventivas, corretivas e calibrações). O aplicativo é monitorado por fluxos do Power Automate que ajustam automaticamente os status dos equipamentos conforme as datas se aproximam. Complementando a solução, criei um dashboard no Power BI que oferece visão geral do parque de equipamentos, identificando os maiores custos com manutenções, status operacional/inativo e projeção de gastos para o próximo ano.",
            "tags": ["Power Apps", "Power BI", "Power Automate", "Gestão", "Manutenção"],
            "media_type": "confidential",
            "media_url": "",
            "is_confidential": True,
            "company": "TechnipFMC",
        },
    ]

    context = {
        'profile': profile,
        'experiences': experiences,
        'education': education,
        'skills': skills,
        'languages': languages,
        'certifications': certifications,
        'projects': projects,
    }
    return render(request, 'portfolio/home.html', context)
